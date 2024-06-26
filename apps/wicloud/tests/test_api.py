from test_plus.test import TestCase
# from ipdbackend.tests import JWTAuthTestCase
from unittest import mock

from web.core.models import UserModel
from django.contrib.auth.models import User
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
            fullName='Full name address'
        )

        d.save()
        id = d.id
        url = reverse('api:address_detail', kwargs={'id': id})
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
            fullName="fullname"
        )

        d.save()
        id = d.id
        url = reverse('api:address_detail', kwargs={'id': id})
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
            fullName="fullname"
        )

        d.save()
        id = d.id
        url = reverse('api:address_detail', kwargs={'id': id})
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
                fullName="Full name"
            )
            d.title = "Address {}".format(i)
            d.save()

        url = reverse('api:address_list')
        response = self.apiClient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(len(response.data['results']), 5)

    def test_create_address(self):
        fullName = 'Via roma'
        address_desc = 'Address description'

        url = reverse('api:address_list')

        data = {'description': address_desc, 'fullName': fullName}  # , 'last_name': 'last name', "title": "doctor"}

        response = self.apiClient.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Address.objects.count(), 1)
        self.assertEqual(Address.objects.get().description, address_desc)
        self.assertEqual(Address.objects.get().fullName, fullName)
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
            fullName='Via roma'
        )

        # you could assign it here after creation
        #d.customer = customer

        obj.description = address_desc
        obj.save()
        id = obj.id
        url = reverse('api:address_detail', kwargs={'id': id})

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
            companyName='Company_name'
        )

        d.save()
        id = d.id
        url = reverse('api:customer_detail', kwargs={'id': id})
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
            companyName='Company_name'
        )

        d.save()
        id = d.id
        url = reverse('api:customer_detail', kwargs={'id': id})
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
            companyName='Company_name'
        )

        d.save()
        id = d.id
        url = reverse('api:customer_detail', kwargs={'id': id})
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
                companyName='Company_name'
            )
            d.title = "Customer {}".format(i)
            d.save()

        url = reverse('api:customer_list')
        response = self.apiClient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(len(response.data['results']), 5)

    def test_create_customer(self):

        customer_desc = 'Customer description'

        url = reverse('api:customer_list')

        data = {'description': customer_desc, 'companyName':'Company_name'}  # , 'last_name': 'last name', "title": "doctor"}

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
            companyName='Company_name'
        )

        # you could assign it here after creation
        #d.customer = customer
        obj.description = customer_desc
        obj.save()
        id = obj.id
        url = reverse('api:customer_detail', kwargs={'id': id})

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
        url = reverse('api:energy_interval_detail', kwargs={'id': id})
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
        url = reverse('api:energy_interval_detail', kwargs={'id': id})
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
        url = reverse('api:energy_interval_detail', kwargs={'id': id})
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

        url = reverse('api:energy_interval_list')

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
        url = reverse('api:energy_interval_detail', kwargs={'id': id})

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
        url = reverse('api:energy_meter_module_detail', kwargs={'id': id})
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
        url = reverse('api:energy_meter_module_detail', kwargs={'id': id})
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
        url = reverse('api:energy_meter_module_detail', kwargs={'id': id})
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

        url = reverse('api:energy_meter_module_list')

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
        url = reverse('api:energy_meter_module_detail', kwargs={'id': id})

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

    # def test_get_energy_meter_module_by_mac(self):
    #     energy_meter_module_desc = 'Energy_meter_module 1'
    #     node_mac = "test"
    #
    #     # if you assign a customer or any other object
    #     # customer = Customer.objects.create()
    #     # customer.first_name = "Mario"
    #     # customer.last_name = "Rossi"
    #     # customer.save()
    #
    #     obj = Energy_meter_module.objects.create(
    #         creator=self.u,
    #         last_modifier=self.u,
    #     )
    #
    #     # you could assign it here after creation
    #     #d.customer = customer
    #     obj.description = energy_meter_module_desc
    #     obj.save()
    #     id = obj.id
    #
    #     modules_obj = Node_module.objects.create(
    #         creator=self.u,
    #         last_modifier=self.u,
    #         energyMeter_id=id
    #     )
    #     modules_obj.save()
    #     node_modules_id = modules_obj.id
    #
    #     node_obj = Node.objects.create(
    #         creator=self.u,
    #         last_modifier=self.u,
    #         mac=node_mac,
    #         modules_id=node_modules_id
    #     )
    #     node_obj.save()
    #
    #     url = reverse('api:energy_meter_module_by_mac_detail', kwargs={'id': node_mac})
    #
    #     # example on how to create child entities that belongs to this entity
    #     # for i in range(0, 5):
    #     #     e = Employee.objects.create()
    #     #     e.title = "employee {}".format(i)
    #     #
    #     #
    #     #     e.save()
    #     #
    #     #     d.structured_doctors.add(e)
    #     #
    #     # for i in range(0, 5):
    #     #     em = Employee.objects.create()
    #     #     em.title = "employee {}".format(i)
    #     #
    #     #     em.save()
    #     #     d.employees.add(em)
    #
    #     response = self.apiClient.get(url)
    #
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    #     data = response.data
    #
    #     self.assertEqual(data['description'], obj.description)
    #
    #     # self.assertEqual(len(dep['structured_doctors']), 5)
    #     # self.assertEqual(len(dep['employees']), 5)
    #
    #
    #     # if you assign a customer
    #     #self.assertEqual(m, customer.id)

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
        url = reverse('api:energy_meter_peak_measure_detail', kwargs={'id': id})
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
        url = reverse('api:energy_meter_peak_measure_detail', kwargs={'id': id})
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
        url = reverse('api:energy_meter_peak_measure_detail', kwargs={'id': id})
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

        url = reverse('api:energy_meter_peak_measure_list')

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
        url = reverse('api:energy_meter_peak_measure_detail', kwargs={'id': id})

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
        url = reverse('api:error_light_level_and_adc_mismatch_detail', kwargs={'id': id})
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
        url = reverse('api:error_light_level_and_adc_mismatch_detail', kwargs={'id': id})
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
        url = reverse('api:error_light_level_and_adc_mismatch_detail', kwargs={'id': id})
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

        url = reverse('api:error_light_level_and_adc_mismatch_list')

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
        url = reverse('api:error_light_level_and_adc_mismatch_detail', kwargs={'id': id})

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
        url = reverse('api:error_light_level_and_power_mismatch_detail', kwargs={'id': id})
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
        url = reverse('api:error_light_level_and_power_mismatch_detail', kwargs={'id': id})
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
        url = reverse('api:error_light_level_and_power_mismatch_detail', kwargs={'id': id})
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

        url = reverse('api:error_light_level_and_power_mismatch_list')

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
        url = reverse('api:error_light_level_and_power_mismatch_detail', kwargs={'id': id})

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
        url = reverse('api:error_node_offline_detail', kwargs={'id': id})
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
        url = reverse('api:error_node_offline_detail', kwargs={'id': id})
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
        url = reverse('api:error_node_offline_detail', kwargs={'id': id})
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

        url = reverse('api:error_node_offline_list')

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
        url = reverse('api:error_node_offline_detail', kwargs={'id': id})

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
            gatewayUUID='1234567890'
        )

        d.save()
        id = d.id
        url = reverse('api:gateway_detail', kwargs={'id': id})
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
            gatewayUUID='1234567890'
        )

        d.save()
        id = d.id
        url = reverse('api:gateway_detail', kwargs={'id': id})
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
            gatewayUUID='1234567890'
        )

        d.save()
        id = d.id
        url = reverse('api:gateway_detail', kwargs={'id': id})
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
                gatewayUUID=f'1234567890{i}'
            )
            d.title = "Gateway {}".format(i)
            d.save()

        url = reverse('api:gateway_list')
        response = self.apiClient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(len(response.data['results']), 5)

    def test_create_gateway(self):

        gateway_desc = 'Gateway description'

        url = reverse('api:gateway_list')

        data = {'description': gateway_desc,'gatewayUUID':'1234567890'}  # , 'last_name': 'last name', "title": "doctor"}

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
            gatewayUUID='1234567890'
        )

        # you could assign it here after creation
        #d.customer = customer
        obj.description = gateway_desc
        obj.save()
        id = obj.id
        url = reverse('api:gateway_detail', kwargs={'id': id})

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
            counterId='1234567890'
        )

        d.save()
        id = d.id
        url = reverse('api:ime_power_counter_detail', kwargs={'id': id})
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
            counterId='1234567890'
        )

        d.save()
        id = d.id
        url = reverse('api:ime_power_counter_detail', kwargs={'id': id})
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
            counterId='1234567890'
        )

        d.save()
        id = d.id
        url = reverse('api:ime_power_counter_detail', kwargs={'id': id})
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
                counterId=f'123456789{i}'
            )
            d.title = "Ime_power_counter {}".format(i)
            d.save()

        url = reverse('api:ime_power_counter_list')
        response = self.apiClient.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIs(len(response.data['results']), 5)

    def test_create_ime_power_counter(self):

        ime_power_counter_desc = 'Ime_power_counter description'

        url = reverse('api:ime_power_counter_list')

        data = {'description': ime_power_counter_desc, 'counterId':'1234567890'}  # , 'last_name': 'last name', "title": "doctor"}

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
            counterId='1234567890'
        )

        # you could assign it here after creation
        #d.customer = customer
        obj.description = ime_power_counter_desc
        obj.save()
        id = obj.id
        url = reverse('api:ime_power_counter_detail', kwargs={'id': id})

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
        url = reverse('api:ime_power_measure_detail', kwargs={'id': id})
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
        url = reverse('api:ime_power_measure_detail', kwargs={'id': id})
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
        url = reverse('api:ime_power_measure_detail', kwargs={'id': id})
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

        url = reverse('api:ime_power_measure_list')

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
        url = reverse('api:ime_power_measure_detail', kwargs={'id': id})

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
        url = reverse('api:installation_detail', kwargs={'id': id})
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
        url = reverse('api:installation_detail', kwargs={'id': id})
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
        url = reverse('api:installation_detail', kwargs={'id': id})
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

        url = reverse('api:installation_list')

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
        url = reverse('api:installation_detail', kwargs={'id': id})

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


    def installation_visibility(self):
        password = 'password'
        installer1 = self.make_user(username='installer1', password=password)
        installer2 = self.make_user(username='installer2', password=password)
        assets_manager = self.make_user(username='assets_manager', password=password)
        viewer = self.make_user(username='viewer', password=password)
        installation_manager = self.make_user(username='installation_manager', password=password)

        installation1 = Installation.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )
        installation1.description = "Installazione 1"
        installation1.installer = installer1
        installation1.save()
        installation2 = Installation.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )
        installation2.description = "Installazione 2"
        installation2.installer = installer2
        installation2.save()
        url_list = reverse('api:installation_list')
        print(url_list)
        # mi autentico come installatore 1
        resp = self.client.post(reverse('api-jwt-auth'), {'email': "installer2", 'password': password},
                                format='json')
        token = resp.data['token']
        self.apiClient.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.apiClient.get(url_list)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['description'], installation2.description)

        installation3 = Installation.objects.create(
            creator=self.u,
            last_modifier=self.u,
        )
        installation3.description = "Installazione 3"
        installation3.assetsManagers.add(installer2)
        installation3.save()
        print(installation3.assetsManagers.get())
        response = self.apiClient.get(url_list)
        self.assertEqual(len(response.data['results']), 2)


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
        url = reverse('api:light_management_measure_detail', kwargs={'id': id})
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
        url = reverse('api:light_management_measure_detail', kwargs={'id': id})
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
        url = reverse('api:light_management_measure_detail', kwargs={'id': id})
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

        url = reverse('api:light_management_measure_list')

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
        url = reverse('api:light_management_measure_detail', kwargs={'id': id})

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
        url = reverse('api:light_management_module_detail', kwargs={'id': id})
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
        url = reverse('api:light_management_module_detail', kwargs={'id': id})
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
        url = reverse('api:light_management_module_detail', kwargs={'id': id})
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

        url = reverse('api:light_management_module_list')

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
        url = reverse('api:light_management_module_detail', kwargs={'id': id})

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
        url = reverse('api:light_profile_detail', kwargs={'id': id})
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
        url = reverse('api:light_profile_detail', kwargs={'id': id})
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
        url = reverse('api:light_profile_detail', kwargs={'id': id})
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

        url = reverse('api:light_profile_list')

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
        url = reverse('api:light_profile_detail', kwargs={'id': id})

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
        url = reverse('api:light_profile_slot_detail', kwargs={'id': id})
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
        url = reverse('api:light_profile_slot_detail', kwargs={'id': id})
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
        url = reverse('api:light_profile_slot_detail', kwargs={'id': id})
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

        url = reverse('api:light_profile_slot_list')

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
        url = reverse('api:light_profile_slot_detail', kwargs={'id': id})

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
        url = reverse('api:motion_event_detail', kwargs={'id': id})
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
        url = reverse('api:motion_event_detail', kwargs={'id': id})
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
        url = reverse('api:motion_event_detail', kwargs={'id': id})
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

        url = reverse('api:motion_event_list')

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
        url = reverse('api:motion_event_detail', kwargs={'id': id})

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
        url = reverse('api:node_detail', kwargs={'id': id})
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
        url = reverse('api:node_detail', kwargs={'id': id})
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
        url = reverse('api:node_detail', kwargs={'id': id})
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

        url = reverse('api:node_list')

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
        url = reverse('api:node_detail', kwargs={'id': id})

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

