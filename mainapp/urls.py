from django.urls import path, include

from .views import index_page

app_name = 'mainapp'

urlpatterns = [
    path('', index_page, name='index-page'),
    path('api/', include('mainapp.api.urls', namespace='api')),
]
