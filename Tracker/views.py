from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm, Time_tablePeriod, AttendanceInputCheck
from django.contrib.auth import login, logout, authenticate

from django.shortcuts import get_object_or_404
from .models import PeriodContainer, AttendaceModel, Profile

import pyotp
from django.conf import settings

from django.utils import timezone
from zoneinfo import ZoneInfo
from datetime import time

from django.http import HttpResponse
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.

# __________________________________________________________________________
# Time Attendance

def is_attendance_time():

    ethiopian_tz = ZoneInfo("Africa/Addis_Ababa")
    now = timezone.now().astimezone(ethiopian_tz).time()

    print("Now", now)

    start = time (15, 45)
    end = time (19, 30)

    return start <= now <= end

def get_totp ():
    return pyotp.TOTP(settings.ATTENDANCE_SECRET, interval=30)


def admin_control (request, username):       
    
    totp = get_totp()
    code = totp.now()
    
    context = {
        'code' : code
    }
    return render (request, 'include/Admin/CreateAttendaceFill.html', context=context)

def control_teacher (request):
    
    model = AttendaceModel.objects.all()
    context = {
        'model' : model
    }
    return render (request, 'include/Admin/ControlTeachers.html', context=context)

# __________________________________________________________________________

@login_required(login_url='/signup/')
def index (request):

    profile, created = Profile.objects.get_or_create(user=request.user)

    allowed_time = is_attendance_time()
    if allowed_time:
        totp = get_totp()
        code = totp.now()
    else:
        return render (request, 'index.html', {
            "message": "Attendance is not open yet ⏰"
        })
    
    # Check Validation
    form = AttendanceInputCheck (request.POST or None)
    if request.method == 'POST':
        if form.is_valid():

            user_code = form.cleaned_data['code']
            totp = get_totp()
            if totp.verify(user_code):

                AttendaceModel.objects.create (
                    teachersFill=profile
                )
                messages.success (request, "Attendance is Filled!!")
                return redirect ('Index')
            else:
                messages.error (request, "The Code is Expired or Invalid")
        
    # Time Table
    InsertTimePeriod = Time_tablePeriod (request.POST)
    if request.method == 'POST':
        if InsertTimePeriod.is_valid():
            obj = InsertTimePeriod.save(commit=False)
            obj.teachers = request.user.profile
            obj.save()
            print ('Saved!!', obj)
            return redirect ('Index')

    TimeTableFilter = PeriodContainer.objects.all()
        
    context = {
        'InputTime' : InsertTimePeriod,
        'TimeTableFilter' : TimeTableFilter,
        'code' : code,
        'form' : form
    }

    return render (request, 'index.html', context=context)

def auth_signUp (request):

    form = SignUpForm (request.POST)
    if request.method == 'POST':
        if form.is_valid ():
            user = form.save()

            profile = user.profile
            profile.teachers_field = form.cleaned_data['subject_field']
            profile.save()

            return redirect ('Index')
        
    context = {
        'Form' : form
    }
    return render (request, 'include/authentication/signUp.html', context=context)

def auth_login (request):

    Form_login = SignInForm (request.POST or None)
    if not request.user.is_authenticated:
        if request.method == 'POST':
            if Form_login.is_valid():
                
                username = Form_login.cleaned_data['username']
                password = Form_login.cleaned_data['password']

                user = authenticate (request, username=username, password=password)
                if user is not None:
                    login (request, user)
                    return redirect ('Index')
                else:
                    Form_login.add_error(None, "Invalid Username or Password")
    else:
        return redirect ('Index')
            
    context = {
        'Form_login' : Form_login
    }

    return render (request, 'include/authentication/signIn.html', context=context)


def auth_logout (request):

    if request.method == 'POST':
        logout (request)
        return redirect ('SignUp')