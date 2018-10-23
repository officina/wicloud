from test_plus.test import TestCase
# from ipdbackend.tests import JWTAuthTestCase
from unittest import mock

from web.core.models import UserModel
from rest_framework.test import APIRequestFactory, APIClient
from rest_framework.test import force_authenticate
from rest_framework import status
from django.urls import reverse
from django.conf import settings
import tempfile
import datetime
from apps.wicloud.models import Address


class TestAddress(TestCase):

    apiClient = APIClient()
    u: UserModel

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

    def test_patch_address(self):

        original_desc = "Address base"
        modified_desc = "Address modified"

        d = Address.objects.create(
            creator=self.u,
            last_modifier=self.u,
            full_name='Full name address'
        )

        d.save()
        id = d.id
        url = reverse('api:address_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_put_address(self):

        original_desc = "Address base"
        modified_desc = "Address modified"

        d = Address.objects.create(
            creator=self.u,
            last_modifier=self.u,
            full_name="fullname"
        )

        d.save()
        id = d.id
        url = reverse('api:address_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_delete_address(self):

        original_desc = "Address base"
        modified_desc = "Address modified"

        d = Address.objects.create(
            creator=self.u,
            last_modifier=self.u,
            full_name="fullname"
        )

        d.save()
        id = d.id
        url = reverse('api:address_destroy', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        self.assertEqual(Address.objects.count(), 1)

        response = self.apiClient.delete(url, data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Address.objects.count(), 0)

    def test_list_address(self):
        for i in range(0, 5):
            d = Address.objects.create(
                creator=self.u,
                last_modifier=self.u,
                full_name="Full name"
            )
            d.title = "Address {}".format(i)
            d.save()

        url = reverse('api:address_list')
        response = self.apiClient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(len(response.data['results']), 5)

    def test_create_address(self):
        full_name = 'Via roma'
        address_desc = 'Address description'

        url = reverse('api:address_create')

        data = {'description': address_desc, 'full_name': full_name}  # , 'last_name': 'last name', "title": "doctor"}

        response = self.apiClient.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Address.objects.count(), 1)
        self.assertEqual(Address.objects.get().description, address_desc)
        self.assertEqual(Address.objects.get().full_name, full_name)
        ##self.assertEqual(response.data[role].count, 1)

    def test_get_address(self):

        address_desc = 'Address 1'
        # if you assign a customer or any other object
        # customer = Customer.objects.create()
        # customer.first_name = "Mario"
        # customer.last_name = "Rossi"
        # customer.save()

        obj = Address.objects.create(
            creator=self.u,
            last_modifier=self.u,
            full_name='Via roma'
        )

        # you could assign it here after creation
        #d.customer = customer

        obj.description = address_desc
        obj.save()
        id = obj.id
        url = reverse('api:address_retrieve', kwargs={'pk': id})

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

        self.assertEqual(data['description'], obj.description)

        # self.assertEqual(len(dep['structured_doctors']), 5)
        # self.assertEqual(len(dep['employees']), 5)


        # if you assign a customer
        #self.assertEqual(m, customer.id)
from apps.wicloud.models import Customer


class TestCustomer(TestCase):

    apiClient = APIClient()
    u: UserModel

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

    def test_patch_customer(self):

        original_desc = "Customer base"
        modified_desc = "Customer modified"

        d = Customer.objects.create(
            creator=self.u,
            last_modifier=self.u,
            company_name='Company_name'
        )

        d.save()
        id = d.id
        url = reverse('api:customer_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_put_customer(self):

        original_desc = "Customer base"
        modified_desc = "Customer modified"

        d = Customer.objects.create(
            creator=self.u,
            last_modifier=self.u,
            company_name='Company_name'
        )

        d.save()
        id = d.id
        url = reverse('api:customer_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_delete_customer(self):

        original_desc = "Customer base"
        modified_desc = "Customer modified"

        d = Customer.objects.create(
            creator=self.u,
            last_modifier=self.u,
            company_name='Company_name'
        )

        d.save()
        id = d.id
        url = reverse('api:customer_destroy', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        self.assertEqual(Customer.objects.count(), 1)

        response = self.apiClient.delete(url, data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Customer.objects.count(), 0)

    def test_list_customer(self):
        for i in range(0, 5):
            d = Customer.objects.create(
                creator=self.u,
                last_modifier=self.u,
                company_name='Company_name'
            )
            d.title = "Customer {}".format(i)
            d.save()

        url = reverse('api:customer_list')
        response = self.apiClient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(len(response.data['results']), 5)

    def test_create_customer(self):

        customer_desc = 'Customer description'

        url = reverse('api:customer_create')

        data = {'description': customer_desc, 'company_name':'Company_name'}  # , 'last_name': 'last name', "title": "doctor"}

        response = self.apiClient.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().description, customer_desc)
        ##self.assertEqual(response.data[role].count, 1)

    def test_get_customer(self):
        customer_desc = 'Customer 1'
        # if you assign a customer or any other object
        # customer = Customer.objects.create()
        # customer.first_name = "Mario"
        # customer.last_name = "Rossi"
        # customer.save()

        obj = Customer.objects.create(
            creator=self.u,
            last_modifier=self.u,
            company_name='Company_name'
        )

        # you could assign it here after creation
        #d.customer = customer
        obj.description = customer_desc
        obj.save()
        id = obj.id
        url = reverse('api:customer_retrieve', kwargs={'pk': id})

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

        self.assertEqual(data['description'], obj.description)

        # self.assertEqual(len(dep['structured_doctors']), 5)
        # self.assertEqual(len(dep['employees']), 5)


        # if you assign a customer
        #self.assertEqual(m, customer.id)
from apps.wicloud.models import Energy_interval


class TestEnergy_interval(TestCase):

    apiClient = APIClient()
    u: UserModel

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

    def test_patch_energy_interval(self):

        original_desc = "Energy_interval base"
        modified_desc = "Energy_interval modified"

        d = Energy_interval.objects.create(
            creator=self.u,
            last_modifier=self.u,
            mac='1234567890'
        )

        d.save()
        id = d.id
        url = reverse('api:energy_interval_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_put_energy_interval(self):

        original_desc = "Energy_interval base"
        modified_desc = "Energy_interval modified"

        d = Energy_interval.objects.create(
            creator=self.u,
            last_modifier=self.u,
            mac='1234567890'
        )

        d.save()
        id = d.id
        url = reverse('api:energy_interval_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_delete_energy_interval(self):

        original_desc = "Energy_interval base"
        modified_desc = "Energy_interval modified"

        d = Energy_interval.objects.create(
            creator=self.u,
            last_modifier=self.u,
            mac='1234567890'
        )

        d.save()
        id = d.id
        url = reverse('api:energy_interval_destroy', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        self.assertEqual(Energy_interval.objects.count(), 1)

        response = self.apiClient.delete(url, data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Energy_interval.objects.count(), 0)

    def test_list_energy_interval(self):
        for i in range(0, 5):
            d = Energy_interval.objects.create(
                creator=self.u,
                last_modifier=self.u,
                mac='1234567890'
            )
            d.title = "Energy_interval {}".format(i)
            d.save()

        url = reverse('api:energy_interval_list')
        response = self.apiClient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(len(response.data['results']), 5)

    def test_create_energy_interval(self):

        energy_interval_desc = 'Energy_interval description'

        url = reverse('api:energy_interval_create')

        data = {'description': energy_interval_desc, 'mac': '1234567890'}  # , 'last_name': 'last name', "title": "doctor"}

        response = self.apiClient.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Energy_interval.objects.count(), 1)
        self.assertEqual(Energy_interval.objects.get().description, energy_interval_desc)
        ##self.assertEqual(response.data[role].count, 1)

    def test_get_energy_interval(self):
        energy_interval_desc = 'Energy_interval 1'
        # if you assign a customer or any other object
        # customer = Customer.objects.create()
        # customer.first_name = "Mario"
        # customer.last_name = "Rossi"
        # customer.save()

        obj = Energy_interval.objects.create(
            creator=self.u,
            last_modifier=self.u,
            mac='1234567890'
        )

        # you could assign it here after creation
        #d.customer = customer
        obj.description = energy_interval_desc
        obj.save()
        id = obj.id
        url = reverse('api:energy_interval_retrieve', kwargs={'pk': id})

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

        self.assertEqual(data['description'], obj.description)

        # self.assertEqual(len(dep['structured_doctors']), 5)
        # self.assertEqual(len(dep['employees']), 5)


        # if you assign a customer
        #self.assertEqual(m, customer.id)
from apps.wicloud.models import Energy_meter_module


class TestEnergy_meter_module(TestCase):

    apiClient = APIClient()
    u: UserModel

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

    def test_patch_energy_meter_module(self):

        original_desc = "Energy_meter_module base"
        modified_desc = "Energy_meter_module modified"

        d = Energy_meter_module.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:energy_meter_module_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_put_energy_meter_module(self):

        original_desc = "Energy_meter_module base"
        modified_desc = "Energy_meter_module modified"

        d = Energy_meter_module.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:energy_meter_module_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_delete_energy_meter_module(self):

        original_desc = "Energy_meter_module base"
        modified_desc = "Energy_meter_module modified"

        d = Energy_meter_module.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:energy_meter_module_destroy', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        self.assertEqual(Energy_meter_module.objects.count(), 1)

        response = self.apiClient.delete(url, data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Energy_meter_module.objects.count(), 0)

    def test_list_energy_meter_module(self):
        for i in range(0, 5):
            d = Energy_meter_module.objects.create(
                creator=self.u,
                last_modifier=self.u,
            )
            d.title = "Energy_meter_module {}".format(i)
            d.save()

        url = reverse('api:energy_meter_module_list')
        response = self.apiClient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(len(response.data['results']), 5)

    def test_create_energy_meter_module(self):

        energy_meter_module_desc = 'Energy_meter_module description'

        url = reverse('api:energy_meter_module_create')

        data = {'description': energy_meter_module_desc}  # , 'last_name': 'last name', "title": "doctor"}

        response = self.apiClient.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Energy_meter_module.objects.count(), 1)
        self.assertEqual(Energy_meter_module.objects.get().description, energy_meter_module_desc)
        ##self.assertEqual(response.data[role].count, 1)

    def test_get_energy_meter_module(self):
        energy_meter_module_desc = 'Energy_meter_module 1'
        # if you assign a customer or any other object
        # customer = Customer.objects.create()
        # customer.first_name = "Mario"
        # customer.last_name = "Rossi"
        # customer.save()

        obj = Energy_meter_module.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        # you could assign it here after creation
        #d.customer = customer
        obj.description = energy_meter_module_desc
        obj.save()
        id = obj.id
        url = reverse('api:energy_meter_module_retrieve', kwargs={'pk': id})

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

        self.assertEqual(data['description'], obj.description)

        # self.assertEqual(len(dep['structured_doctors']), 5)
        # self.assertEqual(len(dep['employees']), 5)


        # if you assign a customer
        #self.assertEqual(m, customer.id)
from apps.wicloud.models import Energy_meter_peak_measure


class TestEnergy_meter_peak_measure(TestCase):

    apiClient = APIClient()
    u: UserModel

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

    def test_patch_energy_meter_peak_measure(self):

        original_desc = "Energy_meter_peak_measure base"
        modified_desc = "Energy_meter_peak_measure modified"

        d = Energy_meter_peak_measure.objects.create(
            creator=self.u,
            last_modifier=self.u,
            mac='1234567890'
        )

        d.save()
        id = d.id
        url = reverse('api:energy_meter_peak_measure_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_put_energy_meter_peak_measure(self):

        original_desc = "Energy_meter_peak_measure base"
        modified_desc = "Energy_meter_peak_measure modified"

        d = Energy_meter_peak_measure.objects.create(
            creator=self.u,
            last_modifier=self.u,
            mac='1234567890'
        )

        d.save()
        id = d.id
        url = reverse('api:energy_meter_peak_measure_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_delete_energy_meter_peak_measure(self):

        original_desc = "Energy_meter_peak_measure base"
        modified_desc = "Energy_meter_peak_measure modified"

        d = Energy_meter_peak_measure.objects.create(
            creator=self.u,
            last_modifier=self.u,
            mac='1234567890'
        )

        d.save()
        id = d.id
        url = reverse('api:energy_meter_peak_measure_destroy', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        self.assertEqual(Energy_meter_peak_measure.objects.count(), 1)

        response = self.apiClient.delete(url, data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Energy_meter_peak_measure.objects.count(), 0)

    def test_list_energy_meter_peak_measure(self):
        for i in range(0, 5):
            d = Energy_meter_peak_measure.objects.create(
                creator=self.u,
                last_modifier=self.u,
                mac='1234567890'
            )
            d.title = "Energy_meter_peak_measure {}".format(i)
            d.save()

        url = reverse('api:energy_meter_peak_measure_list')
        response = self.apiClient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(len(response.data['results']), 5)

    def test_create_energy_meter_peak_measure(self):

        energy_meter_peak_measure_desc = 'Energy_meter_peak_measure description'

        url = reverse('api:energy_meter_peak_measure_create')

        data = {'description': energy_meter_peak_measure_desc,'mac':'1234567890'}  # , 'last_name': 'last name', "title": "doctor"}

        response = self.apiClient.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Energy_meter_peak_measure.objects.count(), 1)
        self.assertEqual(Energy_meter_peak_measure.objects.get().description, energy_meter_peak_measure_desc)
        ##self.assertEqual(response.data[role].count, 1)

    def test_get_energy_meter_peak_measure(self):
        energy_meter_peak_measure_desc = 'Energy_meter_peak_measure 1'
        # if you assign a customer or any other object
        # customer = Customer.objects.create()
        # customer.first_name = "Mario"
        # customer.last_name = "Rossi"
        # customer.save()

        obj = Energy_meter_peak_measure.objects.create(
            creator=self.u,
            last_modifier=self.u,
            mac='1234567890'
        )

        # you could assign it here after creation
        #d.customer = customer
        obj.description = energy_meter_peak_measure_desc
        obj.save()
        id = obj.id
        url = reverse('api:energy_meter_peak_measure_retrieve', kwargs={'pk': id})

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

        self.assertEqual(data['description'], obj.description)

        # self.assertEqual(len(dep['structured_doctors']), 5)
        # self.assertEqual(len(dep['employees']), 5)


        # if you assign a customer
        #self.assertEqual(m, customer.id)
from apps.wicloud.models import Error_light_level_and_adc_mismatch


class TestError_light_level_and_adc_mismatch(TestCase):

    apiClient = APIClient()
    u: UserModel

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

    def test_patch_error_light_level_and_adc_mismatch(self):

        original_desc = "Error_light_level_and_adc_mismatch base"
        modified_desc = "Error_light_level_and_adc_mismatch modified"

        d = Error_light_level_and_adc_mismatch.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:error_light_level_and_adc_mismatch_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_put_error_light_level_and_adc_mismatch(self):

        original_desc = "Error_light_level_and_adc_mismatch base"
        modified_desc = "Error_light_level_and_adc_mismatch modified"

        d = Error_light_level_and_adc_mismatch.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:error_light_level_and_adc_mismatch_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_delete_error_light_level_and_adc_mismatch(self):

        original_desc = "Error_light_level_and_adc_mismatch base"
        modified_desc = "Error_light_level_and_adc_mismatch modified"

        d = Error_light_level_and_adc_mismatch.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:error_light_level_and_adc_mismatch_destroy', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        self.assertEqual(Error_light_level_and_adc_mismatch.objects.count(), 1)

        response = self.apiClient.delete(url, data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Error_light_level_and_adc_mismatch.objects.count(), 0)

    def test_list_error_light_level_and_adc_mismatch(self):
        for i in range(0, 5):
            d = Error_light_level_and_adc_mismatch.objects.create(
                creator=self.u,
                last_modifier=self.u,
            )
            d.title = "Error_light_level_and_adc_mismatch {}".format(i)
            d.save()

        url = reverse('api:error_light_level_and_adc_mismatch_list')
        response = self.apiClient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(len(response.data['results']), 5)

    def test_create_error_light_level_and_adc_mismatch(self):

        error_light_level_and_adc_mismatch_desc = 'Error_light_level_and_adc_mismatch description'

        url = reverse('api:error_light_level_and_adc_mismatch_create')

        # , 'last_name': 'last name', "title": "doctor"}
        data = {'description': error_light_level_and_adc_mismatch_desc}

        response = self.apiClient.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Error_light_level_and_adc_mismatch.objects.count(), 1)
        self.assertEqual(
            Error_light_level_and_adc_mismatch.objects.get().description,
            error_light_level_and_adc_mismatch_desc)
        ##self.assertEqual(response.data[role].count, 1)

    def test_get_error_light_level_and_adc_mismatch(self):
        error_light_level_and_adc_mismatch_desc = 'Error_light_level_and_adc_mismatch 1'
        # if you assign a customer or any other object
        # customer = Customer.objects.create()
        # customer.first_name = "Mario"
        # customer.last_name = "Rossi"
        # customer.save()

        obj = Error_light_level_and_adc_mismatch.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        # you could assign it here after creation
        #d.customer = customer
        obj.description = error_light_level_and_adc_mismatch_desc
        obj.save()
        id = obj.id
        url = reverse('api:error_light_level_and_adc_mismatch_retrieve', kwargs={'pk': id})

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

        self.assertEqual(data['description'], obj.description)

        # self.assertEqual(len(dep['structured_doctors']), 5)
        # self.assertEqual(len(dep['employees']), 5)


        # if you assign a customer
        #self.assertEqual(m, customer.id)
from apps.wicloud.models import Error_light_level_and_power_mismatch


class TestError_light_level_and_power_mismatch(TestCase):

    apiClient = APIClient()
    u: UserModel

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

    def test_patch_error_light_level_and_power_mismatch(self):

        original_desc = "Error_light_level_and_power_mismatch base"
        modified_desc = "Error_light_level_and_power_mismatch modified"

        d = Error_light_level_and_power_mismatch.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:error_light_level_and_power_mismatch_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_put_error_light_level_and_power_mismatch(self):

        original_desc = "Error_light_level_and_power_mismatch base"
        modified_desc = "Error_light_level_and_power_mismatch modified"

        d = Error_light_level_and_power_mismatch.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:error_light_level_and_power_mismatch_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_delete_error_light_level_and_power_mismatch(self):

        original_desc = "Error_light_level_and_power_mismatch base"
        modified_desc = "Error_light_level_and_power_mismatch modified"

        d = Error_light_level_and_power_mismatch.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:error_light_level_and_power_mismatch_destroy', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        self.assertEqual(Error_light_level_and_power_mismatch.objects.count(), 1)

        response = self.apiClient.delete(url, data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Error_light_level_and_power_mismatch.objects.count(), 0)

    def test_list_error_light_level_and_power_mismatch(self):
        for i in range(0, 5):
            d = Error_light_level_and_power_mismatch.objects.create(
                creator=self.u,
                last_modifier=self.u,
            )
            d.title = "Error_light_level_and_power_mismatch {}".format(i)
            d.save()

        url = reverse('api:error_light_level_and_power_mismatch_list')
        response = self.apiClient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(len(response.data['results']), 5)

    def test_create_error_light_level_and_power_mismatch(self):

        error_light_level_and_power_mismatch_desc = 'Error_light_level_and_power_mismatch description'

        url = reverse('api:error_light_level_and_power_mismatch_create')

        # , 'last_name': 'last name', "title": "doctor"}
        data = {'description': error_light_level_and_power_mismatch_desc}

        response = self.apiClient.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Error_light_level_and_power_mismatch.objects.count(), 1)
        self.assertEqual(
            Error_light_level_and_power_mismatch.objects.get().description,
            error_light_level_and_power_mismatch_desc)
        ##self.assertEqual(response.data[role].count, 1)

    def test_get_error_light_level_and_power_mismatch(self):
        error_light_level_and_power_mismatch_desc = 'Error_light_level_and_power_mismatch 1'
        # if you assign a customer or any other object
        # customer = Customer.objects.create()
        # customer.first_name = "Mario"
        # customer.last_name = "Rossi"
        # customer.save()

        obj = Error_light_level_and_power_mismatch.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        # you could assign it here after creation
        #d.customer = customer
        obj.description = error_light_level_and_power_mismatch_desc
        obj.save()
        id = obj.id
        url = reverse('api:error_light_level_and_power_mismatch_retrieve', kwargs={'pk': id})

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

        self.assertEqual(data['description'], obj.description)

        # self.assertEqual(len(dep['structured_doctors']), 5)
        # self.assertEqual(len(dep['employees']), 5)


        # if you assign a customer
        #self.assertEqual(m, customer.id)
from apps.wicloud.models import Error_node_offline


class TestError_node_offline(TestCase):

    apiClient = APIClient()
    u: UserModel

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

    def test_patch_error_node_offline(self):

        original_desc = "Error_node_offline base"
        modified_desc = "Error_node_offline modified"

        d = Error_node_offline.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:error_node_offline_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_put_error_node_offline(self):

        original_desc = "Error_node_offline base"
        modified_desc = "Error_node_offline modified"

        d = Error_node_offline.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:error_node_offline_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_delete_error_node_offline(self):

        original_desc = "Error_node_offline base"
        modified_desc = "Error_node_offline modified"

        d = Error_node_offline.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:error_node_offline_destroy', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        self.assertEqual(Error_node_offline.objects.count(), 1)

        response = self.apiClient.delete(url, data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Error_node_offline.objects.count(), 0)

    def test_list_error_node_offline(self):
        for i in range(0, 5):
            d = Error_node_offline.objects.create(
                creator=self.u,
                last_modifier=self.u,
            )
            d.title = "Error_node_offline {}".format(i)
            d.save()

        url = reverse('api:error_node_offline_list')
        response = self.apiClient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(len(response.data['results']), 5)

    def test_create_error_node_offline(self):

        error_node_offline_desc = 'Error_node_offline description'

        url = reverse('api:error_node_offline_create')

        data = {'description': error_node_offline_desc}  # , 'last_name': 'last name', "title": "doctor"}

        response = self.apiClient.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Error_node_offline.objects.count(), 1)
        self.assertEqual(Error_node_offline.objects.get().description, error_node_offline_desc)
        ##self.assertEqual(response.data[role].count, 1)

    def test_get_error_node_offline(self):
        error_node_offline_desc = 'Error_node_offline 1'
        # if you assign a customer or any other object
        # customer = Customer.objects.create()
        # customer.first_name = "Mario"
        # customer.last_name = "Rossi"
        # customer.save()

        obj = Error_node_offline.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        # you could assign it here after creation
        #d.customer = customer
        obj.description = error_node_offline_desc
        obj.save()
        id = obj.id
        url = reverse('api:error_node_offline_retrieve', kwargs={'pk': id})

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

        self.assertEqual(data['description'], obj.description)

        # self.assertEqual(len(dep['structured_doctors']), 5)
        # self.assertEqual(len(dep['employees']), 5)


        # if you assign a customer
        #self.assertEqual(m, customer.id)
from apps.wicloud.models import Gateway


class TestGateway(TestCase):

    apiClient = APIClient()
    u: UserModel

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

    def test_patch_gateway(self):

        original_desc = "Gateway base"
        modified_desc = "Gateway modified"

        d = Gateway.objects.create(
            creator=self.u,
            last_modifier=self.u,
            gateway_uuid='1234567890'
        )

        d.save()
        id = d.id
        url = reverse('api:gateway_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_put_gateway(self):

        original_desc = "Gateway base"
        modified_desc = "Gateway modified"

        d = Gateway.objects.create(
            creator=self.u,
            last_modifier=self.u,
            gateway_uuid='1234567890'
        )

        d.save()
        id = d.id
        url = reverse('api:gateway_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_delete_gateway(self):

        original_desc = "Gateway base"
        modified_desc = "Gateway modified"

        d = Gateway.objects.create(
            creator=self.u,
            last_modifier=self.u,
            gateway_uuid='1234567890'
        )

        d.save()
        id = d.id
        url = reverse('api:gateway_destroy', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        self.assertEqual(Gateway.objects.count(), 1)

        response = self.apiClient.delete(url, data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Gateway.objects.count(), 0)

    def test_list_gateway(self):
        for i in range(0, 5):
            d = Gateway.objects.create(
                creator=self.u,
                last_modifier=self.u,
                gateway_uuid=f'1234567890{i}'
            )
            d.title = "Gateway {}".format(i)
            d.save()

        url = reverse('api:gateway_list')
        response = self.apiClient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(len(response.data['results']), 5)

    def test_create_gateway(self):

        gateway_desc = 'Gateway description'

        url = reverse('api:gateway_create')

        data = {'description': gateway_desc,'gateway_uuid':'1234567890'}  # , 'last_name': 'last name', "title": "doctor"}

        response = self.apiClient.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Gateway.objects.count(), 1)
        self.assertEqual(Gateway.objects.get().description, gateway_desc)
        ##self.assertEqual(response.data[role].count, 1)

    def test_get_gateway(self):
        gateway_desc = 'Gateway 1'
        # if you assign a customer or any other object
        # customer = Customer.objects.create()
        # customer.first_name = "Mario"
        # customer.last_name = "Rossi"
        # customer.save()

        obj = Gateway.objects.create(
            creator=self.u,
            last_modifier=self.u,
            gateway_uuid='1234567890'
        )

        # you could assign it here after creation
        #d.customer = customer
        obj.description = gateway_desc
        obj.save()
        id = obj.id
        url = reverse('api:gateway_retrieve', kwargs={'pk': id})

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

        self.assertEqual(data['description'], obj.description)

        # self.assertEqual(len(dep['structured_doctors']), 5)
        # self.assertEqual(len(dep['employees']), 5)


        # if you assign a customer
        #self.assertEqual(m, customer.id)
from apps.wicloud.models import Ime_power_counter


class TestIme_power_counter(TestCase):

    apiClient = APIClient()
    u: UserModel

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

    def test_patch_ime_power_counter(self):

        original_desc = "Ime_power_counter base"
        modified_desc = "Ime_power_counter modified"

        d = Ime_power_counter.objects.create(
            creator=self.u,
            last_modifier=self.u,
            counter_id='1234567890'
        )

        d.save()
        id = d.id
        url = reverse('api:ime_power_counter_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_put_ime_power_counter(self):

        original_desc = "Ime_power_counter base"
        modified_desc = "Ime_power_counter modified"

        d = Ime_power_counter.objects.create(
            creator=self.u,
            last_modifier=self.u,
            counter_id='1234567890'
        )

        d.save()
        id = d.id
        url = reverse('api:ime_power_counter_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_delete_ime_power_counter(self):

        original_desc = "Ime_power_counter base"
        modified_desc = "Ime_power_counter modified"

        d = Ime_power_counter.objects.create(
            creator=self.u,
            last_modifier=self.u,
            counter_id='1234567890'
        )

        d.save()
        id = d.id
        url = reverse('api:ime_power_counter_destroy', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        self.assertEqual(Ime_power_counter.objects.count(), 1)

        response = self.apiClient.delete(url, data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Ime_power_counter.objects.count(), 0)

    def test_list_ime_power_counter(self):
        for i in range(0, 5):
            d = Ime_power_counter.objects.create(
                creator=self.u,
                last_modifier=self.u,
                counter_id=f'123456789{i}'
            )
            d.title = "Ime_power_counter {}".format(i)
            d.save()

        url = reverse('api:ime_power_counter_list')
        response = self.apiClient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(len(response.data['results']), 5)

    def test_create_ime_power_counter(self):

        ime_power_counter_desc = 'Ime_power_counter description'

        url = reverse('api:ime_power_counter_create')

        data = {'description': ime_power_counter_desc, 'counter_id':'1234567890'}  # , 'last_name': 'last name', "title": "doctor"}

        response = self.apiClient.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ime_power_counter.objects.count(), 1)
        self.assertEqual(Ime_power_counter.objects.get().description, ime_power_counter_desc)
        ##self.assertEqual(response.data[role].count, 1)

    def test_get_ime_power_counter(self):
        ime_power_counter_desc = 'Ime_power_counter 1'
        # if you assign a customer or any other object
        # customer = Customer.objects.create()
        # customer.first_name = "Mario"
        # customer.last_name = "Rossi"
        # customer.save()

        obj = Ime_power_counter.objects.create(
            creator=self.u,
            last_modifier=self.u,
            counter_id='1234567890'
        )

        # you could assign it here after creation
        #d.customer = customer
        obj.description = ime_power_counter_desc
        obj.save()
        id = obj.id
        url = reverse('api:ime_power_counter_retrieve', kwargs={'pk': id})

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

        self.assertEqual(data['description'], obj.description)

        # self.assertEqual(len(dep['structured_doctors']), 5)
        # self.assertEqual(len(dep['employees']), 5)


        # if you assign a customer
        #self.assertEqual(m, customer.id)
from apps.wicloud.models import Ime_power_measure


class TestIme_power_measure(TestCase):

    apiClient = APIClient()
    u: UserModel

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

    def test_patch_ime_power_measure(self):

        original_desc = "Ime_power_measure base"
        modified_desc = "Ime_power_measure modified"

        d = Ime_power_measure.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:ime_power_measure_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_put_ime_power_measure(self):

        original_desc = "Ime_power_measure base"
        modified_desc = "Ime_power_measure modified"

        d = Ime_power_measure.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:ime_power_measure_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_delete_ime_power_measure(self):

        original_desc = "Ime_power_measure base"
        modified_desc = "Ime_power_measure modified"

        d = Ime_power_measure.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:ime_power_measure_destroy', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        self.assertEqual(Ime_power_measure.objects.count(), 1)

        response = self.apiClient.delete(url, data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Ime_power_measure.objects.count(), 0)

    def test_list_ime_power_measure(self):
        for i in range(0, 5):
            d = Ime_power_measure.objects.create(
                creator=self.u,
                last_modifier=self.u,
            )
            d.title = "Ime_power_measure {}".format(i)
            d.save()

        url = reverse('api:ime_power_measure_list')
        response = self.apiClient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(len(response.data['results']), 5)

    def test_create_ime_power_measure(self):

        ime_power_measure_desc = 'Ime_power_measure description'

        url = reverse('api:ime_power_measure_create')

        data = {'description': ime_power_measure_desc}  # , 'last_name': 'last name', "title": "doctor"}

        response = self.apiClient.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ime_power_measure.objects.count(), 1)
        self.assertEqual(Ime_power_measure.objects.get().description, ime_power_measure_desc)
        ##self.assertEqual(response.data[role].count, 1)

    def test_get_ime_power_measure(self):
        ime_power_measure_desc = 'Ime_power_measure 1'
        # if you assign a customer or any other object
        # customer = Customer.objects.create()
        # customer.first_name = "Mario"
        # customer.last_name = "Rossi"
        # customer.save()

        obj = Ime_power_measure.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        # you could assign it here after creation
        #d.customer = customer
        obj.description = ime_power_measure_desc
        obj.save()
        id = obj.id
        url = reverse('api:ime_power_measure_retrieve', kwargs={'pk': id})

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

        self.assertEqual(data['description'], obj.description)

        # self.assertEqual(len(dep['structured_doctors']), 5)
        # self.assertEqual(len(dep['employees']), 5)


        # if you assign a customer
        #self.assertEqual(m, customer.id)
from apps.wicloud.models import Installation


class TestInstallation(TestCase):

    apiClient = APIClient()
    u: UserModel

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

        original_desc = "Installation base"
        modified_desc = "Installation modified"

        d = Installation.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:installation_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_put_installation(self):

        original_desc = "Installation base"
        modified_desc = "Installation modified"

        d = Installation.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:installation_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_delete_installation(self):

        original_desc = "Installation base"
        modified_desc = "Installation modified"

        d = Installation.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:installation_destroy', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        self.assertEqual(Installation.objects.count(), 1)

        response = self.apiClient.delete(url, data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Installation.objects.count(), 0)

    def test_list_installation(self):
        for i in range(0, 5):
            d = Installation.objects.create(
                creator=self.u,
                last_modifier=self.u,
            )
            d.title = "Installation {}".format(i)
            d.save()

        url = reverse('api:installation_list')
        response = self.apiClient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(len(response.data['results']), 5)

    def test_create_installation(self):

        installation_desc = 'Installation description'

        url = reverse('api:installation_create')

        data = {'description': installation_desc}  # , 'last_name': 'last name', "title": "doctor"}

        response = self.apiClient.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Installation.objects.count(), 1)
        self.assertEqual(Installation.objects.get().description, installation_desc)
        ##self.assertEqual(response.data[role].count, 1)

    def test_get_installation(self):
        installation_desc = 'Installation 1'
        # if you assign a customer or any other object
        # customer = Customer.objects.create()
        # customer.first_name = "Mario"
        # customer.last_name = "Rossi"
        # customer.save()

        obj = Installation.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        # you could assign it here after creation
        #d.customer = customer
        obj.description = installation_desc
        obj.save()
        id = obj.id
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

        self.assertEqual(data['description'], obj.description)

        # self.assertEqual(len(dep['structured_doctors']), 5)
        # self.assertEqual(len(dep['employees']), 5)


        # if you assign a customer
        #self.assertEqual(m, customer.id)
from apps.wicloud.models import Light_management_measure


class TestLight_management_measure(TestCase):

    apiClient = APIClient()
    u: UserModel

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

    def test_patch_light_management_measure(self):

        original_desc = "Light_management_measure base"
        modified_desc = "Light_management_measure modified"

        d = Light_management_measure.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:light_management_measure_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_put_light_management_measure(self):

        original_desc = "Light_management_measure base"
        modified_desc = "Light_management_measure modified"

        d = Light_management_measure.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:light_management_measure_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_delete_light_management_measure(self):

        original_desc = "Light_management_measure base"
        modified_desc = "Light_management_measure modified"

        d = Light_management_measure.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:light_management_measure_destroy', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        self.assertEqual(Light_management_measure.objects.count(), 1)

        response = self.apiClient.delete(url, data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Light_management_measure.objects.count(), 0)

    def test_list_light_management_measure(self):
        for i in range(0, 5):
            d = Light_management_measure.objects.create(
                creator=self.u,
                last_modifier=self.u,
            )
            d.title = "Light_management_measure {}".format(i)
            d.save()

        url = reverse('api:light_management_measure_list')
        response = self.apiClient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(len(response.data['results']), 5)

    def test_create_light_management_measure(self):

        light_management_measure_desc = 'Light_management_measure description'

        url = reverse('api:light_management_measure_create')

        data = {'description': light_management_measure_desc}  # , 'last_name': 'last name', "title": "doctor"}

        response = self.apiClient.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Light_management_measure.objects.count(), 1)
        self.assertEqual(Light_management_measure.objects.get().description, light_management_measure_desc)
        ##self.assertEqual(response.data[role].count, 1)

    def test_get_light_management_measure(self):
        light_management_measure_desc = 'Light_management_measure 1'
        # if you assign a customer or any other object
        # customer = Customer.objects.create()
        # customer.first_name = "Mario"
        # customer.last_name = "Rossi"
        # customer.save()

        obj = Light_management_measure.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        # you could assign it here after creation
        #d.customer = customer
        obj.description = light_management_measure_desc
        obj.save()
        id = obj.id
        url = reverse('api:light_management_measure_retrieve', kwargs={'pk': id})

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

        self.assertEqual(data['description'], obj.description)

        # self.assertEqual(len(dep['structured_doctors']), 5)
        # self.assertEqual(len(dep['employees']), 5)


        # if you assign a customer
        #self.assertEqual(m, customer.id)
from apps.wicloud.models import Light_management_module


class TestLight_management_module(TestCase):

    apiClient = APIClient()
    u: UserModel

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

    def test_patch_light_management_module(self):

        original_desc = "Light_management_module base"
        modified_desc = "Light_management_module modified"

        d = Light_management_module.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:light_management_module_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_put_light_management_module(self):

        original_desc = "Light_management_module base"
        modified_desc = "Light_management_module modified"

        d = Light_management_module.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:light_management_module_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_delete_light_management_module(self):

        original_desc = "Light_management_module base"
        modified_desc = "Light_management_module modified"

        d = Light_management_module.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:light_management_module_destroy', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        self.assertEqual(Light_management_module.objects.count(), 1)

        response = self.apiClient.delete(url, data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Light_management_module.objects.count(), 0)

    def test_list_light_management_module(self):
        for i in range(0, 5):
            d = Light_management_module.objects.create(
                creator=self.u,
                last_modifier=self.u,
            )
            d.title = "Light_management_module {}".format(i)
            d.save()

        url = reverse('api:light_management_module_list')
        response = self.apiClient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(len(response.data['results']), 5)

    def test_create_light_management_module(self):

        light_management_module_desc = 'Light_management_module description'

        url = reverse('api:light_management_module_create')

        data = {'description': light_management_module_desc}  # , 'last_name': 'last name', "title": "doctor"}

        response = self.apiClient.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Light_management_module.objects.count(), 1)
        self.assertEqual(Light_management_module.objects.get().description, light_management_module_desc)
        ##self.assertEqual(response.data[role].count, 1)

    def test_get_light_management_module(self):
        light_management_module_desc = 'Light_management_module 1'
        # if you assign a customer or any other object
        # customer = Customer.objects.create()
        # customer.first_name = "Mario"
        # customer.last_name = "Rossi"
        # customer.save()

        obj = Light_management_module.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        # you could assign it here after creation
        #d.customer = customer
        obj.description = light_management_module_desc
        obj.save()
        id = obj.id
        url = reverse('api:light_management_module_retrieve', kwargs={'pk': id})

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

        self.assertEqual(data['description'], obj.description)

        # self.assertEqual(len(dep['structured_doctors']), 5)
        # self.assertEqual(len(dep['employees']), 5)


        # if you assign a customer
        #self.assertEqual(m, customer.id)
from apps.wicloud.models import Light_profile


class TestLight_profile(TestCase):

    apiClient = APIClient()
    u: UserModel

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

    def test_patch_light_profile(self):

        original_desc = "Light_profile base"
        modified_desc = "Light_profile modified"

        d = Light_profile.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:light_profile_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_put_light_profile(self):

        original_desc = "Light_profile base"
        modified_desc = "Light_profile modified"

        d = Light_profile.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:light_profile_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_delete_light_profile(self):

        original_desc = "Light_profile base"
        modified_desc = "Light_profile modified"

        d = Light_profile.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:light_profile_destroy', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        self.assertEqual(Light_profile.objects.count(), 1)

        response = self.apiClient.delete(url, data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Light_profile.objects.count(), 0)

    def test_list_light_profile(self):
        for i in range(0, 5):
            d = Light_profile.objects.create(
                creator=self.u,
                last_modifier=self.u,
            )
            d.title = "Light_profile {}".format(i)
            d.save()

        url = reverse('api:light_profile_list')
        response = self.apiClient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(len(response.data['results']), 5)

    def test_create_light_profile(self):

        light_profile_desc = 'Light_profile description'

        url = reverse('api:light_profile_create')

        data = {'description': light_profile_desc}  # , 'last_name': 'last name', "title": "doctor"}

        response = self.apiClient.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Light_profile.objects.count(), 1)
        self.assertEqual(Light_profile.objects.get().description, light_profile_desc)
        ##self.assertEqual(response.data[role].count, 1)

    def test_get_light_profile(self):
        light_profile_desc = 'Light_profile 1'
        # if you assign a customer or any other object
        # customer = Customer.objects.create()
        # customer.first_name = "Mario"
        # customer.last_name = "Rossi"
        # customer.save()

        obj = Light_profile.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        # you could assign it here after creation
        #d.customer = customer
        obj.description = light_profile_desc
        obj.save()
        id = obj.id
        url = reverse('api:light_profile_retrieve', kwargs={'pk': id})

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

        self.assertEqual(data['description'], obj.description)

        # self.assertEqual(len(dep['structured_doctors']), 5)
        # self.assertEqual(len(dep['employees']), 5)


        # if you assign a customer
        #self.assertEqual(m, customer.id)
from apps.wicloud.models import Light_profile_slot


class TestLight_profile_slot(TestCase):

    apiClient = APIClient()
    u: UserModel

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

    def test_patch_light_profile_slot(self):

        original_desc = "Light_profile_slot base"
        modified_desc = "Light_profile_slot modified"

        d = Light_profile_slot.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:light_profile_slot_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_put_light_profile_slot(self):

        original_desc = "Light_profile_slot base"
        modified_desc = "Light_profile_slot modified"

        d = Light_profile_slot.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:light_profile_slot_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_delete_light_profile_slot(self):

        original_desc = "Light_profile_slot base"
        modified_desc = "Light_profile_slot modified"

        d = Light_profile_slot.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:light_profile_slot_destroy', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        self.assertEqual(Light_profile_slot.objects.count(), 1)

        response = self.apiClient.delete(url, data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Light_profile_slot.objects.count(), 0)

    def test_list_light_profile_slot(self):
        for i in range(0, 5):
            d = Light_profile_slot.objects.create(
                creator=self.u,
                last_modifier=self.u,
            )
            d.title = "Light_profile_slot {}".format(i)
            d.save()

        url = reverse('api:light_profile_slot_list')
        response = self.apiClient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(len(response.data['results']), 5)

    def test_create_light_profile_slot(self):

        light_profile_slot_desc = 'Light_profile_slot description'

        url = reverse('api:light_profile_slot_create')

        data = {'description': light_profile_slot_desc}  # , 'last_name': 'last name', "title": "doctor"}

        response = self.apiClient.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Light_profile_slot.objects.count(), 1)
        self.assertEqual(Light_profile_slot.objects.get().description, light_profile_slot_desc)
        ##self.assertEqual(response.data[role].count, 1)

    def test_get_light_profile_slot(self):
        light_profile_slot_desc = 'Light_profile_slot 1'
        # if you assign a customer or any other object
        # customer = Customer.objects.create()
        # customer.first_name = "Mario"
        # customer.last_name = "Rossi"
        # customer.save()

        obj = Light_profile_slot.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        # you could assign it here after creation
        #d.customer = customer
        obj.description = light_profile_slot_desc
        obj.save()
        id = obj.id
        url = reverse('api:light_profile_slot_retrieve', kwargs={'pk': id})

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

        self.assertEqual(data['description'], obj.description)

        # self.assertEqual(len(dep['structured_doctors']), 5)
        # self.assertEqual(len(dep['employees']), 5)


        # if you assign a customer
        #self.assertEqual(m, customer.id)
from apps.wicloud.models import Motion_event


class TestMotion_event(TestCase):

    apiClient = APIClient()
    u: UserModel

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

    def test_patch_motion_event(self):

        original_desc = "Motion_event base"
        modified_desc = "Motion_event modified"

        d = Motion_event.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:motion_event_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_put_motion_event(self):

        original_desc = "Motion_event base"
        modified_desc = "Motion_event modified"

        d = Motion_event.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:motion_event_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_delete_motion_event(self):

        original_desc = "Motion_event base"
        modified_desc = "Motion_event modified"

        d = Motion_event.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:motion_event_destroy', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        self.assertEqual(Motion_event.objects.count(), 1)

        response = self.apiClient.delete(url, data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Motion_event.objects.count(), 0)

    def test_list_motion_event(self):
        for i in range(0, 5):
            d = Motion_event.objects.create(
                creator=self.u,
                last_modifier=self.u,
            )
            d.title = "Motion_event {}".format(i)
            d.save()

        url = reverse('api:motion_event_list')
        response = self.apiClient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(len(response.data['results']), 5)

    def test_create_motion_event(self):

        motion_event_desc = 'Motion_event description'

        url = reverse('api:motion_event_create')

        data = {'description': motion_event_desc}  # , 'last_name': 'last name', "title": "doctor"}

        response = self.apiClient.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Motion_event.objects.count(), 1)
        self.assertEqual(Motion_event.objects.get().description, motion_event_desc)
        ##self.assertEqual(response.data[role].count, 1)

    def test_get_motion_event(self):
        motion_event_desc = 'Motion_event 1'
        # if you assign a customer or any other object
        # customer = Customer.objects.create()
        # customer.first_name = "Mario"
        # customer.last_name = "Rossi"
        # customer.save()

        obj = Motion_event.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        # you could assign it here after creation
        #d.customer = customer
        obj.description = motion_event_desc
        obj.save()
        id = obj.id
        url = reverse('api:motion_event_retrieve', kwargs={'pk': id})

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

        self.assertEqual(data['description'], obj.description)

        # self.assertEqual(len(dep['structured_doctors']), 5)
        # self.assertEqual(len(dep['employees']), 5)


        # if you assign a customer
        #self.assertEqual(m, customer.id)
from apps.wicloud.models import Node


class TestNode(TestCase):

    apiClient = APIClient()
    u: UserModel

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

    def test_patch_node(self):

        original_desc = "Node base"
        modified_desc = "Node modified"

        d = Node.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:node_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_put_node(self):

        original_desc = "Node base"
        modified_desc = "Node modified"

        d = Node.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:node_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_delete_node(self):

        original_desc = "Node base"
        modified_desc = "Node modified"

        d = Node.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:node_destroy', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        self.assertEqual(Node.objects.count(), 1)

        response = self.apiClient.delete(url, data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Node.objects.count(), 0)

    def test_list_node(self):
        for i in range(0, 5):
            d = Node.objects.create(
                creator=self.u,
                last_modifier=self.u,
            )
            d.title = "Node {}".format(i)
            d.save()

        url = reverse('api:node_list')
        response = self.apiClient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(len(response.data['results']), 5)

    def test_create_node(self):

        node_desc = 'Node description'

        url = reverse('api:node_create')

        data = {'description': node_desc}  # , 'last_name': 'last name', "title": "doctor"}

        response = self.apiClient.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Node.objects.count(), 1)
        self.assertEqual(Node.objects.get().description, node_desc)
        ##self.assertEqual(response.data[role].count, 1)

    def test_get_node(self):
        node_desc = 'Node 1'
        # if you assign a customer or any other object
        # customer = Customer.objects.create()
        # customer.first_name = "Mario"
        # customer.last_name = "Rossi"
        # customer.save()

        obj = Node.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        # you could assign it here after creation
        #d.customer = customer
        obj.description = node_desc
        obj.save()
        id = obj.id
        url = reverse('api:node_retrieve', kwargs={'pk': id})

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

        self.assertEqual(data['description'], obj.description)

        # self.assertEqual(len(dep['structured_doctors']), 5)
        # self.assertEqual(len(dep['employees']), 5)


        # if you assign a customer
        #self.assertEqual(m, customer.id)
