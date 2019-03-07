# -*- coding: utf-8 -*-

from rest_framework import serializers

from apps.wicloud.domain.statistics.installation import WeeklyEnergyStatistics, InstallationGlobalStatistics, \
    MonthlyEnergyStatistics, IntervalEnergyStatistics, AbsorbedPowerEstimation
from apps.wicloud.models import Address
from .. import models
from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

#   __  __           _      _                 _       _ _
#  |  \/  |         | |    | |               (_)     | (_)
#  | \  / | ___   __| | ___| |  ___  ___ _ __ _  __ _| |_ _______ _ __ ___
#  | |\/| |/ _ \ / _` |/ _ \ | / __|/ _ \ '__| |/ _` | | |_  / _ \ '__/ __|
#  | |  | | (_) | (_| |  __/ | \__ \  __/ |  | | (_| | | |/ /  __/ |  \__ \
#  |_|  |_|\___/ \__,_|\___|_| |___/\___|_|  |_|\__,_|_|_/___\___|_|  |___/
#

class AddressListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class AddressRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class AddressCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class AddressPartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class AddressSetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = ('status',)

    def update(self, instance, validated_data):
        instance.status = validated_data['status']
        instance.save()
        return instance

    def to_representation(self, instance):
        return AddressRetrieveSerializer(instance).data


class AddressStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = ()

    def to_representation(self, instance):
        return AddressRetrieveSerializer(instance).data


class Connected_deviceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Connected_device
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Connected_deviceRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Connected_device
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Connected_deviceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Connected_device
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Connected_devicePartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Connected_device
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Connected_deviceSetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Connected_device
        fields = ('status',)

    def update(self, instance, validated_data):
        instance.status = validated_data['status']
        instance.save()
        return instance

    def to_representation(self, instance):
        return Connected_deviceRetrieveSerializer(instance).data


class Connected_deviceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Connected_device
        fields = ()

    def to_representation(self, instance):
        return Connected_deviceRetrieveSerializer(instance).data

class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class CustomerRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class CustomerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class CustomerPartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class CustomerSetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ('status',)

    def update(self, instance, validated_data):
        instance.status = validated_data['status']
        instance.save()
        return instance

    def to_representation(self, instance):
        return CustomerRetrieveSerializer(instance).data


class CustomerStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ()

    def to_representation(self, instance):
        return CustomerRetrieveSerializer(instance).data


class Energy_intervalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Energy_interval
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Energy_intervalRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Energy_interval
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Energy_intervalCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Energy_interval
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Energy_intervalPartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Energy_interval
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Energy_intervalSetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Energy_interval
        fields = ('status',)

    def update(self, instance, validated_data):
        instance.status = validated_data['status']
        instance.save()
        return instance

    def to_representation(self, instance):
        return Energy_intervalRetrieveSerializer(instance).data


class Energy_intervalStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Energy_interval
        fields = ()

    def to_representation(self, instance):
        return Energy_intervalRetrieveSerializer(instance).data


class Energy_meter_moduleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Energy_meter_module
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Energy_meter_moduleRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Energy_meter_module
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Energy_meter_moduleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Energy_meter_module
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Energy_meter_modulePartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Energy_meter_module
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Energy_meter_moduleSetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Energy_meter_module
        fields = ('status',)

    def update(self, instance, validated_data):
        instance.status = validated_data['status']
        instance.save()
        return instance

    def to_representation(self, instance):
        return Energy_meter_moduleRetrieveSerializer(instance).data


class Energy_meter_moduleStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Energy_meter_module
        fields = ()

    def to_representation(self, instance):
        return Energy_meter_moduleRetrieveSerializer(instance).data


class Energy_meter_peak_measureListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Energy_meter_peak_measure
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Energy_meter_peak_measureRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Energy_meter_peak_measure
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Energy_meter_peak_measureCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Energy_meter_peak_measure
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Energy_meter_peak_measurePartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Energy_meter_peak_measure
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Energy_meter_peak_measureSetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Energy_meter_peak_measure
        fields = ('status',)

    def update(self, instance, validated_data):
        instance.status = validated_data['status']
        instance.save()
        return instance

    def to_representation(self, instance):
        return Energy_meter_peak_measureRetrieveSerializer(instance).data


