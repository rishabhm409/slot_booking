from django.db import models

# Create your models here.
class Avaliable(models.Model):
    name=models.CharField(max_length=50)
    date=models.DateField(auto_now_add=False,auto_now=False,blank=True)
    From=models.TimeField(auto_now_add=False,auto_now=False,blank=True)
    To=models.TimeField(auto_now_add=False,auto_now=False,blank=True)
    ids = models.CharField(max_length=20,default="")



class Busy(models.Model):
    name=models.CharField(max_length=50)
    date=models.DateField(auto_now_add=False,auto_now=False,blank=True)
    From=models.TimeField(auto_now_add=False,auto_now=False,blank=True)
    To=models.TimeField(auto_now_add=False,auto_now=False,blank=True)
    ids = models.CharField(max_length=20,default="")
