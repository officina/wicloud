# -*- coding: utf-8 -*-
import collections
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(('GET',))
def api_root(request, format=None):
    url_dict = collections.OrderedDict()
    url_dict['address_list'] = reverse(
        'api:address_list', request=request, format=format
    )
    url_dict['address_detail'] = reverse(
        'api:address_detail', request=request, format=format, kwargs={'id': 1}
    )
    url_dict['connected_device_list'] = reverse(
        'api:connected_device_list', request=request, format=format
    )
    url_dict['connected_device_detail'] = reverse(
        'api:connected_device_detail', request=request, format=format, kwargs={'id': 1}
    )
    url_dict['customer_list'] = reverse(
        'api:customer_list', request=request, format=format
    )
    url_dict['customer_detail'] = reverse(
        'api:customer_detail', request=request, format=format, kwargs={'id': 1}
    )
    url_dict['energy_interval_list'] = reverse(
        'api:energy_interval_list', request=request, format=format
    )
    url_dict['energy_interval_detail'] = reverse(
        'api:energy_interval_detail', request=request, format=format, kwargs={'id': 1}
    )
    url_dict['energy_meter_module_list'] = reverse(
        'api:energy_meter_module_list', request=request, format=format
    )
    url_dict['energy_meter_module_detail'] = reverse(
        'api:energy_meter_module_detail', request=request, format=format, kwargs={'id': 1}
    )
    url_dict['energy_meter_peak_measure_list'] = reverse(
        'api:energy_meter_peak_measure_list', request=request, format=format
    )
    url_dict['energy_meter_peak_measure_detail'] = reverse(
        'api:energy_meter_peak_measure_detail', request=request, format=format, kwargs={'id': 1}
    )
    url_dict['error_light_level_and_adc_mismatch_list'] = reverse(
        'api:error_light_level_and_adc_mismatch_list', request=request, format=format
    )
    url_dict['error_light_level_and_adc_mismatch_detail'] = reverse(
        'api:error_light_level_and_adc_mismatch_detail', request=request, format=format, kwargs={'id': 1}
    )
    url_dict['error_light_level_and_power_mismatch_list'] = reverse(
        'api:error_light_level_and_power_mismatch_list', request=request, format=format
    )
    url_dict['error_light_level_and_power_mismatch_detail'] = reverse(
        'api:error_light_level_and_power_mismatch_detail', request=request, format=format, kwargs={'id': 1}
    )
    url_dict['error_node_offline_list'] = reverse(
        'api:error_node_offline_list', request=request, format=format
    )
    url_dict['error_node_offline_detail'] = reverse(
        'api:error_node_offline_detail', request=request, format=format, kwargs={'id': 1}
    )
    url_dict['gateway_list'] = reverse(
        'api:gateway_list', request=request, format=format
    )
    url_dict['gateway_detail'] = reverse(
        'api:gateway_detail', request=request, format=format, kwargs={'id': 1}
    )
    url_dict['ime_power_counter_list'] = reverse(
        'api:ime_power_counter_list', request=request, format=format
    )
    url_dict['ime_power_counter_detail'] = reverse(
        'api:ime_power_counter_detail', request=request, format=format, kwargs={'id': 1}
    )
    url_dict['ime_power_measure_list'] = reverse(
        'api:ime_power_measure_list', request=request, format=format
    )
    url_dict['ime_power_measure_detail'] = reverse(
        'api:ime_power_measure_detail', request=request, format=format, kwargs={'id': 1}
    )
    url_dict['installation_list'] = reverse(
        'api:installation_list', request=request, format=format
    )
    url_dict['installation_detail'] = reverse(
        'api:installation_detail', request=request, format=format, kwargs={'id': 1}
    )
    url_dict['light_fixture_list'] = reverse(
        'api:light_fixture_list', request=request, format=format
    )
    url_dict['light_fixture_detail'] = reverse(
        'api:light_fixture_detail', request=request, format=format, kwargs={'id': 1}
    )
    url_dict['light_management_measure_list'] = reverse(
        'api:light_management_measure_list', request=request, format=format
    )
    url_dict['light_management_measure_detail'] = reverse(
        'api:light_management_measure_detail', request=request, format=format, kwargs={'id': 1}
    )
    url_dict['light_management_module_list'] = reverse(
        'api:light_management_module_list', request=request, format=format
    )
    url_dict['light_management_module_detail'] = reverse(
        'api:light_management_module_detail', request=request, format=format, kwargs={'id': 1}
    )
    url_dict['light_profile_list'] = reverse(
        'api:light_profile_list', request=request, format=format
    )
    url_dict['light_profile_detail'] = reverse(
        'api:light_profile_detail', request=request, format=format, kwargs={'id': 1}
    )
    url_dict['light_profile_slot_list'] = reverse(
        'api:light_profile_slot_list', request=request, format=format
    )
    url_dict['light_profile_slot_detail'] = reverse(
        'api:light_profile_slot_detail', request=request, format=format, kwargs={'id': 1}
    )
    url_dict['motion_event_list'] = reverse(
        'api:motion_event_list', request=request, format=format
    )
    url_dict['motion_event_detail'] = reverse(
        'api:motion_event_detail', request=request, format=format, kwargs={'id': 1}
    )
    url_dict['node_list'] = reverse(
        'api:node_list', request=request, format=format
    )
    url_dict['node_detail'] = reverse(
        'api:node_detail', request=request, format=format, kwargs={'id': 1}
    )
    url_dict['node_module_list'] = reverse(
        'api:node_module_list', request=request, format=format
    )
    url_dict['node_module_detail'] = reverse(
        'api:node_module_detail', request=request, format=format, kwargs={'id': 1}
    )
    url_dict['wilamp_alert_list'] = reverse(
        'api:wilamp_alert_list', request=request, format=format
    )
    url_dict['wilamp_alert_detail'] = reverse(
        'api:wilamp_alert_detail', request=request, format=format, kwargs={'id': 1}
    )
    url_dict['feeder_pillar_list'] = reverse(
        'api:feeder_pillar_list', request=request, format=format
    )
    url_dict['feeder_pillar_detail'] = reverse(
        'api:feeder_pillar_detail', request=request, format=format, kwargs={'id': 1}
    )
    url_dict['twilight_management_module_list'] = reverse(
        'api:twilight_management_module_list', request=request, format=format
    )
    url_dict['twilight_management_module_detail'] = reverse(
        'api:twilight_management_module_detail', request=request, format=format, kwargs={'id': 1}
    )
    url_dict['twilight_measure_list'] = reverse(
        'api:twilight_measure_list', request=request, format=format
    )
    url_dict['twilight_measure_detail'] = reverse(
        'api:twilight_measure_detail', request=request, format=format, kwargs={'id': 1}
    )
    url_dict['motion_management_module_list'] = reverse(
        'api:motion_management_module_list', request=request, format=format
    )
    url_dict['user_change_password'] = reverse(
        'api:users_change_password', request=request, format=format,
    )
    return Response(url_dict)