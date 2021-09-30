from django.urls import path

from .api_views import CategoryListApiView


app_name = 'other'

urlpatterns = [
    path('navigation/product_categories/', CategoryListApiView.as_view(), name='product-categories'),
]
