from django.http.response import Http404
from rest_framework.response import Response
from api.permissions import ProjectPermission
from rest_framework import generics, status, viewsets

from .models import Project,PackageRelease
from .serializers import ProjectRetriveSerializer, ProjectSerializer,PackageSerializer
from rest_framework.decorators import action

class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [ProjectPermission]
    serializer_class = ProjectSerializer
    lookup_field = 'name'

    def get_queryset(self):
        queryset = Project.objects.all()

        return queryset
        



