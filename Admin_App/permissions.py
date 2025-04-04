# permissions.py
from rest_framework.permissions import BasePermission

class IsAdminGroupUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.groups.filter(name="Admin").exists()
