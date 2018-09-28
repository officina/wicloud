# -*- coding: utf-8 -*-

import pprint
import requests
import urllib

from django.urls import reverse


class RemoteTestMixin:
    # ADDRESS
    def frontend_wicloud_address_list(self, filters=None):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:address_list')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers, params=filters)
        self.rprint(resp)
        return resp

    def frontend_wicloud_address_retrieve(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:address_retrieve',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers)
        self.rprint(resp)
        return resp

    def frontend_wicloud_address_create(self, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:address_create')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.post(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_address_partial_update(self, pk, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:address_partial_update',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_address_enable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:address_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 1}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_address_disable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:address_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 0}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp
    # CUSTOMER

    def frontend_wicloud_customer_list(self, filters=None):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:customer_list')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers, params=filters)
        self.rprint(resp)
        return resp

    def frontend_wicloud_customer_retrieve(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:customer_retrieve',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers)
        self.rprint(resp)
        return resp

    def frontend_wicloud_customer_create(self, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:customer_create')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.post(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_customer_partial_update(self, pk, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:customer_partial_update',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_customer_enable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:customer_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 1}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_customer_disable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:customer_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 0}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp
    # ENERGY_INTERVAL

    def frontend_wicloud_energy_interval_list(self, filters=None):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:energy_interval_list')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers, params=filters)
        self.rprint(resp)
        return resp

    def frontend_wicloud_energy_interval_retrieve(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:energy_interval_retrieve',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers)
        self.rprint(resp)
        return resp

    def frontend_wicloud_energy_interval_create(self, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:energy_interval_create')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.post(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_energy_interval_partial_update(self, pk, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:energy_interval_partial_update',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_energy_interval_enable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:energy_interval_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 1}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_energy_interval_disable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:energy_interval_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 0}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp
    # ENERGY_METER_MODULE

    def frontend_wicloud_energy_meter_module_list(self, filters=None):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:energy_meter_module_list')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers, params=filters)
        self.rprint(resp)
        return resp

    def frontend_wicloud_energy_meter_module_retrieve(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:energy_meter_module_retrieve',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers)
        self.rprint(resp)
        return resp

    def frontend_wicloud_energy_meter_module_create(self, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:energy_meter_module_create')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.post(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_energy_meter_module_partial_update(self, pk, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:energy_meter_module_partial_update',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_energy_meter_module_enable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:energy_meter_module_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 1}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_energy_meter_module_disable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:energy_meter_module_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 0}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp
    # ENERGY_METER_PEAK_MEASURE

    def frontend_wicloud_energy_meter_peak_measure_list(self, filters=None):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:energy_meter_peak_measure_list')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers, params=filters)
        self.rprint(resp)
        return resp

    def frontend_wicloud_energy_meter_peak_measure_retrieve(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:energy_meter_peak_measure_retrieve',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers)
        self.rprint(resp)
        return resp

    def frontend_wicloud_energy_meter_peak_measure_create(self, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:energy_meter_peak_measure_create')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.post(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_energy_meter_peak_measure_partial_update(self, pk, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:energy_meter_peak_measure_partial_update',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_energy_meter_peak_measure_enable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:energy_meter_peak_measure_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 1}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_energy_meter_peak_measure_disable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:energy_meter_peak_measure_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 0}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp
    # ERROR_LIGHT_LEVEL_AND_ADC_mismatch

    def frontend_wicloud_error_light_level_and_adc_mismatch_list(self, filters=None):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:error_light_level_and_adc_mismatch_list')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers, params=filters)
        self.rprint(resp)
        return resp

    def frontend_wicloud_error_light_level_and_adc_mismatch_retrieve(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:error_light_level_and_adc_mismatch_retrieve',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers)
        self.rprint(resp)
        return resp

    def frontend_wicloud_error_light_level_and_adc_mismatch_create(self, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:error_light_level_and_adc_mismatch_create')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.post(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_error_light_level_and_adc_mismatch_partial_update(self, pk, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:error_light_level_and_adc_mismatch_partial_update',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_error_light_level_and_adc_mismatch_enable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:error_light_level_and_adc_mismatch_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 1}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_error_light_level_and_adc_mismatch_disable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:error_light_level_and_adc_mismatch_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 0}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp
    # ERROR_LIGHT_LEVEL_AND_POWER_MISMATCH

    def frontend_wicloud_error_light_level_and_power_mismatch_list(self, filters=None):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:error_light_level_and_power_mismatch_list')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers, params=filters)
        self.rprint(resp)
        return resp

    def frontend_wicloud_error_light_level_and_power_mismatch_retrieve(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:error_light_level_and_power_mismatch_retrieve',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers)
        self.rprint(resp)
        return resp

    def frontend_wicloud_error_light_level_and_power_mismatch_create(self, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:error_light_level_and_power_mismatch_create')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.post(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_error_light_level_and_power_mismatch_partial_update(self, pk, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:error_light_level_and_power_mismatch_partial_update',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_error_light_level_and_power_mismatch_enable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:error_light_level_and_power_mismatch_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 1}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_error_light_level_and_power_mismatch_disable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:error_light_level_and_power_mismatch_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 0}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp
    # ERROR_NODE_OFFLINE

    def frontend_wicloud_error_node_offline_list(self, filters=None):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:error_node_offline_list')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers, params=filters)
        self.rprint(resp)
        return resp

    def frontend_wicloud_error_node_offline_retrieve(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:error_node_offline_retrieve',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers)
        self.rprint(resp)
        return resp

    def frontend_wicloud_error_node_offline_create(self, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:error_node_offline_create')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.post(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_error_node_offline_partial_update(self, pk, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:error_node_offline_partial_update',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_error_node_offline_enable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:error_node_offline_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 1}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_error_node_offline_disable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:error_node_offline_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 0}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp
    # GATEWAY

    def frontend_wicloud_gateway_list(self, filters=None):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:gateway_list')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers, params=filters)
        self.rprint(resp)
        return resp

    def frontend_wicloud_gateway_retrieve(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:gateway_retrieve',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers)
        self.rprint(resp)
        return resp

    def frontend_wicloud_gateway_create(self, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:gateway_create')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.post(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_gateway_partial_update(self, pk, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:gateway_partial_update',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_gateway_enable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:gateway_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 1}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_gateway_disable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:gateway_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 0}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp
    # IME_POWER_COUNTER

    def frontend_wicloud_ime_power_counter_list(self, filters=None):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:ime_power_counter_list')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers, params=filters)
        self.rprint(resp)
        return resp

    def frontend_wicloud_ime_power_counter_retrieve(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:ime_power_counter_retrieve',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers)
        self.rprint(resp)
        return resp

    def frontend_wicloud_ime_power_counter_create(self, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:ime_power_counter_create')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.post(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_ime_power_counter_partial_update(self, pk, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:ime_power_counter_partial_update',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_ime_power_counter_enable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:ime_power_counter_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 1}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_ime_power_counter_disable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:ime_power_counter_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 0}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp
    # IME_POWER_MEASURE

    def frontend_wicloud_ime_power_measure_list(self, filters=None):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:ime_power_measure_list')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers, params=filters)
        self.rprint(resp)
        return resp

    def frontend_wicloud_ime_power_measure_retrieve(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:ime_power_measure_retrieve',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers)
        self.rprint(resp)
        return resp

    def frontend_wicloud_ime_power_measure_create(self, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:ime_power_measure_create')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.post(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_ime_power_measure_partial_update(self, pk, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:ime_power_measure_partial_update',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_ime_power_measure_enable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:ime_power_measure_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 1}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_ime_power_measure_disable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:ime_power_measure_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 0}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp
    # INSTALLATION

    def frontend_wicloud_installation_list(self, filters=None):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:installation_list')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers, params=filters)
        self.rprint(resp)
        return resp

    def frontend_wicloud_installation_retrieve(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:installation_retrieve',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers)
        self.rprint(resp)
        return resp

    def frontend_wicloud_installation_create(self, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:installation_create')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.post(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_installation_partial_update(self, pk, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:installation_partial_update',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_installation_enable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:installation_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 1}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_installation_disable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:installation_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 0}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp
    # LIGHT_MANAGEMENT_MEASURE

    def frontend_wicloud_light_management_measure_list(self, filters=None):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:light_management_measure_list')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers, params=filters)
        self.rprint(resp)
        return resp

    def frontend_wicloud_light_management_measure_retrieve(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:light_management_measure_retrieve',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers)
        self.rprint(resp)
        return resp

    def frontend_wicloud_light_management_measure_create(self, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:light_management_measure_create')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.post(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_light_management_measure_partial_update(self, pk, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:light_management_measure_partial_update',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_light_management_measure_enable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:light_management_measure_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 1}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_light_management_measure_disable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:light_management_measure_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 0}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp
    # LIGHT_MANAGEMENT_MODULE

    def frontend_wicloud_light_management_module_list(self, filters=None):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:light_management_module_list')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers, params=filters)
        self.rprint(resp)
        return resp

    def frontend_wicloud_light_management_module_retrieve(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:light_management_module_retrieve',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers)
        self.rprint(resp)
        return resp

    def frontend_wicloud_light_management_module_create(self, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:light_management_module_create')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.post(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_light_management_module_partial_update(self, pk, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:light_management_module_partial_update',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_light_management_module_enable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:light_management_module_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 1}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_light_management_module_disable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:light_management_module_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 0}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp
    # LIGHT_PROFILE

    def frontend_wicloud_light_profile_list(self, filters=None):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:light_profile_list')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers, params=filters)
        self.rprint(resp)
        return resp

    def frontend_wicloud_light_profile_retrieve(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:light_profile_retrieve',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers)
        self.rprint(resp)
        return resp

    def frontend_wicloud_light_profile_create(self, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:light_profile_create')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.post(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_light_profile_partial_update(self, pk, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:light_profile_partial_update',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_light_profile_enable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:light_profile_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 1}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_light_profile_disable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:light_profile_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 0}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp
    # LIGHT_PROFILE_SLOT

    def frontend_wicloud_light_profile_slot_list(self, filters=None):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:light_profile_slot_list')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers, params=filters)
        self.rprint(resp)
        return resp

    def frontend_wicloud_light_profile_slot_retrieve(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:light_profile_slot_retrieve',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers)
        self.rprint(resp)
        return resp

    def frontend_wicloud_light_profile_slot_create(self, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:light_profile_slot_create')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.post(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_light_profile_slot_partial_update(self, pk, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:light_profile_slot_partial_update',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_light_profile_slot_enable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:light_profile_slot_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 1}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_light_profile_slot_disable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:light_profile_slot_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 0}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp
    # MOTION_EVENT

    def frontend_wicloud_motion_event_list(self, filters=None):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:motion_event_list')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers, params=filters)
        self.rprint(resp)
        return resp

    def frontend_wicloud_motion_event_retrieve(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:motion_event_retrieve',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers)
        self.rprint(resp)
        return resp

    def frontend_wicloud_motion_event_create(self, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:motion_event_create')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.post(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_motion_event_partial_update(self, pk, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:motion_event_partial_update',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_motion_event_enable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:motion_event_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 1}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_motion_event_disable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:motion_event_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 0}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp
    # NODE

    def frontend_wicloud_node_list(self, filters=None):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:node_list')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers, params=filters)
        self.rprint(resp)
        return resp

    def frontend_wicloud_node_retrieve(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:node_retrieve',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers)
        self.rprint(resp)
        return resp

    def frontend_wicloud_node_create(self, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:node_create')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.post(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_node_partial_update(self, pk, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:node_partial_update',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_node_enable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:node_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 1}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_node_disable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:node_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 0}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp
    # NODE_MODULE

    def frontend_wicloud_node_module_list(self, filters=None):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:node_module_list')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers, params=filters)
        self.rprint(resp)
        return resp

    def frontend_wicloud_node_module_retrieve(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:node_module_retrieve',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers)
        self.rprint(resp)
        return resp

    def frontend_wicloud_node_module_create(self, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:node_module_create')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.post(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_node_module_partial_update(self, pk, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:node_module_partial_update',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_node_module_enable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:node_module_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 1}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_node_module_disable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:node_module_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 0}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp
    # WILAMP_ALERT

    def frontend_wicloud_wilamp_alert_list(self, filters=None):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:wilamp_alert_list')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers, params=filters)
        self.rprint(resp)
        return resp

    def frontend_wicloud_wilamp_alert_retrieve(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:wilamp_alert_retrieve',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers)
        self.rprint(resp)
        return resp

    def frontend_wicloud_wilamp_alert_create(self, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:wilamp_alert_create')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.post(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_wilamp_alert_partial_update(self, pk, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:wilamp_alert_partial_update',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_wilamp_alert_enable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:wilamp_alert_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 1}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_wilamp_alert_disable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:wilamp_alert_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 0}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp
    # FEEDER_PILLAR

    def frontend_wicloud_feeder_pillar_list(self, filters=None):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:feeder_pillar_list')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers, params=filters)
        self.rprint(resp)
        return resp

    def frontend_wicloud_feeder_pillar_retrieve(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:feeder_pillar_retrieve',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers)
        self.rprint(resp)
        return resp

    def frontend_wicloud_feeder_pillar_create(self, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:feeder_pillar_create')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.post(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_feeder_pillar_partial_update(self, pk, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:feeder_pillar_partial_update',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_feeder_pillar_enable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:feeder_pillar_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 1}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_feeder_pillar_disable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:feeder_pillar_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 0}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp
    # TWILIGHT_MANAGEMENT_MODULE

    def frontend_wicloud_twilight_management_module_list(self, filters=None):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:twilight_management_module_list')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers, params=filters)
        self.rprint(resp)
        return resp

    def frontend_wicloud_twilight_management_module_retrieve(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:twilight_management_module_retrieve',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers)
        self.rprint(resp)
        return resp

    def frontend_wicloud_twilight_management_module_create(self, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:twilight_management_module_create')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.post(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_twilight_management_module_partial_update(self, pk, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:twilight_management_module_partial_update',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_twilight_management_module_enable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:twilight_management_module_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 1}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_twilight_management_module_disable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:twilight_management_module_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 0}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp
    # TWILIGHT_MEASURE

    def frontend_wicloud_twilight_measure_list(self, filters=None):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:twilight_measure_list')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers, params=filters)
        self.rprint(resp)
        return resp

    def frontend_wicloud_twilight_measure_retrieve(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:twilight_measure_retrieve',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers)
        self.rprint(resp)
        return resp

    def frontend_wicloud_twilight_measure_create(self, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:twilight_measure_create')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.post(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_twilight_measure_partial_update(self, pk, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:twilight_measure_partial_update',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_twilight_measure_enable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:twilight_measure_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 1}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_twilight_measure_disable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:twilight_measure_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 0}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp
    # MOTION_MANAGEMENT_MODULE

    def frontend_wicloud_motion_management_module_list(self, filters=None):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:motion_management_module_list')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers, params=filters)
        self.rprint(resp)
        return resp

    def frontend_wicloud_motion_management_module_retrieve(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:motion_management_module_retrieve',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.get(url, headers=headers)
        self.rprint(resp)
        return resp

    def frontend_wicloud_motion_management_module_create(self, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse('wicloud:api:frontend:motion_management_module_create')
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.post(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_motion_management_module_partial_update(self, pk, post_dict):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:motion_management_module_partial_update',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_motion_management_module_enable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:motion_management_module_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 1}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp

    def frontend_wicloud_motion_management_module_disable(self, pk):
        headers = {'Authorization': 'JWT {}'.format(self.jwt)}
        endpoint = reverse(
            'wicloud:api:frontend:motion_management_module_set_status',
            args=(pk,)
        )
        url = urllib.parse.urljoin(self.base_url, endpoint)
        post_dict = {'status': 0}
        resp = requests.patch(url, headers=headers, json=post_dict)
        self.rprint(resp)
        return resp
    #
