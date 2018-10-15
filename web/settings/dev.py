# -*- coding: utf-8 -*-
import datetime
import os
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CORS_ORIGIN_ALLOW_ALL = True

EMAIL_SUBJECT_PREFIX = '[Wicloud_dev]'

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=86400),
}





