from django.shortcuts import get_object_or_404, render, get_list_or_404

from .models import Basket, Product
from .forms import OrderForm


class BasketController:
    def show_products(self, request, ):
        user_basket, created = Basket.objects.get_or_create(user=request.user)
        products = user_basket.products.all()
        form = OrderForm()

        if user_basket is None:
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
