from django.urls import path

from .api_views import *


app_name = 'product'

urlpatterns = [
    path('all/', ProductModelViewSet.as_view({'get': 'list'}), name='all'),
    path('get_by_id/<int:pk>', ProductModelViewSet.as_view({'get': 'retrieve'}), name='by-id'),
]
