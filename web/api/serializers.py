# -*- coding: utf-8 -*-

from rest_framework import serializers

from django.contrib.auth import models


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Permission
        fields = '__all__'


class ThuxListSerializerMixin:
    pass


class ThuxRetrieveSerializerMixin:
    pass


class ThuxCreateSerializerMixin:
    pass


class ThuxUpdateSerializerMixin:
    pass