class Energy_meter_peak_measureStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Energy_meter_peak_measure
        fields = ()

    def to_representation(self, instance):
        return Energy_meter_peak_measureRetrieveSerializer(instance).data


class Error_light_level_and_adc_mismatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Error_light_level_and_adc_mismatch
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Error_light_level_and_adc_mismatchRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Error_light_level_and_adc_mismatch
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Error_light_level_and_adc_mismatchCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Error_light_level_and_adc_mismatch
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Error_light_level_and_adc_mismatchPartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Error_light_level_and_adc_mismatch
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Error_light_level_and_adc_mismatchSetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Error_light_level_and_adc_mismatch
        fields = ('status',)

    def update(self, instance, validated_data):
        instance.status = validated_data['status']
        instance.save()
        return instance

    def to_representation(self, instance):
        return Error_light_level_and_adc_mismatchRetrieveSerializer(instance).data


class Error_light_level_and_adc_mismatchStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Error_light_level_and_adc_mismatch
        fields = ()

    def to_representation(self, instance):
        return Error_light_level_and_adc_mismatchRetrieveSerializer(instance).data


class Error_light_level_and_power_mismatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Error_light_level_and_power_mismatch
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Error_light_level_and_power_mismatchRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Error_light_level_and_power_mismatch
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Error_light_level_and_power_mismatchCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Error_light_level_and_power_mismatch
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Error_light_level_and_power_mismatchPartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Error_light_level_and_power_mismatch
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Error_light_level_and_power_mismatchSetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Error_light_level_and_power_mismatch
        fields = ('status',)

    def update(self, instance, validated_data):
        instance.status = validated_data['status']
        instance.save()
        return instance

    def to_representation(self, instance):
        return Error_light_level_and_power_mismatchRetrieveSerializer(instance).data


class Error_light_level_and_power_mismatchStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Error_light_level_and_power_mismatch
        fields = ()

    def to_representation(self, instance):
        return Error_light_level_and_power_mismatchRetrieveSerializer(instance).data


class Error_node_offlineListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Error_node_offline
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Error_node_offlineRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Error_node_offline
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Error_node_offlineCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Error_node_offline
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Error_node_offlinePartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Error_node_offline
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Error_node_offlineSetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Error_node_offline
        fields = ('status',)

    def update(self, instance, validated_data):
        instance.status = validated_data['status']
        instance.save()
        return instance

    def to_representation(self, instance):
        return Error_node_offlineRetrieveSerializer(instance).data


class Error_node_offlineStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Error_node_offline
        fields = ()

    def to_representation(self, instance):
        return Error_node_offlineRetrieveSerializer(instance).data


class GatewayListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gateway
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class GatewayRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gateway
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class GatewayCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gateway
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class GatewayPartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gateway
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class GatewaySetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gateway
        fields = ('status',)

    def update(self, instance, validated_data):
        instance.status = validated_data['status']
        instance.save()
        return instance

    def to_representation(self, instance):
        return GatewayRetrieveSerializer(instance).data


class GatewayStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gateway
        fields = ()

    def to_representation(self, instance):
        return GatewayRetrieveSerializer(instance).data


class Ime_power_counterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ime_power_counter
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Ime_power_counterRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ime_power_counter
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Ime_power_counterCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ime_power_counter
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Ime_power_counterPartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ime_power_counter
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Ime_power_counterSetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ime_power_counter
        fields = ('status',)

    def update(self, instance, validated_data):
        instance.status = validated_data['status']
        instance.save()
        return instance

    def to_representation(self, instance):
        return Ime_power_counterRetrieveSerializer(instance).data


