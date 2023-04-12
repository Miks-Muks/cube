from django.urls import path
from news.views import (NewsView,
                        PaymentView,
                        NewsDetailView,
                        DeliveryView,
                        ReviewsCreateView,
                        DiscontView,)

urlpatterns = [
    path('news', NewsView.as_view(), name='news'),
    path('payment', PaymentView.as_view(), name='payment'),
    path('detail/<slug:slug>', NewsDetailView.as_view(), name='detail'),
    path('delivery', DeliveryView.as_view(), name='delivery'),
    path('reviews', DeliveryView.as_view(), name='reviews'),
    path('discont', DiscontView.as_view(), name='discont'),
    path('create', ReviewsCreateView.as_view(), name='create'),
]
