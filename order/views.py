from rest_framework import viewsets
from order.models.order import Order
from order.serializers.order_serializer import OrderSerializer
from .permissions import IsAuthenticatedCustom

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedCustom]