from apps.wicloud.models import Node_module


class TestNode_module(TestCase):

    apiClient = APIClient()
    u: UserModel

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

    def test_patch_node_module(self):

        original_desc = "Node_module base"
        modified_desc = "Node_module modified"

        d = Node_module.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:node_module_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_put_node_module(self):

        original_desc = "Node_module base"
        modified_desc = "Node_module modified"

        d = Node_module.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:node_module_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_delete_node_module(self):

        original_desc = "Node_module base"
        modified_desc = "Node_module modified"

        d = Node_module.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:node_module_destroy', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        self.assertEqual(Node_module.objects.count(), 1)

        response = self.apiClient.delete(url, data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Node_module.objects.count(), 0)

    def test_list_node_module(self):
        for i in range(0, 5):
            d = Node_module.objects.create(
                creator=self.u,
                last_modifier=self.u,
            )
            d.title = "Node_module {}".format(i)
            d.save()

        url = reverse('api:node_module_list')
        response = self.apiClient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(len(response.data['results']), 5)

    def test_create_node_module(self):

        node_module_desc = 'Node_module description'

        url = reverse('api:node_module_create')

        data = {'description': node_module_desc}  # , 'last_name': 'last name', "title": "doctor"}

        response = self.apiClient.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Node_module.objects.count(), 1)
        self.assertEqual(Node_module.objects.get().description, node_module_desc)
        ##self.assertEqual(response.data[role].count, 1)

    def test_get_node_module(self):
        node_module_desc = 'Node_module 1'
        # if you assign a customer or any other object
        # customer = Customer.objects.create()
        # customer.first_name = "Mario"
        # customer.last_name = "Rossi"
        # customer.save()

        obj = Node_module.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        # you could assign it here after creation
        #d.customer = customer
        obj.description = node_module_desc
        obj.save()
        id = obj.id
        url = reverse('api:node_module_retrieve', kwargs={'pk': id})

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

        self.assertEqual(data['description'], obj.description)

        # self.assertEqual(len(dep['structured_doctors']), 5)
        # self.assertEqual(len(dep['employees']), 5)


        # if you assign a customer
        #self.assertEqual(m, customer.id)
