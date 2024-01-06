from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    print(22)
    def has_object_permission(self, request, view, obj):
        print(1)
        return obj.user == request.user
