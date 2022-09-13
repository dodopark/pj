from django.db import models

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
    p_satisfaction = models.IntegerField(null=True)
    p_access = models.IntegerField(null=True)
    p_crownded = models.IntegerField(null=True)
    p_landscape = models.IntegerField(null=True)
    p_spacial =  models.IntegerField(null=True)