from apps.wicloud.models import Wilamp_alert


class TestWilamp_alert(TestCase):

    apiClient = APIClient()
    u: UserModel

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

    def test_patch_wilamp_alert(self):

        original_desc = "Wilamp_alert base"
        modified_desc = "Wilamp_alert modified"

        d = Wilamp_alert.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:wilamp_alert_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_put_wilamp_alert(self):

        original_desc = "Wilamp_alert base"
        modified_desc = "Wilamp_alert modified"

        d = Wilamp_alert.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:wilamp_alert_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_delete_wilamp_alert(self):

        original_desc = "Wilamp_alert base"
        modified_desc = "Wilamp_alert modified"

        d = Wilamp_alert.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:wilamp_alert_destroy', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        self.assertEqual(Wilamp_alert.objects.count(), 1)

        response = self.apiClient.delete(url, data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Wilamp_alert.objects.count(), 0)

    def test_list_wilamp_alert(self):
        for i in range(0, 5):
            d = Wilamp_alert.objects.create(
                creator=self.u,
                last_modifier=self.u,
            )
            d.title = "Wilamp_alert {}".format(i)
            d.save()

        url = reverse('api:wilamp_alert_list')
        response = self.apiClient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(len(response.data['results']), 5)

    def test_create_wilamp_alert(self):

        wilamp_alert_desc = 'Wilamp_alert description'

        url = reverse('api:wilamp_alert_create')

        data = {'description': wilamp_alert_desc}  # , 'last_name': 'last name', "title": "doctor"}

        response = self.apiClient.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Wilamp_alert.objects.count(), 1)
        self.assertEqual(Wilamp_alert.objects.get().description, wilamp_alert_desc)
        ##self.assertEqual(response.data[role].count, 1)

    def test_get_wilamp_alert(self):
        wilamp_alert_desc = 'Wilamp_alert 1'
        # if you assign a customer or any other object
        # customer = Customer.objects.create()
        # customer.first_name = "Mario"
        # customer.last_name = "Rossi"
        # customer.save()

        obj = Wilamp_alert.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        # you could assign it here after creation
        #d.customer = customer
        obj.description = wilamp_alert_desc
        obj.save()
        id = obj.id
        url = reverse('api:wilamp_alert_retrieve', kwargs={'pk': id})

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

        self.assertEqual(data['description'], obj.description)

        # self.assertEqual(len(dep['structured_doctors']), 5)
        # self.assertEqual(len(dep['employees']), 5)


        # if you assign a customer
        #self.assertEqual(m, customer.id)
