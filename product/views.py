from rest_framework import viewsets
from product.models.product import Product
from product.serializers.product_serializer import ProductSerializer
from rest_framework.permissions import AllowAny

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer   
    permission_classes = [AllowAny]
    
