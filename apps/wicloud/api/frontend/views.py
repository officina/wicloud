# -*- coding: utf-8 -*-
import collections

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import parsers
from rest_framework import renderers

from web.api import views
from . import serializers
from ... import models
from django.contrib.auth.models import User
from rest_framework import status


@api_view(('GET',))
def api_root(request, format=None):
    url_dict = collections.OrderedDict()
    url_dict['users_list'] = reverse(
        'wicloud:api:frontend:users_list', request=request, format=format
    )
    url_dict['users_register'] = reverse(
        'wicloud:api:frontend:users_register', request=request, format=format
    )
    url_dict['users_change_password'] = reverse(
        'wicloud:api:frontend:users_change_password', request=request, format=format
    )
    url_dict['users_register'] = reverse(
        'wicloud:api:frontend:users_register', request=request, format=format
    )
    url_dict['address_list'] = reverse(
        'wicloud:api:frontend:address_list', request=request, format=format
    )
    url_dict['address_create'] = reverse(
        'wicloud:api:frontend:address_create', request=request, format=format
    )
    url_dict['customer_list'] = reverse(
        'wicloud:api:frontend:customer_list', request=request, format=format
    )
    url_dict['customer_create'] = reverse(
        'wicloud:api:frontend:customer_create', request=request, format=format
    )
    url_dict['energy_interval_list'] = reverse(
        'wicloud:api:frontend:energy_interval_list', request=request, format=format
    )
    url_dict['energy_interval_create'] = reverse(
        'wicloud:api:frontend:energy_interval_create', request=request, format=format
    )
    url_dict['energy_meter_module_list'] = reverse(
        'wicloud:api:frontend:energy_meter_module_list', request=request, format=format
    )
    url_dict['energy_meter_module_create'] = reverse(
        'wicloud:api:frontend:energy_meter_module_create', request=request, format=format
    )
    url_dict['energy_meter_peak_measure_list'] = reverse(
        'wicloud:api:frontend:energy_meter_peak_measure_list', request=request, format=format
    )
    url_dict['energy_meter_peak_measure_create'] = reverse(
        'wicloud:api:frontend:energy_meter_peak_measure_create', request=request, format=format
    )
    url_dict['error_light_level_and_adc_mismatch_list'] = reverse(
        'wicloud:api:frontend:error_light_level_and_adc_mismatch_list', request=request, format=format
    )
    url_dict['error_light_level_and_adc_mismatch_create'] = reverse(
        'wicloud:api:frontend:error_light_level_and_adc_mismatch_create', request=request, format=format
    )
    url_dict['error_light_level_and_power_mismatch_list'] = reverse(
        'wicloud:api:frontend:error_light_level_and_power_mismatch_list', request=request, format=format
    )
    url_dict['error_light_level_and_power_mismatch_create'] = reverse(
        'wicloud:api:frontend:error_light_level_and_power_mismatch_create', request=request, format=format
    )
    url_dict['error_node_offline_list'] = reverse(
        'wicloud:api:frontend:error_node_offline_list', request=request, format=format
    )
    url_dict['error_node_offline_create'] = reverse(
        'wicloud:api:frontend:error_node_offline_create', request=request, format=format
    )
    url_dict['gateway_list'] = reverse(
        'wicloud:api:frontend:gateway_list', request=request, format=format
    )
    url_dict['gateway_create'] = reverse(
        'wicloud:api:frontend:gateway_create', request=request, format=format
    )
    url_dict['ime_power_counter_list'] = reverse(
        'wicloud:api:frontend:ime_power_counter_list', request=request, format=format
    )
    url_dict['ime_power_counter_create'] = reverse(
        'wicloud:api:frontend:ime_power_counter_create', request=request, format=format
    )
    url_dict['ime_power_measure_list'] = reverse(
        'wicloud:api:frontend:ime_power_measure_list', request=request, format=format
    )
    url_dict['ime_power_measure_create'] = reverse(
        'wicloud:api:frontend:ime_power_measure_create', request=request, format=format
    )
    url_dict['installation_list'] = reverse(
        'wicloud:api:frontend:installation_list', request=request, format=format
    )
    url_dict['installation_create'] = reverse(
        'wicloud:api:frontend:installation_create', request=request, format=format
    )
    url_dict['light_management_measure_list'] = reverse(
        'wicloud:api:frontend:light_management_measure_list', request=request, format=format
    )
    url_dict['light_management_measure_create'] = reverse(
        'wicloud:api:frontend:light_management_measure_create', request=request, format=format
    )
    url_dict['light_management_module_list'] = reverse(
        'wicloud:api:frontend:light_management_module_list', request=request, format=format
    )
    url_dict['light_management_module_create'] = reverse(
        'wicloud:api:frontend:light_management_module_create', request=request, format=format
    )
    url_dict['light_profile_list'] = reverse(
        'wicloud:api:frontend:light_profile_list', request=request, format=format
    )
    url_dict['light_profile_create'] = reverse(
        'wicloud:api:frontend:light_profile_create', request=request, format=format
    )
    url_dict['light_profile_slot_list'] = reverse(
        'wicloud:api:frontend:light_profile_slot_list', request=request, format=format
    )
    url_dict['light_profile_slot_create'] = reverse(
        'wicloud:api:frontend:light_profile_slot_create', request=request, format=format
    )
    url_dict['motion_event_list'] = reverse(
        'wicloud:api:frontend:motion_event_list', request=request, format=format
    )
    url_dict['motion_event_create'] = reverse(
        'wicloud:api:frontend:motion_event_create', request=request, format=format
    )
    url_dict['node_list'] = reverse(
        'wicloud:api:frontend:node_list', request=request, format=format
    )
    url_dict['node_create'] = reverse(
        'wicloud:api:frontend:node_create', request=request, format=format
    )
    url_dict['node_module_list'] = reverse(
        'wicloud:api:frontend:node_module_list', request=request, format=format
    )
    url_dict['node_module_create'] = reverse(
        'wicloud:api:frontend:node_module_create', request=request, format=format
    )
    url_dict['wilamp_alert_list'] = reverse(
        'wicloud:api:frontend:wilamp_alert_list', request=request, format=format
    )
    url_dict['wilamp_alert_create'] = reverse(
        'wicloud:api:frontend:wilamp_alert_create', request=request, format=format
    )
    url_dict['feeder_pillar_list'] = reverse(
        'wicloud:api:frontend:feeder_pillar_list', request=request, format=format
    )
    url_dict['feeder_pillar_create'] = reverse(
        'wicloud:api:frontend:feeder_pillar_create', request=request, format=format
    )
    url_dict['twilight_management_module_list'] = reverse(
        'wicloud:api:frontend:twilight_management_module_list', request=request, format=format
    )
    url_dict['twilight_management_module_create'] = reverse(
        'wicloud:api:frontend:twilight_management_module_create', request=request, format=format
    )
    url_dict['twilight_measure_list'] = reverse(
        'wicloud:api:frontend:twilight_measure_list', request=request, format=format
    )
    url_dict['twilight_measure_create'] = reverse(
        'wicloud:api:frontend:twilight_measure_create', request=request, format=format
    )
    url_dict['motion_management_module_list'] = reverse(
        'wicloud:api:frontend:motion_management_module_list', request=request, format=format
    )
    url_dict['motion_management_module_create'] = reverse(
        'wicloud:api:frontend:motion_management_module_create', request=request, format=format
    )
    return Response(url_dict)


