from django.contrib import admin

from .models import Overhead, Product, Warehouse


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['nameproduct', 'code']
    search_fields = ['nameproduct', 'code']


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['namewar', 'price', 'remainder']
    list_filter = ['namewar']


@admin.register(Overhead)
class OverheadAdmin(admin.ModelAdmin):
    list_display = ['nameover', 'price', 'quantity']
    list_filter = ['nameover']
