from django.urls import reverse
from rest_framework.test import APITestCase



class TestUsers(APITestCase):

    def test01_register_user(self):
        endpoint = 'http://127.0.0.1:8000/' + reverse('wicloud:api:frontend:users_list')
        print(endpoint)
        response = self.client.get(endpoint)
        print(response)