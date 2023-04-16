from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from shop.models import Category, Product, Basket
from news.models import Reviews, News

from .serializers import (CategorySerializer,
                          ProductSerializer,
                          ReviewsSerializer,
                          NewsSerializer,
                          )


class CatalogView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response({'cat': serializer.data})


class ProductView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        products = Product.objects.select_related('category').filter(pk=pk)
        serializer = ProductSerializer(products, many=True)
        return Response({'product': serializer.data})


class ProductAddView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        book = get_object_or_404(Product, pk=pk)
        basket, created = Basket.objects.get_or_create(user=request.user)
        basket.products.add(book)
        basket.save()
        return Response(status=status.HTTP_201_CREATED)


class NewsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, ):
        products = News.objects.all()
        serializer = NewsSerializer(products, many=True)
        return Response({'news': serializer.data})


class ReviewsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, ):
        products = Reviews.objects.all()
        serializer = ReviewsSerializer(products, many=True)
        return Response({'reviews': serializer.data})

    @login_required
    def post(self, request):
        serializer = ReviewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
