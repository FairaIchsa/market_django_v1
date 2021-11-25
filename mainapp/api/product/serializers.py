from rest_framework import serializers
from itertools import chain

from mainapp.models.product_models import *


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
    status = serializers.SerializerMethodField()
    main_specifications = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'category', 'subcategory', 'name', 'slug', 'description',
            'price', 'quantity', 'in_sale', 'is_popular', 'status', 'main_specifications', 'image',
        ]
        depth = 0

    @staticmethod
    def get_in_sale(obj):
        if obj.sale is not None:
            return obj.sale.is_active
        return False

    @staticmethod
    def get_description(obj):
        if obj.description.first() is not None:
            return obj.description.get(position=0).content
        return None

    @staticmethod
    def get_status(obj):
        if obj.status is not None:
            return {
                'name': obj.status,
                'text': obj.get_status_display(),
            }
        return None

    @staticmethod
    def get_main_specifications(obj):
        MAIN_SPECIFICATIONS = {     # спецификации для определенной категории
            'balls': (
                ('size', 'Размер'),
            ),
            'tennis_tables': (
                ('foldable', 'Складной'),
                ('unfolded_size', 'Размер в разложенном состоянии'),
            ),
        }
        CHILD_OBJECTS = {
            'balls': 'child_product_ball',
            'tennis_tables': 'child_product_tennis_table',
        }
        category = obj.category.slug
        child_obj = getattr(obj, CHILD_OBJECTS[category])
        specifications = MAIN_SPECIFICATIONS[category]
        serialized = []
        for specification in specifications:
            field_value = getattr(child_obj, specification[0])
            spescification_dict = {
                'type': specification[0],
                'title': specification[1],
                'data': field_value
            }
            serialized.append(spescification_dict)
        return serialized


class ProductRetrieveSerializer(serializers.ModelSerializer):
    category = CategoryForProductSerializer()
    subcategory = SubcategoryForProductSerializer()
    sale = SaleForProductSerializer()
    description = DescriptionForProductSerializer(many=True)
    images = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
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
    def get_status(obj):
        if obj.status is not None:
            return {
                'name': obj.status,
                'text': obj.get_status_display(),
            }
        return None

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
