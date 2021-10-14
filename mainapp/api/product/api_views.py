from rest_framework.generics import ListAPIView, RetrieveAPIView

from .serializers import *
from ...models import *


class ProductListApiView(ListAPIView):  # добавить пагинацию
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductRetrieveApiView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductRetrieveSerializer


