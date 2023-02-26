from django.urls import path
from .views import HomeView, CategoryList, all_product_category, ProductDetail, show_basket, add_to_basket

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('all_categories/', CategoryList.as_view(), name='all_categories'),
    path('all_product_category/<int:category_pk>', all_product_category, name='all_product_category'),
    path('product_detail/<int:product_pk>', ProductDetail.as_view(), name='product_detail'),
    path('show basket', show_basket, name='show_basket'),
    path('add_to_basket/<int:product_pk>', add_to_basket, name='add_to_basket'),
]
