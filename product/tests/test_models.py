from django.test import TestCase

from product.models import category, product
from ..models import Category


class ProductTestCase(TestCase):
    
    
    def test_product_criado(self):
        
        Category = Category.objects.create(
            title='Remédios',
            slug='remédios',
            description='Medicamentos em geral',
            active=True
        )
        
        Product = Product.objects.create(
            title='Dipirona',
            description='500 mg uma vez ao dia',
            price=20,
            active=True
        )
        
        product.category.add(Category)
    
        self.assertEqual(product.title, 'Dipirona')
        self.assertEqual(product.description, '500 mg uma vez ao dia')
        self.assertEqual(product.price, 20)
        self.assertEqual(product.active)   
        self.assertEqual(product.category.count(), 1)
        self.assertEqual(product.category.first().name, "Remédios")

            
        
    def test_category_criado(self):
        Category = Category.objects.create(
            title='Remédios',
            slug='remédios',
            description='Medicamentos em geral',
            active=True
        )
    
        
        self.assertEqual(category.title, "Remédios")
        self.assertEqual(category.slug, "remedios")
        self.assertEqual(category.description, "Medicamentos em geral")
        self.assertTrue(category.active)