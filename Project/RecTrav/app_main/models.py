from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Register(models.Model):
    STATUS = [
        ('unapproved','Unapproved'),
        ('approved','Approved'),
        ('banned','Banned'),
    ]
    username = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    email = models.EmailField(max_length=60, unique=True)
    password = models.CharField(max_length=20)
    status = models.CharField(max_length=15, choices=STATUS, default='unapproved')

class Place(models.Model):
    p_name = models.CharField(max_length=60)
    p_address = models.CharField(max_length=60)
    p_province = models.CharField(max_length=60)
    p_district = models.CharField(max_length=60)
    p_subdistrict = models.CharField(max_length=60)
    p_postnumber = models.CharField(max_length=60)
    p_image = models.CharField(max_length=50, null=True, blank=True)
    p_url = models.CharField(max_length=50, null=True, blank=True)
    p_type = models.CharField(max_length=50, null=True, blank=True)
    

class Score(models.Model):    
    satisfaction = models.IntegerField(null=True)
    access = models.IntegerField(null=True)
    crownded = models.IntegerField(null=True)
    landscape = models.IntegerField(null=True)
    spacial =  models.IntegerField(null=True)
    u_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    p_id = models.ForeignKey(Place, on_delete=models.CASCADE, null=True, blank=True)