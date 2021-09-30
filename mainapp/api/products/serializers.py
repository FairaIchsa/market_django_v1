from rest_framework import serializers

from ...models import *


class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    subcategory = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'category', 'subcategory', 'name', 'slug', 'description',
            'price', 'quantity', 'sale', 'is_popular', 'image',
        ]
        depth = 1

    @staticmethod
    def get_category(obj):
        return CategoryForProductSerializer(Category.objects.get(id=obj.category.id)).data

    @staticmethod
    def get_subcategory(obj):
        return SubcategoryForProductSerializer(Subcategory.objects.get(id=obj.subcategory.id)).data


class CategoryForProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name', 'slug',
        ]


class SubcategoryForProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = [
            'name', 'slug',
        ]