from apps.wicloud.models import Feeder_pillar


class TestFeeder_pillar(TestCase):

    apiClient = APIClient()
    u: UserModel

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

    def test_patch_feeder_pillar(self):

        original_desc = "Feeder_pillar base"
        modified_desc = "Feeder_pillar modified"

        d = Feeder_pillar.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:feeder_pillar_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_put_feeder_pillar(self):

        original_desc = "Feeder_pillar base"
        modified_desc = "Feeder_pillar modified"

        d = Feeder_pillar.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:feeder_pillar_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_delete_feeder_pillar(self):

        original_desc = "Feeder_pillar base"
        modified_desc = "Feeder_pillar modified"

        d = Feeder_pillar.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:feeder_pillar_destroy', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        self.assertEqual(Feeder_pillar.objects.count(), 1)

        response = self.apiClient.delete(url, data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Feeder_pillar.objects.count(), 0)

    def test_list_feeder_pillar(self):
        for i in range(0, 5):
            d = Feeder_pillar.objects.create(
                creator=self.u,
                last_modifier=self.u,
            )
            d.title = "Feeder_pillar {}".format(i)
            d.save()

        url = reverse('api:feeder_pillar_list')
        response = self.apiClient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(len(response.data['results']), 5)

    def test_create_feeder_pillar(self):

        feeder_pillar_desc = 'Feeder_pillar description'

        url = reverse('api:feeder_pillar_create')

        data = {'description': feeder_pillar_desc}  # , 'last_name': 'last name', "title": "doctor"}

        response = self.apiClient.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Feeder_pillar.objects.count(), 1)
        self.assertEqual(Feeder_pillar.objects.get().description, feeder_pillar_desc)
        ##self.assertEqual(response.data[role].count, 1)

    def test_get_feeder_pillar(self):
        feeder_pillar_desc = 'Feeder_pillar 1'
        # if you assign a customer or any other object
        # customer = Customer.objects.create()
        # customer.first_name = "Mario"
        # customer.last_name = "Rossi"
        # customer.save()

        obj = Feeder_pillar.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        # you could assign it here after creation
        #d.customer = customer
        obj.description = feeder_pillar_desc
        obj.save()
        id = obj.id
        url = reverse('api:feeder_pillar_retrieve', kwargs={'pk': id})

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

        self.assertEqual(data['description'], obj.description)

        # self.assertEqual(len(dep['structured_doctors']), 5)
        # self.assertEqual(len(dep['employees']), 5)


        # if you assign a customer
        #self.assertEqual(m, customer.id)
