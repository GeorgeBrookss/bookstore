import json
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from product.factories import CategoryFactory, ProductFactory
from order.factories import UserFactory, OrderFactory
from order.models import Order


class TestOrderViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.user = UserFactory()
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        self.category = CategoryFactory(title="technology")
        self.product = ProductFactory(
            title="mouse", price=100, category=[self.category]
        )

        self.order = OrderFactory(user=self.user, product=[self.product])

    def test_order_list(self):
        response = self.client.get(reverse("order-list", kwargs={"version": "v1"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()

        if "results" in data:
            order_data = data["results"][0]
        else:
            order_data = data[0]

        self.assertEqual(order_data["product"][0]["title"], self.product.title)
        self.assertEqual(order_data["product"][0]["price"], self.product.price)
        self.assertEqual(
            order_data["product"][0]["category"][0]["title"], self.category.title
        )

    def test_create_order(self):
        product = ProductFactory()
        data = json.dumps({"products_id": [product.id]})

        response = self.client.post(
            reverse("order-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_order = Order.objects.filter(user=self.user).last()
        self.assertEqual(created_order.product.first().id, product.id)