class AddressListView(views.ThuxListViewMixin, generics.ListAPIView):
    """
    Get all addresses
    """
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressListSerializer


class AddressRetrieveView(views.ThuxRetrieveViewMixin, generics.RetrieveAPIView):
    """
    Get a single address
    """
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressRetrieveSerializer


class AddressCreateView(views.ThuxCreateViewMixin, generics.CreateAPIView):
    """
    Create a single address
    """
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressCreateSerializer


class AddressPartialUpdateView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Update a single address
    """
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressPartialUpdateSerializer


class AddressDestroyView(views.ThuxDestroyViewMixin, generics.DestroyAPIView):
    """
    Delete a single address
    """
    queryset = models.Address.objects.all()


class AddressSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single address
    """
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSetStatusSerializer


class AddressEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single address
    """
    queryset = models.Address.objects.filter(status=0)
    serializer_class = serializers.AddressStatusSerializer
    new_status = 1


class AddressDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single address
    """
    queryset = models.Address.objects.filter(status=1)
    serializer_class = serializers.AddressStatusSerializer
    new_status = 0


class CustomerListView(views.ThuxListViewMixin, generics.ListAPIView):
    """
    Get all  customers
    """
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerListSerializer


class CustomerRetrieveView(views.ThuxRetrieveViewMixin, generics.RetrieveAPIView):
    """
    Get a single customer
    """
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerRetrieveSerializer


class CustomerCreateView(views.ThuxCreateViewMixin, generics.CreateAPIView):
    """
    Create a single customer
    """
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerCreateSerializer


class CustomerPartialUpdateView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Update a single customer
    """
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerPartialUpdateSerializer


class CustomerDestroyView(views.ThuxDestroyViewMixin, generics.DestroyAPIView):
    """
    Delete a single customer
    """
    queryset = models.Customer.objects.all()


class CustomerSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single customer
    """
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSetStatusSerializer


class CustomerEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single customer
    """
    queryset = models.Customer.objects.filter(status=0)
    serializer_class = serializers.CustomerStatusSerializer
    new_status = 1


class CustomerDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single customer
    """
    queryset = models.Customer.objects.filter(status=1)
    serializer_class = serializers.CustomerStatusSerializer
    new_status = 0


class Energy_intervalListView(views.ThuxListViewMixin, generics.ListAPIView):
    """
    Get all  energy_intervals
    """
    queryset = models.Energy_interval.objects.all()
    serializer_class = serializers.Energy_intervalListSerializer


class Energy_intervalRetrieveView(views.ThuxRetrieveViewMixin, generics.RetrieveAPIView):
    """
    Get a single energy_interval
    """
    queryset = models.Energy_interval.objects.all()
    serializer_class = serializers.Energy_intervalRetrieveSerializer


class Energy_intervalCreateView(views.ThuxCreateViewMixin, generics.CreateAPIView):
    """
    Create a single energy_interval
    """
    queryset = models.Energy_interval.objects.all()
    serializer_class = serializers.Energy_intervalCreateSerializer


class Energy_intervalPartialUpdateView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Update a single energy_interval
    """
    queryset = models.Energy_interval.objects.all()
    serializer_class = serializers.Energy_intervalPartialUpdateSerializer


class Energy_intervalDestroyView(views.ThuxDestroyViewMixin, generics.DestroyAPIView):
    """
    Delete a single energy_interval
    """
    queryset = models.Energy_interval.objects.all()


class Energy_intervalSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single energy_interval
    """
    queryset = models.Energy_interval.objects.all()
    serializer_class = serializers.Energy_intervalSetStatusSerializer


class Energy_intervalEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single energy_interval
    """
    queryset = models.Energy_interval.objects.filter(status=0)
    serializer_class = serializers.Energy_intervalStatusSerializer
    new_status = 1


class Energy_intervalDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single energy_interval
    """
    queryset = models.Energy_interval.objects.filter(status=1)
    serializer_class = serializers.Energy_intervalStatusSerializer
    new_status = 0


class Energy_meter_moduleListView(views.ThuxListViewMixin, generics.ListAPIView):
    """
    Get all  energy_meter_modules
    """
    queryset = models.Energy_meter_module.objects.all()
    serializer_class = serializers.Energy_meter_moduleListSerializer


class Energy_meter_moduleRetrieveView(views.ThuxRetrieveViewMixin, generics.RetrieveAPIView):
    """
    Get a single energy_meter_module
    """
    queryset = models.Energy_meter_module.objects.all()
    serializer_class = serializers.Energy_meter_moduleRetrieveSerializer


class Energy_meter_moduleCreateView(views.ThuxCreateViewMixin, generics.CreateAPIView):
    """
    Create a single energy_meter_module
    """
    queryset = models.Energy_meter_module.objects.all()
    serializer_class = serializers.Energy_meter_moduleCreateSerializer


