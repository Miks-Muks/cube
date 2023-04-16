from django.shortcuts import render, redirect
from django.views.generic import (TemplateView,
                                  ListView,
                                  CreateView,
                                  UpdateView,
                                  DetailView)
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import News, Reviews
from .forms import ReviewsForm


# View for information about company
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


# view for reviews
class ReviewsCreateView(LoginRequiredMixin, CreateView):
    login_url = "/login_user/"

    def get(self, request, *args, **kwargs):
        context = {'form': ReviewsForm()}
        return render(request, 'news/create_reviews.html', context)

    def post(self, request, *args, **kwargs):
        form = ReviewsForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews')
        messages.error(request, "Что-то пошло не так.")
        return render(request, 'news/create_reviews.html', {'form': form})


class ReviewsListView(ListView):
    template_name = 'news/reviews.html'
    queryset = Reviews.objects.all()
    context_object_name = 'reviews'
