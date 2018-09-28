# -*- coding: utf-8 -*-

from django.conf import settings


# It seems, we are not using this function anymore.
def get_setting(setting_name, default):
    return getattr(settings, setting_name, default)
