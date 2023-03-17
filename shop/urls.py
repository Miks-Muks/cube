from django.urls import path

from shop import views
from .services import send_sms

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contacts', views.ContactView.as_view(), name='contacts'),
    path('all_categories/', views.CategoryList.as_view(), name='all_categories'),
    path('all_product_category/<slug:slug>', views.AllProductCategory.as_view(), name='all_product_category'),
    path('product_detail/<int:product_pk>', views.ProductDetail.as_view(), name='product_detail'),
    path('show basket', views.show_basket, name='show_basket'),
    path('add_to_basket/<int:product_pk>', views.add_to_basket, name='add_to_basket'),
    path('send_sms', send_sms, name='send_sms'),
    path('sigh_up', views.sigh_up, name='sigh_up_user'),
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('delete_product/<int:product_pk>', views.delete_product, name='delete_product'),

    path('create_order', views.create_order, name='create_order'),
]
    