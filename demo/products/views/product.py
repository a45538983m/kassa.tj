from rest_framework import viewsets

from products.models import Overhead, Product, Warehouse
from products.serializer import (
    OverheadSerializer,
    ProductSerializer,
    WarehouseSerializer,
)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.select_related('namewar').order_by('id')
    serializer_class = WarehouseSerializer


class OverheadViewSet(viewsets.ModelViewSet):
    queryset = Overhead.objects.select_related('nameover').order_by('id')
    serializer_class = OverheadSerializer
