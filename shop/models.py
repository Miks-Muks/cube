from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=70, verbose_name='Название категории', unique=True)
    slug = models.SlugField(max_length=70, unique=True)
    image_cat = models.ImageField(verbose_name='Фотография категории', upload_to='shop/images_cat')

    class Meta:
        verbose_name = 'Категория'

    def __str__(self):
        return self.name


class Product(models.Model):
    name_product = models.CharField(verbose_name='Имя товара', max_length=100)
    description = models.TextField(verbose_name='Описание товара')
    size = models.TextField(verbose_name='Размеры Товара')
    brand_of_cardboard = models.CharField(verbose_name='Марка картона', max_length=50)
    price_1 = models.FloatField(verbose_name='Цена от 10 до 99 шт', blank=False)
    price_2 = models.FloatField(verbose_name='Цена от 100 до 999 шт', blank=False)
    price_3 = models.FloatField(verbose_name='Цена от 1000 шт', blank=False)
    image = models.ImageField(verbose_name='Фотография товара', upload_to='shop/images')
    in_stock = models.BooleanField(verbose_name="В наличии")
    category = models.ForeignKey(Category, verbose_name='Выберите категорию товара', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Товары"

    def __str__(self):
        return self.name_product


class Orders(models.Model):
    products = models.ManyToManyField(Product, related_name='orders')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'


class Basket(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='product_basket')

    class Meta:
        verbose_name = 'Корзина'

    def __str__(self):
        return f'{self.user}'
