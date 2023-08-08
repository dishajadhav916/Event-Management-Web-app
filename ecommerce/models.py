from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
 

class Product_crud(models.Model):
    pro_name=models.CharField(max_length=40)
    pro_img= models.ImageField(upload_to='product/',null=True,blank=True)
    price = models.PositiveIntegerField()
    description=models.CharField(max_length=40)

class Cart_crud(models.Model):
    user = models.ForeignKey(User, on_delete=(models.CASCADE))
    prod_name = models.CharField(max_length=60,default="true")
    price = models.IntegerField(default=0)
    description=models.CharField(max_length=40)

  
    
    
    
# Create your models here.
