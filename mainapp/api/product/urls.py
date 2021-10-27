from django.urls import path

from .api_views import *


app_name = 'product'

urlpatterns = [
    path('all/', ProductListAPIView.as_view(), name='all'),
    path('get_by_id/<int:pk>', ProductRetrieveAPIView.as_view(), name='by-id'),
]
