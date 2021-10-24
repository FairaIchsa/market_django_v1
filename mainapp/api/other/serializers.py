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


class SliderTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderText
        fields = [
            'id', 'main', 'base',
        ]


class SliderInfoSerializer(serializers.ModelSerializer):
    content = SliderTextSerializer(many=True)

    class Meta:
        model = SliderInfo
        fields = [
            'id', 'img', 'main', 'base', 'content',
        ]
