from django.urls import path

from .views import HomeView, CategoryList, AllProductCategory, ProductDetail, show_basket, add_to_basket,create_order
from .services import send_sms

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('all_categories/', CategoryList.as_view(), name='all_categories'),
    path('all_product_category/<slug:slug>', AllProductCategory.as_view(), name='all_product_category'),
    path('product_detail/<int:product_pk>', ProductDetail.as_view(), name='product_detail'),
    path('show basket', show_basket, name='show_basket'),
    path('add_to_basket/<int:product_pk>', add_to_basket, name='add_to_basket'),
    path('send_sms>', send_sms, name='send_sms'),
    path('create_order', create_order, name='create_order'),
]
    