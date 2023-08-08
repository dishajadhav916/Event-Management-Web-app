from django.shortcuts import render, redirect, reverse
from .import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from ecommerce.models import Product_crud
from ecommerce.models import Cart_crud
from django.conf import settings

#from product.models import Product_form

#@login_required



def home(request):
     return render(request,"index.html")



def Register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('sname')
        name = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass')

        new_user = User.objects.create_user(name, email, password)
        new_user.first_name = fname
        new_user.last_name = lname

        new_user.save()
        return redirect('login-page')
  
    return render(request, 'register.html', {})

def Login(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('product-page')
        else:
            return HttpResponse('Error, user does not exist')


    return render(request, 'login.html', {})

def product(request):
    pro_data = Product_crud.objects.all()
    return render(request,"product.html",{'pro_data':pro_data})

def logoutuser(request):
    logout(request)
    return redirect('login-page')

def test(request):
    return render(request, 'test.html', {})


#crud functions for Product

def products_view(request):
    products=Product_crud.objects.all()
    return render(request,'product-crud.html',{'products':products})

def add_product(request):
    productForm=forms.ProductForm()
    if request.method=='POST':
        productForm=forms.ProductForm(request.POST, request.FILES)
        if productForm.is_valid():
            productForm.save()
            return redirect('productview')
    return render(request,'add-product.html',{'productForm':productForm})

def update_product(request,pk):
    product=Product_crud.objects.get(id=pk)
    productForm=forms.ProductForm(instance=product)
    if request.method=='POST':
        productForm=forms.ProductForm(request.POST,request.FILES,instance=product)
        if productForm.is_valid():
            productForm.save()
            return redirect('productview')
    return render(request,'update-product.html',{'productForm':productForm})


def delete_product(request,pk):
    product=Product_crud.objects.get(id=pk)
    product.delete()
    return redirect('productview')

#crud functions for Cart

def cart(request):
    carts = Cart_crud.objects.all()
    user = request.user 
    return render(request, 'cart.html',{'carts':carts})


def add_to_cart(request,pk):
    if request.method=='POST':
        product = Product_crud.objects.get(id=pk)
        product_loop=Product_crud.objects.filter(id=pk)
        for i in product_loop:
            prod_name = i.pro_name
            price= i.price
            reg = Cart_crud(user=request.user,id=pk, prod_name=prod_name,description=i.description,price=price)
            reg.save()
        return redirect('cart-page')
 
def delete_cart(request,pk):
    Cart_crud.objects.filter(id=pk).delete()
    return redirect('cart-page')