class Ime_power_counterStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ime_power_counter
        fields = ()

    def to_representation(self, instance):
        return Ime_power_counterRetrieveSerializer(instance).data


class Ime_power_measureListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ime_power_measure
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Ime_power_measureRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ime_power_measure
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Ime_power_measureCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ime_power_measure
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Ime_power_measurePartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ime_power_measure
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Ime_power_measureSetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ime_power_measure
        fields = ('status',)

    def update(self, instance, validated_data):
        instance.status = validated_data['status']
        instance.save()
        return instance

    def to_representation(self, instance):
        return Ime_power_measureRetrieveSerializer(instance).data


class Ime_power_measureStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ime_power_measure
        fields = ()

    def to_representation(self, instance):
        return Ime_power_measureRetrieveSerializer(instance).data


class InstallationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Installation
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')

    address = serializers.SerializerMethodField()

    def get_address(self, obj):
        "obj is a Member instance. Returns list of dicts"""
        qset = models.Address.objects.filter(installation=obj).first()
        return AddressRetrieveSerializer(qset).data

    customer = serializers.SerializerMethodField()

    def get_customer(self, obj):
        "obj is a Member instance. Returns list of dicts"""
        q = models.Customer.objects.filter(installation=obj).first()
        return CustomerRetrieveSerializer(q).data


class InstallationRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Installation
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class InstallationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Installation
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class InstallationPartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Installation
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class InstallationSetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Installation
        fields = ('status',)

    def update(self, instance, validated_data):
        instance.status = validated_data['status']
        instance.save()
        return instance

    def to_representation(self, instance):
        return InstallationRetrieveSerializer(instance).data


class InstallationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Installation
        fields = ()

    def to_representation(self, instance):
        return InstallationRetrieveSerializer(instance).data

class Light_fixtureListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_fixture
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Light_fixtureRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_fixture
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Light_fixtureCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_fixture
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Light_fixturePartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_fixture
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Light_fixtureSetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_fixture
        fields = ('status',)

    def update(self, instance, validated_data):
        instance.status = validated_data['status']
        instance.save()
        return instance

    def to_representation(self, instance):
        return Light_fixtureRetrieveSerializer(instance).data


class Light_fixtureStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_fixture
        fields = ()

    def to_representation(self, instance):
        return Light_fixtureRetrieveSerializer(instance).data

class Light_management_measureListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_management_measure
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Light_management_measureRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_management_measure
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Light_management_measureCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_management_measure
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Light_management_measurePartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_management_measure
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Light_management_measureSetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_management_measure
        fields = ('status',)

    def update(self, instance, validated_data):
        instance.status = validated_data['status']
        instance.save()
        return instance

    def to_representation(self, instance):
        return Light_management_measureRetrieveSerializer(instance).data


class Light_management_measureStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_management_measure
        fields = ()

    def to_representation(self, instance):
        return Light_management_measureRetrieveSerializer(instance).data


class Light_management_moduleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_management_module
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Light_management_moduleRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_management_module
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Light_management_moduleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_management_module
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Light_management_modulePartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_management_module
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Light_management_moduleSetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_management_module
        fields = ('status',)

    def update(self, instance, validated_data):
        instance.status = validated_data['status']
        instance.save()
        return instance

    def to_representation(self, instance):
        return Light_management_moduleRetrieveSerializer(instance).data


class Light_management_moduleStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_management_module
        fields = ()

    def to_representation(self, instance):
        return Light_management_moduleRetrieveSerializer(instance).data


class Light_profileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_profile
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Light_profileRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_profile
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Light_profileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_profile
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Light_profilePartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_profile
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Light_profileSetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_profile
        fields = ('status',)

    def update(self, instance, validated_data):
        instance.status = validated_data['status']
        instance.save()
        return instance

    def to_representation(self, instance):
        return Light_profileRetrieveSerializer(instance).data


class Light_profileStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_profile
        fields = ()

    def to_representation(self, instance):
        return Light_profileRetrieveSerializer(instance).data


