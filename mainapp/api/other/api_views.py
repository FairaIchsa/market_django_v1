from collections import OrderedDict

from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from .serializers import *
from ...product_models import Category
from ...other_models import MenuCategory, SliderInfo


class SliderInfoPagination(PageNumberPagination):
    page_size = 100

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('slides_count', self.page.paginator.count),
            ('slides', data),
        ]))


class MenuCategoryListApiView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategoryListSerializer


class CategoryListApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class SliderInfoListApiView(ListAPIView):
    queryset = SliderInfo.objects.all()
    serializer_class = SliderInfoSerializer
    pagination_class = SliderInfoPagination
