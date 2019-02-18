# -*- coding: utf-8 -*-

from import_export import resources

from . import models


class AddressResource(resources.ModelResource):
    class Meta:
        model = models.Address
        exclude = ('id', 'creator', 'created_date', 'last_modifier', 'last_modified_date')
        import_id_fields = ('id',)

    def before_import(self, dataset, dry_run, *args, **kwargs):
        self.user = kwargs.get('user')
        return super().before_import(dataset, dry_run, *args, **kwargs)

    def before_save_instance(self, instance, using_transactions, dry_run):
        self.user
        if not instance.id:
            instance.creator = self.user
        instance.last_modifier = self.user

class Connected_deviceResource(resources.ModelResource):
    class Meta:
        model = models.Connected_device
        exclude = ('id', 'creator', 'created_date', 'last_modifier', 'last_modified_date')
        import_id_fields = ('id',)

    def before_import(self, dataset, dry_run, *args, **kwargs):
        self.user = kwargs.get('user')
        return super().before_import(dataset, dry_run, *args, **kwargs)

    def before_save_instance(self, instance, using_transactions, dry_run):
        self.user
        if not instance.id:
            instance.creator = self.user
        instance.last_modifier = self.user

class CustomerResource(resources.ModelResource):
    class Meta:
        model = models.Customer
        exclude = ('id', 'creator', 'created_date', 'last_modifier', 'last_modified_date')
        import_id_fields = ('id',)

    def before_import(self, dataset, dry_run, *args, **kwargs):
        self.user = kwargs.get('user')
        return super().before_import(dataset, dry_run, *args, **kwargs)

    def before_save_instance(self, instance, using_transactions, dry_run):
        self.user
        if not instance.id:
            instance.creator = self.user
        instance.last_modifier = self.user


class Energy_intervalResource(resources.ModelResource):
    class Meta:
        model = models.Energy_interval
        exclude = ('id', 'creator', 'created_date', 'last_modifier', 'last_modified_date')
        import_id_fields = ('id',)

    def before_import(self, dataset, dry_run, *args, **kwargs):
        self.user = kwargs.get('user')
        return super().before_import(dataset, dry_run, *args, **kwargs)

    def before_save_instance(self, instance, using_transactions, dry_run):
        self.user
        if not instance.id:
            instance.creator = self.user
        instance.last_modifier = self.user


class Energy_meter_moduleResource(resources.ModelResource):
    class Meta:
        model = models.Energy_meter_module
        exclude = ('id', 'creator', 'created_date', 'last_modifier', 'last_modified_date')
        import_id_fields = ('id',)

    def before_import(self, dataset, dry_run, *args, **kwargs):
        self.user = kwargs.get('user')
        return super().before_import(dataset, dry_run, *args, **kwargs)

    def before_save_instance(self, instance, using_transactions, dry_run):
        self.user
        if not instance.id:
            instance.creator = self.user
        instance.last_modifier = self.user


class Energy_meter_peak_measureResource(resources.ModelResource):
    class Meta:
        model = models.Energy_meter_peak_measure
        exclude = ('id', 'creator', 'created_date', 'last_modifier', 'last_modified_date')
        import_id_fields = ('id',)

    def before_import(self, dataset, dry_run, *args, **kwargs):
        self.user = kwargs.get('user')
        return super().before_import(dataset, dry_run, *args, **kwargs)

    def before_save_instance(self, instance, using_transactions, dry_run):
        self.user
        if not instance.id:
            instance.creator = self.user
        instance.last_modifier = self.user


class Error_light_level_and_adc_mismatchResource(resources.ModelResource):
    class Meta:
        model = models.Error_light_level_and_adc_mismatch
        exclude = ('id', 'creator', 'created_date', 'last_modifier', 'last_modified_date')
        import_id_fields = ('id',)

    def before_import(self, dataset, dry_run, *args, **kwargs):
        self.user = kwargs.get('user')
        return super().before_import(dataset, dry_run, *args, **kwargs)

    def before_save_instance(self, instance, using_transactions, dry_run):
        self.user
        if not instance.id:
            instance.creator = self.user
        instance.last_modifier = self.user


class Error_light_level_and_power_mismatchResource(resources.ModelResource):
    class Meta:
        model = models.Error_light_level_and_power_mismatch
        exclude = ('id', 'creator', 'created_date', 'last_modifier', 'last_modified_date')
        import_id_fields = ('id',)

    def before_import(self, dataset, dry_run, *args, **kwargs):
        self.user = kwargs.get('user')
        return super().before_import(dataset, dry_run, *args, **kwargs)

    def before_save_instance(self, instance, using_transactions, dry_run):
        self.user
        if not instance.id:
            instance.creator = self.user
        instance.last_modifier = self.user


