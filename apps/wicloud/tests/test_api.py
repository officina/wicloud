from test_plus.test import TestCase
# from ipdbackend.tests import JWTAuthTestCase
from unittest import mock
from apps.wicloud.models import Installation
from web.core.models import UserModel
from rest_framework.test import APIRequestFactory, APIClient
from rest_framework.test import force_authenticate
from rest_framework import status
from django.urls import reverse
from django.conf import settings
import tempfile
import datetime


class TestInstallation(TestCase):

    apiClient = APIClient()
    u:UserModel


    def setUp(self):
        settings.MEDIA_ROOT = tempfile.mkdtemp()

        url = reverse('api-jwt-auth')
        self.u = self.make_user(username='apitest', password='apitest')
        self.u.is_active = False
        self.u.save()

        resp = self.client.post(url, {'email': 'testuser', 'password': 'password'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

        self.u.is_active = True
        self.u.must_change_password = False
        self.u.save()

        resp = self.client.post(url, {'email': 'apitest', 'password': 'apitest'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in resp.data)
        # self.assertTrue('refresh' in resp.data)
        token = resp.data['token']
        # refresh = resp.data['refresh']

        # print(token)

        verification_url = reverse('api-jwt-refresh')
        resp = self.client.post(verification_url, {'token': token}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        resp = self.client.post(verification_url, {'token': 'abc'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)


        self.apiClient.credentials(HTTP_AUTHORIZATION='Bearer ' + token)


    def test_patch_installation(self):

        original_desc = "installation base"
        modified_desc = "installation modified"

        d = Installation.objects.create(
            creator=self.u,
            created_date=datetime.datetime.now(),
            creator_id=self.u.id,
            last_modifier=self.u
        )
        d.description = original_desc
        d.save()
        id = d.id
        url = reverse('api:installation_retrieve', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_put_installation(self):

        original_desc = "installation base"
        modified_desc = "installation modified"

        d = Installation.objects.create()
        d.description = original_desc
        d.save()
        id = d.id
        url = reverse('api:installation_retrieve', kwargs={'id': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_list_installation(self):
        for i in range(0, 5):
            d  = Installation.objects.create(
            creator=self.u,
            created_date=datetime.datetime.now(),
            creator_id=self.u.id,
            last_modifier=self.u
        )
            d.title = "installation {}".format(i)
            d.save()

        url = reverse('api:installation_list')
        response = self.apiClient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(len(response.data), 5)

    def test_create_installation(self):

        installation_desc = 'installation description'

        url = reverse('api:installation_create')

        data = {'description': installation_desc} #, 'last_name': 'last name', "title": "doctor"}

        response = self.apiClient.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Installation.objects.count(), 1)
        self.assertEqual(Installation.objects.get().description, installation_desc)
        ##self.assertEqual(response.data[role].count, 1)



    def test_get_installation(self):
        installation_desc = 'Installazione 1'
        #if you assign a customer or any other object
        # customer = Customer.objects.create()
        # customer.first_name = "Mario"
        # customer.last_name = "Rossi"
        # customer.save()

        installation = Installation.objects.create(
            creator=self.u,
            created_date=datetime.datetime.now(),
            creator_id=self.u.id,
            last_modifier=self.u
        )
        installation.description = installation_desc
        # you could assign it here after creation
        #d.customer = customer
        installation.save()
        id = installation.id
        url = reverse('api:installation_retrieve', kwargs={'pk': id})


        # example on how to create child entities that belongs to this entity
        # for i in range(0, 5):
        #     e = Employee.objects.create()
        #     e.title = "employee {}".format(i)
        #
        #
        #     e.save()
        #
        #     d.structured_doctors.add(e)
        #
        # for i in range(0, 5):
        #     em = Employee.objects.create()
        #     em.title = "employee {}".format(i)
        #
        #     em.save()
        #     d.employees.add(em)


        response = self.apiClient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.data

        self.assertEqual(data['description'], installation.description)

        # self.assertEqual(len(dep['structured_doctors']), 5)
        # self.assertEqual(len(dep['employees']), 5)

        #if you assign a customer
        #self.assertEqual(m, customer.id)



