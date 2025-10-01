from django.test import TestCase
from django.contrib.auth.models import User
from product.models import Product
from order.models import Order


class OrderModelTestCase(TestCase):
    def setUp(self):
        # Criar usuário
        self.user = User.objects.create_user(username="Wagner", password="teste123")

        # Criar produtos
        self.product1 = Product.objects.create(
            title="Dipirona", description="500 mg", price=20, active=True
        )
        self.product2 = Product.objects.create(
            title="Paracetamol", description="750 mg", price=15, active=True
        )

        # Criar pedido
        self.order = Order.objects.create(user=self.user)
        self.order.product.add(self.product1, self.product2)

    def test_order_products(self):
        self.assertEqual(self.order.product.count(), 2)
        self.assertIn(self.product1, self.order.product.all())
        self.assertIn(self.product2, self.order.product.all())

    def test_order_user(self):
        self.assertEqual(self.order.user.username, "Wagner")
