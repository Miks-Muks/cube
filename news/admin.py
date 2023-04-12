from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import News, Reviews


# Register your models here.

class ProductAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget(), label='Описание')

    class Meta:
        model = News
        fields = '__all__'


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}
    form = ProductAdminForm


admin.site.register(Reviews)