from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(max_length=60, required=True, label='Name')
    surname = forms.CharField(max_length=60, required=True, label='Surname')
    address = forms.CharField(max_length=60, required=True, label='Address')
    email = forms.EmailField(max_length=60, required=True, label='Email')
    password = forms.CharField(max_length=60, required=True, label='Password')
