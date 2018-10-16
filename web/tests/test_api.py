from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory, APIClient
import json
from rest_framework import status



class TestUsers(APITestCase):

    api_client =  APIClient()

    def test01_authentication(self):
        url = reverse('api-jwt-auth')
        test_username = "nicola"
        data = {'username': test_username, 'password': 'officinadev'}
        u = User.objects.create_user(username='nicola', password='officinadev')
        resp = self.client.post(url, {'username': 'nicola', 'password': 'officinadev'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        token = resp.data['token']
        endpoint = reverse('wicloud:api:frontend:users_list')
        self.api_client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        response = self.api_client.get(endpoint)
        self.assertEqual(response.data['results'][0]['username'], test_username)
        resp = self.client.post(url, {'username': 'nicola2', 'password': 'officinadev'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)


    def test02_registration(self):
        registration_endpoint = reverse('wicloud:api:frontend:users_register')
        test_username = "nicola"
        data = {'username': test_username, 'password': 'officinadev'}
        resp = self.client.post(registration_endpoint, {'username': 'nicola', 'password': 'officinadev'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        resp = self.client.get(registration_endpoint)
        self.assertEqual(resp.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        resp = self.client.patch(registration_endpoint)
        self.assertEqual(resp.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        short_test_username = "n"
        data = {'username': short_test_username, 'password': 'officinadev'}
        resp = self.client.post(registration_endpoint, {'username': 'nicola', 'password': 'officinadev'}, format='json')