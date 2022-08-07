from dataclasses import field
from django import forms
from app_main.models import Register, Place



class RegisterModelForm(forms.ModelForm):
    class Meta:
        model = Register 
        
        fields = ['username', 'name', 'surname', 'email', 'address', 'password']
        lebels = {
            'Username' : 'ชื่อผู้ใช้',
            'Name': 'ชื่อ',
            'Surname': 'นามสกุล',
            'Address': 'ที่อยู่',
            'Email': 'อีเมล',
            'Password': 'รหัสผ่าน'
        }    

