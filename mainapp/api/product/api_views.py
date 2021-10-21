from collections import OrderedDict

from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination

from .serializers import *
from ...models import *


class ProductListPagination(PageNumberPagination):
    page_size = 20

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('page', self.page.number),
            ('page_size', self.page_size),
            ('page_count', self.page.paginator.num_pages),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('items', data)
        ]))


class ProductListApiView(ListAPIView):  # добавить пагинацию
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = ProductListPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        if category:
            return queryset.filter(category__slug=category)
        return queryset


class ProductRetrieveApiView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductRetrieveSerializer


