# -*- coding: utf-8 -*-

from .backend.remote_test import RemoteTestMixin as BRTM
from .frontend.remote_test import RemoteTestMixin as FRMT


class RemoteTestMixin(BRTM, FRMT):
    pass
