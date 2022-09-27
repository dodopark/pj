from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from app_main.forms import RegisterModelForm
from .models import Register,Place,Score
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import random
import requests
import re 
import numpy as np
import pandas as pd 
from sklearn.metrics.pairwise import cosine_similarity



# Create your views here.
def home(request):
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    rand_num1 = random.choice(my_list)
    rand_num2 = random.choice(my_list)
    rand_num3 = random.choice(my_list)
    all_place = Place.objects.filter(id__in=[rand_num1,  rand_num2, rand_num3])
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
    url = Place.objects.only('p_url').get(id = place_id).p_url
    rt = GetRating(url)
    rw = GetReviews(url) 
    if request.method == 'POST':
            sat = request.POST.get('range1')
            acc = request.POST.get('range2')
            cro = request.POST.get('range3')
            lad = request.POST.get('range4')
            spe = request.POST.get('range5')
            sc = Score()
            sc.satisfaction = sat 
            sc.access = acc 
            sc.crownded = cro 
            sc.landscape = lad 
            sc.spacial = spe
            sc.p_id_id = place_id
            sc.u_id_id = request.user.id
            sc.save() 
            
    one_place = None
    try:
        one_place = Place.objects.get(id=place_id)
        
    except:
        print('Error') 
    context = { 'place': one_place, 'review' : rw, 'source' : url, 'rating' : rt}
        
    return render(request, 'app_main/place.html', context) 

def rec(request):
    if request.user.is_authenticated:  
        n_place = 20
        allusrs = User.objects.values_list('id')
        n_user = len(allusrs)
        print(n_user)
        first_k = 5
            # place_list = Score.objects.all()
        df = pd.DataFrame(list(Score.objects.all().values('satisfaction', 'u_id_id', 'p_id_id')))
      
        curr_usr = request.user.id
    
        place_select = FindRecommendPlace(df,n_place,n_user,curr_usr,first_k)
        p1 = place_select[0]
        p2 = place_select[1]
        p3 = place_select[2]
        p4 = place_select[3]
        p5 = place_select[4]
        place1 = Place.objects.get(id = p1)
        place2 = Place.objects.get(id = p2)
        place3 = Place.objects.get(id = p3)
        place4 = Place.objects.get(id = p4)
        place5 = Place.objects.get(id = p5) 
    else:
       return redirect('/')      
    context = {'pl1':  place1,'pl2':  place2,'pl3':  place3,'pl4':  place4,'pl5':  place5}
    return render(request, 'app_main/rec.html',context)

def logout_user(request):
    logout(request)
    return render(request, 'app_main/home.html')

def sea(request):
    all_place = Place.objects.filter(p_type = 'ทะเล')
    context = {'places':  all_place }
    return render(request, 'app_main/sea.html', context)

def island(request):
    all_place = Place.objects.filter(p_type = 'เกาะ')
    context = {'places':  all_place }
    return render(request, 'app_main/island.html', context)    

def mount(request):
    all_place = Place.objects.filter(p_type = 'ภูเขา')
    context = {'places':  all_place }
    return render(request, 'app_main/mount.html', context)

def waterfall(request):
    all_place = Place.objects.filter(p_type = 'น้ำตก')
    context = {'places':  all_place }
    return render(request, 'app_main/waterfall.html', context)    

def cave(request):
    all_place = Place.objects.filter(p_type = 'ถ้ำ')
    context = {'places':  all_place }
    return render(request, 'app_main/cave.html', context)                    

def market(request):
    all_place = Place.objects.filter(p_type = 'ตลาด')
    context = {'places':  all_place }
    return render(request, 'app_main/market.html', context)  
        
def river(request):
    all_place = Place.objects.filter(p_type = 'ลำธาร')
    context = {'places':  all_place }
    return render(request, 'app_main/river.html', context) 

def GetReviews(url):
    req = requests.get(url)
    str_reviews_summary = re.findall(r'"//lh3.goog?.*?].*?]', req.text)
    reviews = []
    for i in range(len(str_reviews_summary)):
        text = str_reviews_summary[i]
        text = text.split(',')
        rev = text[2]
        rev = re.sub(r'\\', '', rev)
        rev = re.sub(r'""', '', rev) 
        reviews.append(rev)
        
    return reviews

def GetRating(url):
    req = requests.get(url)
    str_rating = re.findall(r'ความเห็น?.*?].*?]', req.text)
    str_rating = str_rating[0].split(',')[6]
    rating = float(str_rating)
    
    return rating

def FindRecommendPlace(df,n_place,n_user,curr_usr,first_k):
    
    #usr_plc_matrix = 0*np.ones([n_user,n_place])
    usr_plc_matrix = 2.5*np.ones([n_user,n_place])  #initial score as 3
    curr_u = curr_usr -1

    for i in range(len(df)):
        u = df['u_id_id'][i]-1
        p = df['p_id_id'][i]-1
        usr_plc_matrix[u,p] = df['satisfaction'][i]

    sim = cosine_similarity(usr_plc_matrix, usr_plc_matrix)
    sim[curr_u,curr_u] = -1
    sim_u = np.argmax(sim[curr_u,:])

    #print(usr_plc_matrix)
    #print(sim)
    place_recmd = np.flip(np.argsort(usr_plc_matrix[sim_u,:]))
    place_recmd = place_recmd + 1
    place_recmd = place_recmd.tolist()
    
    return place_recmd[:first_k]    