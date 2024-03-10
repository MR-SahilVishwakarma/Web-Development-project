from django.db import models
from django.db import *

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=122)
    email= models.CharField(max_length=122)
    phone= models.IntegerField()
    desc= models.TextField()
    # image=models.ImageField(upload_to='media')
    date= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
    

class Billing(models.Model):
    firstName= models.CharField(max_length=122,default="")
    lastName= models.CharField(max_length=122,default="")
    username= models.CharField(max_length=122,default="")
    email= models.CharField(max_length=122,default="")
    address= models.TextField(default='')
    address2= models.TextField(default='')
    ccname= models.CharField(max_length=122,default="")
    ccnumber= models.IntegerField(default=0)
    ccexpiration= models.TextField(default='')
    date= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username

class Signin(models.Model):
    name= models.CharField(max_length=122)
    email= models.EmailField(max_length=122)
    phone= models.IntegerField()
    uname= models.CharField(max_length=122)
    psw= models.CharField(max_length=122)
    date= models.DateTimeField(auto_now=True)
    role=models.IntegerField(default=2)
    def __str__(self):
        return self.uname

# class thrd(models.Model):
#     table= models.CharField()
    
    
