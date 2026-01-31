from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm
from django.contrib.auth import login, logout, authenticate

from django.shortcuts import get_object_or_404
# Create your views here.

def index (request):

    return render (request, 'index.html')

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
        return redirect ('Index', id=request.user.id)
            
    context = {
        'Form_login' : Form_login
    }

    return render (request, 'include/authentication/signIn.html', context=context)


def auth_logout (request):

    if request.method == 'POST':
        logout (request)
        return redirect ('SignUp')