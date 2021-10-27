from django.urls import path

from .api_views import *


app_name = 'other'

urlpatterns = [
    path('navigation/main_categories/', MenuCategoryListAPIView.as_view(), name='menu-categories'),
    path('navigation/product_categories/', CategoryListAPIView.as_view(), name='product-categories'),
    path('store/sliders/main_slider/', SliderInfoListAPIView.as_view(), name='slider-info'),
]