class Light_profile_slotListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_profile_slot
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Light_profile_slotRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_profile_slot
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Light_profile_slotCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_profile_slot
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Light_profile_slotPartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_profile_slot
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Light_profile_slotSetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_profile_slot
        fields = ('status',)

    def update(self, instance, validated_data):
        instance.status = validated_data['status']
        instance.save()
        return instance

    def to_representation(self, instance):
        return Light_profile_slotRetrieveSerializer(instance).data


class Light_profile_slotStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_profile_slot
        fields = ()

    def to_representation(self, instance):
        return Light_profile_slotRetrieveSerializer(instance).data


class Motion_eventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Motion_event
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Motion_eventRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Motion_event
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Motion_eventCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Motion_event
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Motion_eventPartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Motion_event
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Motion_eventSetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Motion_event
        fields = ('status',)

    def update(self, instance, validated_data):
        instance.status = validated_data['status']
        instance.save()
        return instance

    def to_representation(self, instance):
        return Motion_eventRetrieveSerializer(instance).data


class Motion_eventStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Motion_event
        fields = ()

    def to_representation(self, instance):
        return Motion_eventRetrieveSerializer(instance).data


class NodeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Node
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class NodeRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Node
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class NodeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Node
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class NodePartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Node
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class NodeSetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Node
        fields = ('status',)

    def update(self, instance, validated_data):
        instance.status = validated_data['status']
        instance.save()
        return instance

    def to_representation(self, instance):
        return NodeRetrieveSerializer(instance).data


class NodeStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Node
        fields = ()

    def to_representation(self, instance):
        return NodeRetrieveSerializer(instance).data


# class Node_moduleListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Node_module
#         exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')
#
#
# class Node_moduleRetrieveSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Node_module
#         exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')
#
#
# class Node_moduleCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Node_module
#         exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')
#
#
# class Node_modulePartialUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Node_module
#         exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')
#
#
# class Node_moduleSetStatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Node_module
#         fields = ('status',)
#
#     def update(self, instance, validated_data):
#         instance.status = validated_data['status']
#         instance.save()
#         return instance
#
#     def to_representation(self, instance):
#         return Node_moduleRetrieveSerializer(instance).data
#
#
# class Node_moduleStatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Node_module
#         fields = ()
#
#     def to_representation(self, instance):
#         return Node_moduleRetrieveSerializer(instance).data


class Wilamp_alertListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Wilamp_alert
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Wilamp_alertRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Wilamp_alert
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Wilamp_alertCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Wilamp_alert
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Wilamp_alertPartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Wilamp_alert
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Wilamp_alertSetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Wilamp_alert
        fields = ('status',)

    def update(self, instance, validated_data):
        instance.status = validated_data['status']
        instance.save()
        return instance

    def to_representation(self, instance):
        return Wilamp_alertRetrieveSerializer(instance).data


class Wilamp_alertStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Wilamp_alert
        fields = ()

    def to_representation(self, instance):
        return Wilamp_alertRetrieveSerializer(instance).data


class Feeder_pillarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Feeder_pillar
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Feeder_pillarRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Feeder_pillar
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Feeder_pillarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Feeder_pillar
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Feeder_pillarPartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Feeder_pillar
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Feeder_pillarSetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Feeder_pillar
        fields = ('status',)

    def update(self, instance, validated_data):
        instance.status = validated_data['status']
        instance.save()
        return instance

    def to_representation(self, instance):
        return Feeder_pillarRetrieveSerializer(instance).data


class Feeder_pillarStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Feeder_pillar
        fields = ()

    def to_representation(self, instance):
        return Feeder_pillarRetrieveSerializer(instance).data


class Twilight_management_moduleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Twilight_management_module
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Twilight_management_moduleRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Twilight_management_module
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Twilight_management_moduleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Twilight_management_module
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Twilight_management_modulePartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Twilight_management_module
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Twilight_management_moduleSetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Twilight_management_module
        fields = ('status',)

    def update(self, instance, validated_data):
        instance.status = validated_data['status']
        instance.save()
        return instance

    def to_representation(self, instance):
        return Twilight_management_moduleRetrieveSerializer(instance).data


