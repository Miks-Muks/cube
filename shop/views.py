from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Category, Product, Basket, Orders
from .forms import OrderForm


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
        return self.model.objects.filter(category__slug=self.kwargs['slug'], in_stock=True).select_related(
            'category')


class ProductDetail(DetailView):
    model = Product
    pk_url_kwarg = 'product_pk'


@login_required
def add_to_basket(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    basket = Basket.objects.filter(user=request.user.id)
    if basket is None:
        basket = Basket.objects.create(user=request.user.id)
    basket.products.add(product)
    return redirect('product_detail', product_pk=product.id)

@login_required
def show_basket(request):
    user_basket = Basket.objects.filter(user=request.user.id).first()
    products = user_basket.products.all()
    return render(request, 'shop/show_basket.html', {'user_basket': user_basket, 'products': products})


def delete_from_bakset(request, pk_product):
    user_basket = Basket.objects.filter(user=request.user.id).first()
    product = get_object_or_404(Product, pk=pk_product)
    user_basket.products


def sigh_up(request):
    if request.method == "GET":
        form = UserCreationForm
        return render(request, 'shop/signup.html', context={'form': form})
    else:
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password2'])
                user.save()
                login(request, user)
                return redirect(to='HomeView')
            except IntegrityError as ext:
                print(ext)
                return render(request, 'shop/signup.html', {'form': UserCreationForm,
                                                            'error': 'That username has already been taken. Please choose a new username'})


def login(request):
    if request.method == 'GET':
        form = AuthenticationForm
        return render(request, 'shop/login.html', context={'form': form})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('HomeView')
        else:
            return render(request, 'shop/login.html',
                          context={'form': AuthenticationForm(), 'error': 'Username and password did not match'})

