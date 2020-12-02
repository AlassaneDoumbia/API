"""dgid_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from schema_graph.views import Schema
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions, routers

from rest_framework_simplejwt import views as jwt_views


schema_view = get_schema_view(
   openapi.Info(
      title="LBA partnership API",
      default_version='v1',
      description="This APi have been made for LBA design",
      contact=openapi.Contact(email="vannicknonongo@gmail.com"),
      license=openapi.License(name="Personal License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('auth/email/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_refresh'),
    url(r'^docs/swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^docs/swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^docs/redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    #url(r'^media/images/avatar/$', include('media'), {'document_root': settings.MEDIA_ROOT, }),
    path('schema/', Schema.as_view()),
    #path('', include('historiques.urls')), 
    path('api-auth/', include('rest_framework.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
