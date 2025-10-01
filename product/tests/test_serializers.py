from django.test import TestCase
from product.models import Category
from product.serializers.category_serializer import CategorySerializer


class CategorySerializerTest(TestCase):
    def test_category_serialization(self):
        category = Category.objects.create(
            title="Remédios",
            slug="remedios",
            description="Medicamentos em geral",
            active=True,
        )

        serializer = CategorySerializer(category)
        data = serializer.data

        self.assertEqual(data["title"], "Remédios")
        self.assertEqual(data["slug"], "remedios")
        self.assertEqual(data["description"], "Medicamentos em geral")
        self.assertTrue(data["active"])

    def test_category_deserialization(self):
        data = {
            "title": "Cosméticos",
            "slug": "cosmeticos",
            "description": "Produtos de beleza",
            "active": True,
        }

        serializer = CategorySerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        validated = serializer.validated_data

        self.assertEqual(validated["title"], "Cosméticos")
        self.assertEqual(validated["slug"], "cosmeticos")
        self.assertEqual(validated["description"], "Produtos de beleza")
        self.assertTrue(validated["active"])
