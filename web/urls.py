# -*- coding: utf-8 -*-

"""Wicloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin

from web.api import views as permission_views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from web import views


urlpatterns = [
    # ADMIN URL
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),


    # DRF API URL
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/permission/$', permission_views.PermissionListView.as_view(), name='permission_root'),
    url(r'^api/permission/(?P<app_label>\w+)/$', permission_views.PermissionListView.as_view(), name='permission_app_root'),
    url(r'^api/permission/(?P<app_label>\w+)/(?P<model_name>\w+)/$',
        permission_views.PermissionListView.as_view(), name='permission_model_root'),

    # JWT TOKEN URL
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    # REST AUTH URL
    url(r'^rest-auth/', include('rest_auth.urls')),

    url(r'^wicloud/', include('apps.wicloud.urls')),

    url(r'^$',views.home),
    # url('^$', RedirectView.as_view(url='/admin/', permanent=False)),
]

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

urlpatterns += i18n_patterns()

if settings.DEBUG:
    # ON DEBUG

    # MEDIA
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # DEBUG TOOLBAR
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
