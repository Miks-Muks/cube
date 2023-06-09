from django.urls import path, include
from django.contrib.auth import urls

from users import views

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register', views.RegisterView.as_view(), name='register'),
]
