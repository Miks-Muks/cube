from django.contrib import admin
from .models import Category, Product, Basket, Orders
from django import form

# Register your models here.


class ProductAdminForm(form.ModelForm):
    pass
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['slug', 'name']
    list_editable = ['name']
    list_filter = ['name']



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name_product', 'price_1', 'price_2', 'price_3', 'in_stock']
    list_filter = ['in_stock', 'category']
    list_editable = ['in_stock', 'price_1', 'price_2', 'price_3']
    search_fields = ['brand_of_cardboard']
    list_display_links = ['name_product']


admin.site.register(Orders)