class Twilight_management_moduleStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Twilight_management_module
        fields = ()

    def to_representation(self, instance):
        return Twilight_management_moduleRetrieveSerializer(instance).data


class Twilight_measureListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Twilight_measure
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Twilight_measureRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Twilight_measure
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Twilight_measureCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Twilight_measure
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Twilight_measurePartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Twilight_measure
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Twilight_measureSetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Twilight_measure
        fields = ('status',)

    def update(self, instance, validated_data):
        instance.status = validated_data['status']
        instance.save()
        return instance

    def to_representation(self, instance):
        return Twilight_measureRetrieveSerializer(instance).data


class Twilight_measureStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Twilight_measure
        fields = ()

    def to_representation(self, instance):
        return Twilight_measureRetrieveSerializer(instance).data


class Motion_management_moduleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Motion_management_module
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Motion_management_moduleRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Motion_management_module
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Motion_management_moduleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Motion_management_module
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Motion_management_modulePartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Motion_management_module
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Motion_management_moduleSetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Motion_management_module
        fields = ('status',)

    def update(self, instance, validated_data):
        instance.status = validated_data['status']
        instance.save()
        return instance

    def to_representation(self, instance):
        return Motion_management_moduleRetrieveSerializer(instance).data


class Motion_management_moduleStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Motion_management_module
        fields = ()

    def to_representation(self, instance):
        return Motion_management_moduleRetrieveSerializer(instance).data

class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


#    _____ _        _   _     _   _
#   / ____| |      | | (_)   | | (_)
#  | (___ | |_ __ _| |_ _ ___| |_ _  ___ ___
#   \___ \| __/ _` | __| / __| __| |/ __/ __|
#   ____) | || (_| | |_| \__ \ |_| | (__\__ \
#  |_____/ \__\__,_|\__|_|___/\__|_|\___|___/
#

