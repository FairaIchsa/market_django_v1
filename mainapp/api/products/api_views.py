from rest_framework.generics import ListAPIView

from .serializers import *
from ...models import *


class ProductListApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


