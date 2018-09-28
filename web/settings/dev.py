# -*- coding: utf-8 -*-
import datetime

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CORS_ORIGIN_ALLOW_ALL = True

EMAIL_SUBJECT_PREFIX = '[MYGENERALI_dev]'

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=86400),
}
PLAYOFF_HOSTNAME = 'playoff.cc'
