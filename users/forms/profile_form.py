from django import forms

from users.models.Profile import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'})
        }
