from collections import OrderedDict

from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from .serializers import *
from ...product_models import Category
from ...other_models import MenuCategory, SliderInfo


class MenuCategoryListAPIView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategoryListSerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class SliderInfoListAPIView(ListAPIView):
    queryset = SliderInfo.objects.all().order_by('id')
    serializer_class = SliderInfoSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        count = queryset.count()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'slides_count': count,
            'slides': serializer.data,
        })
