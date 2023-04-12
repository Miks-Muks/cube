from django.shortcuts import render, redirect
from django.views.generic import (TemplateView,
                                  ListView,
                                  CreateView,
                                  UpdateView,
                                  DetailView)
from django.contrib import messages


from .models import News
from .forms import ReviewsForm


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
    context_object_name = 'news'


class ReviewsCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': ReviewsForm()}
        return render(request, 'news/create_reviews.html', context)

    def post(self, request, *args, **kwargs):
        form = ReviewsForm(request.POST)
        if form.is_valid():
            book = form.save()
            book.save()
            return redirect('reviews')
        messages.error(request, "Document deleted.")
        return render(request, 'news/create_reviews.html', {'form': form})