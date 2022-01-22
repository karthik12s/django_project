from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        #fields = "__all__"

class loginForm(forms.Form):
    name = forms.CharField(max_length=20)
    age = forms.IntegerField(max_value=120)
