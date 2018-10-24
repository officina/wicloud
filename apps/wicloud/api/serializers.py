# -*- coding: utf-8 -*-

from rest_framework import serializers

from apps.wicloud.models import Address
from .. import models
from rest_framework import serializers
from rest_framework.serializers import  ModelSerializer



class AddressListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = '__all__'


class AddressRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = '__all__'


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


class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = '__all__'


class CustomerRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = '__all__'


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
        fields = '__all__'


class Energy_intervalRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Energy_interval
        fields = '__all__'


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
        fields = '__all__'


class Energy_meter_moduleRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Energy_meter_module
        fields = '__all__'


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
        fields = '__all__'


class Energy_meter_peak_measureRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Energy_meter_peak_measure
        fields = '__all__'


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
        fields = '__all__'


class Error_light_level_and_adc_mismatchRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Error_light_level_and_adc_mismatch
        fields = '__all__'


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
        fields = '__all__'


class Error_light_level_and_power_mismatchRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Error_light_level_and_power_mismatch
        fields = '__all__'


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
        fields = '__all__'


class Error_node_offlineRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Error_node_offline
        fields = '__all__'


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
        fields = '__all__'


class GatewayRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gateway
        fields = '__all__'


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
        fields = '__all__'


class Ime_power_counterRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ime_power_counter
        fields = '__all__'


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
        fields = '__all__'


class Ime_power_measureRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ime_power_measure
        fields = '__all__'


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
        fields = '__all__'

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
        fields = '__all__'


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


class Light_management_measureListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_management_measure
        fields = '__all__'


class Light_management_measureRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_management_measure
        fields = '__all__'


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
        fields = '__all__'


class Light_management_moduleRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_management_module
        fields = '__all__'


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
        fields = '__all__'


class Light_profileRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_profile
        fields = '__all__'


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
        fields = '__all__'


class Light_profile_slotRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Light_profile_slot
        fields = '__all__'


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
        fields = '__all__'


class Motion_eventRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Motion_event
        fields = '__all__'


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
        fields = '__all__'


class NodeRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Node
        fields = '__all__'


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


class Node_moduleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Node_module
        fields = '__all__'


class Node_moduleRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Node_module
        fields = '__all__'


class Node_moduleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Node_module
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Node_modulePartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Node_module
        exclude = ('created_date', 'last_modified_date', 'creator', 'last_modifier')


class Node_moduleSetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Node_module
        fields = ('status',)

    def update(self, instance, validated_data):
        instance.status = validated_data['status']
        instance.save()
        return instance

    def to_representation(self, instance):
        return Node_moduleRetrieveSerializer(instance).data


class Node_moduleStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Node_module
        fields = ()

    def to_representation(self, instance):
        return Node_moduleRetrieveSerializer(instance).data


class Wilamp_alertListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Wilamp_alert
        fields = '__all__'


class Wilamp_alertRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Wilamp_alert
        fields = '__all__'


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
        fields = '__all__'


class Feeder_pillarRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Feeder_pillar
        fields = '__all__'


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
        fields = '__all__'


class Twilight_management_moduleRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Twilight_management_module
        fields = '__all__'


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
        fields = '__all__'


class Twilight_measureRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Twilight_measure
        fields = '__all__'


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
        fields = '__all__'


class Motion_management_moduleRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Motion_management_module
        fields = '__all__'


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