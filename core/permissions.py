from rest_framework.permissions import BasePermission, IsAuthenticated as IsAuth


class IsMagazineAdmin(BasePermission):

    def has_permission(self, request, view):
        return hasattr(request.user, 'magazine')


# class IsMagazineAdminOrSafeMethod

class IsAuthenticatedOrSafeMethod(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated() or request.method.lower() in ["get", "options"]


class IsAuthenticated(IsAuth):

    def has_permission(self, request, view):
        if request.method == 'OPTIONS':
            return True

        return super().has_permission(request, view)
