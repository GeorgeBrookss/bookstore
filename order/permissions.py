from rest_framework.permissions import BasePermission

class IsAuthenticatedCustom(BasePermission):
    message = "Autenticação necessária para acessar esta rota."

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)
