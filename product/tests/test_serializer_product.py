from django.test import TestCase
from product.models import Product, Category
from product.serializers.product_serializer import ProductSerializer


class ProductSerializerTest(TestCase):
    def test_product_serialization(self):
        category = Category.objects.create(
            title="Remédios",
            slug="remedios",
            description="Medicamentos em geral",
            active=True
        )

        product = Product.objects.create(
            title="Dipirona",
            description="500 mg uma vez ao dia",
            price=20,
            active=True
        )
        product.category.add(category)

        serializer = ProductSerializer(product)
        data = serializer.data

        self.assertEqual(data["title"], "Dipirona")
        self.assertEqual(data["description"], "500 mg uma vez ao dia")
        self.assertEqual(data["price"], 20)
        self.assertTrue(data["active"])
        self.assertEqual(len(data["category"]), 1)
        self.assertEqual(data["category"][0]["title"], "Remédios")

    def test_product_deserialization(self):
        category = Category.objects.create(
            title="Vitaminas",
            slug="vitaminas",
            description="Suplementos alimentares",
            active=True
        )

        data = {
            "title": "Vitamina C",
            "description": "Tomar 1 comprimido por dia",
            "price": 15,
            "active": True,
            "category": [
                {
                    "title": "Vitaminas",
                    "slug": "vitaminas",
                    "description": "Suplementos alimentares",
                    "active": True
                }
            ]
        }

        serializer = ProductSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        validated = serializer.validated_data

        self.assertEqual(validated["title"], "Vitamina C")
        self.assertEqual(validated["description"], "Tomar 1 comprimido por dia")
        self.assertEqual(validated["price"], 15)
        self.assertTrue(validated["active"])
        self.assertEqual(len(validated["category"]), 1)
        self.assertEqual(validated["category"][0]["title"], "Vitaminas")