class Error_node_offlineResource(resources.ModelResource):
    class Meta:
        model = models.Error_node_offline
        exclude = ('id', 'creator', 'created_date', 'last_modifier', 'last_modified_date')
        import_id_fields = ('id',)

    def before_import(self, dataset, dry_run, *args, **kwargs):
        self.user = kwargs.get('user')
        return super().before_import(dataset, dry_run, *args, **kwargs)

    def before_save_instance(self, instance, using_transactions, dry_run):
        self.user
        if not instance.id:
            instance.creator = self.user
        instance.last_modifier = self.user


class GatewayResource(resources.ModelResource):
    class Meta:
        model = models.Gateway
        exclude = ('id', 'creator', 'created_date', 'last_modifier', 'last_modified_date')
        import_id_fields = ('id',)

    def before_import(self, dataset, dry_run, *args, **kwargs):
        self.user = kwargs.get('user')
        return super().before_import(dataset, dry_run, *args, **kwargs)

    def before_save_instance(self, instance, using_transactions, dry_run):
        self.user
        if not instance.id:
            instance.creator = self.user
        instance.last_modifier = self.user


class Ime_power_counterResource(resources.ModelResource):
    class Meta:
        model = models.Ime_power_counter
        exclude = ('id', 'creator', 'created_date', 'last_modifier', 'last_modified_date')
        import_id_fields = ('id',)

    def before_import(self, dataset, dry_run, *args, **kwargs):
        self.user = kwargs.get('user')
        return super().before_import(dataset, dry_run, *args, **kwargs)

    def before_save_instance(self, instance, using_transactions, dry_run):
        self.user
        if not instance.id:
            instance.creator = self.user
        instance.last_modifier = self.user


class Ime_power_measureResource(resources.ModelResource):
    class Meta:
        model = models.Ime_power_measure
        exclude = ('id', 'creator', 'created_date', 'last_modifier', 'last_modified_date')
        import_id_fields = ('id',)

    def before_import(self, dataset, dry_run, *args, **kwargs):
        self.user = kwargs.get('user')
        return super().before_import(dataset, dry_run, *args, **kwargs)

    def before_save_instance(self, instance, using_transactions, dry_run):
        self.user
        if not instance.id:
            instance.creator = self.user
        instance.last_modifier = self.user


class InstallationResource(resources.ModelResource):
    class Meta:
        model = models.Installation
        exclude = ('id', 'creator', 'created_date', 'last_modifier', 'last_modified_date')
        import_id_fields = ('id',)

    def before_import(self, dataset, dry_run, *args, **kwargs):
        self.user = kwargs.get('user')
        return super().before_import(dataset, dry_run, *args, **kwargs)

    def before_save_instance(self, instance, using_transactions, dry_run):
        self.user
        if not instance.id:
            instance.creator = self.user
        instance.last_modifier = self.user


class Light_fixtureResource(resources.ModelResource):
    class Meta:
        model = models.Light_fixture
        exclude = ('id', 'creator', 'created_date', 'last_modifier', 'last_modified_date')
        import_id_fields = ('id',)

    def before_import(self, dataset, dry_run, *args, **kwargs):
        self.user = kwargs.get('user')
        return super().before_import(dataset, dry_run, *args, **kwargs)

    def before_save_instance(self, instance, using_transactions, dry_run):
        self.user
        if not instance.id:
            instance.creator = self.user
        instance.last_modifier = self.user


class Light_management_measureResource(resources.ModelResource):
    class Meta:
        model = models.Light_management_measure
        exclude = ('id', 'creator', 'created_date', 'last_modifier', 'last_modified_date')
        import_id_fields = ('id',)

    def before_import(self, dataset, dry_run, *args, **kwargs):
        self.user = kwargs.get('user')
        return super().before_import(dataset, dry_run, *args, **kwargs)

    def before_save_instance(self, instance, using_transactions, dry_run):
        self.user
        if not instance.id:
            instance.creator = self.user
        instance.last_modifier = self.user


class Light_management_moduleResource(resources.ModelResource):
    class Meta:
        model = models.Light_management_module
        exclude = ('id', 'creator', 'created_date', 'last_modifier', 'last_modified_date')
        import_id_fields = ('id',)

    def before_import(self, dataset, dry_run, *args, **kwargs):
        self.user = kwargs.get('user')
        return super().before_import(dataset, dry_run, *args, **kwargs)

    def before_save_instance(self, instance, using_transactions, dry_run):
        self.user
        if not instance.id:
            instance.creator = self.user
        instance.last_modifier = self.user


class Light_profileResource(resources.ModelResource):
    class Meta:
        model = models.Light_profile
        exclude = ('id', 'creator', 'created_date', 'last_modifier', 'last_modified_date')
        import_id_fields = ('id',)

    def before_import(self, dataset, dry_run, *args, **kwargs):
        self.user = kwargs.get('user')
        return super().before_import(dataset, dry_run, *args, **kwargs)

    def before_save_instance(self, instance, using_transactions, dry_run):
        self.user
        if not instance.id:
            instance.creator = self.user
        instance.last_modifier = self.user


