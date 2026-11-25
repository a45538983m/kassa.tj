from rest_framework import serializers

from ..models import Overhead, Product, Warehouse


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'nameproduct', 'code']


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['id', 'namewar', 'price', 'remainder']


class OverheadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Overhead
        fields = ['id', 'nameover', 'price', 'quantity']
