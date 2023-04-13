from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductsSerializer

# Create your views here.


class ProductsViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
