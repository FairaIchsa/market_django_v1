from django.urls import path

from .api_views import CategoryListApiView, MenuCategoryListApiView


app_name = 'other'

urlpatterns = [
    path('navigation/main_categories/', MenuCategoryListApiView.as_view(), name='menu-categories'),
    path('navigation/product_categories/', CategoryListApiView.as_view(), name='product-categories'),
]
