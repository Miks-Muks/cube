from django.db import models
from django.contrib.auth.models import AbstractUser

from .User import CustomUser


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile', default='default.jpg')
