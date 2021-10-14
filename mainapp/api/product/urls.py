from django.urls import path

from .api_views import ProductListApiView, ProductRetrieveApiView


app_name = 'product'

urlpatterns = [
    path('all/', ProductListApiView.as_view(), name='all'),
    path('get_by_id/<int:pk>', ProductRetrieveApiView.as_view(), name='by-id'),
]