class Energy_meter_modulePartialUpdateView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Update a single energy_meter_module
    """
    queryset = models.Energy_meter_module.objects.all()
    serializer_class = serializers.Energy_meter_modulePartialUpdateSerializer


class Energy_meter_moduleDestroyView(views.ThuxDestroyViewMixin, generics.DestroyAPIView):
    """
    Delete a single energy_meter_module
    """
    queryset = models.Energy_meter_module.objects.all()


class Energy_meter_moduleSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single energy_meter_module
    """
    queryset = models.Energy_meter_module.objects.all()
    serializer_class = serializers.Energy_meter_moduleSetStatusSerializer


class Energy_meter_moduleEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single energy_meter_module
    """
    queryset = models.Energy_meter_module.objects.filter(status=0)
    serializer_class = serializers.Energy_meter_moduleStatusSerializer
    new_status = 1


class Energy_meter_moduleDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single energy_meter_module
    """
    queryset = models.Energy_meter_module.objects.filter(status=1)
    serializer_class = serializers.Energy_meter_moduleStatusSerializer
    new_status = 0


class Energy_meter_peak_measureListView(views.ThuxListViewMixin, generics.ListAPIView):
    """
    Get all  energy_meter_peak_measures
    """
    queryset = models.Energy_meter_peak_measure.objects.all()
    serializer_class = serializers.Energy_meter_peak_measureListSerializer


class Energy_meter_peak_measureRetrieveView(views.ThuxRetrieveViewMixin, generics.RetrieveAPIView):
    """
    Get a single energy_meter_peak_measure
    """
    queryset = models.Energy_meter_peak_measure.objects.all()
    serializer_class = serializers.Energy_meter_peak_measureRetrieveSerializer


class Energy_meter_peak_measureCreateView(views.ThuxCreateViewMixin, generics.CreateAPIView):
    """
    Create a single energy_meter_peak_measure
    """
    queryset = models.Energy_meter_peak_measure.objects.all()
    serializer_class = serializers.Energy_meter_peak_measureCreateSerializer


class Energy_meter_peak_measurePartialUpdateView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Update a single energy_meter_peak_measure
    """
    queryset = models.Energy_meter_peak_measure.objects.all()
    serializer_class = serializers.Energy_meter_peak_measurePartialUpdateSerializer


class Energy_meter_peak_measureDestroyView(views.ThuxDestroyViewMixin, generics.DestroyAPIView):
    """
    Delete a single energy_meter_peak_measure
    """
    queryset = models.Energy_meter_peak_measure.objects.all()


class Energy_meter_peak_measureSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single energy_meter_peak_measure
    """
    queryset = models.Energy_meter_peak_measure.objects.all()
    serializer_class = serializers.Energy_meter_peak_measureSetStatusSerializer


class Energy_meter_peak_measureEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single energy_meter_peak_measure
    """
    queryset = models.Energy_meter_peak_measure.objects.filter(status=0)
    serializer_class = serializers.Energy_meter_peak_measureStatusSerializer
    new_status = 1


class Energy_meter_peak_measureDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single energy_meter_peak_measure
    """
    queryset = models.Energy_meter_peak_measure.objects.filter(status=1)
    serializer_class = serializers.Energy_meter_peak_measureStatusSerializer
    new_status = 0


class Error_light_level_and_adc_mismatchListView(views.ThuxListViewMixin, generics.ListAPIView):
    """
    Get all  error_light_level_and_adc_mismatchs
    """
    queryset = models.Error_light_level_and_adc_mismatch.objects.all()
    serializer_class = serializers.Error_light_level_and_adc_mismatchListSerializer


class Error_light_level_and_adc_mismatchRetrieveView(views.ThuxRetrieveViewMixin, generics.RetrieveAPIView):
    """
    Get a single error_light_level_and_adc_mismatch
    """
    queryset = models.Error_light_level_and_adc_mismatch.objects.all()
    serializer_class = serializers.Error_light_level_and_adc_mismatchRetrieveSerializer


class Error_light_level_and_adc_mismatchCreateView(views.ThuxCreateViewMixin, generics.CreateAPIView):
    """
    Create a single error_light_level_and_adc_mismatch
    """
    queryset = models.Error_light_level_and_adc_mismatch.objects.all()
    serializer_class = serializers.Error_light_level_and_adc_mismatchCreateSerializer


class Error_light_level_and_adc_mismatchPartialUpdateView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Update a single error_light_level_and_adc_mismatch
    """
    queryset = models.Error_light_level_and_adc_mismatch.objects.all()
    serializer_class = serializers.Error_light_level_and_adc_mismatchPartialUpdateSerializer


class Error_light_level_and_adc_mismatchDestroyView(views.ThuxDestroyViewMixin, generics.DestroyAPIView):
    """
    Delete a single error_light_level_and_adc_mismatch
    """
    queryset = models.Error_light_level_and_adc_mismatch.objects.all()


class Error_light_level_and_adc_mismatchSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single error_light_level_and_adc_mismatch
    """
    queryset = models.Error_light_level_and_adc_mismatch.objects.all()
    serializer_class = serializers.Error_light_level_and_adc_mismatchSetStatusSerializer


class Error_light_level_and_adc_mismatchEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single error_light_level_and_adc_mismatch
    """
    queryset = models.Error_light_level_and_adc_mismatch.objects.filter(status=0)
    serializer_class = serializers.Error_light_level_and_adc_mismatchStatusSerializer
    new_status = 1


class Error_light_level_and_adc_mismatchDisableView(
        views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single error_light_level_and_adc_mismatch
    """
    queryset = models.Error_light_level_and_adc_mismatch.objects.filter(status=1)
    serializer_class = serializers.Error_light_level_and_adc_mismatchStatusSerializer
    new_status = 0


class Error_light_level_and_power_mismatchListView(views.ThuxListViewMixin, generics.ListAPIView):
    """
    Get all  error_light_level_and_power_mismatchs
    """
    queryset = models.Error_light_level_and_power_mismatch.objects.all()
    serializer_class = serializers.Error_light_level_and_power_mismatchListSerializer


class Error_light_level_and_power_mismatchRetrieveView(views.ThuxRetrieveViewMixin, generics.RetrieveAPIView):
    """
    Get a single error_light_level_and_power_mismatch
    """
    queryset = models.Error_light_level_and_power_mismatch.objects.all()
    serializer_class = serializers.Error_light_level_and_power_mismatchRetrieveSerializer


class Error_light_level_and_power_mismatchCreateView(views.ThuxCreateViewMixin, generics.CreateAPIView):
    """
    Create a single error_light_level_and_power_mismatch
    """
    queryset = models.Error_light_level_and_power_mismatch.objects.all()
    serializer_class = serializers.Error_light_level_and_power_mismatchCreateSerializer


class Error_light_level_and_power_mismatchPartialUpdateView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Update a single error_light_level_and_power_mismatch
    """
    queryset = models.Error_light_level_and_power_mismatch.objects.all()
    serializer_class = serializers.Error_light_level_and_power_mismatchPartialUpdateSerializer


class Error_light_level_and_power_mismatchDestroyView(views.ThuxDestroyViewMixin, generics.DestroyAPIView):
    """
    Delete a single error_light_level_and_power_mismatch
    """
    queryset = models.Error_light_level_and_power_mismatch.objects.all()


class Error_light_level_and_power_mismatchSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single error_light_level_and_power_mismatch
    """
    queryset = models.Error_light_level_and_power_mismatch.objects.all()
    serializer_class = serializers.Error_light_level_and_power_mismatchSetStatusSerializer


class Error_light_level_and_power_mismatchEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single error_light_level_and_power_mismatch
    """
    queryset = models.Error_light_level_and_power_mismatch.objects.filter(status=0)
    serializer_class = serializers.Error_light_level_and_power_mismatchStatusSerializer
    new_status = 1


class Error_light_level_and_power_mismatchDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single error_light_level_and_power_mismatch
    """
    queryset = models.Error_light_level_and_power_mismatch.objects.filter(status=1)
    serializer_class = serializers.Error_light_level_and_power_mismatchStatusSerializer
    new_status = 0


class Error_node_offlineListView(views.ThuxListViewMixin, generics.ListAPIView):
    """
    Get all  error_node_offlines
    """
    queryset = models.Error_node_offline.objects.all()
    serializer_class = serializers.Error_node_offlineListSerializer


class Error_node_offlineRetrieveView(views.ThuxRetrieveViewMixin, generics.RetrieveAPIView):
    """
    Get a single error_node_offline
    """
    queryset = models.Error_node_offline.objects.all()
    serializer_class = serializers.Error_node_offlineRetrieveSerializer


class Error_node_offlineCreateView(views.ThuxCreateViewMixin, generics.CreateAPIView):
    """
    Create a single error_node_offline
    """
    queryset = models.Error_node_offline.objects.all()
    serializer_class = serializers.Error_node_offlineCreateSerializer


class Error_node_offlinePartialUpdateView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Update a single error_node_offline
    """
    queryset = models.Error_node_offline.objects.all()
    serializer_class = serializers.Error_node_offlinePartialUpdateSerializer


class Error_node_offlineDestroyView(views.ThuxDestroyViewMixin, generics.DestroyAPIView):
    """
    Delete a single error_node_offline
    """
    queryset = models.Error_node_offline.objects.all()


class Error_node_offlineSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single error_node_offline
    """
    queryset = models.Error_node_offline.objects.all()
    serializer_class = serializers.Error_node_offlineSetStatusSerializer


class Error_node_offlineEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single error_node_offline
    """
    queryset = models.Error_node_offline.objects.filter(status=0)
    serializer_class = serializers.Error_node_offlineStatusSerializer
    new_status = 1


class Error_node_offlineDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single error_node_offline
    """
    queryset = models.Error_node_offline.objects.filter(status=1)
    serializer_class = serializers.Error_node_offlineStatusSerializer
    new_status = 0


class GatewayListView(views.ThuxListViewMixin, generics.ListAPIView):
    """
    Get all  gateways
    """
    queryset = models.Gateway.objects.all()
    serializer_class = serializers.GatewayListSerializer


class GatewayRetrieveView(views.ThuxRetrieveViewMixin, generics.RetrieveAPIView):
    """
    Get a single gateway
    """
    queryset = models.Gateway.objects.all()
    serializer_class = serializers.GatewayRetrieveSerializer


class GatewayCreateView(views.ThuxCreateViewMixin, generics.CreateAPIView):
    """
    Create a single gateway
    """
    queryset = models.Gateway.objects.all()
    serializer_class = serializers.GatewayCreateSerializer


class GatewayPartialUpdateView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Update a single gateway
    """
    queryset = models.Gateway.objects.all()
    serializer_class = serializers.GatewayPartialUpdateSerializer


class GatewayDestroyView(views.ThuxDestroyViewMixin, generics.DestroyAPIView):
    """
    Delete a single gateway
    """
    queryset = models.Gateway.objects.all()


class GatewaySetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single gateway
    """
    queryset = models.Gateway.objects.all()
    serializer_class = serializers.GatewaySetStatusSerializer


class GatewayEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single gateway
    """
    queryset = models.Gateway.objects.filter(status=0)
    serializer_class = serializers.GatewayStatusSerializer
    new_status = 1


class GatewayDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single gateway
    """
    queryset = models.Gateway.objects.filter(status=1)
    serializer_class = serializers.GatewayStatusSerializer
    new_status = 0


class Ime_power_counterListView(views.ThuxListViewMixin, generics.ListAPIView):
    """
    Get all  ime_power_counters
    """
    queryset = models.Ime_power_counter.objects.all()
    serializer_class = serializers.Ime_power_counterListSerializer


class Ime_power_counterRetrieveView(views.ThuxRetrieveViewMixin, generics.RetrieveAPIView):
    """
    Get a single ime_power_counter
    """
    queryset = models.Ime_power_counter.objects.all()
    serializer_class = serializers.Ime_power_counterRetrieveSerializer


class Ime_power_counterCreateView(views.ThuxCreateViewMixin, generics.CreateAPIView):
    """
    Create a single ime_power_counter
    """
    queryset = models.Ime_power_counter.objects.all()
    serializer_class = serializers.Ime_power_counterCreateSerializer


class Ime_power_counterPartialUpdateView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Update a single ime_power_counter
    """
    queryset = models.Ime_power_counter.objects.all()
    serializer_class = serializers.Ime_power_counterPartialUpdateSerializer


class Ime_power_counterDestroyView(views.ThuxDestroyViewMixin, generics.DestroyAPIView):
    """
    Delete a single ime_power_counter
    """
    queryset = models.Ime_power_counter.objects.all()


class Ime_power_counterSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single ime_power_counter
    """
    queryset = models.Ime_power_counter.objects.all()
    serializer_class = serializers.Ime_power_counterSetStatusSerializer


