# -*- coding: utf-8 -*-

import collections

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(('GET',))
def wicloud_root(request, format= None):
    url_dict = collections.OrderedDict()

    url_dict['api'] = reverse(
        'wicloud:api:api_root',
        request=request, format=format
    )
    return Response(url_dict)
