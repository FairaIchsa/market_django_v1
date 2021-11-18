from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('product/', include('mainapp.api.product.urls', namespace='product')),
    path('profile/', include('mainapp.api.profile.urls', namespace='profile')),
    path('auth/', include('mainapp.api.auth.urls', namespace='auth')),
    path('', include('mainapp.api.other.urls', namespace='other')),
]
