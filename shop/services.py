from django.shortcuts import get_object_or_404, render, get_list_or_404, redirect
from django.contrib import messages
from .models import Basket, Product
from .forms import OrderForm


class BasketController:
    def show_products(self, request, ):
        user_basket, created = Basket.objects.get_or_create(user=request.user)
        products = user_basket.products.all()
        form = OrderForm()

        if products is None:
            return render(request, 'shop/show_basket.html', {'messsage': 'Корзина пуста}', 'form': form})
        else:
            return render(request, 'shop/show_basket.html',
                          {'user_basket': user_basket, 'products': products, 'form': form}, )

    def set_product(self, request, product_pk):
        book = get_object_or_404(Product, pk=product_pk)
        basket, created = Basket.objects.get_or_create(user=request.user)
        basket.products.add(book)

    def delete_product(self, request, product_pk):
        user_basket = Basket.objects.get(user=request.user.id)
        product = get_object_or_404(Product, pk=product_pk)
        user_basket.products.remove(product)
        user_basket.save()


class OrderCreator:

    def __init__(self, order_manager: 'OrderManager'):
        self._order_manager = order_manager

    def create(self, request):
        order = self._order_manager
        try:
            order.prepare_order(request)
            messages.info(request, 'Товар оформлен, с вами свяжутся')
            return redirect('show_basket')

        except (Exception, ValueError) as ext:
            message = 'Something went wrong'
            return render(request, 'shop/show_basket.html', context={'message': message})


class OrderManager:

    def prepare_order(self, request):
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.user = request.user
            basket = Basket.objects.get(user=request.user)
            products = basket.products.all()
            for product in products:
                form.products.add(product)
            form.save()
            basket.delete()
        else:
            message = 'Введите данные или добавьте товар в корзину'
            return render(request, 'shop/show_basket.html', context={'message': message})
