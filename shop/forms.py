from django import forms
from .models import Orders


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('phone_number', 'name', 'address', )
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-controll'}),
            'name': forms.TextInput(attrs={'class': 'form-controll'}),
            'address': forms.TextInput(attrs={'class': 'form-controll'}),
        }
