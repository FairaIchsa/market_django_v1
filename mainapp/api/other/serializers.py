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


class SliderInfoSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()

    class Meta:
        model = SliderInfo
        fields = [
            'id', 'img', 'main', 'base', 'content'
        ]

    @staticmethod
    def get_content(obj):
        return {
            'text_1': {'main': obj.text_1_main, 'base': obj.text_1_base},
            'text_2': obj.text_2,
            'text_3': {'main': obj.text_3_main, 'base': obj.text_3_base},
            'text_4': obj.text_4,
            }