#from apps.wicloud.models import Node_module
#
#
# class TestNode_module(TestCase):
#
#     apiClient = APIClient()
#     u: UserModel
#
#     def setUp(self):
#         settings.MEDIA_ROOT = tempfile.mkdtemp()
#
#         url = reverse('api-jwt-auth')
#         self.u = self.make_user(username='apitest', password='apitest')
#         self.u.is_active = False
#         self.u.save()
#
#         resp = self.client.post(url, {'email': 'testuser', 'password': 'password'}, format='json')
#         self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
#
#         self.u.is_active = True
#         self.u.must_change_password = False
#         self.u.save()
#
#         resp = self.client.post(url, {'email': 'apitest', 'password': 'apitest'}, format='json')
#         self.assertEqual(resp.status_code, status.HTTP_200_OK)
#         self.assertTrue('token' in resp.data)
#         # self.assertTrue('refresh' in resp.data)
#         token = resp.data['token']
#         # refresh = resp.data['refresh']
#
#         # print(token)
#
#         verification_url = reverse('api-jwt-refresh')
#         resp = self.client.post(verification_url, {'token': token}, format='json')
#         self.assertEqual(resp.status_code, status.HTTP_200_OK)
#
#         resp = self.client.post(verification_url, {'token': 'abc'}, format='json')
#         self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
#
#         self.apiClient.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
#
#     def test_patch_node_module(self):
#
#         original_desc = "Node_module base"
#         modified_desc = "Node_module modified"
#
#         d = Node_module.objects.create(
#             creator=self.u,
#             last_modifier=self.u,
#         )
#
#         d.save()
#         id = d.id
#         url = reverse('api:node_module_detail', kwargs={'id': id})
#         data = {'description': modified_desc, 'id': id}
#
#         response = self.apiClient.patch(url, data)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data["description"], modified_desc)
#         self.assertEqual(response.data["id"], id)
#
#     def test_put_node_module(self):
#
#         original_desc = "Node_module base"
#         modified_desc = "Node_module modified"
#
#         d = Node_module.objects.create(
#             creator=self.u,
#             last_modifier=self.u,
#         )
#
#         d.save()
#         id = d.id
#         url = reverse('api:node_module_detail', kwargs={'id': id})
#         data = {'description': modified_desc, 'id': id}
#
#         response = self.apiClient.put(url, data)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data["description"], modified_desc)
#         self.assertEqual(response.data["id"], id)
#
#     def test_delete_node_module(self):
#
#         original_desc = "Node_module base"
#         modified_desc = "Node_module modified"
#
#         d = Node_module.objects.create(
#             creator=self.u,
#             last_modifier=self.u,
#         )
#
#         d.save()
#         id = d.id
#         url = reverse('api:node_module_detail', kwargs={'id': id})
#         data = {'description': modified_desc, 'id': id}
#
#         self.assertEqual(Node_module.objects.count(), 1)
#
#         response = self.apiClient.delete(url, data)
#
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Node_module.objects.count(), 0)
#
#     def test_list_node_module(self):
#         for i in range(0, 5):
#             d = Node_module.objects.create(
#                 creator=self.u,
#                 last_modifier=self.u,
#             )
#             d.title = "Node_module {}".format(i)
#             d.save()
#
#         url = reverse('api:node_module_list')
#         response = self.apiClient.get(url)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIs(len(response.data['results']), 5)
#
#     def test_create_node_module(self):
#
#         node_module_desc = 'Node_module description'
#
#         url = reverse('api:node_module_list')
#
#         data = {'description': node_module_desc}  # , 'last_name': 'last name', "title": "doctor"}
#
#         response = self.apiClient.post(url, data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Node_module.objects.count(), 1)
#         self.assertEqual(Node_module.objects.get().description, node_module_desc)
#         ##self.assertEqual(response.data[role].count, 1)
#
#     def test_get_node_module(self):
#         node_module_desc = 'Node_module 1'
#         # if you assign a customer or any other object
#         # customer = Customer.objects.create()
#         # customer.first_name = "Mario"
#         # customer.last_name = "Rossi"
#         # customer.save()
#
#         obj = Node_module.objects.create(
#             creator=self.u,
#             last_modifier=self.u,
#         )
#
#         # you could assign it here after creation
#         #d.customer = customer
#         obj.description = node_module_desc
#         obj.save()
#         id = obj.id
#         url = reverse('api:node_module_detail', kwargs={'id': id})
#
#         # example on how to create child entities that belongs to this entity
#         # for i in range(0, 5):
#         #     e = Employee.objects.create()
#         #     e.title = "employee {}".format(i)
#         #
#         #
#         #     e.save()
#         #
#         #     d.structured_doctors.add(e)
#         #
#         # for i in range(0, 5):
#         #     em = Employee.objects.create()
#         #     em.title = "employee {}".format(i)
#         #
#         #     em.save()
#         #     d.employees.add(em)
#
#         response = self.apiClient.get(url)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#         data = response.data
#
#         self.assertEqual(data['description'], obj.description)
#
#         # self.assertEqual(len(dep['structured_doctors']), 5)
#         # self.assertEqual(len(dep['employees']), 5)
#
#
#         # if you assign a customer
#         #self.assertEqual(m, customer.id)


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
        url = reverse('api:wilamp_alert_detail', kwargs={'id': id})
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
        url = reverse('api:wilamp_alert_detail', kwargs={'id': id})
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
        url = reverse('api:wilamp_alert_detail', kwargs={'id': id})
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

        url = reverse('api:wilamp_alert_list')

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
        url = reverse('api:wilamp_alert_detail', kwargs={'id': id})

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
        url = reverse('api:feeder_pillar_detail', kwargs={'id': id})
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
        url = reverse('api:feeder_pillar_detail', kwargs={'id': id})
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
        url = reverse('api:feeder_pillar_detail', kwargs={'id': id})
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

        url = reverse('api:feeder_pillar_list')

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
        url = reverse('api:feeder_pillar_detail', kwargs={'id': id})

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
        url = reverse('api:twilight_management_module_detail', kwargs={'id': id})
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
        url = reverse('api:twilight_management_module_detail', kwargs={'id': id})
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
        url = reverse('api:twilight_management_module_detail', kwargs={'id': id})
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

        url = reverse('api:twilight_management_module_list')

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
        url = reverse('api:twilight_management_module_detail', kwargs={'id': id})

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
        url = reverse('api:twilight_measure_detail', kwargs={'id': id})
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
        url = reverse('api:twilight_measure_detail', kwargs={'id': id})
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
        url = reverse('api:twilight_measure_detail', kwargs={'id': id})
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

        url = reverse('api:twilight_measure_list')

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
        url = reverse('api:twilight_measure_detail', kwargs={'id': id})

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
        url = reverse('api:motion_management_module_detail', kwargs={'id': id})
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
        url = reverse('api:motion_management_module_detail', kwargs={'id': id})
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
        url = reverse('api:motion_management_module_detail', kwargs={'id': id})
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

        url = reverse('api:motion_management_module_list')

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
        url = reverse('api:motion_management_module_detail', kwargs={'id': id})

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


class TestUser(TestCase):
    apiClient = APIClient()

    def test_change_password(self):

        old_password = 'password123'
        new_password = 'password321'
        username = 'apitest_password'
        self.make_user(username='apitest_password', password=old_password)
        resp = self.client.post(reverse('api-jwt-auth'), {'email': username, 'password': old_password},
                                format='json')
        token = resp.data['token']
        self.apiClient.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        endpoint = reverse('api:users_change_password')
        print(endpoint)
        resp = self.apiClient.put(endpoint, {'old_password': old_password, 'new_password': new_password})
        print(resp.data)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        # l'autenticazione fallisce con la vecchia password
        resp = self.apiClient.post(reverse('api-jwt-auth'), {'email': username, 'password': old_password},
                                    format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        # l'autenticazione NON fallisce con la NUOVA password
        resp = self.apiClient.post(reverse('api-jwt-auth'), {'email': username, 'password': new_password},
                                    format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
