# -*- coding: utf-8 -*-
"""
WSGI config for My Generali project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")
# add the hellodjango project path into the sys.path
sys.path.append('/var/www/html/wicloud/')
# add the virtualenv site-packages path to the sys.path
sys.path.append('/var/www/html/wicloud/django/lib/python3.6/site-packages')

application = get_wsgi_application()