from apps.wicloud.models import Twilight_management_module


class TestTwilight_management_module(TestCase):

    apiClient = APIClient()
    u: UserModel

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

    def test_patch_twilight_management_module(self):

        original_desc = "Twilight_management_module base"
        modified_desc = "Twilight_management_module modified"

        d = Twilight_management_module.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:twilight_management_module_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_put_twilight_management_module(self):

        original_desc = "Twilight_management_module base"
        modified_desc = "Twilight_management_module modified"

        d = Twilight_management_module.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:twilight_management_module_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_delete_twilight_management_module(self):

        original_desc = "Twilight_management_module base"
        modified_desc = "Twilight_management_module modified"

        d = Twilight_management_module.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:twilight_management_module_destroy', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        self.assertEqual(Twilight_management_module.objects.count(), 1)

        response = self.apiClient.delete(url, data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Twilight_management_module.objects.count(), 0)

    def test_list_twilight_management_module(self):
        for i in range(0, 5):
            d = Twilight_management_module.objects.create(
                creator=self.u,
                last_modifier=self.u,
            )
            d.title = "Twilight_management_module {}".format(i)
            d.save()

        url = reverse('api:twilight_management_module_list')
        response = self.apiClient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(len(response.data['results']), 5)

    def test_create_twilight_management_module(self):

        twilight_management_module_desc = 'Twilight_management_module description'

        url = reverse('api:twilight_management_module_create')

        data = {'description': twilight_management_module_desc}  # , 'last_name': 'last name', "title": "doctor"}

        response = self.apiClient.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Twilight_management_module.objects.count(), 1)
        self.assertEqual(Twilight_management_module.objects.get().description, twilight_management_module_desc)
        ##self.assertEqual(response.data[role].count, 1)

    def test_get_twilight_management_module(self):
        twilight_management_module_desc = 'Twilight_management_module 1'
        # if you assign a customer or any other object
        # customer = Customer.objects.create()
        # customer.first_name = "Mario"
        # customer.last_name = "Rossi"
        # customer.save()

        obj = Twilight_management_module.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        # you could assign it here after creation
        #d.customer = customer
        obj.description = twilight_management_module_desc
        obj.save()
        id = obj.id
        url = reverse('api:twilight_management_module_retrieve', kwargs={'pk': id})

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

        self.assertEqual(data['description'], obj.description)

        # self.assertEqual(len(dep['structured_doctors']), 5)
        # self.assertEqual(len(dep['employees']), 5)


        # if you assign a customer
        #self.assertEqual(m, customer.id)
