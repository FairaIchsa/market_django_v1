from rest_framework import serializers

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
        return Sale.objects.get(id=obj.sale.id).is_active


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
        ]

    @staticmethod
    def get_images(obj):
        return SubImage.objects.filter(product=obj.id).values()