class IntervalEnergyStatisticsSerializer(serializers.Serializer):
    startIntervalTimestamp = serializers.DateTimeField()
    endIntervalTimestamp = serializers.DateTimeField()
    sumEnergy = serializers.FloatField()
    sumEnergyWithoutDim = serializers.FloatField()
    sumEnergyWithoutControl = serializers.FloatField()
    sumEnergyOldLamps = serializers.FloatField()
    lastMeasureIntervalTimestamp = serializers.DateTimeField()

    def create(self, validated_data):
        return IntervalEnergyStatistics(**validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance


class AbsorbedPowerEstimationSerializer(serializers.Serializer):
    countMeasures = serializers.IntegerField()
    startIntervalTimestamp = serializers.DateTimeField()
    endIntervalTimestamp = serializers.DateTimeField()
    avgDimLevel = serializers.FloatField()
    avgAdc0Value = serializers.FloatField()
    avgAdc1Value = serializers.FloatField()
    sumActivePower = serializers.FloatField()
    sumEnergy = serializers.FloatField()
    sumEnergyWithoutDim = serializers.FloatField()
    sumEnergyWithoutControl = serializers.FloatField()
    sumEnergyOldLamps = serializers.FloatField()
    lastMeasureIntervalTimestamp = serializers.DateTimeField()

    def create(self, validated_data):
        return AbsorbedPowerEstimation(**validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance


class WeeklyEnergyStatisticsSerializer(serializers.Serializer):
    year = serializers.IntegerField()
    weekNumber = serializers.IntegerField()
    dayOfWeek = serializers.IntegerField()
    hour = serializers.IntegerField()
    activePowerAverage = serializers.FloatField()
    reactivePowerAverage = serializers.FloatField()
    activeEnergySum = serializers.FloatField()
    reactiveEnergySum = serializers.FloatField()
    activeEnergyWithoutDimSum = serializers.FloatField()
    activeEnergyWithoutControlSum = serializers.FloatField()
    activeEnergyOldLampsSum = serializers.FloatField()
    burningTimeAverage = serializers.FloatField()
    nodeLifeAverage = serializers.FloatField()

    def create(self, validated_data):
        return WeeklyEnergyStatistics(**validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance


class MonthlyEnergyStatisticsSerializer(serializers.Serializer):
    year = serializers.IntegerField()
    month = serializers.IntegerField()
    day = serializers.IntegerField()
    activePowerAverage = serializers.FloatField()
    reactivePowerAverage = serializers.FloatField()
    activeEnergySum = serializers.FloatField()
    reactiveEnergySum = serializers.FloatField()
    activeEnergyWithoutDimSum = serializers.FloatField()
    activeEnergyWithoutControlSum = serializers.FloatField()
    activeEnergyOldLampsSum = serializers.FloatField()
    burningTimeAverage = serializers.FloatField()
    nodeLifeAverage = serializers.FloatField()

    def create(self, validated_data):
        return MonthlyEnergyStatistics(**validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance


class InstallationGlobalStatisticsSerializer(serializers.Serializer):
    byWeek = WeeklyEnergyStatisticsSerializer(many=True)
    byMonth = MonthlyEnergyStatisticsSerializer(many=True)
    globalEnergyConsumption = IntervalEnergyStatisticsSerializer()
    currentIntervalEnergyConsumption = IntervalEnergyStatisticsSerializer()
    absorbedPowerEstimation =  AbsorbedPowerEstimationSerializer()

    def create(self, validated_data):
        result = InstallationGlobalStatistics(**validated_data)
        if 'byWeek' in validated_data.keys():
            byWeekSerializer = WeeklyEnergyStatisticsSerializer(data=validated_data['byWeek'], many=True)
            if byWeekSerializer.is_valid():
                result.byWeek = byWeekSerializer.save()
        if 'byMonth' in validated_data.keys():
            byMonthSerializer = MonthlyEnergyStatisticsSerializer(data=validated_data['byMonth'], many=True)
            if byMonthSerializer.is_valid():
                result.byMonth = byMonthSerializer.save()
        return result

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance


#   ______ _           _   _                                _
#  |  ____| |         | | (_)                              | |
#  | |__  | | __ _ ___| |_ _  ___   ___  ___  __ _ _ __ ___| |__
#  |  __| | |/ _` / __| __| |/ __| / __|/ _ \/ _` | '__/ __| '_ \
#  | |____| | (_| \__ \ |_| | (__  \__ \  __/ (_| | | | (__| | | |
#  |______|_|\__,_|___/\__|_|\___| |___/\___|\__,_|_|  \___|_| |_|
#
# Elastic search serializers
from ..documents import InstallationDocument, GatewayDocument, NodeDocument

class InstallationDocumentSerializer(DocumentSerializer):
    """Serializer for the Book document."""

    class Meta(object):
        """Meta options."""

        # Specify the correspondent document class
        document = InstallationDocument

        # List the serializer fields. Note, that the order of the fields
        # is preserved in the ViewSet.
        fields = (
            'id',
            'name',
            'description',
            'notes',
        )

class GatewayDocumentSerializer(DocumentSerializer):
    """Serializer for the Book document."""

    class Meta(object):
        """Meta options."""

        # Specify the correspondent document class
        document = GatewayDocument

        # List the serializer fields. Note, that the order of the fields
        # is preserved in the ViewSet.
        fields = (
            'id',
            'name',
            'description',
            'notes',
        )


class NodeDocumentSerializer(DocumentSerializer):
    """Serializer for the Book document."""

    class Meta(object):
        """Meta options."""

        # Specify the correspondent document class
        document = NodeDocument

        # List the serializer fields. Note, that the order of the fields
        # is preserved in the ViewSet.
        fields = (
            'id',
            'name',
            'description',
            'notes',
        )
