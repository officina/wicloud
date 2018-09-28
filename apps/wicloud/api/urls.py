# coding: utf-8

from django.conf.urls import url, include
from . import views

app_name = 'api'

urlpatterns = [
    url(r'^backend/', include('apps.wicloud.api.backend.urls', namespace='backend')),
    url(r'^frontend/', include('apps.wicloud.api.frontend.urls', namespace='frontend')),
    url(r'^$', views.api_wicloud_root, name='api_wicloud_root')
]
