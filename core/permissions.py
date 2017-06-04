from rest_framework.permissions import BasePermission, IsAuthenticated as IsAuth


class IsMagazineAdmin(BasePermission):

    def has_permission(self, request, view):
        return hasattr(request.user, 'magazine')


# class IsMagazineAdminOrSafeMethod

class IsAuthenticated(IsAuth):

    def has_permission(self, request, view):
        if request.method == 'OPTIONS':
            return True

        return super().has_permission(request, view)
