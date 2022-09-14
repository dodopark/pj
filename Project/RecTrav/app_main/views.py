from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from app_main.forms import RegisterModelForm
from .models import Register,Place,Score
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
import random



# Create your views here.
def home(request):
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    rand_num1 = random.choice(my_list)
    rand_num2 = random.choice(my_list)
    rand_num3 = random.choice(my_list)
    all_place = Place.objects.filter(id__in=[rand_num3,  rand_num2, rand_num1])
    print(all_place)
    context = {'places':  all_place }
    return render(request, 'app_main/home.html',context)

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = RegisterModelForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('register_thank'))
        else:
            return HttpResponseRedirect(reverse('register'))   
    else:
        form = RegisterModelForm()
        return render(request, 'app_main/register.html', {'form': form}) 

    #if request.method == 'POST':
    #    form = RegisterModelForm(request.POST)
    #    if form.is_valid():
    #      form.save()      
    #    return HttpResponseRedirect(reverse('register_thank'))
    #else:

    # form = RegisterModelForm()
    # context = {'form': form}
    # return render(request, 'app_main/register.html', context) 

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)  
        print(user)
        if user is not None:
            login(request, user)
            return render(request, 'app_main/home.html')
        else :
            print('1')    
    context = {}   
    return render(request, 'app_main/login.html', context)       
    
def register_thank(request):
    return render(request, 'app_main/register_thank.html')

def places(request):
    all_place = Place.objects.all()
    context = {'places':  all_place }
    return render(request, 'app_main/places.html',context)   

def place(request, place_id):
    if request.method == 'POST':
            test = Score()
            test.satisfaction = 2 
            test.access = 4 
            test.crownded = 1 
            test.landscape = 5 
            test.spacial = 4
            test.p_id_id = place_id
            test.u_id_id = request.user.id
            test.save() 
    one_place = None
    try:
        one_place = Place.objects.get(id=place_id)
    except:
        print('Error') 
    context = { 'place': one_place}
        
    return render(request, 'app_main/place.html', context) 

def rec(request):

    return render(request, 'app_main/rec.html')  

def logout_user(request):
    logout(request)
    return render(request, 'app_main/home.html')     


        