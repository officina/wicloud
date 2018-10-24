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
        test_username = "nicola"
        data = {'username': test_username, 'password': 'officinadev'}
        u = User.objects.create_user(username='nicola', password='officinadev')
        resp = self.client.post(url, {'username': 'nicola', 'password': 'officinadev'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        token = resp.data['token']
        endpoint = reverse('wicloud:api:users_list')
        self.api_client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        response = self.api_client.get(endpoint)
        self.assertEqual(response.data['results'][0]['username'], test_username)
        resp = self.client.post(url, {'username': 'nicola2', 'password': 'officinadev'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test02_registration(self):
        registration_endpoint = reverse('wicloud:api:users_register')
        test_username = "nicola"
        data = {'username': test_username, 'password': 'password123'}
        resp = self.client.post(registration_endpoint, {'username': 'nicola', 'password': 'password123'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        resp = self.client.get(registration_endpoint)
        self.assertEqual(resp.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        resp = self.client.patch(registration_endpoint)
        self.assertEqual(resp.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        resp = self.client.post(registration_endpoint, {'username': 'nicola', 'password': 'password123'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        # ricevo un'indicazione di errore sul campo username, eventualmente verificare il codice
        self.assertTrue('username' in resp.data)
        short_test_username = "n"
        data = {'username': short_test_username, 'password': 'officinadev'}
        resp = self.client.post(registration_endpoint, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test03_change_password(self):
        u = User.objects.create_user(username='nicola', password='password123')
        endpoint = reverse('api:users_change_password')
        print(endpoint)
        old_password = 'password123'
        new_password = 'password321'
        # la chiamata deve essere autenticata
        resp = self.api_client.put(endpoint, {'old_password': old_password, 'new_password': new_password},
                                   format='json')
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)
        # effettuo autenticazione
        resp = self.api_client.post(reverse('api-jwt-auth'), {'username': 'nicola', 'password': old_password},
                                    format='json')
        self.api_client.credentials(HTTP_AUTHORIZATION=f"JWT {resp.data['token']}")
        #cambio password
        resp = self.api_client.put(endpoint, {'old_password': old_password, 'new_password': new_password},
                                   format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        # l'autenticazione fallisce con la vecchia password
        resp = self.api_client.post(reverse('api-jwt-auth'), {'username': 'nicola', 'password': old_password},
                                    format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        # l'autenticazione NON fallisce con la NUOVA password
        resp = self.api_client.post(reverse('api-jwt-auth'), {'username': 'nicola', 'password': new_password},
                                    format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
