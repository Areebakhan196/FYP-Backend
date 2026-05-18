from django.conf import settings
from rest_framework import permissions


class IsStaffUserOrDevOpen(permissions.BasePermission):
    """
    Production: same as staff-only admin access.
    When ADMIN_API_RELAX_PERMISSIONS is True (typical local DEBUG), skip staff check
    so the Vite dev app can load the dashboard without a Django admin browser session.
    """

    def has_permission(self, request, view):
        if getattr(settings, "ADMIN_API_RELAX_PERMISSIONS", False):
            return True
        user = request.user
        return bool(user and user.is_authenticated and user.is_staff)
