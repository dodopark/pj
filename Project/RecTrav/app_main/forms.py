from dataclasses import field
from django import forms
from app_main.models import Register, Place
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class RegisterModelForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    address = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'address', 'password1', 'password2']
        lebels = {
            'Username' : 'ชื่อผู้ใช้',
            'Name': 'ชื่อ',
            'Surname': 'นามสกุล',
            'Address': 'ที่อยู่',
            'Email': 'อีเมล',
            'Password': 'รหัสผ่าน'
        }    

