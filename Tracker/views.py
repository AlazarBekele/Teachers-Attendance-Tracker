from django.shortcuts import render, redirect
from .forms import SignUpForm
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