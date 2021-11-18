from django.urls import path

from .api_views import *


app_name = 'auth'

urlpatterns = [
    path('register/', SignUpAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('csrf_cookie/', GetCSRFTokenAPIView.as_view(), name='csrf-cookie'),
]
