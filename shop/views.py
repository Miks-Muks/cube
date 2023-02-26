from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView

from .models import Category, Product, Basket, Orders


# Create your views here.

class HomeView(TemplateView):
    template_name = 'shop/home.html'


class CategoryList(ListView):
    model = Category
    context_object_name = 'cat'
    # queryset = Category.objects.all()
    template_name = 'shop/all_category.html'

    def get_queryset(self):
        return Category.objects.all()


def all_product_category(request, category_pk):
    products = Product.objects.filter(category__pk=category_pk).select_related('category')
    return render(request, 'shop/all_product_category.html', {'products': products})


class ProductDetail(DetailView):
    model = Product
    pk_url_kwarg = 'product_pk'


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
