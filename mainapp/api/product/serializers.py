from rest_framework import serializers
from itertools import chain

from ...product_models import *


# sub serializers #######################

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


class SaleForProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = [
            'is_active', 'sale_modifier',
        ]


# class StatusForProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Status
#         fields = [
#             'name', 'text',
#         ]

class DescriptionForProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = [
            'content', 'position',
        ]


class SubImagesForProductSerializer(serializers.Serializer):
    sub_image = serializers.URLField()


class BallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ball
        exclude = [
            'product',
        ]


class TennisTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TennisTable
        exclude = [
            'product',
        ]


# main serializers #######################


class ProductListSerializer(serializers.ModelSerializer):
    category = CategoryForProductSerializer()
    subcategory = SubcategoryForProductSerializer()
    in_sale = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    # status = StatusForProductSerializer()

    class Meta:
        model = Product
        fields = [
            'id', 'category', 'subcategory', 'name', 'slug', 'description',
            'price', 'quantity', 'in_sale', 'is_popular', 'status', 'image',
        ]
        depth = 1

    @staticmethod
    def get_in_sale(obj):
        if obj.sale:
            return obj.sale.is_active
        return False

    @staticmethod
    def get_description(obj):
        if obj.description.first() is not None:
            return obj.description.get(position=0).content
        return None


class ProductRetrieveSerializer(serializers.ModelSerializer):
    category = CategoryForProductSerializer()
    subcategory = SubcategoryForProductSerializer()
    sale = SaleForProductSerializer()
    description = DescriptionForProductSerializer(many=True)
    images = serializers.SerializerMethodField()
    # status = StatusForProductSerializer()
    child_product_data = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'category', 'subcategory', 'name', 'slug', 'description',
            'price', 'quantity', 'sale', 'is_popular', 'status', 'images',
            'child_product_data',
        ]
        depth = 0

    @staticmethod
    def get_images(obj):    # это наверняка можно написать лучше
        return chain(Product.objects.filter(id=obj.id).values_list('image', flat=True),
                     obj.images.all().values_list('sub_image', flat=True))

    @staticmethod
    def get_child_product_data(obj):
        slug = obj.category.slug
        if slug == 'balls':
            return BallSerializer(Ball.objects.get(product=obj)).data
        elif slug == 'tennis_tables':
            return TennisTableSerializer(TennisTable.objects.get(product=obj)).data
