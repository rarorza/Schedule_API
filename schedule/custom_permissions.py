from rest_framework import permissions


class IsOwnerOrCreateOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        username_query_params = request.query_params.get("worker", None)
        username_authentication = request.user.username
        if username_authentication == username_query_params:
            return True
        return False


class IsWorker(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.worker == request.user:
            return True
        return False
