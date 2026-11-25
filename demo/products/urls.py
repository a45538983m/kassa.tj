from django.urls import include, path
from rest_framework import routers

from .views import OverheadViewSet, ProductViewSet, WarehouseViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'warehouse', WarehouseViewSet, basename='warehouse')
router.register(r'overheads', OverheadViewSet, basename='overhead')

urlpatterns = [
    path('', include(router.urls)),
]
