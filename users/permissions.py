from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsOwner(BasePermission):
    message = "Вы не являетесь владельцем"
    def has_object_permission(self, request, view, obj):
        if obj.name_user == request.user:
            return True
        return False

class IsModerator(BasePermission):
    message = "Вы не являетесь модератором"
    def has_permission(self, request, view):
        return UserRoles.MODERATOR

class IsNotModerator(BasePermission):
    message = "Модератор - без прав на содание контента"
    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR:
            return False
        return True