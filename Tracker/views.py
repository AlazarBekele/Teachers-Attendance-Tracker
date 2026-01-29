from django.shortcuts import render

# Create your views here.

def index (request):

    return render (request, 'index.html')

def auth_signUp (request):

    return render (request, 'include/authentication/signUp.html')