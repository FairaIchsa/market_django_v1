from django.urls import path

from .api_views import *

app_name = 'profile'

urlpatterns = [
    path('get_user_data/', UserDataAPIView.as_view(), name='info'),
]
