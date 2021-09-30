from rest_framework.generics import ListAPIView

from .serializers import *
from ...models import *


class CategoryListApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
