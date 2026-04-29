from django.core.cache import cache
from rest_framework import generics
from rest_framework.response import Response

from .filters import category_filter, price_filter, search_filter
from .models import Product, Review
from .pagination import ProductPagination
from .serializers import ProductSerializer, ReviewSerializer


class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

    def get_queryset(self):
        products = Product.objects.all().order_by('id')
        products = category_filter(products, self.request.GET)
        products = price_filter(products, self.request.GET)
        return search_filter(products, self.request.GET)
    

    def list(self, request, *args, **kwargs):
        cache_key = f'products:{request.get_full_path()}'
        cached_data = cache.get(cache_key)
        print(cached_data)
        print(cache_key)
        if cached_data is not None:
            
            return Response(cached_data)

        response = super().list(request, *args, **kwargs)
        cache.set(cache_key, response.data, 60)
        return response


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        cache_key = f'product:{kwargs.get("pk")}'
        cached_data = cache.get(cache_key)
        if cached_data is not None:
            return Response(cached_data)

        response = super().retrieve(request, *args, **kwargs)
        cache.set(cache_key, response.data, 60)
        return response



class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save()
        cache.clear()


class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_update(self, serializer):
        serializer.save()
        cache.clear()


class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_destroy(self, instance):
        instance.delete()
        cache.clear()




class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all().order_by('id')
    serializer_class = ReviewSerializer


class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        serializer.save()
        cache.clear()
