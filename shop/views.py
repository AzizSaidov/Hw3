from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *
from .models import *

from .pagination import ProductPagination
from .filters import *




@api_view(['GET'])
def get_all_products(request):
    products = Product.objects.all()

    products = category_filter(products, request.GET)
    products = price_filter(products, request.GET)
    products = search_filter(products, request.GET)

    paginator = ProductPagination()

    paginated_queryset = paginator.paginate_queryset(products, request)

    serializer = ProductSerializer(paginated_queryset, many=True)
    return paginator.get_paginated_response(serializer.data)




@api_view(['GET'])
def get_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error':'Not found'}, status=404)
    
    serializers = ProductSerializer(product)
    return Response(serializers.data)



@api_view(['POST'])
def create_productds(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors)



@api_view(['PUT'])
def update_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error':'Not found'}, status=404)
    
    serializers = ProductSerializer(product, data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    return Response(serializers.errors)



@api_view(['DELETE'])
def delete_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)

    product.delete()
    return Response(status=204)








@api_view(['GET'])
def get_reviews(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)




@api_view(['POST'])
def create_review(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors)
