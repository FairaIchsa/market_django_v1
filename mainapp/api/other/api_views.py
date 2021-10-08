from rest_framework.generics import ListAPIView

from .serializers import *
from ...models import *


class MenuCategoryListApiView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategoryListSerializer


class CategoryListApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class SliderInfoListApiView(ListAPIView):
    queryset = SliderInfo.objects.all()
    serializer_class = SliderInfoListSerializer
