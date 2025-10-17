from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from order import viewsets
from order.models.order import Order
from order.serializers.order_serializer import OrderSerializer

# Create your views here.

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]