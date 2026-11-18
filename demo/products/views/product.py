from rest_framework import generics
from products.models.product import Product
from products.serializer.product import ProductSerializer
from rest_framework import viewsets

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer