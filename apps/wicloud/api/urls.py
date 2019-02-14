# -*- coding: utf-8 -*-


from . import views

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter


app_name = 'api'

urlpatterns = [

    url(
        regex=r'address/$',
        view=views.AddressListCreateAPIView.as_view(),
        name='address_list'
    ),

    url(
        regex=r'address/(?P<id>[-\w]+)/$',
        view=views.AddressRetrieveUpdateDestroyAPIView.as_view(),
        name='address_detail'
    ),
    url(
        r'^address/set-status/(?P<pk>\w+)/$',
        views.AddressSetStatusView.as_view(),
        name='address_set_status'
    ),
    url(
        r'^address/enable/(?P<pk>\w+)/$',
        views.AddressEnableView.as_view(),
        name='address_enable'
    ),
    url(
        r'^address/disable/(?P<pk>\w+)/$',
        views.AddressDisableView.as_view(),
        name='address_disable'
    ),
    url(
        r'^connected-device/$',
        views.Connected_deviceListCreateAPIView.as_view(),
        name='connected_device_list'
    ),
    url(
        r'^connected-device/(?P<id>[-\w]+)/$',
        views.Connected_deviceRetrieveUpdateDestroyAPIView.as_view(),
        name='connected_device_detail'
    ),
    url(
        r'^connected-device/set-status/(?P<pk>\w+)/$',
        views.Connected_deviceSetStatusView.as_view(),
        name='connected_device_set_status'
    ),
    url(
        r'^connected-device/enable/(?P<pk>\w+)/$',
        views.Connected_deviceEnableView.as_view(),
        name='connected_device_enable'
    ),
    url(
        r'^connected-device/disable/(?P<pk>\w+)/$',
        views.Connected_deviceDisableView.as_view(),
        name='connected_device_disable'
    ),
    url(
        r'^customer/$',
        views.CustomerListCreateAPIView.as_view(),
        name='customer_list'
    ),
    url(
        r'^customer/(?P<id>[-\w]+)/$',
        views.CustomerRetrieveUpdateDestroyAPIView.as_view(),
        name='customer_detail'
    ),
    url(
        r'^customer/set-status/(?P<pk>\w+)/$',
        views.CustomerSetStatusView.as_view(),
        name='customer_set_status'
    ),
    url(
        r'^customer/enable/(?P<pk>\w+)/$',
        views.CustomerEnableView.as_view(),
        name='customer_enable'
    ),
    url(
        r'^customer/disable/(?P<pk>\w+)/$',
        views.CustomerDisableView.as_view(),
        name='customer_disable'
    ),
    url(
        r'^energy-interval/$',
        views.Energy_intervalListCreateAPIView.as_view(),
        name='energy_interval_list'
    ),
    url(
        r'^energy-interval/(?P<id>[-\w]+)/$',
        views.Energy_intervalRetrieveUpdateDestroyAPIView.as_view(),
        name='energy_interval_detail'
    ),
    url(
        r'^energy-interval/set-status/(?P<pk>\w+)/$',
        views.Energy_intervalSetStatusView.as_view(),
        name='energy_interval_set_status'
    ),
    url(
        r'^energy-interval/enable/(?P<pk>\w+)/$',
        views.Energy_intervalEnableView.as_view(),
        name='energy_interval_enable'
    ),
    url(
        r'^energy-interval/disable/(?P<pk>\w+)/$',
        views.Energy_intervalDisableView.as_view(),
        name='energy_interval_disable'
    ),
    url(
        r'^energy-meter-module/$',
        views.Energy_meter_moduleListCreateAPIView.as_view(),
        name='energy_meter_module_list'
    ),
    url(
        r'^energy-meter-module/(?P<id>[-\w]+)/$',
        views.Energy_meter_moduleRetrieveUpdateDestroyAPIView.as_view(),
        name='energy_meter_module_detail'
    ),
    url(
        r'^energy-meter-module-by-mac/(?P<id>[-\w]+)/$',
        views.Energy_meter_moduleByMacRetrieveUpdateDestroyAPIView.as_view(),
        name='energy_meter_module_by_mac_detail'
    ),
    url(
        r'^energy-meter-module/set-status/(?P<pk>\w+)/$',
        views.Energy_meter_moduleSetStatusView.as_view(),
        name='energy_meter_module_set_status'
    ),
    url(
        r'^energy-meter-module/enable/(?P<pk>\w+)/$',
        views.Energy_meter_moduleEnableView.as_view(),
        name='energy_meter_module_enable'
    ),
    url(
        r'^energy-meter-module/disable/(?P<pk>\w+)/$',
        views.Energy_meter_moduleDisableView.as_view(),
        name='energy_meter_module_disable'
    ),
    url(
        r'^energy-meter-peak-measure/$',
        views.Energy_meter_peak_measureListCreateAPIView.as_view(),
        name='energy_meter_peak_measure_list'
    ),
    url(
        r'^energy-meter-peak-measure/(?P<id>[-\w]+)/$',
        views.Energy_meter_peak_measureRetrieveUpdateDestroyAPIView.as_view(),
        name='energy_meter_peak_measure_detail'
    ),
    url(
        r'^energy-meter-peak-measure/set-status/(?P<pk>\w+)/$',
        views.Energy_meter_peak_measureSetStatusView.as_view(),
        name='energy_meter_peak_measure_set_status'
    ),
    url(
        r'^energy-meter-peak-measure/enable/(?P<pk>\w+)/$',
        views.Energy_meter_peak_measureEnableView.as_view(),
        name='energy_meter_peak_measure_enable'
    ),
    url(
        r'^energy-meter-peak-measure/disable/(?P<pk>\w+)/$',
        views.Energy_meter_peak_measureDisableView.as_view(),
        name='energy_meter_peak_measure_disable'
    ),
    url(
        r'^error-light-level-and-adc-mismatch/$',
        views.Error_light_level_and_adc_mismatchListCreateAPIView.as_view(),
        name='error_light_level_and_adc_mismatch_list'
    ),
    url(
        r'^error-light-level-and-adc-mismatch/(?P<id>[-\w]+)/$',
        views.Error_light_level_and_adc_mismatchRetrieveUpdateDestroyAPIView.as_view(),
        name='error_light_level_and_adc_mismatch_detail'
    ),
    url(
        r'^error-light-level-and-adc-mismatch/set-status/(?P<pk>\w+)/$',
        views.Error_light_level_and_adc_mismatchSetStatusView.as_view(),
        name='error_light_level_and_adc_mismatch_set_status'
    ),
    url(
        r'^error-light-level-and-adc-mismatch/enable/(?P<pk>\w+)/$',
        views.Error_light_level_and_adc_mismatchEnableView.as_view(),
        name='error_light_level_and_adc_mismatch_enable'
    ),
    url(
        r'^error-light-level-and-adc-mismatch/disable/(?P<pk>\w+)/$',
        views.Error_light_level_and_adc_mismatchDisableView.as_view(),
        name='error_light_level_and_adc_mismatch_disable'
    ),
    url(
        r'^error-light-level-and-power-mismatch/$',
        views.Error_light_level_and_power_mismatchListCreateAPIView.as_view(),
        name='error_light_level_and_power_mismatch_list'
    ),
    url(
        r'^error-light-level-and-power-mismatch/(?P<id>[-\w]+)/$',
        views.Error_light_level_and_power_mismatchRetrieveUpdateDestroyAPIView.as_view(),
        name='error_light_level_and_power_mismatch_detail'
    ),
    url(
        r'^error-light-level-and-power-mismatch/set-status/(?P<pk>\w+)/$',
        views.Error_light_level_and_power_mismatchSetStatusView.as_view(),
        name='error_light_level_and_power_mismatch_set_status'
    ),
    url(
        r'^error-light-level-and-power-mismatch/enable/(?P<pk>\w+)/$',
        views.Error_light_level_and_power_mismatchEnableView.as_view(),
        name='error_light_level_and_power_mismatch_enable'
    ),
    url(
        r'^error-light-level-and-power-mismatch/disable/(?P<pk>\w+)/$',
        views.Error_light_level_and_power_mismatchDisableView.as_view(),
        name='error_light_level_and_power_mismatch_disable'
    ),
    url(
        r'^error-node-offline/$',
        views.Error_node_offlineListCreateAPIView.as_view(),
        name='error_node_offline_list'
    ),
    url(
        r'^error-node-offline/(?P<id>[-\w]+)/$',
        views.Error_node_offlineRetrieveUpdateDestroyAPIView.as_view(),
        name='error_node_offline_detail'
    ),
    url(
        r'^error-node-offline/set-status/(?P<pk>\w+)/$',
        views.Error_node_offlineSetStatusView.as_view(),
        name='error_node_offline_set_status'
    ),
    url(
        r'^error-node-offline/enable/(?P<pk>\w+)/$',
        views.Error_node_offlineEnableView.as_view(),
        name='error_node_offline_enable'
    ),
    url(
        r'^error-node-offline/disable/(?P<pk>\w+)/$',
        views.Error_node_offlineDisableView.as_view(),
        name='error_node_offline_disable'
    ),
    url(
        r'^gateway/$',
        views.GatewayListCreateAPIView.as_view(),
        name='gateway_list'
    ),
    url(
        r'^gateway/(?P<id>[-\w]+)/$',
        views.GatewayRetrieveUpdateDestroyAPIView.as_view(),
        name='gateway_detail'
    ),
    url(
        r'^gateway-by-serial-number/(?P<id>[-\w]+)/$',
        views.GatewayBySerialNumberRetrieveUpdateDestroyAPIView.as_view(),
        name='energy_meter_module_by_mac_detail'
    ),
    url(
        r'^gateway/set-status/(?P<pk>\w+)/$',
        views.GatewaySetStatusView.as_view(),
        name='gateway_set_status'
    ),
    url(
        r'^gateway/enable/(?P<pk>\w+)/$',
        views.GatewayEnableView.as_view(),
        name='gateway_enable'
    ),
    url(
        r'^gateway/disable/(?P<pk>\w+)/$',
        views.GatewayDisableView.as_view(),
        name='gateway_disable'
    ),
    url(
        r'^ime-power-counter/$',
        views.Ime_power_counterListCreateAPIView.as_view(),
        name='ime_power_counter_list'
    ),
    url(
        r'^ime-power-counter/(?P<id>[-\w]+)/$',
        views.Ime_power_counterRetrieveUpdateDestroyAPIView.as_view(),
        name='ime_power_counter_detail'
    ),
    url(
        r'^ime-power-counter/set-status/(?P<pk>\w+)/$',
        views.Ime_power_counterSetStatusView.as_view(),
        name='ime_power_counter_set_status'
    ),
    url(
        r'^ime-power-counter/enable/(?P<pk>\w+)/$',
        views.Ime_power_counterEnableView.as_view(),
        name='ime_power_counter_enable'
    ),
    url(
        r'^ime-power-counter/disable/(?P<pk>\w+)/$',
        views.Ime_power_counterDisableView.as_view(),
        name='ime_power_counter_disable'
    ),
    url(
        r'^ime-power-measure/$',
        views.Ime_power_measureListCreateAPIView.as_view(),
        name='ime_power_measure_list'
    ),
    url(
        r'^ime-power-measure/(?P<id>[-\w]+)/$',
        views.Ime_power_measureRetrieveUpdateDestroyAPIView.as_view(),
        name='ime_power_measure_detail'
    ),
    url(
        r'^ime-power-measure/set-status/(?P<pk>\w+)/$',
        views.Ime_power_measureSetStatusView.as_view(),
        name='ime_power_measure_set_status'
    ),
    url(
        r'^ime-power-measure/enable/(?P<pk>\w+)/$',
        views.Ime_power_measureEnableView.as_view(),
        name='ime_power_measure_enable'
    ),
    url(
        r'^ime-power-measure/disable/(?P<pk>\w+)/$',
        views.Ime_power_measureDisableView.as_view(),
        name='ime_power_measure_disable'
    ),
    url(
        r'^installation/$',
        views.InstallationListCreateAPIView.as_view(),
        name='installation_list'
    ),
    url(
        r'^installation/(?P<id>[-\w]+)/$',
        views.InstallationRetrieveUpdateDestroyAPIView.as_view(),
        name='installation_detail'
    ),
    url(
        r'^installation/set-status/(?P<pk>\w+)/$',
        views.InstallationSetStatusView.as_view(),
        name='installation_set_status'
    ),
    url(
        r'^installation/enable/(?P<pk>\w+)/$',
        views.InstallationEnableView.as_view(),
        name='installation_enable'
    ),
    url(
        r'^installation/disable/(?P<pk>\w+)/$',
        views.InstallationDisableView.as_view(),
        name='installation_disable'
    ),
    url(
        r'^light-fixture/$',
        views.Light_fixtureListCreateAPIView.as_view(),
        name='light_fixture_list'
    ),
    url(
        r'^light-fixture/(?P<id>[-\w]+)/$',
        views.Light_fixtureRetrieveUpdateDestroyAPIView.as_view(),
        name='light_fixture_detail'
    ),
    url(
        r'^light-fixture-by-serial-number/(?P<id>[-\w]+)/$',
        views.Light_fixtureBySerialNumberRetrieveUpdateDestroyAPIView.as_view(),
        name='light_feature_by_serial_number'
    ),

    url(
        r'^light-fixture/set-status/(?P<pk>\w+)/$',
        views.Light_fixtureSetStatusView.as_view(),
        name='light_fixture_set_status'
    ),
    url(
        r'^light-fixture/enable/(?P<pk>\w+)/$',
        views.Light_fixtureEnableView.as_view(),
        name='light_fixture_enable'
    ),
    url(
        r'^light-fixture/disable/(?P<pk>\w+)/$',
        views.Light_fixtureDisableView.as_view(),
        name='light_fixture_disable'
    ),
    url(
        r'^light-management-measure/$',
        views.Light_management_measureListCreateAPIView.as_view(),
        name='light_management_measure_list'
    ),
    url(
        r'^light-management-measure/(?P<id>[-\w]+)/$',
        views.Light_management_measureRetrieveUpdateDestroyAPIView.as_view(),
        name='light_management_measure_detail'
    ),
    url(
        r'^light-management-measure/set-status/(?P<pk>\w+)/$',
        views.Light_management_measureSetStatusView.as_view(),
        name='light_management_measure_set_status'
    ),
    url(
        r'^light-management-measure/enable/(?P<pk>\w+)/$',
        views.Light_management_measureEnableView.as_view(),
        name='light_management_measure_enable'
    ),
    url(
        r'^light-management-measure/disable/(?P<pk>\w+)/$',
        views.Light_management_measureDisableView.as_view(),
        name='light_management_measure_disable'
    ),
    url(
        r'^light-management-module/$',
        views.Light_management_moduleListCreateAPIView.as_view(),
        name='light_management_module_list'
    ),
    url(
        r'^light-management-module/(?P<id>[-\w]+)/$',
        views.Light_management_moduleRetrieveUpdateDestroyAPIView.as_view(),
        name='light_management_module_detail'
    ),
    url(
        r'^light-management-module-by-mac/(?P<id>[-\w]+)/$',
        views.Light_management_moduleByMacRetrieveUpdateDestroyAPIView.as_view(),
        name='light_management_module_by_mac_detail'
    ),
    url(
        r'^light-management-module/set-status/(?P<pk>\w+)/$',
        views.Light_management_moduleSetStatusView.as_view(),
        name='light_management_module_set_status'
    ),
    url(
        r'^light-management-module/enable/(?P<pk>\w+)/$',
        views.Light_management_moduleEnableView.as_view(),
        name='light_management_module_enable'
    ),
    url(
        r'^light-management-module/disable/(?P<pk>\w+)/$',
        views.Light_management_moduleDisableView.as_view(),
        name='light_management_module_disable'
    ),
    url(
        r'^light-profile/$',
        views.Light_profileListCreateAPIView.as_view(),
        name='light_profile_list'
    ),
    url(
        r'^light-profile/(?P<id>[-\w]+)/replace-slots/$',
        views.Light_profile_replace_slots_CreateView.as_view(),
        #views.Light_profileReplaceSlotsView,
        name='light_profile_replace-slots'
    ),
    url(
        r'^light-profile/(?P<id>[-\w]+)/$',
        views.Light_profileRetrieveUpdateDestroyAPIView.as_view(),
        name='light_profile_detail'
    ),
    url(
        r'^light-profile-by-reference/(?P<id>[-\w]+)/$',
        views.Light_profileByReferenceRetrieveUpdateDestroyAPIView.as_view(),
        name='light_profile-by-reference'
    ),
    url(
        r'^light-profile/set-status/(?P<pk>\w+)/$',
        views.Light_profileSetStatusView.as_view(),
        name='light_profile_set_status'
    ),
    url(
        r'^light-profile/enable/(?P<pk>\w+)/$',
        views.Light_profileEnableView.as_view(),
        name='light_profile_enable'
    ),
    url(
        r'^light-profile/disable/(?P<pk>\w+)/$',
        views.Light_profileDisableView.as_view(),
        name='light_profile_disable'
    ),
    url(
        r'^light-profile-slot/$',
        views.Light_profile_slotListCreateAPIView.as_view(),
        name='light_profile_slot_list'
    ),
    url(
        r'^light-profile-slot/(?P<id>[-\w]+)/$',
        views.Light_profile_slotRetrieveUpdateDestroyAPIView.as_view(),
        name='light_profile_slot_detail'
    ),
    url(
        r'^light-profile-slot/set-status/(?P<pk>\w+)/$',
        views.Light_profile_slotSetStatusView.as_view(),
        name='light_profile_slot_set_status'
    ),
    url(
        r'^light-profile-slot/enable/(?P<pk>\w+)/$',
        views.Light_profile_slotEnableView.as_view(),
        name='light_profile_slot_enable'
    ),
    url(
        r'^light-profile-slot/disable/(?P<pk>\w+)/$',
        views.Light_profile_slotDisableView.as_view(),
        name='light_profile_slot_disable'
    ),
    url(
        r'^motion-event/$',
        views.Motion_eventListCreateAPIView.as_view(),
        name='motion_event_list'
    ),
    url(
        r'^motion-event/(?P<id>[-\w]+)/$',
        views.Motion_eventRetrieveUpdateDestroyAPIView.as_view(),
        name='motion_event_detail'
    ),
    url(
        r'^motion-event/set-status/(?P<pk>\w+)/$',
        views.Motion_eventSetStatusView.as_view(),
        name='motion_event_set_status'
    ),
    url(
        r'^motion-event/enable/(?P<pk>\w+)/$',
        views.Motion_eventEnableView.as_view(),
        name='motion_event_enable'
    ),
    url(
        r'^motion-event/disable/(?P<pk>\w+)/$',
        views.Motion_eventDisableView.as_view(),
        name='motion_event_disable'
    ),
    url(
        r'^node/$',
        views.NodeListCreateAPIView.as_view(),
        name='node_list'
    ),
    url(
        r'^node/(?P<id>[-\w]+)/$',
        views.NodeRetrieveUpdateDestroyAPIView.as_view(),
        name='node_detail'
    ),
    url(
        r'^node-by-mac/(?P<id>[-\w]+)/$',
        views.NodeByMacRetrieveUpdateDestroyAPIView.as_view(),
        name='node_by_mac_detail'
    ),
    url(
        r'^node/set-status/(?P<pk>\w+)/$',
        views.NodeSetStatusView.as_view(),
        name='node_set_status'
    ),
    url(
        r'^node/enable/(?P<pk>\w+)/$',
        views.NodeEnableView.as_view(),
        name='node_enable'
    ),
    url(
        r'^node/disable/(?P<pk>\w+)/$',
        views.NodeDisableView.as_view(),
        name='node_disable'
    ),
    # url(
    #     r'^node-module/$',
    #     views.Node_moduleListCreateAPIView.as_view(),
    #     name='node_module_list'
    # ),
    # url(
    #     r'^node-module/(?P<id>[-\w]+)/$',
    #     views.Node_moduleRetrieveUpdateDestroyAPIView.as_view(),
    #     name='node_module_detail'
    # ),
    # url(
    #     r'^node-module-by-mac/(?P<id>[-\w]+)/$',
    #     views.Node_moduleByMacRetrieveUpdateDestroyAPIView.as_view(),
    #     name='node_module_by_mac_detail'
    # ),
    # url(
    #     r'^node-module/set-status/(?P<pk>\w+)/$',
    #     views.Node_moduleSetStatusView.as_view(),
    #     name='node_module_set_status'
    # ),
    # url(
    #     r'^node-module/enable/(?P<pk>\w+)/$',
    #     views.Node_moduleEnableView.as_view(),
    #     name='node_module_enable'
    # ),
    # url(
    #     r'^node-module/disable/(?P<pk>\w+)/$',
    #     views.Node_moduleDisableView.as_view(),
    #     name='node_module_disable'
    # ),
    url(
        r'^wilamp-alert/$',
        views.Wilamp_alertListCreateAPIView.as_view(),
        name='wilamp_alert_list'
    ),
    url(
        r'^wilamp-alert/(?P<id>[-\w]+)/$',
        views.Wilamp_alertRetrieveUpdateDestroyAPIView.as_view(),
        name='wilamp_alert_detail'
    ),
    url(
        r'^wilamp-alert/set-status/(?P<pk>\w+)/$',
        views.Wilamp_alertSetStatusView.as_view(),
        name='wilamp_alert_set_status'
    ),
    url(
        r'^wilamp-alert/enable/(?P<pk>\w+)/$',
        views.Wilamp_alertEnableView.as_view(),
        name='wilamp_alert_enable'
    ),
    url(
        r'^wilamp-alert/disable/(?P<pk>\w+)/$',
        views.Wilamp_alertDisableView.as_view(),
        name='wilamp_alert_disable'
    ),
    url(
        r'^feeder-pillar/$',
        views.Feeder_pillarListCreateAPIView.as_view(),
        name='feeder_pillar_list'
    ),
    url(
        r'^feeder-pillar/(?P<id>[-\w]+)/$',
        views.Feeder_pillarRetrieveUpdateDestroyAPIView.as_view(),
        name='feeder_pillar_detail'
    ),
    url(
        r'^feeder-pillar/set-status/(?P<pk>\w+)/$',
        views.Feeder_pillarSetStatusView.as_view(),
        name='feeder_pillar_set_status'
    ),
    url(
        r'^feeder-pillar/enable/(?P<pk>\w+)/$',
        views.Feeder_pillarEnableView.as_view(),
        name='feeder_pillar_enable'
    ),
    url(
        r'^feeder-pillar/disable/(?P<pk>\w+)/$',
        views.Feeder_pillarDisableView.as_view(),
        name='feeder_pillar_disable'
    ),
    url(
        r'^twilight-management-module/$',
        views.Twilight_management_moduleListCreateAPIView.as_view(),
        name='twilight_management_module_list'
    ),
    url(
        r'^twilight-management-module/(?P<id>[-\w]+)/$',
        views.Twilight_management_moduleRetrieveUpdateDestroyAPIView.as_view(),
        name='twilight_management_module_detail'
    ),
    url(
        r'^twilight-management-module/set-status/(?P<pk>\w+)/$',
        views.Twilight_management_moduleSetStatusView.as_view(),
        name='twilight_management_module_set_status'
    ),
    url(
        r'^twilight-management-module/enable/(?P<pk>\w+)/$',
        views.Twilight_management_moduleEnableView.as_view(),
        name='twilight_management_module_enable'
    ),
    url(
        r'^twilight-management-module/disable/(?P<pk>\w+)/$',
        views.Twilight_management_moduleDisableView.as_view(),
        name='twilight_management_module_disable'
    ),
    url(
        r'^twilight-measure/$',
        views.Twilight_measureListCreateAPIView.as_view(),
        name='twilight_measure_list'
    ),
    url(
        r'^twilight-measure/(?P<id>[-\w]+)/$',
        views.Twilight_measureRetrieveUpdateDestroyAPIView.as_view(),
        name='twilight_measure_detail'
    ),
    url(
        r'^twilight-measure/set-status/(?P<pk>\w+)/$',
        views.Twilight_measureSetStatusView.as_view(),
        name='twilight_measure_set_status'
    ),
    url(
        r'^twilight-measure/enable/(?P<pk>\w+)/$',
        views.Twilight_measureEnableView.as_view(),
        name='twilight_measure_enable'
    ),
    url(
        r'^twilight-measure/disable/(?P<pk>\w+)/$',
        views.Twilight_measureDisableView.as_view(),
        name='twilight_measure_disable'
    ),
    url(
        r'^motion-management-module/$',
        views.Motion_management_moduleListCreateAPIView.as_view(),
        name='motion_management_module_list'
    ),
    url(
        r'^motion-management-module/(?P<id>[-\w]+)/$',
        views.Motion_management_moduleRetrieveUpdateDestroyAPIView.as_view(),
        name='motion_management_module_detail'
    ),
    url(
        r'^motion-management-module/set-status/(?P<pk>\w+)/$',
        views.Motion_management_moduleSetStatusView.as_view(),
        name='motion_management_module_set_status'
    ),
    url(
        r'^motion-management-module/enable/(?P<pk>\w+)/$',
        views.Motion_management_moduleEnableView.as_view(),
        name='motion_management_module_enable'
    ),
    url(
        r'^motion-management-module/disable/(?P<pk>\w+)/$',
        views.Motion_management_moduleDisableView.as_view(),
        name='motion_management_module_disable'
    ),
    url(r'^user/change-password/',
        views.UserChangePasswordView.as_view(),
        name='users_change_password'
    ),
    url(r'^search/installations/',
        views.InstallationSearchView.as_view({'get': 'list'}),
        name='search'
    ),
    url(r'^search/gateways/',
        views.GatewaySearchView.as_view({'get': 'list'}),
        name='search'
    ),
    url(r'^search/nodes/',
        views.NodeSearchView.as_view({'get': 'list'}),
        name='search'
    ),
    url(r'^$', views.api_root, name='api_root'),
]
