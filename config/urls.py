from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="auto_filter API",
      default_version='v1',
      description="Документация фильтрации автомобилей",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

swagger_urls = [
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json',
    ),
    re_path(
        r'^swagger/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
    re_path(
        r'^redoc/$',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc',
    ),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('auto_filter.urls')),
    path('auth/', include('rest_framework.urls')),
] + swagger_urls
