from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm (UserCreationForm):

    firstName = forms.CharField (max_length=20, widget=forms.TextInput(attrs={
        'class' : 'pl-4 bg-cyan-100/50 w-full h-[40px] shadow-sm shadow-blue-500/10',
        'placeholder' : 'First Name'
    }))

    lastName = forms.CharField (max_length=20, widget=forms.TextInput(attrs={
        'class' : 'pl-4 bg-cyan-100/50 w-full h-[40px] shadow-sm shadow-blue-500/10',
        'placeholder' : 'Last Name'
    }))

    username = forms.CharField (max_length=20, widget=forms.TextInput(attrs={
        'class' : 'pl-4 bg-cyan-100/50 w-full h-[40px] shadow-sm shadow-blue-500/10',
        'placeholder' : 'Username'
    }))

    email = forms.EmailField (widget=forms.EmailInput(attrs={
        'class' : 'pl-4 bg-cyan-100/50 w-full h-[40px] shadow-sm shadow-blue-500/10',
        'placeholder' : 'Email'
    }))

    password1 = forms.CharField (max_length=10, widget=forms.PasswordInput(attrs={
        'class' : 'pl-4 bg-cyan-100/50 w-full h-[40px] shadow-sm shadow-blue-500/10',
        'placeholder' : 'Password'
    }))

    password2 = forms.CharField (max_length=10, widget=forms.PasswordInput(attrs={
        'class' : 'pl-4 bg-cyan-100/50 w-full h-[40px] shadow-sm shadow-blue-500/10',
        'placeholder' : 'Password2'
    }))

    class Meta:
        model = User
        fields = ('firstName', 'lastName', 'email', 'username', 'password1', 'password2')