from apps.wicloud.models import Twilight_measure


class TestTwilight_measure(TestCase):

    apiClient = APIClient()
    u: UserModel

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

    def test_patch_twilight_measure(self):

        original_desc = "Twilight_measure base"
        modified_desc = "Twilight_measure modified"

        d = Twilight_measure.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:twilight_measure_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_put_twilight_measure(self):

        original_desc = "Twilight_measure base"
        modified_desc = "Twilight_measure modified"

        d = Twilight_measure.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:twilight_measure_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_delete_twilight_measure(self):

        original_desc = "Twilight_measure base"
        modified_desc = "Twilight_measure modified"

        d = Twilight_measure.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:twilight_measure_destroy', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        self.assertEqual(Twilight_measure.objects.count(), 1)

        response = self.apiClient.delete(url, data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Twilight_measure.objects.count(), 0)

    def test_list_twilight_measure(self):
        for i in range(0, 5):
            d = Twilight_measure.objects.create(
                creator=self.u,
                last_modifier=self.u,
            )
            d.title = "Twilight_measure {}".format(i)
            d.save()

        url = reverse('api:twilight_measure_list')
        response = self.apiClient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(len(response.data['results']), 5)

    def test_create_twilight_measure(self):

        twilight_measure_desc = 'Twilight_measure description'

        url = reverse('api:twilight_measure_create')

        data = {'description': twilight_measure_desc}  # , 'last_name': 'last name', "title": "doctor"}

        response = self.apiClient.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Twilight_measure.objects.count(), 1)
        self.assertEqual(Twilight_measure.objects.get().description, twilight_measure_desc)
        ##self.assertEqual(response.data[role].count, 1)

    def test_get_twilight_measure(self):
        twilight_measure_desc = 'Twilight_measure 1'
        # if you assign a customer or any other object
        # customer = Customer.objects.create()
        # customer.first_name = "Mario"
        # customer.last_name = "Rossi"
        # customer.save()

        obj = Twilight_measure.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        # you could assign it here after creation
        #d.customer = customer
        obj.description = twilight_measure_desc
        obj.save()
        id = obj.id
        url = reverse('api:twilight_measure_retrieve', kwargs={'pk': id})

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

        self.assertEqual(data['description'], obj.description)

        # self.assertEqual(len(dep['structured_doctors']), 5)
        # self.assertEqual(len(dep['employees']), 5)


        # if you assign a customer
        #self.assertEqual(m, customer.id)
