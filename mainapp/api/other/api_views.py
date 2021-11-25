from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from .serializers import *
from mainapp.models.product_models import Category
from mainapp.models.other_models import MenuCategory, SliderInfo


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
