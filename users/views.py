from django.shortcuts import render, redirect
from django.views import (
    View,
)
from django.contrib.auth import authenticate, login
from .forms.auth_form import UserCreateForm
from .services import CreateDefaultProfile


# Create your views here.


class RegisterView(View):
    template_name = 'registration/register.html'

    def get(self, request):
        form = UserCreateForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = UserCreateForm(request.POST)

        if form.is_valid():
            form.save(commit=False)
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            form.save()
            user = authenticate(email=email, password=password)
            profile = CreateDefaultProfile.create_default_profile(user=user)
            print(profile)
            login(request, user)
            return redirect('shop:home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
