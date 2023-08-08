from django import forms
from django.contrib.auth.models import User
from ecommerce.models import Product_crud



class ProductForm(forms.ModelForm):
    class Meta:
        model=Product_crud
        fields=['pro_name','price','description','pro_img']