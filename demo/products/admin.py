from django.contrib import admin

# Register your models here.
from .models import Product
from .models import Warehouse
from .models import Overhead

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['nameproduct','code']
    list_filter=['nameproduct']

@admin.register(Warehouse)
class WarehousAdmin(admin.ModelAdmin):
    list_display = ['namewar','price','remainder']
    list_filter=['namewar']

@admin.register(Overhead)
class OverheadAdmin(admin.ModelAdmin):
    list_display = ['nameover','price','quantity']
    list_filter = ['nameover']



