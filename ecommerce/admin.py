from django.contrib import admin
from ecommerce.models import Product_crud
from ecommerce.models import Cart_crud


class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product_crud, ProductAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display=('prod_name','price','user','description')
admin.site.register(Cart_crud, CartAdmin)



# Register your models here.
