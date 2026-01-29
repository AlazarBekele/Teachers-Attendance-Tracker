from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm (UserCreationForm):

    firstName = forms.CharField (max_length=20, widget=forms.TextInput(attrs={
        'class' : 'bg-white w-full h-[30px] shadow-sm shadow-blue-500/10'
    }))

    lastName = forms.CharField (max_length=20, widget=forms.TextInput(attrs={
        'class' : 'bg-white w-full h-[30px] shadow-sm shadow-blue-500/10'
    }))

    username = forms.CharField (max_length=20, widget=forms.TextInput(attrs={
        'class' : 'bg-white w-full h-[30px] shadow-sm shadow-blue-500/10'
    }))

    email = forms.EmailField (widget=forms.EmailInput(attrs={
        'class' : 'bg-white w-full h-[30px] shadow-sm shadow-blue-500/10'
    }))

    password1 = forms.CharField (max_length=10, widget=forms.PasswordInput(attrs={
        'class' : 'bg-white w-full h-[30px] shadow-sm shadow-blue-500/10'
    }))

    password2 = forms.CharField (max_length=10, widget=forms.PasswordInput(attrs={
        'class' : 'bg-white w-full h-[30px] shadow-sm shadow-blue-500/10'
    }))

    class Meta:
        model = User
        fields = ('firstName', 'lastName', 'email', 'username', 'password1', 'password2')