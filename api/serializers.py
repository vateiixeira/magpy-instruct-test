from django.core.exceptions import ValidationError
from rest_framework import serializers

from .models import PackageRelease, Project
from api.libs.pypi.gateway import Pypi, PypiException


class PackageRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageRelease
        fields = ['name', 'version']
        extra_kwargs = {'version': {'required': False}}

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageRelease
        fields = ['name', 'version','project']
        extra_kwargs = {'version': {'required': False}}


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'packages']

    packages = PackageRetriveSerializer(many=True)

    def create(self, validated_data):
        packages = validated_data['packages']
        
        pypi = Pypi()
        project = Project(name=validated_data['name'])
        project.save()
        
        for package in packages:
            try:
                version = pypi.check_package(package)
            except PypiException as ex:
                project.delete()
                raise serializers.ValidationError({'error': ex})
            
            if version:
                index = validated_data['packages'].index(package)
                validated_data['packages'][index]['version'] = version
            
            package['project'] = project.id
            project_release = PackageSerializer(data=package)
            project_release.is_valid(raise_exception=True)
            project_release.save()
        
        return validated_data


class ProjectRetriveSerializer(serializers.ModelSerializer):
    packages = PackageSerializer(many=True)
    class Meta:
        model = Project
        fields = ['name', 'packages']
