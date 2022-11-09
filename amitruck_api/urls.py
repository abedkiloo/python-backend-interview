
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import HelloView
from django.urls import path, re_path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), 
    re_path('api/(?P<version>(v1|v2))/', include('trips.urls')),




]
