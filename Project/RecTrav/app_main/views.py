from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from app_main.forms import RegisterForm
from .models import Register

# Create your views here.
def home(request):
    return render(request, 'app_main/home.html')

def login(request):
    return render(request, 'app_main/login.html')    

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
           data =  form.cleaned_data
           regis = Register()
           regis.name = data['name']
           regis.surname = data['surname']
           regis.address = data['address']
           regis.email = data['email']
           regis.password = data['password']
           regis.save()       
        return HttpResponseRedirect(reverse('register_thank'))
    else:

     form = RegisterForm()
    context = {'form': form}
    return render(request, 'app_main/register.html', context) 
    
def register_thank(request):
    return render(request, 'app_main/register_thank.html')    