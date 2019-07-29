from django.db import models
from django.contrib.auth.models import AbstractUser


from django.utils import timezone
import datetime


class MyGenericModel(models.Model):
    theFile = models.FileField(upload_to='media/files/',default='aa',blank=True)
    firebase_id_token = models.CharField(max_length=50)

class Expert(models.Model):
    full_name = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='media/',default='aa',blank=True)
    expert_type =  models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    best_dish = models.CharField(max_length=250,blank=True)
    rate = models.CharField(max_length=50,blank=True)
    station = models.CharField(max_length=50,blank=True)
    availability = models.CharField(max_length=50,blank=True)
    fb = models.CharField(max_length=250,blank=True)
    twitter = models.CharField(max_length=250,blank=True)
    youtube = models.CharField(max_length=250,blank=True)
    instagram = models.CharField(max_length=250,blank=True)

  



    def __str__(self):
        return self.full_name
    


