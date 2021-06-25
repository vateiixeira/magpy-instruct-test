from rest_framework import permissions

class ProjectPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return True