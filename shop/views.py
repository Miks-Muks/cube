from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages

from .models import Category, Product
from .forms import OrderForm
from .task import send_sms
from .services import BasketController


# Create your views here.

class HomeView(TemplateView):
    """Home page"""
    template_name = 'shop/home.html'


class CategoryList(ListView):
    """View which present all category"""
    model = Category
    context_object_name = 'cat'
    template_name = 'shop/all_category.html'
    paginate_by = 4

    def get_queryset(self):
        return Category.objects.all()


class AllProductCategory(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop/all_product_category.html'

    def get_queryset(self):
        return self.model.objects.filter(category__slug=self.kwargs['slug'], in_stock=True).select_related(
            'category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class ProductDetail(DetailView):
    model = Product
    pk_url_kwarg = 'product_pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


@login_required
def add_to_basket(request, product_pk):
    controller = BasketController()
    controller.set_product(request, product_pk)
    return redirect('product_detail', product_pk=product_pk)


class BasketView(View):
    def get(self, request):
        controller = BasketController.show_products(request)

    def post(self, request):
        pass


# @login_required
# def show_basket(request):
#     controller = BasketController()
#     controller.show_products(request)


@login_required
def delete_product(request, product_pk):
    controller = BasketController()
    controller.delete_product(request, product_pk)
    return redirect('show_basket')


@login_required
def create_order(request):
    pass

