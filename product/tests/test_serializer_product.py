from rest_framework import serializers
from product.models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    # Campo de leitura: mostra objetos Category no GET
    category = serializers.StringRelatedField(many=True, read_only=True)

    # Campo de escrita: aceita IDs de Category no POST/PUT
    categories_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        many=True,
        write_only=True
    )

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'active', 'category', 'categories_id']

    def create(self, validated_data):
        categories = validated_data.pop('categories_id', [])
        product = Product.objects.create(**validated_data)
        product.category.set(categories)  # adiciona as categorias corretamente
        return product

    def update(self, instance, validated_data):
        categories = validated_data.pop('categories_id', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if categories is not None:
            instance.category.set(categories)
        instance.save()
        return instance
