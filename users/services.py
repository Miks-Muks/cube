from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from .models.Profile import Profile


class CreateDefaultProfile:

    @staticmethod
    def create_default_profile(user):
        return Profile.objects.create(user=user)
