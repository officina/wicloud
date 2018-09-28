# -*- coding: utf-8 -*-

import pprint
import requests

from apps.wicloud.api.remote_test import RemoteTestMixin as RMTEditor


class RemoteTest(RMTEditor):
    def __init__(self, base_url="http://127.0.0.1:8000/", log=True):
        self.base_url = base_url
        self.log = log
        self.jwt = None

    def rprint(self, resp):
        if self.log:
            pprint.pprint(resp.url)
            pprint.pprint(resp.status_code)
            pprint.pprint(resp.reason)
            try:
                pprint.pprint(resp.json())
            except BaseException:
                pass
            print()

    def login(self, username, password):
        post_dict = {'username': username, 'password': password}
        resp = requests.post(self.base_url + 'api-token-auth/', json=post_dict)
        if resp.status_code == 200:
            self.jwt = resp.json()['token']
            self.rprint(resp)
            return resp
        self.rprint(resp)
        return resp

    def logout(self):
        self.jwt = None
        return
