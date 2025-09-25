import factory

from product.models import Product
from product.models import Category

class CatergoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('pystr')
    slug = factory.Faker('pystr')
    description = factory.Faker('pystr')
    active = factory.Iterator([True, False])
    
    class meta:
        model = Category
        
class ProductFactory(factory.django.DjangoModelFactory):
    price = factory.Faker('pyint')
    category = factory.LazyAttribute(CatergoryFactory)
    title = factory.Faker('pystr')
    
    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return
        
        if extracted:
            for category in extracted:
                self.category.add(category)
                
    class meta:
        model = Product