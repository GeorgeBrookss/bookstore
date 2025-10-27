from django.urls import path, include
from rest_framework import routers
from product.viewsets import ProductViewSet
from product.viewsets import CategoryViewSet
router = routers.SimpleRouter()
router.register(r'product', ProductViewSet, basename='product')
router.register(r'category', CategoryViewSet, basename='category')

urlpatterns = []