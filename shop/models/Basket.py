from django.db import models
from core.settings.base import AUTH_USER_MODEL
from .Product import Product


class Basket(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    products = models.ManyToManyField(Product, related_name='product_basket',
                                      verbose_name='Товары добавленные в корзину', null=True, )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'{self.user}'