class Light_profile_slotResource(resources.ModelResource):
    class Meta:
        model = models.Light_profile_slot
        exclude = ('id', 'creator', 'created_date', 'last_modifier', 'last_modified_date')
        import_id_fields = ('id',)

    def before_import(self, dataset, dry_run, *args, **kwargs):
        self.user = kwargs.get('user')
        return super().before_import(dataset, dry_run, *args, **kwargs)

    def before_save_instance(self, instance, using_transactions, dry_run):
        self.user
        if not instance.id:
            instance.creator = self.user
        instance.last_modifier = self.user


class Motion_eventResource(resources.ModelResource):
    class Meta:
        model = models.Motion_event
        exclude = ('id', 'creator', 'created_date', 'last_modifier', 'last_modified_date')
        import_id_fields = ('id',)

    def before_import(self, dataset, dry_run, *args, **kwargs):
        self.user = kwargs.get('user')
        return super().before_import(dataset, dry_run, *args, **kwargs)

    def before_save_instance(self, instance, using_transactions, dry_run):
        self.user
        if not instance.id:
            instance.creator = self.user
        instance.last_modifier = self.user


class NodeResource(resources.ModelResource):
    class Meta:
        model = models.Node
        exclude = ('id', 'creator', 'created_date', 'last_modifier', 'last_modified_date')
        import_id_fields = ('id',)

    def before_import(self, dataset, dry_run, *args, **kwargs):
        self.user = kwargs.get('user')
        return super().before_import(dataset, dry_run, *args, **kwargs)

    def before_save_instance(self, instance, using_transactions, dry_run):
        self.user
        if not instance.id:
            instance.creator = self.user
        instance.last_modifier = self.user


# class Node_moduleResource(resources.ModelResource):
#     class Meta:
#         model = models.Node_module
#         exclude = ('id', 'creator', 'created_date', 'last_modifier', 'last_modified_date')
#         import_id_fields = ('id',)
#
#     def before_import(self, dataset, dry_run, *args, **kwargs):
#         self.user = kwargs.get('user')
#         return super().before_import(dataset, dry_run, *args, **kwargs)
#
#     def before_save_instance(self, instance, using_transactions, dry_run):
#         self.user
#         if not instance.id:
#             instance.creator = self.user
#         instance.last_modifier = self.user


class Wilamp_alertResource(resources.ModelResource):
    class Meta:
        model = models.Wilamp_alert
        exclude = ('id', 'creator', 'created_date', 'last_modifier', 'last_modified_date')
        import_id_fields = ('id',)

    def before_import(self, dataset, dry_run, *args, **kwargs):
        self.user = kwargs.get('user')
        return super().before_import(dataset, dry_run, *args, **kwargs)

    def before_save_instance(self, instance, using_transactions, dry_run):
        self.user
        if not instance.id:
            instance.creator = self.user
        instance.last_modifier = self.user


class Feeder_pillarResource(resources.ModelResource):
    class Meta:
        model = models.Feeder_pillar
        exclude = ('id', 'creator', 'created_date', 'last_modifier', 'last_modified_date')
        import_id_fields = ('id',)

    def before_import(self, dataset, dry_run, *args, **kwargs):
        self.user = kwargs.get('user')
        return super().before_import(dataset, dry_run, *args, **kwargs)

    def before_save_instance(self, instance, using_transactions, dry_run):
        self.user
        if not instance.id:
            instance.creator = self.user
        instance.last_modifier = self.user


class Twilight_management_moduleResource(resources.ModelResource):
    class Meta:
        model = models.Twilight_management_module
        exclude = ('id', 'creator', 'created_date', 'last_modifier', 'last_modified_date')
        import_id_fields = ('id',)

    def before_import(self, dataset, dry_run, *args, **kwargs):
        self.user = kwargs.get('user')
        return super().before_import(dataset, dry_run, *args, **kwargs)

    def before_save_instance(self, instance, using_transactions, dry_run):
        self.user
        if not instance.id:
            instance.creator = self.user
        instance.last_modifier = self.user


class Twilight_measureResource(resources.ModelResource):
    class Meta:
        model = models.Twilight_measure
        exclude = ('id', 'creator', 'created_date', 'last_modifier', 'last_modified_date')
        import_id_fields = ('id',)

    def before_import(self, dataset, dry_run, *args, **kwargs):
        self.user = kwargs.get('user')
        return super().before_import(dataset, dry_run, *args, **kwargs)

    def before_save_instance(self, instance, using_transactions, dry_run):
        self.user
        if not instance.id:
            instance.creator = self.user
        instance.last_modifier = self.user


class Motion_management_moduleResource(resources.ModelResource):
    class Meta:
        model = models.Motion_management_module
        exclude = ('id', 'creator', 'created_date', 'last_modifier', 'last_modified_date')
        import_id_fields = ('id',)

    def before_import(self, dataset, dry_run, *args, **kwargs):
        self.user = kwargs.get('user')
        return super().before_import(dataset, dry_run, *args, **kwargs)

    def before_save_instance(self, instance, using_transactions, dry_run):
        self.user
        if not instance.id:
            instance.creator = self.user
        instance.last_modifier = self.user



