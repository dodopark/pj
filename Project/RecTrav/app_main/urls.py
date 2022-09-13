from django.urls import path
from . import views
urlpatterns = [ 
    path('', views.home, name='home'),
    path('login_user', views.login_user, name='login'),
    path('places', views.places, name='places'),
    path('rec', views.rec, name='rec'),
    path('register', views.register, name='register'),
    path('register/thankyou', views.register_thank, name='register_thank'),
    path('places/<int:place_id>', views.place, name='place'),
    path('logout_user', views.logout_user, name='logout'),
]