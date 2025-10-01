from rest_framework import serializers
from product.serializers.product_serializer import ProductSerializer
from product.models.product import Product
from ..models.order import Order


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(required=False, many=True, read_only=True)
    products_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), write_only=True, many=True
    )
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        return sum([product.price for product in instance.product.all()])

    class Meta:
        model = Order
        fields = ["product", "total", "products_id"]

    def create(self, validated_data):
        products_data = validated_data.pop("products_id")
        user = self.context["request"].user  # pega usuário do token
        order = Order.objects.create(user=user)
        order.product.set(products_data)
        return order
