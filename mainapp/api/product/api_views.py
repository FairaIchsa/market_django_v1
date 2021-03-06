from collections import OrderedDict

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

from .serializers import *
from mainapp.models.product_models import *


class ProductListPagination(PageNumberPagination):
    page_size = 20

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('page', self.page.number),
            ('page_size', self.page_size),
            ('page_count', self.page.paginator.num_pages),
            ('items', data)
        ]))


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    pagination_class = ProductListPagination

    def get_queryset(self):
        queryset = super().get_queryset().order_by('id')
        if self.action == 'list':
            category = self.request.query_params.get('category')
            if category:
                return queryset.filter(category__slug=category)
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        elif self.action == 'retrieve':
            return ProductRetrieveSerializer
        return None

