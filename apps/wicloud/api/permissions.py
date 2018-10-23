from rest_framework.permissions import BasePermission
from ..models import Installation

class IsInstaller(BasePermission):

    def has_object_permission(self, request, view, obj: Installation):
            return obj.is_installer(self, request.user)


class IsInstallationManager(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.is_installation_manager(self, request.user)


class IsAssetsManager(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.is_assets_manager(self, request.user)


class IsViewer(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.is_viewer(self, request.user)



# class IsAllowedToRead(BasePermission):
#
#     def has_object_permission(self, request, view, obj):
#         return obj.is_allowed_to_read == "YES"