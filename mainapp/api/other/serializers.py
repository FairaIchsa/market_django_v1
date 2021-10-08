from rest_framework import serializers

from ...models import *


class MenuCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = [
            'name', 'url',
        ]


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name', 'slug', 'subcategories',
        ]
        depth = 1
