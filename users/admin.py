from django.contrib import admin

from .models.Profile import Profile
from .models.User import CustomUser

# Register your models here.

admin.site.register(Profile)
admin.site.register(CustomUser)
