from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from .Category import Category


class Product(models.Model):
    name_product = models.CharField(verbose_name='Имя товара', max_length=100)
    description = models.TextField(verbose_name='Описание товара', help_text='Введите подробное описание товара')
    size = models.CharField(verbose_name='Размеры Товара', max_length=30)
    brand_of_cardboard = models.CharField(verbose_name='Марка картона', max_length=50)
    price_1 = models.FloatField(verbose_name='Цена от 1', blank=False)
    price_2 = models.FloatField(verbose_name='Цена от 100 шт', blank=False)
    image = models.ImageField(verbose_name='Фотография товара', upload_to='shop/images')
    in_stock = models.BooleanField(verbose_name="В наличии")
    category = models.ForeignKey(Category, verbose_name='Выберите категорию товара', on_delete=models.CASCADE)
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False, )
    image_thumbnail = ImageSpecField(source='image', processors=ResizeToFill(220, 310), format='jpeg')

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        indexes = [models.Index(fields=['name_product', ])]
        ordering = ['my_order', ]

    def __str__(self):
        return self.name_product
