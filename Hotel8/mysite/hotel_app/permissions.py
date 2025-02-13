from rest_framework import permissions


class CheckOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.profile == 'owner':
            return True
        if request.user.profile == 'client':
            return False




