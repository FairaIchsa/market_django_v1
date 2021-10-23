from rest_framework import serializers

from ...product_models import Category, Subcategory
from ...other_models import *


class MenuCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        exclude = [
            'id',
        ]


class SubCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = [
            'name', 'slug',
        ]


class CategoryListSerializer(serializers.ModelSerializer):
    subcategories = SubCategoryListSerializer(many=True)

    class Meta:
        model = Category
        fields = [
            'name', 'slug', 'subcategories',
        ]
        depth = 1


class SliderInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderInfo
        exclude = [
            'id',
        ]
