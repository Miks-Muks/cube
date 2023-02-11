from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название категории')
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        verbose_name = 'Категория'
        indexes = models.Index(fields='name')
        image_cat = models.ImageField(verbose_name='Фотография категории', upload_to='/images_cat')

    def __str__(self):
        return self.name


class Product(models.Model):
    name_product = models.CharField(verbose_name='Имя товара', max_length=200)
    description = models.TextField(verbose_name='Описание товара')
    size = models.TextField(verbose_name='Размеры Товара')
    brand_of_cardboard = models.CharField(verbose_name='Марка картона', max_length=50)
    price_1 = models.FloatField(verbose_name='Цена от 10 до 99 шт', blank=False)
    price_2 = models.FloatField(verbose_name='Цена от 100 до 999 шт', blank=False)
    price_3 = models.FloatField(verbose_name='Цена от 1000 шт', blank=False)
    image = models.ImageField(verbose_name='Фотография товара', upload_to='/images')
    in_stock = models.BooleanField()

