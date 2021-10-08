from rest_framework import serializers
from itertools import chain

from ...models import *


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


class StatusForProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'name', 'text',
        ]


class SubImagesForProductSerializer(serializers.Serializer):
    sub_image = serializers.URLField()


# main serializers #######################


class ProductListSerializer(serializers.ModelSerializer):
    category = CategoryForProductSerializer()
    subcategory = SubcategoryForProductSerializer()
    in_sale = serializers.SerializerMethodField()
    status = StatusForProductSerializer()

    class Meta:
        model = Product
        fields = [
            'id', 'category', 'subcategory', 'name', 'slug', 'description',
            'price', 'quantity', 'in_sale', 'is_popular', 'status', 'image',
        ]

    @staticmethod
    def get_in_sale(obj):
        return obj.sale.is_active


class ProductRetrieveSerializer(serializers.ModelSerializer):
    category = CategoryForProductSerializer()
    subcategory = SubcategoryForProductSerializer()
    sale = SaleForProductSerializer()
    images = serializers.SerializerMethodField()
    status = StatusForProductSerializer()

    class Meta:
        model = Product
        fields = [
            'id', 'category', 'subcategory', 'name', 'slug', 'description',
            'price', 'quantity', 'sale', 'is_popular', 'status', 'images',
            #'child_product_data',
        ]
        depth = 0

    @staticmethod
    def get_images(obj):
        return chain(Product.objects.filter(id=obj.id).values_list('image', flat=True),     # это наверняка можно написать лучше
                     obj.images.all().values_list('sub_image', flat=True))
