from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import News


# Create your views here.


class NewsView(ListView):
    template_name = 'news/news.html'
    queryset = News.objects.filter(published=True)
    context_object_name = 'news'


class PaymentView(TemplateView):
    template_name = 'news/payment.html'


class DeliveryView(TemplateView):
    template_name = 'news/delivery.html'


class DiscontView(TemplateView):
    template_name = 'news/discont.html'


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/detail.html'