class Ime_power_counterEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single ime_power_counter
    """
    queryset = models.Ime_power_counter.objects.filter(status=0)
    serializer_class = serializers.Ime_power_counterStatusSerializer
    new_status = 1


class Ime_power_counterDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single ime_power_counter
    """
    queryset = models.Ime_power_counter.objects.filter(status=1)
    serializer_class = serializers.Ime_power_counterStatusSerializer
    new_status = 0


class Ime_power_measureListView(views.ThuxListViewMixin, generics.ListAPIView):
    """
    Get all  ime_power_measures
    """
    queryset = models.Ime_power_measure.objects.all()
    serializer_class = serializers.Ime_power_measureListSerializer


class Ime_power_measureRetrieveView(views.ThuxRetrieveViewMixin, generics.RetrieveAPIView):
    """
    Get a single ime_power_measure
    """
    queryset = models.Ime_power_measure.objects.all()
    serializer_class = serializers.Ime_power_measureRetrieveSerializer


class Ime_power_measureCreateView(views.ThuxCreateViewMixin, generics.CreateAPIView):
    """
    Create a single ime_power_measure
    """
    queryset = models.Ime_power_measure.objects.all()
    serializer_class = serializers.Ime_power_measureCreateSerializer


class Ime_power_measurePartialUpdateView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Update a single ime_power_measure
    """
    queryset = models.Ime_power_measure.objects.all()
    serializer_class = serializers.Ime_power_measurePartialUpdateSerializer


class Ime_power_measureDestroyView(views.ThuxDestroyViewMixin, generics.DestroyAPIView):
    """
    Delete a single ime_power_measure
    """
    queryset = models.Ime_power_measure.objects.all()


class Ime_power_measureSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single ime_power_measure
    """
    queryset = models.Ime_power_measure.objects.all()
    serializer_class = serializers.Ime_power_measureSetStatusSerializer


class Ime_power_measureEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single ime_power_measure
    """
    queryset = models.Ime_power_measure.objects.filter(status=0)
    serializer_class = serializers.Ime_power_measureStatusSerializer
    new_status = 1


class Ime_power_measureDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single ime_power_measure
    """
    queryset = models.Ime_power_measure.objects.filter(status=1)
    serializer_class = serializers.Ime_power_measureStatusSerializer
    new_status = 0


class InstallationListView(views.ThuxListViewMixin, generics.ListAPIView):
    """
    Get all  installations
    """
    queryset = models.Installation.objects.all()
    serializer_class = serializers.InstallationListSerializer


class InstallationRetrieveView(views.ThuxRetrieveViewMixin, generics.RetrieveAPIView):
    """
    Get a single installation
    """
    queryset = models.Installation.objects.all()
    serializer_class = serializers.InstallationRetrieveSerializer


class InstallationCreateView(views.ThuxCreateViewMixin, generics.CreateAPIView):
    """
    Create a single installation
    """
    queryset = models.Installation.objects.all()
    serializer_class = serializers.InstallationCreateSerializer


class InstallationPartialUpdateView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Update a single installation
    """
    queryset = models.Installation.objects.all()
    serializer_class = serializers.InstallationPartialUpdateSerializer


class InstallationDestroyView(views.ThuxDestroyViewMixin, generics.DestroyAPIView):
    """
    Delete a single installation
    """
    queryset = models.Installation.objects.all()


class InstallationSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single installation
    """
    queryset = models.Installation.objects.all()
    serializer_class = serializers.InstallationSetStatusSerializer


class InstallationEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single installation
    """
    queryset = models.Installation.objects.filter(status=0)
    serializer_class = serializers.InstallationStatusSerializer
    new_status = 1


class InstallationDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single installation
    """
    queryset = models.Installation.objects.filter(status=1)
    serializer_class = serializers.InstallationStatusSerializer
    new_status = 0


class Light_management_measureListView(views.ThuxListViewMixin, generics.ListAPIView):
    """
    Get all  light_management_measures
    """
    queryset = models.Light_management_measure.objects.all()
    serializer_class = serializers.Light_management_measureListSerializer


class Light_management_measureRetrieveView(views.ThuxRetrieveViewMixin, generics.RetrieveAPIView):
    """
    Get a single light_management_measure
    """
    queryset = models.Light_management_measure.objects.all()
    serializer_class = serializers.Light_management_measureRetrieveSerializer


class Light_management_measureCreateView(views.ThuxCreateViewMixin, generics.CreateAPIView):
    """
    Create a single light_management_measure
    """
    queryset = models.Light_management_measure.objects.all()
    serializer_class = serializers.Light_management_measureCreateSerializer


class Light_management_measurePartialUpdateView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Update a single light_management_measure
    """
    queryset = models.Light_management_measure.objects.all()
    serializer_class = serializers.Light_management_measurePartialUpdateSerializer


class Light_management_measureDestroyView(views.ThuxDestroyViewMixin, generics.DestroyAPIView):
    """
    Delete a single light_management_measure
    """
    queryset = models.Light_management_measure.objects.all()


class Light_management_measureSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single light_management_measure
    """
    queryset = models.Light_management_measure.objects.all()
    serializer_class = serializers.Light_management_measureSetStatusSerializer


class Light_management_measureEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single light_management_measure
    """
    queryset = models.Light_management_measure.objects.filter(status=0)
    serializer_class = serializers.Light_management_measureStatusSerializer
    new_status = 1


class Light_management_measureDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single light_management_measure
    """
    queryset = models.Light_management_measure.objects.filter(status=1)
    serializer_class = serializers.Light_management_measureStatusSerializer
    new_status = 0


class Light_management_moduleListView(views.ThuxListViewMixin, generics.ListAPIView):
    """
    Get all  light_management_module
    """
    queryset = models.Light_management_module.objects.all()
    serializer_class = serializers.Light_management_moduleListSerializer


class Light_management_moduleRetrieveView(views.ThuxRetrieveViewMixin, generics.RetrieveAPIView):
    """
    Get a single light_management_module
    """
    queryset = models.Light_management_module.objects.all()
    serializer_class = serializers.Light_management_moduleRetrieveSerializer


