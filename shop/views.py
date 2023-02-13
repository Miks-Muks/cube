from django.shortcuts import render
from .models import Category


# Create your views here.

def home(request):
    category = Category.objects.all()[:3]
    return render(request, 'shop/home.html', {'cat': category})


def all_categories(request):
    categories = category = Category.objects.all()
    return render(request, 'shop/all_category.html', {'cat': categories})
