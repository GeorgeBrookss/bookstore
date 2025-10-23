import factory
from product.models.product import Product
from product.models.category import Category
import factory
from product.models import Category


class ProductFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('word')
    description = factory.Faker('sentence')
    price = factory.Faker('pydecimal', left_digits=3, right_digits=2, positive=True)
    active = True



    @factory.post_generation
    def category(self, create, extracted, **kwargs):
    
        if not create:
            return
        if extracted:
            for cat in extracted:
                self.category.add(cat)

    class Meta:
        model = Product


class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('word')
    slug = factory.Faker('slug')
    description = factory.Faker('sentence')
    active = True

    class Meta:
        model = Category
