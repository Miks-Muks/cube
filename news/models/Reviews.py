from django.db import models
from django.utils import timezone

from core.settings.base import AUTH_USER_MODEL


class Reviews(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=40, blank=False)
    reviews = models.TextField(verbose_name='Отзыв', blank=False)
    date = models.DateTimeField(verbose_name='Дата создания', default=timezone.now())
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
