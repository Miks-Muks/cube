from django.urls import path
from .views import home, all_categories

urlpatterns = [
    path('', home, name='home'),
    path('all_categories/', all_categories, name='all_categories'),
]
