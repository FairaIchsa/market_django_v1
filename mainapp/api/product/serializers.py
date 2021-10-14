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

    class Meta:
        model = Product
        fields = [
            'id', 'category', 'subcategory', 'name', 'slug', 'description',
            'price', 'quantity', 'in_sale', 'is_popular', 'image',
        ]

    @staticmethod
    def get_in_sale(obj):
        if obj.sale:
            return obj.sale.is_active
        return False


class ProductRetrieveSerializer(serializers.ModelSerializer):
    category = CategoryForProductSerializer()
    subcategory = SubcategoryForProductSerializer()
    sale = SaleForProductSerializer()
    images = serializers.SerializerMethodField()
    status = StatusForProductSerializer()
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
    def get_images(obj):
        return chain(Product.objects.filter(id=obj.id).values_list('image', flat=True),
                     obj.images.all().values_list('sub_image', flat=True))
            # это наверняка можно написать лучше

    @staticmethod
    def get_child_product_data(obj):
        slug = obj.category.slug
        if slug == 'balls':
            return BallSerializer(Ball.objects.get(product=obj)).data
        elif slug == 'tennis_tables':
            return TennisTableSerializer(TennisTable.objects.get(product=obj)).data
