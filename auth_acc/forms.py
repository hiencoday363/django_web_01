from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50,required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(max_length=255,required=True)
    password2 = forms.CharField(max_length=255,required=True)

    class Meta:
        model = User
        fields = ("username", 'email', 'password1', 'password2')
        field_classes = {'username': UsernameField}