class Light_management_moduleCreateView(views.ThuxCreateViewMixin, generics.CreateAPIView):
    """
    Create a single light_management_module
    """
    queryset = models.Light_management_module.objects.all()
    serializer_class = serializers.Light_management_moduleCreateSerializer


class Light_management_modulePartialUpdateView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Update a single light_management_module
    """
    queryset = models.Light_management_module.objects.all()
    serializer_class = serializers.Light_management_modulePartialUpdateSerializer


class Light_management_moduleDestroyView(views.ThuxDestroyViewMixin, generics.DestroyAPIView):
    """
    Delete a single light_management_module
    """
    queryset = models.Light_management_module.objects.all()


class Light_management_moduleSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single light_management_module
    """
    queryset = models.Light_management_module.objects.all()
    serializer_class = serializers.Light_management_moduleSetStatusSerializer


class Light_management_moduleEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single light_management_module
    """
    queryset = models.Light_management_module.objects.filter(status=0)
    serializer_class = serializers.Light_management_moduleStatusSerializer
    new_status = 1


class Light_management_moduleDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single light_management_module
    """
    queryset = models.Light_management_module.objects.filter(status=1)
    serializer_class = serializers.Light_management_moduleStatusSerializer
    new_status = 0


class Light_profileListView(views.ThuxListViewMixin, generics.ListAPIView):
    """
    Get all  light_profiles
    """
    queryset = models.Light_profile.objects.all()
    serializer_class = serializers.Light_profileListSerializer


class Light_profileRetrieveView(views.ThuxRetrieveViewMixin, generics.RetrieveAPIView):
    """
    Get a single light_profile
    """
    queryset = models.Light_profile.objects.all()
    serializer_class = serializers.Light_profileRetrieveSerializer


class Light_profileCreateView(views.ThuxCreateViewMixin, generics.CreateAPIView):
    """
    Create a single light_profile
    """
    queryset = models.Light_profile.objects.all()
    serializer_class = serializers.Light_profileCreateSerializer


class Light_profilePartialUpdateView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Update a single light_profile
    """
    queryset = models.Light_profile.objects.all()
    serializer_class = serializers.Light_profilePartialUpdateSerializer


class Light_profileDestroyView(views.ThuxDestroyViewMixin, generics.DestroyAPIView):
    """
    Delete a single light_profile
    """
    queryset = models.Light_profile.objects.all()


class Light_profileSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single light_profile
    """
    queryset = models.Light_profile.objects.all()
    serializer_class = serializers.Light_profileSetStatusSerializer


class Light_profileEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single light_profile
    """
    queryset = models.Light_profile.objects.filter(status=0)
    serializer_class = serializers.Light_profileStatusSerializer
    new_status = 1


class Light_profileDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single light_profile
    """
    queryset = models.Light_profile.objects.filter(status=1)
    serializer_class = serializers.Light_profileStatusSerializer
    new_status = 0


class Light_profile_slotListView(views.ThuxListViewMixin, generics.ListAPIView):
    """
    Get all  light_profile_slots
    """
    queryset = models.Light_profile_slot.objects.all()
    serializer_class = serializers.Light_profile_slotListSerializer


class Light_profile_slotRetrieveView(views.ThuxRetrieveViewMixin, generics.RetrieveAPIView):
    """
    Get a single light_profile_slot
    """
    queryset = models.Light_profile_slot.objects.all()
    serializer_class = serializers.Light_profile_slotRetrieveSerializer


class Light_profile_slotCreateView(views.ThuxCreateViewMixin, generics.CreateAPIView):
    """
    Create a single light_profile_slot
    """
    queryset = models.Light_profile_slot.objects.all()
    serializer_class = serializers.Light_profile_slotCreateSerializer


class Light_profile_slotPartialUpdateView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Update a single light_profile_slot
    """
    queryset = models.Light_profile_slot.objects.all()
    serializer_class = serializers.Light_profile_slotPartialUpdateSerializer


class Light_profile_slotDestroyView(views.ThuxDestroyViewMixin, generics.DestroyAPIView):
    """
    Delete a single light_profile_slot
    """
    queryset = models.Light_profile_slot.objects.all()


class Light_profile_slotSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single light_profile_slot
    """
    queryset = models.Light_profile_slot.objects.all()
    serializer_class = serializers.Light_profile_slotSetStatusSerializer


class Light_profile_slotEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single light_profile_slot
    """
    queryset = models.Light_profile_slot.objects.filter(status=0)
    serializer_class = serializers.Light_profile_slotStatusSerializer
    new_status = 1


class Light_profile_slotDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single light_profile_slot
    """
    queryset = models.Light_profile_slot.objects.filter(status=1)
    serializer_class = serializers.Light_profile_slotStatusSerializer
    new_status = 0


class Motion_eventListView(views.ThuxListViewMixin, generics.ListAPIView):
    """
    Get all  motion_events
    """
    queryset = models.Motion_event.objects.all()
    serializer_class = serializers.Motion_eventListSerializer


class Motion_eventRetrieveView(views.ThuxRetrieveViewMixin, generics.RetrieveAPIView):
    """
    Get a single motion_event
    """
    queryset = models.Motion_event.objects.all()
    serializer_class = serializers.Motion_eventRetrieveSerializer


class Motion_eventCreateView(views.ThuxCreateViewMixin, generics.CreateAPIView):
    """
    Create a single motion_event
    """
    queryset = models.Motion_event.objects.all()
    serializer_class = serializers.Motion_eventCreateSerializer


class Motion_eventPartialUpdateView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Update a single motion_event
    """
    queryset = models.Motion_event.objects.all()
    serializer_class = serializers.Motion_eventPartialUpdateSerializer


class Motion_eventDestroyView(views.ThuxDestroyViewMixin, generics.DestroyAPIView):
    """
    Delete a single motion_event
    """
    queryset = models.Motion_event.objects.all()


class Motion_eventSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single motion_event
    """
    queryset = models.Motion_event.objects.all()
    serializer_class = serializers.Motion_eventSetStatusSerializer


class Motion_eventEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single motion_event
    """
    queryset = models.Motion_event.objects.filter(status=0)
    serializer_class = serializers.Motion_eventStatusSerializer
    new_status = 1


class Motion_eventDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single motion_event
    """
    queryset = models.Motion_event.objects.filter(status=1)
    serializer_class = serializers.Motion_eventStatusSerializer
    new_status = 0


