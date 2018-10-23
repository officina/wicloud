from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory, APIClient
import json
from rest_framework import status


class TestUsers(APITestCase):

    api_client = APIClient()

    def test01_authentication(self):
        url = reverse('api-jwt-auth')
        print(url)
        test_username = "nicola"
        data = {'username': test_username, 'password': 'password'}
        u = User.objects.create_user(email='nicola.zambon@officina.cc', username='nicola', password='password')
        resp = self.client.post(url, {'email': 'nicola.zambon@officina.cc', 'password': 'password'}, format='json')
        token = resp.data['token']
        self.api_client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        response = self.api_client.get(reverse('wicloud:installation_list'))
        print(response)
        # self.assertEqual(resp.status_code, status.HTTP_200_OK)
        # token = resp.data['token']
        # endpoint = reverse('wicloud:api:frontend:users_list')
        #  self.api_client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        # response = self.api_client.get(endpoint)
        # self.assertEqual(response.data['results'][0]['username'], test_username)
        # resp = self.client.post(url, {'username': 'nicola2', 'password': 'officinadev'}, format='json')
        # self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
