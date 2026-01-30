from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm (UserCreationForm):

    first_name = forms.CharField (max_length=20, widget=forms.TextInput(attrs={
        'class' : 'pl-4 bg-cyan-100/50 w-full h-[40px] shadow-sm shadow-blue-500/10 outline-none',
        'placeholder' : 'First Name'
    }))

    last_name = forms.CharField (max_length=20, widget=forms.TextInput(attrs={
        'class' : 'pl-4 bg-cyan-100/50 w-full h-[40px] shadow-sm shadow-blue-500/10 outline-none',
        'placeholder' : 'Last Name'
    }))

    username = forms.CharField (max_length=20, widget=forms.TextInput(attrs={
        'class' : 'pl-4 bg-cyan-100/50 w-full h-[40px] shadow-sm shadow-blue-500/10 outline-none',
        'placeholder' : 'Username'
    }))

    email = forms.EmailField (widget=forms.EmailInput(attrs={
        'class' : 'pl-4 bg-cyan-100/50 w-full h-[40px] shadow-sm shadow-blue-500/10 outline-none',
        'placeholder' : 'Email'
    }))

    password1 = forms.CharField (max_length=10, widget=forms.PasswordInput(attrs={
        'class' : 'pl-4 bg-cyan-100/50 w-full h-[40px] shadow-sm shadow-blue-500/10 outline-none',
        'placeholder' : 'Password'
    }))

    password2 = forms.CharField (max_length=10, widget=forms.PasswordInput(attrs={
        'class' : 'pl-4 bg-cyan-100/50 w-full h-[40px] shadow-sm shadow-blue-500/10 outline-none',
        'placeholder' : 'Password2'
    }))

    subject_field = forms.ChoiceField (choices=Profile.SUBJECT_CHOICES, label='Select Subject', widget=forms.Select(attrs={
        'class' : 'pl-4 bg-cyan-100/50 w-full h-[40px] shadow-sm shadow-blue-500/10 outline-none'
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'subject_field')


class SignInForm (forms.Form):

    username = forms.CharField (max_length=20, widget=forms.TextInput(attrs={
        'class' : 'pl-4 bg-cyan-100/50 w-full h-[50px] shadow-sm shadow-blue-500/10 outline-none',
        'placeholder' : 'Username'
    }))

    password = forms.CharField (max_length=10, widget=forms.PasswordInput(attrs={
        'class' : 'pl-4 bg-cyan-100/50 w-full h-[50px] shadow-sm shadow-blue-500/10 outline-none',
        'placeholder' : 'Password'
    }))