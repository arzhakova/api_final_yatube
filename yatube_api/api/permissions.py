from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        return request.method in permissions.SAFE_METHODS
