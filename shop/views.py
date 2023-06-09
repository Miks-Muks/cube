from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages

from .models import Category, Product, Basket, Orders
from .forms import OrderForm
from .services import send_sms


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


class ProductDetail(DetailView):
    model = Product
    pk_url_kwarg = 'product_pk'


@login_required
def add_to_basket(request, product_pk):
    book = get_object_or_404(Product, pk=product_pk)
    basket, created = Basket.objects.get_or_create(user=request.user)
    basket.products.add(book)
    messages.success(request, 'Товар добавлен в корзину')
    basket.save()
    return redirect('product_detail', product_pk=product_pk)


@login_required
def show_basket(request):
    try:
        form = OrderForm()
        user_basket = Basket.objects.prefetch_related('products').get(user=request.user.id)
        products = user_basket.products.all()

        return render(request, 'shop/show_basket.html',
                      {'user_basket': user_basket, 'products': products, 'form': form})
    except Exception:
        return render(request, 'shop/show_basket.html', {'message': 'Корзина пуста'})
    except AttributeError as ext:

        return render(request, 'shop/show_basket.html', {'message': 'Корзина пуста'})


@login_required
def delete_product(request, product_pk):
    user_basket = Basket.objects.get(user=request.user.id)
    messages.success(request, 'Товар добавлен')
    product = get_object_or_404(Product, pk=product_pk)
    user_basket.products.remove(product)
    user_basket.save()

    return redirect('show_basket')


@login_required
def create_order(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST['name']
        address = request.POST['address']
        created = timezone.now()
        phone_number = request.POST['phone_number']
        check_fields = (name, phone_number)
        if all(check_fields):
            order = Orders.objects.create(user=user, name=name,
                                          phone_number=phone_number, created=created, address=address)
            try:
                basket = Basket.objects.get(user=request.user)
                products = basket.products.all()
                for product in products:
                    order.products.add(product)
                order.save()
                # send_sms(request)
                basket.delete()
                messages.info(request, 'Товар оформлен, с вами свяжутся')
                return redirect('show_basket')
            except ValueError:
                message = 'Введите данные или добавьте товар в корзину'
                return render(request, 'shop/show_basket.html', context={'message': message})

        else:
            return render(request, 'shop/show_basket.html',
                          context={'message': 'Введите данные или добавьте товар в корзину'})


# View для Auth
def sigh_up(request):
    if request.method == 'GET':
        return render(request, 'shop/signup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'shop/signup.html', {'form': UserCreationForm(),
                                                            'error': 'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'shop/signup.html',
                          {'form': UserCreationForm(), 'error': 'Passwords did not match'})


def login_user(request):
    if request.method == 'GET':
        return render(request, 'shop/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'shop/login.html',
                          {'form': AuthenticationForm(), 'error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect('home')


@login_required
def logout_user(request):
    logout(request)
    return redirect('home')
