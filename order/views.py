from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from order.models.order import Order
from order.serializers.order_serializer import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
