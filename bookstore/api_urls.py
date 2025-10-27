from rest_framework import routers
from django.urls import path, include

from order.views import OrderViewSet
from product.views import ProductViewSet


router = routers.DefaultRouter()

router.register(r'product', ProductViewSet, basename='product')
router.register(r'order', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)), 
]