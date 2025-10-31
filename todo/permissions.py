from rest_framework import permissions


class IsProjectManagerOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow project managers or admins to access certain views.
    """
    def has_permission(self, request, view):
        return request.user.role in ['PROJECT_MANAGER', 'ADMIN']
    
    
    
class IsTaskOwnerOrProjectManagerOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow task owners or project managers to access certain views.
    """
    def has_object_permission(self, request, view, obj):
        return request.user == obj.created_by or request.user.role in ['PROJECT_MANAGER', 'ADMIN']