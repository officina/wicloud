# -*- coding: utf-8 -*-

from rest_framework import permissions


class GenericListPermission(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': [
            '%(app_label)s.list_%(model_name)s',
            '%(app_label)s.list_own_%(model_name)s',
        ],
        'OPTIONS': [],
    }


class GenericDetailPermission(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': [
            '%(app_label)s.detail_%(model_name)s',
            '%(app_label)s.detail_own_%(model_name)s',
        ],
        'OPTIONS': [],
    }


class GenericDisablePermission(permissions.DjangoModelPermissions):
    perms_map = {
        'PUT': ['%(app_label)s.disable_%(model_name)s'],
        'OPTIONS': [],
    }


class ThuxModelPermissions(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': [
            '%(app_label)s.list_%(model_name)s',
        ],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