from apps.wicloud.models import Motion_management_module


class TestMotion_management_module(TestCase):

    apiClient = APIClient()
    u: UserModel

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

    def test_patch_motion_management_module(self):

        original_desc = "Motion_management_module base"
        modified_desc = "Motion_management_module modified"

        d = Motion_management_module.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:motion_management_module_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_put_motion_management_module(self):

        original_desc = "Motion_management_module base"
        modified_desc = "Motion_management_module modified"

        d = Motion_management_module.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:motion_management_module_partial_update', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        response = self.apiClient.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], modified_desc)
        self.assertEqual(response.data["id"], id)

    def test_delete_motion_management_module(self):

        original_desc = "Motion_management_module base"
        modified_desc = "Motion_management_module modified"

        d = Motion_management_module.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        d.save()
        id = d.id
        url = reverse('api:motion_management_module_destroy', kwargs={'pk': id})
        data = {'description': modified_desc, 'id': id}

        self.assertEqual(Motion_management_module.objects.count(), 1)

        response = self.apiClient.delete(url, data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Motion_management_module.objects.count(), 0)

    def test_list_motion_management_module(self):
        for i in range(0, 5):
            d = Motion_management_module.objects.create(
                creator=self.u,
                last_modifier=self.u,
            )
            d.title = "Motion_management_module {}".format(i)
            d.save()

        url = reverse('api:motion_management_module_list')
        response = self.apiClient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(len(response.data['results']), 5)

    def test_create_motion_management_module(self):

        motion_management_module_desc = 'Motion_management_module description'

        url = reverse('api:motion_management_module_create')

        data = {'description': motion_management_module_desc}  # , 'last_name': 'last name', "title": "doctor"}

        response = self.apiClient.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Motion_management_module.objects.count(), 1)
        self.assertEqual(Motion_management_module.objects.get().description, motion_management_module_desc)
        ##self.assertEqual(response.data[role].count, 1)

    def test_get_motion_management_module(self):
        motion_management_module_desc = 'Motion_management_module 1'
        # if you assign a customer or any other object
        # customer = Customer.objects.create()
        # customer.first_name = "Mario"
        # customer.last_name = "Rossi"
        # customer.save()

        obj = Motion_management_module.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )

        # you could assign it here after creation
        #d.customer = customer
        obj.description = motion_management_module_desc
        obj.save()
        id = obj.id
        url = reverse('api:motion_management_module_retrieve', kwargs={'pk': id})

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

        self.assertEqual(data['description'], obj.description)

        # self.assertEqual(len(dep['structured_doctors']), 5)
        # self.assertEqual(len(dep['employees']), 5)

        # if you assign a customer
        #self.assertEqual(m, customer.id)
