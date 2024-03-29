from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from adminsortable2.admin import SortableAdminMixin

from .models import Category, Product, Orders, Basket


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget(), label='Описание')

    class Meta:
        model = Product
        fields = '__all__'


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Настройки для категорий"""
    list_display = ['slug', 'name']
    list_editable = ['name']
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(SortableAdminMixin, admin.ModelAdmin):
    """Настройки для товаров"""
    list_display = ['name_product', 'price_1', 'price_2', 'in_stock']
    list_filter = ['in_stock', 'category']
    list_editable = ['in_stock', 'price_1', 'price_2']
    search_fields = ['brand_of_cardboard']
    list_display_links = ['name_product']
    form = ProductAdminForm


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    readonly_fields = ['products', 'name', 'phone_number', 'created', 'address']
    list_display = ['user', 'name']
    list_display_links = ['user']


admin.site.register(Basket)
