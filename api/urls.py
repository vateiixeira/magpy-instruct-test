from rest_framework import routers
from api import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from django.urls import re_path

schema_view = get_schema_view(
   openapi.Info(
      title="MagPy API",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()

router.register(r'projects', views.ProjectViewSet, basename='projects')

urlpatterns = [
    re_path(r'^swagger$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns += router.urls