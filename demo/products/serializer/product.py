from rest_framework import serializers
from ..models import Product,Warehouse,Overhead

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fileds = ['name','code']

class WarehouseSerializer(serializers.ModelSerialzer):
    class Meta:
        model = Warehouse
        fileds = ['namewar','price','remainder']

class OverheadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Overhead
        fields = ['nameover','price','quantity']