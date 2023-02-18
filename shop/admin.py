from django.contrib import admin
from .models import Category, Product, Basket, Orders


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['slug', 'name']
    list_editable = ['name']
    list_filter = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name_product', 'in_stock']
    list_filter = ['in_stock', 'category']
    list_editable = ['in_stock']


admin.site.register(Orders)
