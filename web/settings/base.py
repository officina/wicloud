# -*- coding: utf-8 -*-
"""
Django settings for web project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import datetime
import os

from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))
)

SETTINGS_PATH = os.path.abspath(os.path.dirname(__file__))

PROJECT_PATH = os.path.dirname(SETTINGS_PATH)

BASE_SITE_DOMAIN = 'www.wicloud.it'

LOGIN_URL = '/admin/login/'

APPEND_SLASH = True

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = ['127.0.0.1']

ADMIN_LANGUAGE_CODE = 'it'

# Application definition

INSTALLED_APPS = [
    'flat_responsive',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'django_extensions',
    'debug_toolbar',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'corsheaders',
    'storages',
    'web',
    'apps.wicloud',
    'webpack_loader',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_PATH, "templates")],
        # 'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ]

        },
    },
]

WSGI_APPLICATION = 'web.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'it'
LANGUAGES = [
    ('it', _('Italian')),
    ('en', _('English')),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'web', 'locale'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# STATIC_URL will be the url to serve the static files
STATIC_URL = '/static2/'
# STATIC_ROOT will be used as the path to serve the static files in production
# and will be used when using collectstatic command
STATIC_ROOT = os.path.join(BASE_DIR, "static")
# STATICFILES_DIRS are the extra paths to fetch the static file for project
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "web", "static"),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

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
            'filename': '/var/log/django/wicloud-exceptions.log',
            'level': 'DEBUG',
        },
        'api_exceptions': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': '/var/log/django/wicloud-api_exceptions.log',
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
            'filename': '/var/log/django/wicloud.log',
            'level': 'INFO',
        },
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'level': 'INFO',
        },
    },
    'loggers': {
        # tail -f /var/log/django/wicloud-exceptions.log
        'exceptions': {
            'handlers': ['exceptions'],
            'level': 'DEBUG',
        },
        # tail -f /var/log/django/wicloud-api_exceptions.log
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
        # tail -f /var/log/django/wicloud.log
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

# django rest framework
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'web.api.pagination.ThuxPageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'PAGE_SIZE_QUERY_PARAM': 'per_page',
    'EXCEPTION_HANDLER': 'web.drf.exceptions.wicloud_exception_handler'
}
CORS_ORIGIN_WHITELIST = [
    'wicloud'
]
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
}



TEST_RUNNER = 'web.runner.GeneraliDiscoverRunner'

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': '',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
    }
}
