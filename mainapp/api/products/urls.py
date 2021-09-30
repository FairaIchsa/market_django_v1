from django.urls import path

from .api_views import ProductListApiView


app_name = 'products'

urlpatterns = [
    path('all/', ProductListApiView.as_view(), name='all'),
]
