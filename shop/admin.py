from django.contrib import admin
from .models import Category, Product, Basket, Orders
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Basket)
admin.site.register(Orders)
