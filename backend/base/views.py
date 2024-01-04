
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .products import products
from .models import Product
from .serializers import ProductSerializer

def getRouters(request):
    return JsonResponse("Welcome to Python world", safe=False)
@api_view(['GET'])
def getHome(request):
        routes = [
            '/api/products/',                # List all products
            '/api/products/create/',         # Create a new product
            '/api/products/<int:pk>/',       # Retrieve a single product
            '/api/products/<int:pk>/update/',# Update a product
            '/api/products/<int:pk>/delete/',# Delete a product
            '/api/products/<int:pk>/reviews/',               # List all reviews for a product
            '/api/products/<int:pk>/reviews/create/',        # Create a new review for a product
            '/api/products/<int:pk>/reviews/<int:review_pk>/', # Retrieve a single review
            '/api/products/<int:pk>/reviews/<int:review_pk>/update/',  # Update a review
            '/api/products/<int:pk>/reviews/<int:review_pk>/delete/',  # Delete a review
        ]
        return Response(routes)
@api_view(['GET', 'POST'])
def getProducts(request):
     products = Product.objects.all()
     serializer = ProductSerializer(products, many=True)
     return Response(serializer.data)
@api_view(['GET'])
def ProductDetail(request, pk):
    try:
        product = Product.objects.get(_id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({"message": "Product not found"}, status=404)