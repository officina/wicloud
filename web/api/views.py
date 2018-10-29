# -*- coding: utf-8 -*-
from django.contrib.auth.models import Permission
from django.db.models import Q

from rest_framework import generics, viewsets
from rest_framework.response import Response

from . import serializers


class QuerysetMixin:
    def get_filters(self):
        filters = dict()
        for key, value in self.request.GET.items():
            if key.startswith('filter__'):
                key = key[8:]
                filters[key] = value
        return filters

    def get_excludes(self):
        excludes = dict()
        for key, value in self.request.GET.items():
            if key.startswith('exclude__'):
                key = key[9:]
                excludes[key] = value
        return excludes

    def get_order_by(self):
        order_by = list()
        for key, value in self.request.GET.items():
            if key.startswith('order_by__'):
                # key = key[10:]
                order_by.append(value)
        return order_by

    def get_queryset(self):
        filters = self.get_filters()
        excludes = self.get_excludes()
        order_by = self.get_order_by()
        queryset = super(QuerysetMixin, self).get_queryset()
        if filters:
            queryset = queryset.filter(**filters)
        if excludes:
            queryset = queryset.exclude(**excludes)
        if order_by:
            queryset = queryset.order_by(*order_by).distinct()
        return queryset

    @property
    def paginator(self):
        if self.request.query_params.get('no_page'):
            self.pagination_class = None
        return super(QuerysetMixin, self).paginator


class StatusUpdateViewMixin(object):
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = self.new_status
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class PermissionListView(generics.ListAPIView):
    """
    Get all permissions
    """
    serializer_class = serializers.PermissionSerializer
    pagination_class = None

    def get_queryset(self):
        user = self.request.user
        qs = Permission.objects.all()
        if not user.is_superuser:
            qs = qs.filter(Q(group__user=user) | Q(user=user))

        if 'app_label' in self.kwargs:
            qs = qs.filter(content_type__app_label=self.kwargs['app_label'])
            if 'model_name' in self.kwargs:
                qs = qs.filter(content_type__model=self.kwargs['model_name'])

        return qs



class ThuxListViewMixin(QuerysetMixin):
    pass


class ThuxRetrieveViewMixin:
    pass


class ThuxCreateViewMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None

    def perform_create(self, serializer):
        self.user = self.request.user
        serializer.save(
            creator=self.user,
            last_modifier=self.user,
        )


class ThuxUpdateViewMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None

    def perform_update(self, serializer):
        self.user = self.request.user
        serializer.save(
            last_modifier=self.user
        )


class ThuxDestroyViewMixin:
    pass


class ThuxStatusViewMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None

    def perform_update(self, serializer):
        self.user = self.request.user
        serializer.save(
            last_modifier=self.user,
            status=self.new_status
        )
