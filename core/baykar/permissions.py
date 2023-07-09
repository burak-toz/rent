from rest_framework import permissions

class IsOwnerProfilPermission(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        is_authenticated = super().has_permission(request, view)
        return is_authenticated and obj.user == request.user

