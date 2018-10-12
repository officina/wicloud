#!python
import datetime
# -*- coding: utf-8 -*-
SECRET_KEY = 'afgdaasdlkja8s74dfdfd897a3sddlkjaasds45jasldkjalkdjhf79'
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wicloud',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

EMAIL_HOST = ''
EMAIL_PORT = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
EMAIL_SUBJECT_PREFIX = ['wicloud']
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# non usa AWS - usa default
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'exceptions': {
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': './logs/wicloud-exceptions.log',
            'level': 'DEBUG',
        },
        'api_exceptions': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': './logs/wicloud-api_exceptions.log',
        },
        'console': {
            'class': 'logging.StreamHandler',
            'filters': ['require_debug_true'],
            'formatter': 'verbose',
            'level': 'DEBUG',
        },
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': './logs/wicloud.log',
            'level': 'INFO',
        },
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'level': 'INFO',
        },
    },
    'loggers': {
        # tail -f ./logs/wicloud-exceptions.log
        'exceptions': {
            'handlers': ['exceptions'],
            'level': 'DEBUG',
        },
        # tail -f ./logs/wicloud-api_exceptions.log
        'api_exceptions': {
            'handlers': ['api_exceptions'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'console': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        # tail -f ./logs/wicloud.log
        'file': {
            'handlers': ['file'],
            'level': 'INFO',
        },
        'email': {
            'handlers': ['mail_admins'],
            'level': 'INFO',
        },
    }
}
# AWS SETTINGS

AWS_ACCESS_KEY_ID = 'AKIAJI7KKFRWWRE6JRYQ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'wicloud-development-andrea'
AWS_DEFAULT_ACL = 'public-read'
AWS_QUERYSTRING_AUTH = False
AWS_AUTO_CREATE_BUCKET = True
AWS_S3_FILE_OVERWRITE = False

# PLAYOFF SETTINGS

CORS_ORIGIN_ALLOW_ALL = True

DEBUG = True

EMAIL_SUBJECT_PREFIX = '[Wicloud_dev]'

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=86400),
}

