from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('', include('mainapp.api.other.urls', namespace='other')),
    path('product/', include('mainapp.api.product.urls', namespace='product')),
    path('auth/', include('mainapp.api.user.urls', namespace='user')),
]
