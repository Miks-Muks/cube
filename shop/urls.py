from django.urls import path
from .views import home, all_categories, product_category, product_detail, show_basket

urlpatterns = [
    path('', home, name='home'),
    path('all_categories/', all_categories, name='all_categories'),
    path('all_categories/product_category/<int:category_pk>', product_category, name='product_category'),
    path('product_detail/<int:product_pk>', product_detail, name='product_detail'),
    path('show basket', show_basket, name='show_basket'),
]
