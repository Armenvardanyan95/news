from rest_framework.permissions import BasePermission


class IsMagazineAdmin(BasePermission):

    def has_permission(self, request, view):
        return hasattr(request.user, 'magazine')
