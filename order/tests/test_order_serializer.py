from django.test import TestCase
from django.contrib.auth.models import User
from product.models import Product
from order.models import Order
from order.serializers import OrderSerializer


class OrderSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="john", password="test123")

        self.product1 = Product.objects.create(
            title="Dipirona",
            description="500 mg",
            price=20,
            active=True
        )
        self.product2 = Product.objects.create(
            title="Paracetamol",
            description="750 mg",
            price=15,
            active=True
        )

        self.order = Order.objects.create(user=self.user)
        self.order.product.add(self.product1, self.product2)

    def test_order_serializer_data(self):
        serializer = OrderSerializer(instance=self.order)
        data = serializer.data

        # Verifica os produtos serializados
        self.assertEqual(len(data["product"]), 2)
        self.assertEqual(data["product"][0]["title"], "Dipirona")
        self.assertEqual(data["product"][1]["title"], "Paracetamol")

        # Verifica o total
        self.assertEqual(data["total"], 35)
