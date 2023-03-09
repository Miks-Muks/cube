from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView

from .models import Category, Product, Basket, Orders


# Create your views here.

class HomeView(TemplateView):
    """Home page"""
    template_name = 'shop/home.html'


class CategoryList(ListView):
    """View which present all category"""
    model = Category
    context_object_name = 'cat'
    template_name = 'shop/all_category.html'

    def get_queryset(self):
        return Category.objects.all()


class AllProductCategory(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop/all_product_category.html'

    def get_queryset(self):
        return self.model.objects.filter(category__pk=self.kwargs['category_pk'], in_stock=True).select_related(
            'category')


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
        user_basket = Basket.objects.filter(user=request.user.id)
        products = user_basket.products.all
        return render(request, 'shop/show_basket.html', {'user_basket': user_basket, 'products': products})
    except AttributeError:
        return render(request, 'shop/show_basket.html', {'user_basket': user_basket, 'error': 'Miss'})
