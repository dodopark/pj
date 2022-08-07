from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from app_main.forms import RegisterModelForm
from .models import Register,Place
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'app_main/home.html')

def register(request):
    if request.method == 'POST':
        form = RegisterModelForm(request.POST)
        if form.is_valid():
          form.save()      
        return HttpResponseRedirect(reverse('register_thank'))
    else:

     form = RegisterModelForm()
    context = {'form': form}
    return render(request, 'app_main/register.html', context) 

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(username)
        print(password)
        print(user)
        if user is not None:
            login(request, user)
            return render(request, 'app_main/home.html')
            
    context = {}   
    return render(request, 'app_main/login.html', context)       
    
def register_thank(request):
    return render(request, 'app_main/register_thank.html')

def places(request):
    all_place = Place.objects.all()
    print(all_place)
    context = {'places':  all_place }
    return render(request, 'app_main/places.html',context)   

def place(request, place_id):
    one_place = None
    try:
        one_place = Place.objects.get(id=place_id)
    except:
        print('Error') 
    context = { 'place': one_place}       
    return render(request, 'app_main/place.html', context) 


        