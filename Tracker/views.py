from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def index (request):

    return render (request, 'index.html')

def auth_signUp (request):

    Form = SignUpForm (request.POST)
    if request.method == 'POST':
        if Form.is_valid ():
            Form.save()
            return redirect ('Index')
        
    context = {
        'Form' : Form
    }
    return render (request, 'include/authentication/signUp.html', context=context)

def auth_login (request):

    Form_login = SignInForm (request.POST or None)
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
            
    context = {
        'Form_login' : Form_login
    }

    return render (request, 'include/authentication/signIn.html', context=context)