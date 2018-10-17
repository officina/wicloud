# -*- coding: utf-8 -*-
"""
Mygenerali APIExceptions tree
+-- APIException (DRF)
    +-- MygeneraliAPIException
"""

import logging

from django.core import exceptions as django_exceptions

from rest_framework.exceptions import APIException
from rest_framework.request import Request
from rest_framework.views import exception_handler
from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from web import exceptions


# API EXCEPTION HANDLER
def wicloud_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code
    else:
        if isinstance(exc, exceptions.WicloudException):
            data = {'detail': _(exc.msg)}
            response = Response(data, status=status.HTTP_400_BAD_REQUEST)
        if isinstance(exc, django_exceptions.ValidationError):
            data = exc.message_dict
            response = Response(data, status=status.HTTP_400_BAD_REQUEST)
    return response


# GENERIC CUSTOM API EXCEPTION
class WicloudAPIException(APIException):
    """
    To import:
        from web.drf import exceptions

    To raise:
        from rest_framework import status

        raise exceptions.MygeneraliAPIException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            request=request,
            msg='text of error',
        )
    """

    def __init__(self, status_code, request, msg=None, write_log=True):
        """
        :param status_code: HTTP status code
        :param request: view's request
        :param msg: error description
        :param write_log: if true a log is written in /var/log/django/wicloud-api_exceptions.log
        """
        self.logger = logging.getLogger('api_exceptions')
        self.status_code = status_code
        self.request = request
        if isinstance(self.request, Request):
            # if request is DRF-request then self.request = DJANGO-request
            self.request = self.request._request
        self.http_method = request.method

        super(WicloudAPIException, self).__init__(msg)
        if write_log:
            log_string = """{detail}\nurl: {url}\nmethod: {method}\nuser: {user}\ndata: {data}\n""".format(
                detail=self.detail,
                url=request.get_full_path(),
                method=getattr(request, 'method', ''),
                user=getattr(request, 'user', ''),
                data=getattr(request, 'data', ''),
            )
            self.logger.error(log_string)

    def get_repr_str(self):
        repr_str = u''
        if self.http_method:
            repr_str += '{} '.format(self.http_method.upper())
        repr_str += u'{} {}'.format(self.status_code, self.default_detail)
        return repr_str

    def __str__(self):
        return repr(self.get_repr_str())

    def __repr__(self):
        return repr(self.get_repr_str())
