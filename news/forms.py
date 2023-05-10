from django import forms

from .models import Reviews


class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = [
            'name',
            'reviews'
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'reviews': forms.TextInput(attrs={'class': 'form-control'}),
        }

