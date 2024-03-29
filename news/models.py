from django.db import models
from django.utils import timezone


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок', help_text='не больше 50 символов', blank=False)
    text = models.TextField(verbose_name='Содержание', blank=False)
    published = models.BooleanField(verbose_name='Опубликовать', default=False)
    image = models.ImageField(upload_to='shop/news')
    created = models.DateTimeField(verbose_name='Дата создания', default=timezone.now())
    slug = models.SlugField(help_text='Заполняется автоматически')

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title


class Reviews(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=40, blank=False)
    reviews = models.TextField(verbose_name='Отзыв', blank=False)
    date = models.DateTimeField(verbose_name='Дата создания', default=timezone.now())
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
