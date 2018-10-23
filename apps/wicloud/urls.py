# coding: utf-8

from django.conf.urls import url, include
from . import views

app_name='wicloud'

urlpatterns = [
    url(r'^', include('apps.wicloud.api.urls', namespace='api')),
    url(r'^$', views.wicloud_root, name = 'wicloud_root')
]
