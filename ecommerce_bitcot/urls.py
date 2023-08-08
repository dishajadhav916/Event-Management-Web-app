"""ecommerce_bitcot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ecommerce_bitcot import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from user.views import RegisterAPI
from knox import views as knox_views
from user.views import LoginAPI




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="homepage"),
    path('cart/', views.cart, name="cart-page"),
    path('login/',views.Login,name="login-page"),
    path('register/',views.Register,name="register-page"),
    path('product/',views.product,name="product-page"),
    path('productview/',views.products_view,name='productview'),
    path('add-product/', views.add_product,name='add-product'),
    path('update-product/<int:pk>', views.update_product,name='update-product'),
    path('delete-product/<int:pk>', views.delete_product,name='delete-product'),
    path('add-to-cart/<int:pk>',views.add_to_cart,name='add-to-cart'),
    path('remove_cart/<int:pk>',views.delete_cart,name='remove-cart'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login-page'), name="logout"),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)