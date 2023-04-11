from django.urls import path
from news.views import NewsView, PaymentView, NewsDetailView

urlpatterns = [
    path('news', NewsView.as_view(), name='news'),
    path('payment', PaymentView.as_view(), name='payment'),
    path('detail/<slug:slug>', NewsDetailView.as_view(), name='detail'),
]