class NodeListView(views.ThuxListViewMixin, generics.ListAPIView):
    """
    Get all  nodes
    """
    queryset = models.Node.objects.all()
    serializer_class = serializers.NodeListSerializer


class NodeRetrieveView(views.ThuxRetrieveViewMixin, generics.RetrieveAPIView):
    """
    Get a single node
    """
    queryset = models.Node.objects.all()
    serializer_class = serializers.NodeRetrieveSerializer


class NodeCreateView(views.ThuxCreateViewMixin, generics.CreateAPIView):
    """
    Create a single node
    """
    queryset = models.Node.objects.all()
    serializer_class = serializers.NodeCreateSerializer


class NodePartialUpdateView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Update a single node
    """
    queryset = models.Node.objects.all()
    serializer_class = serializers.NodePartialUpdateSerializer


class NodeDestroyView(views.ThuxDestroyViewMixin, generics.DestroyAPIView):
    """
    Delete a single node
    """
    queryset = models.Node.objects.all()


class NodeSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single node
    """
    queryset = models.Node.objects.all()
    serializer_class = serializers.NodeSetStatusSerializer


class NodeEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single node
    """
    queryset = models.Node.objects.filter(status=0)
    serializer_class = serializers.NodeStatusSerializer
    new_status = 1


class NodeDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single node
    """
    queryset = models.Node.objects.filter(status=1)
    serializer_class = serializers.NodeStatusSerializer
    new_status = 0


class Node_moduleListView(views.ThuxListViewMixin, generics.ListAPIView):
    """
    Get all  node_modules
    """
    queryset = models.Node_module.objects.all()
    serializer_class = serializers.Node_moduleListSerializer


class Node_moduleRetrieveView(views.ThuxRetrieveViewMixin, generics.RetrieveAPIView):
    """
    Get a single node_module
    """
    queryset = models.Node_module.objects.all()
    serializer_class = serializers.Node_moduleRetrieveSerializer


class Node_moduleCreateView(views.ThuxCreateViewMixin, generics.CreateAPIView):
    """
    Create a single node_module
    """
    queryset = models.Node_module.objects.all()
    serializer_class = serializers.Node_moduleCreateSerializer


class Node_modulePartialUpdateView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Update a single node_module
    """
    queryset = models.Node_module.objects.all()
    serializer_class = serializers.Node_modulePartialUpdateSerializer


class Node_moduleDestroyView(views.ThuxDestroyViewMixin, generics.DestroyAPIView):
    """
    Delete a single node_module
    """
    queryset = models.Node_module.objects.all()


class Node_moduleSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single node_module
    """
    queryset = models.Node_module.objects.all()
    serializer_class = serializers.Node_moduleSetStatusSerializer


class Node_moduleEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single node_module
    """
    queryset = models.Node_module.objects.filter(status=0)
    serializer_class = serializers.Node_moduleStatusSerializer
    new_status = 1


class Node_moduleDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single node_module
    """
    queryset = models.Node_module.objects.filter(status=1)
    serializer_class = serializers.Node_moduleStatusSerializer
    new_status = 0


class Wilamp_alertListView(views.ThuxListViewMixin, generics.ListAPIView):
    """
    Get all  wilamp_alerts
    """
    queryset = models.Wilamp_alert.objects.all()
    serializer_class = serializers.Wilamp_alertListSerializer


class Wilamp_alertRetrieveView(views.ThuxRetrieveViewMixin, generics.RetrieveAPIView):
    """
    Get a single wilamp_alert
    """
    queryset = models.Wilamp_alert.objects.all()
    serializer_class = serializers.Wilamp_alertRetrieveSerializer


class Wilamp_alertCreateView(views.ThuxCreateViewMixin, generics.CreateAPIView):
    """
    Create a single wilamp_alert
    """
    queryset = models.Wilamp_alert.objects.all()
    serializer_class = serializers.Wilamp_alertCreateSerializer


class Wilamp_alertPartialUpdateView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Update a single wilamp_alert
    """
    queryset = models.Wilamp_alert.objects.all()
    serializer_class = serializers.Wilamp_alertPartialUpdateSerializer


class Wilamp_alertDestroyView(views.ThuxDestroyViewMixin, generics.DestroyAPIView):
    """
    Delete a single wilamp_alert
    """
    queryset = models.Wilamp_alert.objects.all()


class Wilamp_alertSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single wilamp_alert
    """
    queryset = models.Wilamp_alert.objects.all()
    serializer_class = serializers.Wilamp_alertSetStatusSerializer


class Wilamp_alertEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single wilamp_alert
    """
    queryset = models.Wilamp_alert.objects.filter(status=0)
    serializer_class = serializers.Wilamp_alertStatusSerializer
    new_status = 1


class Wilamp_alertDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single wilamp_alert
    """
    queryset = models.Wilamp_alert.objects.filter(status=1)
    serializer_class = serializers.Wilamp_alertStatusSerializer
    new_status = 0


class Feeder_pillarListView(views.ThuxListViewMixin, generics.ListAPIView):
    """
    Get all  feeder_pillars
    """
    queryset = models.Feeder_pillar.objects.all()
    serializer_class = serializers.Feeder_pillarListSerializer


class Feeder_pillarRetrieveView(views.ThuxRetrieveViewMixin, generics.RetrieveAPIView):
    """
    Get a single feeder_pillar
    """
    queryset = models.Feeder_pillar.objects.all()
    serializer_class = serializers.Feeder_pillarRetrieveSerializer


class Feeder_pillarCreateView(views.ThuxCreateViewMixin, generics.CreateAPIView):
    """
    Create a single feeder_pillar
    """
    queryset = models.Feeder_pillar.objects.all()
    serializer_class = serializers.Feeder_pillarCreateSerializer


class Feeder_pillarPartialUpdateView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Update a single feeder_pillar
    """
    queryset = models.Feeder_pillar.objects.all()
    serializer_class = serializers.Feeder_pillarPartialUpdateSerializer


class Feeder_pillarDestroyView(views.ThuxDestroyViewMixin, generics.DestroyAPIView):
    """
    Delete a single feeder_pillar
    """
    queryset = models.Feeder_pillar.objects.all()


class Feeder_pillarSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single feeder_pillar
    """
    queryset = models.Feeder_pillar.objects.all()
    serializer_class = serializers.Feeder_pillarSetStatusSerializer


