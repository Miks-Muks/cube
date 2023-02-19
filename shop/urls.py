from django.urls import path
from .views import home, all_categories, all_product_category, product_detail, show_basket, add_to_basket

urlpatterns = [
    path('', home, name='home'),
    path('all_categories/', all_categories, name='all_categories'),
    path('all_product_category/<int:category_pk>', all_product_category, name='all_product_category'),
    path('product_detail/<int:product_pk>', product_detail, name='product_detail'),
    path('show basket', show_basket, name='show_basket'),
    path('add_to_basket/<int:product_pk>', add_to_basket, name='add_to_basket'),
]
