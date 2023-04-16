from django.urls import path
from api import views

urlpatterns = [
    path('all_cat', views.CatalogView.as_view()),
    path('products/<int:pk>', views.ProductView.as_view()),
    path('products_add/<int:pk>', views.ProductAddView.as_view()),
    path('reviews', views.ReviewsView.as_view()),
    path('news', views.NewsView.as_view()),
]