class Feeder_pillarEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single feeder_pillar
    """
    queryset = models.Feeder_pillar.objects.filter(status=0)
    serializer_class = serializers.Feeder_pillarStatusSerializer
    new_status = 1


class Feeder_pillarDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single feeder_pillar
    """
    queryset = models.Feeder_pillar.objects.filter(status=1)
    serializer_class = serializers.Feeder_pillarStatusSerializer
    new_status = 0


class Twilight_management_moduleListView(views.ThuxListViewMixin, generics.ListAPIView):
    """
    Get all  twilight_management_modules
    """
    queryset = models.Twilight_management_module.objects.all()
    serializer_class = serializers.Twilight_management_moduleListSerializer


class Twilight_management_moduleRetrieveView(views.ThuxRetrieveViewMixin, generics.RetrieveAPIView):
    """
    Get a single twilight_management_module
    """
    queryset = models.Twilight_management_module.objects.all()
    serializer_class = serializers.Twilight_management_moduleRetrieveSerializer


class Twilight_management_moduleCreateView(views.ThuxCreateViewMixin, generics.CreateAPIView):
    """
    Create a single twilight_management_module
    """
    queryset = models.Twilight_management_module.objects.all()
    serializer_class = serializers.Twilight_management_moduleCreateSerializer


class Twilight_management_modulePartialUpdateView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Update a single twilight_management_module
    """
    queryset = models.Twilight_management_module.objects.all()
    serializer_class = serializers.Twilight_management_modulePartialUpdateSerializer


class Twilight_management_moduleDestroyView(views.ThuxDestroyViewMixin, generics.DestroyAPIView):
    """
    Delete a single twilight_management_module
    """
    queryset = models.Twilight_management_module.objects.all()


class Twilight_management_moduleSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single twilight_management_module
    """
    queryset = models.Twilight_management_module.objects.all()
    serializer_class = serializers.Twilight_management_moduleSetStatusSerializer


class Twilight_management_moduleEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single twilight_management_module
    """
    queryset = models.Twilight_management_module.objects.filter(status=0)
    serializer_class = serializers.Twilight_management_moduleStatusSerializer
    new_status = 1


class Twilight_management_moduleDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single twilight_management_module
    """
    queryset = models.Twilight_management_module.objects.filter(status=1)
    serializer_class = serializers.Twilight_management_moduleStatusSerializer
    new_status = 0


class Twilight_measureListView(views.ThuxListViewMixin, generics.ListAPIView):
    """
    Get all  twilight_measure
    """
    queryset = models.Twilight_measure.objects.all()
    serializer_class = serializers.Twilight_measureListSerializer


class Twilight_measureRetrieveView(views.ThuxRetrieveViewMixin, generics.RetrieveAPIView):
    """
    Get a single twilight_measure
    """
    queryset = models.Twilight_measure.objects.all()
    serializer_class = serializers.Twilight_measureRetrieveSerializer


class Twilight_measureCreateView(views.ThuxCreateViewMixin, generics.CreateAPIView):
    """
    Create a single twilight_measure
    """
    queryset = models.Twilight_measure.objects.all()
    serializer_class = serializers.Twilight_measureCreateSerializer


class Twilight_measurePartialUpdateView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Update a single twilight_measure
    """
    queryset = models.Twilight_measure.objects.all()
    serializer_class = serializers.Twilight_measurePartialUpdateSerializer


class Twilight_measureDestroyView(views.ThuxDestroyViewMixin, generics.DestroyAPIView):
    """
    Delete a single twilight_measure
    """
    queryset = models.Twilight_measure.objects.all()


class Twilight_measureSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single twilight_measure
    """
    queryset = models.Twilight_measure.objects.all()
    serializer_class = serializers.Twilight_measureSetStatusSerializer


class Twilight_measureEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single twilight_measure
    """
    queryset = models.Twilight_measure.objects.filter(status=0)
    serializer_class = serializers.Twilight_measureStatusSerializer
    new_status = 1


class Twilight_measureDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single twilight_measure
    """
    queryset = models.Twilight_measure.objects.filter(status=1)
    serializer_class = serializers.Twilight_measureStatusSerializer
    new_status = 0


class Motion_management_moduleListView(views.ThuxListViewMixin, generics.ListAPIView):
    """
    Get all  motion_management_modules
    """
    queryset = models.Motion_management_module.objects.all()
    serializer_class = serializers.Motion_management_moduleListSerializer


class Motion_management_moduleRetrieveView(views.ThuxRetrieveViewMixin, generics.RetrieveAPIView):
    """
    Get a single motion_management_module
    """
    queryset = models.Motion_management_module.objects.all()
    serializer_class = serializers.Motion_management_moduleRetrieveSerializer


class Motion_management_moduleCreateView(views.ThuxCreateViewMixin, generics.CreateAPIView):
    """
    Create a single motion_management_module
    """
    queryset = models.Motion_management_module.objects.all()
    serializer_class = serializers.Motion_management_moduleCreateSerializer


class Motion_management_modulePartialUpdateView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Update a single motion_management_module
    """
    queryset = models.Motion_management_module.objects.all()
    serializer_class = serializers.Motion_management_modulePartialUpdateSerializer


class Motion_management_moduleDestroyView(views.ThuxDestroyViewMixin, generics.DestroyAPIView):
    """
    Delete a single motion_management_module
    """
    queryset = models.Motion_management_module.objects.all()


class Motion_management_moduleSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single motion_management_module
    """
    queryset = models.Motion_management_module.objects.all()
    serializer_class = serializers.Motion_management_moduleSetStatusSerializer


class Motion_management_moduleEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single motion_management_module
    """
    queryset = models.Motion_management_module.objects.filter(status=0)
    serializer_class = serializers.Motion_management_moduleStatusSerializer
    new_status = 1


class Motion_management_moduleDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single motion_management_module
    """
    queryset = models.Motion_management_module.objects.filter(status=1)
    serializer_class = serializers.Motion_management_moduleStatusSerializer
    new_status = 0


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserCreateView(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = serializers.UserSerializer


class UserChangePasswordView(generics.UpdateAPIView):
    serializer_class = serializers.ChangePasswordSerializer

    def get_object(self, queryset=None):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response("Success.", status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

