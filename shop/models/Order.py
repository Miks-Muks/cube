from django.db import models
from core.settings.base import AUTH_USER_MODEL
from phone_field import PhoneField

from .Product import Product


class Orders(models.Model):
    products = models.ManyToManyField(Product, related_name='orders')
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = PhoneField(blank=True, help_text='Номер телефона заказчика')
    name = models.CharField(max_length=30, verbose_name='ФИО', blank=True)
    created = models.DateTimeField(verbose_name='Дата создания ')
    address = models.CharField(verbose_name='Адресс доставки', max_length=70, default='Чистопольская ул. 7, Казань')

    class Meta:
        default_permissions = ('delete', 'view')
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.user}'
