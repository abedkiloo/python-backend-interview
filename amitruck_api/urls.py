from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework.authtoken import views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('',include('user.urls')),
  path('api-token-auth', views.obtain_auth_token),
  re_path('api/(?P<version>(v1|v2))/', include('trips.urls')),

]
