from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Basket, Orders


# Create your views here.

def home(request):
    return render(request, 'shop/home.html')


def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'shop/all_category.html', {'cat': categories})


def all_product_category(request, category_pk):
    category = Category.objects.select_releted('product')
    return render(request, 'shop/all_product_category.html', {'products': products, 'cat': category})


def product_detail(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    return render(request, 'shop/product_detail.html', {'product': product})


def add_to_basket(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    basket = Basket.objects.filter(user=request.user).first()
    if basket is None:
        basket = Basket.objects.create(user=request.user)
    basket.product.add(product)
    return redirect('product_detail', product_pk=product.id)


def show_basket(request):
    try:
        user_basket = Basket.objects.filter(user=request.user).first()
        products = user_basket.products.all
        return render(request, 'shop/show_basket.html', {'user_basket': user_basket, 'products': products})
    except AttributeError:
        return render(request, 'shop/show_basket.html', {'user_basket': user_basket, 'error': 'Miss'})

