# -*- coding: utf-8 -*-


from apps.wicloud.api.views import model_views, index_views, domain_views

from django.conf.urls import url

app_name = 'api'

urlpatterns = [

    #   __  __           _      _
    #  |  \/  |         | |    | |
    #  | \  / | ___   __| | ___| |
    #  | |\/| |/ _ \ / _` |/ _ \ |
    #  | |  | | (_) | (_| |  __/ |
    #  |_|  |_|\___/ \__,_|\___|_|
    #

    url(
        regex=r'address/$',
        view=model_views.AddressListCreateAPIView.as_view(),
        name='address_list'
    ),

    url(
        regex=r'address/(?P<id>[-\w]+)/$',
        view=model_views.AddressRetrieveUpdateDestroyAPIView.as_view(),
        name='address_detail'
    ),
    url(
        r'^address/set-status/(?P<pk>\w+)/$',
        model_views.AddressSetStatusView.as_view(),
        name='address_set_status'
    ),
    url(
        r'^address/enable/(?P<pk>\w+)/$',
        model_views.AddressEnableView.as_view(),
        name='address_enable'
    ),
    url(
        r'^address/disable/(?P<pk>\w+)/$',
        model_views.AddressDisableView.as_view(),
        name='address_disable'
    ),
    url(
        r'^connected-device/$',
        model_views.Connected_deviceListCreateAPIView.as_view(),
        name='connected_device_list'
    ),
    url(
        r'^connected-device/(?P<id>[-\w]+)/$',
        model_views.Connected_deviceRetrieveUpdateDestroyAPIView.as_view(),
        name='connected_device_detail'
    ),
    url(
        r'^connected-device/set-status/(?P<pk>\w+)/$',
        model_views.Connected_deviceSetStatusView.as_view(),
        name='connected_device_set_status'
    ),
    url(
        r'^connected-device/enable/(?P<pk>\w+)/$',
        model_views.Connected_deviceEnableView.as_view(),
        name='connected_device_enable'
    ),
    url(
        r'^connected-device/disable/(?P<pk>\w+)/$',
        model_views.Connected_deviceDisableView.as_view(),
        name='connected_device_disable'
    ),
    url(
        r'^customer/$',
        model_views.CustomerListCreateAPIView.as_view(),
        name='customer_list'
    ),
    url(
        r'^customer/(?P<id>[-\w]+)/$',
        model_views.CustomerRetrieveUpdateDestroyAPIView.as_view(),
        name='customer_detail'
    ),
    url(
        r'^customer/set-status/(?P<pk>\w+)/$',
        model_views.CustomerSetStatusView.as_view(),
        name='customer_set_status'
    ),
    url(
        r'^customer/enable/(?P<pk>\w+)/$',
        model_views.CustomerEnableView.as_view(),
        name='customer_enable'
    ),
    url(
        r'^customer/disable/(?P<pk>\w+)/$',
        model_views.CustomerDisableView.as_view(),
        name='customer_disable'
    ),
    url(
        r'^energy-interval/$',
        model_views.Energy_intervalListCreateAPIView.as_view(),
        name='energy_interval_list'
    ),
    url(
        r'^energy-interval/(?P<id>[-\w]+)/$',
        model_views.Energy_intervalRetrieveUpdateDestroyAPIView.as_view(),
        name='energy_interval_detail'
    ),
    url(
        r'^energy-interval/set-status/(?P<pk>\w+)/$',
        model_views.Energy_intervalSetStatusView.as_view(),
        name='energy_interval_set_status'
    ),
    url(
        r'^energy-interval/enable/(?P<pk>\w+)/$',
        model_views.Energy_intervalEnableView.as_view(),
        name='energy_interval_enable'
    ),
    url(
        r'^energy-interval/disable/(?P<pk>\w+)/$',
        model_views.Energy_intervalDisableView.as_view(),
        name='energy_interval_disable'
    ),
    url(
        r'^energy-meter-module/$',
        model_views.Energy_meter_moduleListCreateAPIView.as_view(),
        name='energy_meter_module_list'
    ),
    url(
        r'^energy-meter-module/(?P<id>[-\w]+)/$',
        model_views.Energy_meter_moduleRetrieveUpdateDestroyAPIView.as_view(),
        name='energy_meter_module_detail'
    ),
    url(
        r'^energy-meter-module-by-mac/(?P<id>[-\w]+)/$',
        model_views.Energy_meter_moduleByMacRetrieveUpdateDestroyAPIView.as_view(),
        name='energy_meter_module_by_mac_detail'
    ),
    url(
        r'^energy-meter-module/set-status/(?P<pk>\w+)/$',
        model_views.Energy_meter_moduleSetStatusView.as_view(),
        name='energy_meter_module_set_status'
    ),
    url(
        r'^energy-meter-module/enable/(?P<pk>\w+)/$',
        model_views.Energy_meter_moduleEnableView.as_view(),
        name='energy_meter_module_enable'
    ),
    url(
        r'^energy-meter-module/disable/(?P<pk>\w+)/$',
        model_views.Energy_meter_moduleDisableView.as_view(),
        name='energy_meter_module_disable'
    ),
    url(
        r'^energy-meter-peak-measure/$',
        model_views.Energy_meter_peak_measureListCreateAPIView.as_view(),
        name='energy_meter_peak_measure_list'
    ),
    url(
        r'^energy-meter-peak-measure/(?P<id>[-\w]+)/$',
        model_views.Energy_meter_peak_measureRetrieveUpdateDestroyAPIView.as_view(),
        name='energy_meter_peak_measure_detail'
    ),
    url(
        r'^energy-meter-peak-measure/set-status/(?P<pk>\w+)/$',
        model_views.Energy_meter_peak_measureSetStatusView.as_view(),
        name='energy_meter_peak_measure_set_status'
    ),
    url(
        r'^energy-meter-peak-measure/enable/(?P<pk>\w+)/$',
        model_views.Energy_meter_peak_measureEnableView.as_view(),
        name='energy_meter_peak_measure_enable'
    ),
    url(
        r'^energy-meter-peak-measure/disable/(?P<pk>\w+)/$',
        model_views.Energy_meter_peak_measureDisableView.as_view(),
        name='energy_meter_peak_measure_disable'
    ),
    url(
        r'^error-light-level-and-adc-mismatch/$',
        model_views.Error_light_level_and_adc_mismatchListCreateAPIView.as_view(),
        name='error_light_level_and_adc_mismatch_list'
    ),
    url(
        r'^error-light-level-and-adc-mismatch/(?P<id>[-\w]+)/$',
        model_views.Error_light_level_and_adc_mismatchRetrieveUpdateDestroyAPIView.as_view(),
        name='error_light_level_and_adc_mismatch_detail'
    ),
    url(
        r'^error-light-level-and-adc-mismatch/set-status/(?P<pk>\w+)/$',
        model_views.Error_light_level_and_adc_mismatchSetStatusView.as_view(),
        name='error_light_level_and_adc_mismatch_set_status'
    ),
    url(
        r'^error-light-level-and-adc-mismatch/enable/(?P<pk>\w+)/$',
        model_views.Error_light_level_and_adc_mismatchEnableView.as_view(),
        name='error_light_level_and_adc_mismatch_enable'
    ),
    url(
        r'^error-light-level-and-adc-mismatch/disable/(?P<pk>\w+)/$',
        model_views.Error_light_level_and_adc_mismatchDisableView.as_view(),
        name='error_light_level_and_adc_mismatch_disable'
    ),
    url(
        r'^error-light-level-and-power-mismatch/$',
        model_views.Error_light_level_and_power_mismatchListCreateAPIView.as_view(),
        name='error_light_level_and_power_mismatch_list'
    ),
    url(
        r'^error-light-level-and-power-mismatch/(?P<id>[-\w]+)/$',
        model_views.Error_light_level_and_power_mismatchRetrieveUpdateDestroyAPIView.as_view(),
        name='error_light_level_and_power_mismatch_detail'
    ),
    url(
        r'^error-light-level-and-power-mismatch/set-status/(?P<pk>\w+)/$',
        model_views.Error_light_level_and_power_mismatchSetStatusView.as_view(),
        name='error_light_level_and_power_mismatch_set_status'
    ),
    url(
        r'^error-light-level-and-power-mismatch/enable/(?P<pk>\w+)/$',
        model_views.Error_light_level_and_power_mismatchEnableView.as_view(),
        name='error_light_level_and_power_mismatch_enable'
    ),
    url(
        r'^error-light-level-and-power-mismatch/disable/(?P<pk>\w+)/$',
        model_views.Error_light_level_and_power_mismatchDisableView.as_view(),
        name='error_light_level_and_power_mismatch_disable'
    ),
    url(
        r'^error-node-offline/$',
        model_views.Error_node_offlineListCreateAPIView.as_view(),
        name='error_node_offline_list'
    ),
    url(
        r'^error-node-offline/(?P<id>[-\w]+)/$',
        model_views.Error_node_offlineRetrieveUpdateDestroyAPIView.as_view(),
        name='error_node_offline_detail'
    ),
    url(
        r'^error-node-offline/set-status/(?P<pk>\w+)/$',
        model_views.Error_node_offlineSetStatusView.as_view(),
        name='error_node_offline_set_status'
    ),
    url(
        r'^error-node-offline/enable/(?P<pk>\w+)/$',
        model_views.Error_node_offlineEnableView.as_view(),
        name='error_node_offline_enable'
    ),
    url(
        r'^error-node-offline/disable/(?P<pk>\w+)/$',
        model_views.Error_node_offlineDisableView.as_view(),
        name='error_node_offline_disable'
    ),
    url(
        r'^feeder-pillar/$',
        model_views.Feeder_pillarListCreateAPIView.as_view(),
        name='feeder_pillar_list'
    ),
    url(
        r'^feeder-pillar/(?P<id>[-\w]+)/$',
        model_views.Feeder_pillarRetrieveUpdateDestroyAPIView.as_view(),
        name='feeder_pillar_detail'
    ),
    url(
        r'^feeder-pillar/set-status/(?P<pk>\w+)/$',
        model_views.Feeder_pillarSetStatusView.as_view(),
        name='feeder_pillar_set_status'
    ),
    url(
        r'^feeder-pillar/enable/(?P<pk>\w+)/$',
        model_views.Feeder_pillarEnableView.as_view(),
        name='feeder_pillar_enable'
    ),
    url(
        r'^feeder-pillar/disable/(?P<pk>\w+)/$',
        model_views.Feeder_pillarDisableView.as_view(),
        name='feeder_pillar_disable'
    ),
    url(
        r'^gateway/$',
        model_views.GatewayListCreateAPIView.as_view(),
        name='gateway_list'
    ),
    url(
        r'^gateway/(?P<id>[-\w]+)/$',
        model_views.GatewayRetrieveUpdateDestroyAPIView.as_view(),
        name='gateway_detail'
    ),
    url(
        r'^gateway-by-serial-number/(?P<id>[-\w]+)/$',
        model_views.GatewayBySerialNumberRetrieveUpdateDestroyAPIView.as_view(),
        name='gateway_by_serial_number'
    ),
    url(
        r'^gateway-by-installation/(?P<id>[-\w]+)/$',
        model_views.GatewayByInstallationListAPIView.as_view(),
        name='gateway_by_installation'
    ),
    url(
        r'^gateway/set-status/(?P<pk>\w+)/$',
        model_views.GatewaySetStatusView.as_view(),
        name='gateway_set_status'
    ),
    url(
        r'^gateway/enable/(?P<pk>\w+)/$',
        model_views.GatewayEnableView.as_view(),
        name='gateway_enable'
    ),
    url(
        r'^gateway/disable/(?P<pk>\w+)/$',
        model_views.GatewayDisableView.as_view(),
        name='gateway_disable'
    ),
    url(
        r'^ime-power-counter/$',
        model_views.Ime_power_counterListCreateAPIView.as_view(),
        name='ime_power_counter_list'
    ),
    url(
        r'^ime-power-counter/(?P<id>[-\w]+)/$',
        model_views.Ime_power_counterRetrieveUpdateDestroyAPIView.as_view(),
        name='ime_power_counter_detail'
    ),
    url(
        r'^ime-power-counter/set-status/(?P<pk>\w+)/$',
        model_views.Ime_power_counterSetStatusView.as_view(),
        name='ime_power_counter_set_status'
    ),
    url(
        r'^ime-power-counter/enable/(?P<pk>\w+)/$',
        model_views.Ime_power_counterEnableView.as_view(),
        name='ime_power_counter_enable'
    ),
    url(
        r'^ime-power-counter/disable/(?P<pk>\w+)/$',
        model_views.Ime_power_counterDisableView.as_view(),
        name='ime_power_counter_disable'
    ),
    url(
        r'^ime-power-measure/$',
        model_views.Ime_power_measureListCreateAPIView.as_view(),
        name='ime_power_measure_list'
    ),
    url(
        r'^ime-power-measure/(?P<id>[-\w]+)/$',
        model_views.Ime_power_measureRetrieveUpdateDestroyAPIView.as_view(),
        name='ime_power_measure_detail'
    ),
    url(
        r'^ime-power-measure/set-status/(?P<pk>\w+)/$',
        model_views.Ime_power_measureSetStatusView.as_view(),
        name='ime_power_measure_set_status'
    ),
    url(
        r'^ime-power-measure/enable/(?P<pk>\w+)/$',
        model_views.Ime_power_measureEnableView.as_view(),
        name='ime_power_measure_enable'
    ),
    url(
        r'^ime-power-measure/disable/(?P<pk>\w+)/$',
        model_views.Ime_power_measureDisableView.as_view(),
        name='ime_power_measure_disable'
    ),
    url(
        r'^installation/$',
        model_views.InstallationListCreateAPIView.as_view(),
        name='installation_list'
    ),
    url(
        r'^installation/(?P<id>[-\w]+)/$',
        model_views.InstallationRetrieveUpdateDestroyAPIView.as_view(),
        name='installation_detail'
    ),
    url(
        r'^installation/set-status/(?P<pk>\w+)/$',
        model_views.InstallationSetStatusView.as_view(),
        name='installation_set_status'
    ),
    url(
        r'^installation/enable/(?P<pk>\w+)/$',
        model_views.InstallationEnableView.as_view(),
        name='installation_enable'
    ),
    url(
        r'^installation/disable/(?P<pk>\w+)/$',
        model_views.InstallationDisableView.as_view(),
        name='installation_disable'
    ),
    url(
        r'^light-fixture/$',
        model_views.Light_fixtureListCreateAPIView.as_view(),
        name='light_fixture_list'
    ),
    url(
        r'^light-fixture/(?P<id>[-\w]+)/$',
        model_views.Light_fixtureRetrieveUpdateDestroyAPIView.as_view(),
        name='light_fixture_detail'
    ),
    url(
        r'^light-fixture-by-serial-number/(?P<id>[-\w]+)/$',
        model_views.Light_fixtureBySerialNumberRetrieveUpdateDestroyAPIView.as_view(),
        name='light_feature_by_serial_number'
    ),
    url(
        r'^light-fixture-by-installation/(?P<id>[-\w]+)/$',
        model_views.Light_fixtureByInstallationListAPIView.as_view(),
        name='gateway_by_serial_number'
    ),
    url(
        r'^light-fixture/set-status/(?P<pk>\w+)/$',
        model_views.Light_fixtureSetStatusView.as_view(),
        name='light_fixture_set_status'
    ),
    url(
        r'^light-fixture/enable/(?P<pk>\w+)/$',
        model_views.Light_fixtureEnableView.as_view(),
        name='light_fixture_enable'
    ),
    url(
        r'^light-fixture/disable/(?P<pk>\w+)/$',
        model_views.Light_fixtureDisableView.as_view(),
        name='light_fixture_disable'
    ),
    url(
        r'^light-management-measure/$',
        model_views.Light_management_measureListCreateAPIView.as_view(),
        name='light_management_measure_list'
    ),
    url(
        r'^light-management-measure/(?P<id>[-\w]+)/$',
        model_views.Light_management_measureRetrieveUpdateDestroyAPIView.as_view(),
        name='light_management_measure_detail'
    ),
    url(
        r'^light-management-measure/set-status/(?P<pk>\w+)/$',
        model_views.Light_management_measureSetStatusView.as_view(),
        name='light_management_measure_set_status'
    ),
    url(
        r'^light-management-measure/enable/(?P<pk>\w+)/$',
        model_views.Light_management_measureEnableView.as_view(),
        name='light_management_measure_enable'
    ),
    url(
        r'^light-management-measure/disable/(?P<pk>\w+)/$',
        model_views.Light_management_measureDisableView.as_view(),
        name='light_management_measure_disable'
    ),
    url(
        r'^light-management-module/$',
        model_views.Light_management_moduleListCreateAPIView.as_view(),
        name='light_management_module_list'
    ),
    url(
        r'^light-management-module/(?P<id>[-\w]+)/$',
        model_views.Light_management_moduleRetrieveUpdateDestroyAPIView.as_view(),
        name='light_management_module_detail'
    ),
    url(
        r'^light-management-module-by-mac/(?P<id>[-\w]+)/$',
        model_views.Light_management_moduleByMacRetrieveUpdateDestroyAPIView.as_view(),
        name='light_management_module_by_mac_detail'
    ),
    url(
        r'^light-management-module/set-status/(?P<pk>\w+)/$',
        model_views.Light_management_moduleSetStatusView.as_view(),
        name='light_management_module_set_status'
    ),
    url(
        r'^light-management-module/enable/(?P<pk>\w+)/$',
        model_views.Light_management_moduleEnableView.as_view(),
        name='light_management_module_enable'
    ),
    url(
        r'^light-management-module/disable/(?P<pk>\w+)/$',
        model_views.Light_management_moduleDisableView.as_view(),
        name='light_management_module_disable'
    ),
    url(
        r'^light-profile/$',
        model_views.Light_profileListCreateAPIView.as_view(),
        name='light_profile_list'
    ),
    url(
        r'^light-profile/(?P<id>[-\w]+)/replace-slots/$',
        model_views.Light_profile_replace_slots_CreateView.as_view(),
        #views.Light_profileReplaceSlotsView,
        name='light_profile_replace-slots'
    ),
    url(
        r'^light-profile/(?P<id>[-\w]+)/$',
        model_views.Light_profileRetrieveUpdateDestroyAPIView.as_view(),
        name='light_profile_detail'
    ),
    url(
        r'^light-profile-by-reference/(?P<id>[-\w]+)/$',
        model_views.Light_profileByReferenceRetrieveUpdateDestroyAPIView.as_view(),
        name='light_profile-by-reference'
    ),
    url(
        r'^light-profile/set-status/(?P<pk>\w+)/$',
        model_views.Light_profileSetStatusView.as_view(),
        name='light_profile_set_status'
    ),
    url(
        r'^light-profile/enable/(?P<pk>\w+)/$',
        model_views.Light_profileEnableView.as_view(),
        name='light_profile_enable'
    ),
    url(
        r'^light-profile/disable/(?P<pk>\w+)/$',
        model_views.Light_profileDisableView.as_view(),
        name='light_profile_disable'
    ),
    url(
        r'^light-profile-slot/$',
        model_views.Light_profile_slotListCreateAPIView.as_view(),
        name='light_profile_slot_list'
    ),
    url(
        r'^light-profile-slot/(?P<id>[-\w]+)/$',
        model_views.Light_profile_slotRetrieveUpdateDestroyAPIView.as_view(),
        name='light_profile_slot_detail'
    ),
    url(
        r'^light-profile-slot/set-status/(?P<pk>\w+)/$',
        model_views.Light_profile_slotSetStatusView.as_view(),
        name='light_profile_slot_set_status'
    ),
    url(
        r'^light-profile-slot/enable/(?P<pk>\w+)/$',
        model_views.Light_profile_slotEnableView.as_view(),
        name='light_profile_slot_enable'
    ),
    url(
        r'^light-profile-slot/disable/(?P<pk>\w+)/$',
        model_views.Light_profile_slotDisableView.as_view(),
        name='light_profile_slot_disable'
    ),
    url(
        r'^motion-event/$',
        model_views.Motion_eventListCreateAPIView.as_view(),
        name='motion_event_list'
    ),
    url(
        r'^motion-event/(?P<id>[-\w]+)/$',
        model_views.Motion_eventRetrieveUpdateDestroyAPIView.as_view(),
        name='motion_event_detail'
    ),
    url(
        r'^motion-event/set-status/(?P<pk>\w+)/$',
        model_views.Motion_eventSetStatusView.as_view(),
        name='motion_event_set_status'
    ),
    url(
        r'^motion-event/enable/(?P<pk>\w+)/$',
        model_views.Motion_eventEnableView.as_view(),
        name='motion_event_enable'
    ),
    url(
        r'^motion-event/disable/(?P<pk>\w+)/$',
        model_views.Motion_eventDisableView.as_view(),
        name='motion_event_disable'
    ),
    url(
        r'^motion-management-module/$',
        model_views.Motion_management_moduleListCreateAPIView.as_view(),
        name='motion_management_module_list'
    ),
    url(
        r'^motion-management-module/(?P<id>[-\w]+)/$',
        model_views.Motion_management_moduleRetrieveUpdateDestroyAPIView.as_view(),
        name='motion_management_module_detail'
    ),
    url(
        r'^motion-management-module/set-status/(?P<pk>\w+)/$',
        model_views.Motion_management_moduleSetStatusView.as_view(),
        name='motion_management_module_set_status'
    ),
    url(
        r'^motion-management-module/enable/(?P<pk>\w+)/$',
        model_views.Motion_management_moduleEnableView.as_view(),
        name='motion_management_module_enable'
    ),
    url(
        r'^motion-management-module/disable/(?P<pk>\w+)/$',
        model_views.Motion_management_moduleDisableView.as_view(),
        name='motion_management_module_disable'
    ),
    url(
        r'^node/$',
        model_views.NodeListCreateAPIView.as_view(),
        name='node_list'
    ),
    url(
        r'^node/(?P<id>[-\w]+)/$',
        model_views.NodeRetrieveUpdateDestroyAPIView.as_view(),
        name='node_detail'
    ),
    url(
        r'^node-by-mac/(?P<id>[-\w]+)/$',
        model_views.NodeByMacRetrieveUpdateDestroyAPIView.as_view(),
        name='node_by_mac_detail'
    ),
    url(
        r'^node/set-status/(?P<pk>\w+)/$',
        model_views.NodeSetStatusView.as_view(),
        name='node_set_status'
    ),
    url(
        r'^node/enable/(?P<pk>\w+)/$',
        model_views.NodeEnableView.as_view(),
        name='node_enable'
    ),
    url(
        r'^node/disable/(?P<pk>\w+)/$',
        model_views.NodeDisableView.as_view(),
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
    #
    url(
        r'^twilight-management-module/$',
        model_views.Twilight_management_moduleListCreateAPIView.as_view(),
        name='twilight_management_module_list'
    ),
    url(
        r'^twilight-management-module/(?P<id>[-\w]+)/$',
        model_views.Twilight_management_moduleRetrieveUpdateDestroyAPIView.as_view(),
        name='twilight_management_module_detail'
    ),
    url(
        r'^twilight-management-module/set-status/(?P<pk>\w+)/$',
        model_views.Twilight_management_moduleSetStatusView.as_view(),
        name='twilight_management_module_set_status'
    ),
    url(
        r'^twilight-management-module/enable/(?P<pk>\w+)/$',
        model_views.Twilight_management_moduleEnableView.as_view(),
        name='twilight_management_module_enable'
    ),
    url(
        r'^twilight-management-module/disable/(?P<pk>\w+)/$',
        model_views.Twilight_management_moduleDisableView.as_view(),
        name='twilight_management_module_disable'
    ),
    url(
        r'^twilight-measure/$',
        model_views.Twilight_measureListCreateAPIView.as_view(),
        name='twilight_measure_list'
    ),
    url(
        r'^twilight-measure/(?P<id>[-\w]+)/$',
        model_views.Twilight_measureRetrieveUpdateDestroyAPIView.as_view(),
        name='twilight_measure_detail'
    ),
    url(
        r'^twilight-measure/set-status/(?P<pk>\w+)/$',
        model_views.Twilight_measureSetStatusView.as_view(),
        name='twilight_measure_set_status'
    ),
    url(
        r'^twilight-measure/enable/(?P<pk>\w+)/$',
        model_views.Twilight_measureEnableView.as_view(),
        name='twilight_measure_enable'
    ),
    url(
        r'^twilight-measure/disable/(?P<pk>\w+)/$',
        model_views.Twilight_measureDisableView.as_view(),
        name='twilight_measure_disable'
    ),
    url(r'^user/change-password/',
        model_views.UserChangePasswordView.as_view(),
        name='users_change_password'
        ),
    url(
        r'^wilamp-alert/$',
        model_views.Wilamp_alertListCreateAPIView.as_view(),
        name='wilamp_alert_list'
    ),
    url(
        r'^wilamp-alert/(?P<id>[-\w]+)/$',
        model_views.Wilamp_alertRetrieveUpdateDestroyAPIView.as_view(),
        name='wilamp_alert_detail'
    ),
    url(
        r'^wilamp-alert/set-status/(?P<pk>\w+)/$',
        model_views.Wilamp_alertSetStatusView.as_view(),
        name='wilamp_alert_set_status'
    ),
    url(
        r'^wilamp-alert/enable/(?P<pk>\w+)/$',
        model_views.Wilamp_alertEnableView.as_view(),
        name='wilamp_alert_enable'
    ),
    url(
        r'^wilamp-alert/disable/(?P<pk>\w+)/$',
        model_views.Wilamp_alertDisableView.as_view(),
        name='wilamp_alert_disable'
    ),

    #    _____ _        _   _     _   _
    #   / ____| |      | | (_)   | | (_)
    #  | (___ | |_ __ _| |_ _ ___| |_ _  ___ ___
    #   \___ \| __/ _` | __| / __| __| |/ __/ __|
    #   ____) | || (_| | |_| \__ \ |_| | (__\__ \
    #  |_____/ \__\__,_|\__|_|___/\__|_|\___|___/
    #
    #

    url(r'^statistics/installation/global/',
        domain_views.InstallationGlobalStatisticsViewSet.as_view({'get': 'retrieve'}),
        name='installation_global_statistics'
        ),

    #    _____                     _
    #   / ____|                   | |
    #  | (___   ___  __ _ _ __ ___| |__
    #   \___ \ / _ \/ _` | '__/ __| '_ \
    #   ____) |  __/ (_| | | | (__| | | |
    #  |_____/ \___|\__,_|_|  \___|_| |_|
    #

    url(r'^search/installations/',
        model_views.InstallationSearchView.as_view({'get': 'list'}),
        name='search'
        ),
    url(r'^search/gateways/',
        model_views.GatewaySearchView.as_view({'get': 'list'}),
        name='search'
        ),
    url(r'^search/nodes/',
        model_views.NodeSearchView.as_view({'get': 'list'}),
        name='search'
        ),

    #   _____           _
    #  |_   _|         | |
    #    | |  _ __   __| | _____  __
    #    | | | '_ \ / _` |/ _ \ \/ /
    #   _| |_| | | | (_| |  __/>  <
    #  |_____|_| |_|\__,_|\___/_/\_\
    #

    url(r'^$', index_views.api_root, name='api_root'),
]
