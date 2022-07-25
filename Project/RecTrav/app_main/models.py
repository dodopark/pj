from django.db import models

# Create your models here.

class Register(models.Model):
    STATUS = [
        ('unapproved','Unapproved'),
        ('approved','Approved'),
        ('banned','Banned'),
    ]

    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    email = models.EmailField(max_length=60, unique=True)
    password = models.CharField(max_length=20)
    status = models.CharField(max_length=15, choices=STATUS, default='unapproved')