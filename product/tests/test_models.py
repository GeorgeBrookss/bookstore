from django.test import TestCase
from product.models import Product, Category


class ProductTestCase(TestCase):

    def test_product_criado(self):
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

        self.assertEqual(product.title, "Dipirona")
        self.assertEqual(product.description, "500 mg uma vez ao dia")
        self.assertEqual(product.price, 20)
        self.assertTrue(product.active)
        self.assertEqual(product.category.count(), 1)
        self.assertEqual(product.category.first().title, "Remédios")

    def test_category_criado(self):
        category = Category.objects.create(
            title="Remédios",
            slug="remedios",
            description="Medicamentos em geral",
            active=True
        )

        self.assertEqual(category.title, "Remédios")
        self.assertEqual(category.slug, "remedios")
        self.assertEqual(category.description, "Medicamentos em geral")
        self.assertTrue(category.active)
