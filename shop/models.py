from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=70, verbose_name='Название категории', unique=True)
    slug = models.SlugField(max_length=70, unique=True)
    image_cat = models.ImageField(verbose_name='Фотография категории', upload_to='shop/images_cat')

    class Meta:
        verbose_name = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name_product = models.CharField(verbose_name='Имя товара', max_length=100)
    description = models.TextField(verbose_name='Описание товара', help_text='Введите подробное описание товара')
    size = models.CharField(verbose_name='Размеры Товара', max_length=30)
    brand_of_cardboard = models.CharField(verbose_name='Марка картона', max_length=50)
    price_1 = models.FloatField(verbose_name='Цена от 1', blank=False)
    price_2 = models.FloatField(verbose_name='Цена от 100 шт', blank=False)
    price_3 = models.FloatField(verbose_name='Цена от 1000 шт', blank=False)
    image = models.ImageField(verbose_name='Фотография товара', upload_to='shop/images')
    in_stock = models.BooleanField(verbose_name="В наличии")
    category = models.ForeignKey(Category, verbose_name='Выберите категорию товара', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        indexes = [models.Index(fields=['name_product', ])]

    def __str__(self):
        return self.name_product


class Orders(models.Model):
    products = models.ManyToManyField(Product, related_name='orders')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    number_phone = models.CharField(max_length=20, verbose_name='Номер телефона')

    class Meta:
        default_permissions = ('delete', 'view')
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


    def __str__(self):
        return f'{self.user}'


class Basket(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='product_basket')

    class Meta:
        verbose_name = 'Корзина'

    def __str__(self):
        return f'{self.user}'
