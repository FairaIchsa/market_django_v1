from django.urls import path

from .api_views import *

app_name = 'user'

urlpatterns = [
    path('get_user_data/', UserAPIView.as_view(), name='current-user'),
]
