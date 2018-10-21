# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from import_export import admin as import_export_admin
from import_export import formats as import_export_admin_formats
from web.core.admin import UserAdminMixin
from . import models
from . import resources


class AddressAdmin(UserAdminMixin, import_export_admin.ImportExportModelAdmin):
    resource_class = resources.AddressResource
    formats = (
        import_export_admin_formats.base_formats.XLS,
        import_export_admin_formats.base_formats.CSV,
        import_export_admin_formats.base_formats.JSON,
    )

    # fieldsets = (
    #     (_('general information'), {
    #        'fields': ()
    #     }),
    #
    #     (_('visualization admin'), {
    #         'classes': ('collapse',),
    #         'fields': ('ordering', 'status')
    #     }),
    #     (_('logs admin'), {
    #         'classes': ('collapse',),
    #         'fields': ('creator', 'created_date', 'last_modifier', 'last_modified_date')
    #     }),
    # )
    list_display = ('id', 'full_name','description', 'city', 'country', 'lat', 'lng', 'installation')
    readonly_fields = ('creator', 'created_date', 'last_modifier', 'last_modified_date')


admin.site.register(models.Address, AddressAdmin)


class CustomerAdmin(UserAdminMixin, import_export_admin.ImportExportModelAdmin):
    resource_class = resources.CustomerResource
    formats = (
        import_export_admin_formats.base_formats.XLS,
        import_export_admin_formats.base_formats.CSV,
        import_export_admin_formats.base_formats.JSON,
    )

    # fieldsets = (
    #     # (_('general information'), {
    #     #    'fields': ()
    #     # }),
    #     (_('visualization admin'), {
    #         'classes': ('collapse',),
    #         'fields': ('ordering', 'status')
    #     }),
    #     (_('logs admin'), {
    #         'classes': ('collapse',),
    #         'fields': ('creator', 'created_date', 'last_modifier', 'last_modified_date')
    #     }),
    # )
    list_display = ('id', 'company_name', 'description')
    readonly_fields = ('creator', 'created_date', 'last_modifier', 'last_modified_date')


admin.site.register(models.Customer, CustomerAdmin)


class Energy_intervalAdmin(UserAdminMixin, import_export_admin.ImportExportModelAdmin):
    resource_class = resources.Energy_intervalResource
    formats = (
        import_export_admin_formats.base_formats.XLS,
        import_export_admin_formats.base_formats.CSV,
        import_export_admin_formats.base_formats.JSON,
    )

    # fieldsets = (
    #     # (_('general information'), {
    #     #    'fields': ()
    #     # }),
    #     (_('visualization admin'), {
    #         'classes': ('collapse',),
    #         'fields': ('ordering', 'status')
    #     }),
    #     (_('logs admin'), {
    #         'classes': ('collapse',),
    #         'fields': ('creator', 'created_date', 'last_modifier', 'last_modified_date')
    #     }),
    # )
    list_display = ('id', 'mac', 'installation')
    readonly_fields = ('creator', 'created_date', 'last_modifier', 'last_modified_date')


admin.site.register(models.Energy_interval, Energy_intervalAdmin)


class Energy_meter_moduleAdmin(UserAdminMixin, import_export_admin.ImportExportModelAdmin):
    resource_class = resources.Energy_meter_moduleResource
    formats = (
        import_export_admin_formats.base_formats.XLS,
        import_export_admin_formats.base_formats.CSV,
        import_export_admin_formats.base_formats.JSON,
    )

    # fieldsets = (
    #     # (_('general information'), {
    #     #    'fields': ()
    #     # }),
    #     (_('visualization admin'), {
    #         'classes': ('collapse',),
    #         'fields': ('ordering', 'status')
    #     }),
    #     (_('logs admin'), {
    #         'classes': ('collapse',),
    #         'fields': ('creator', 'created_date', 'last_modifier', 'last_modified_date')
    #     }),
    # )
    list_display = ('get_status_display', 'ordering')
    readonly_fields = ('creator', 'created_date', 'last_modifier', 'last_modified_date')


admin.site.register(models.Energy_meter_module, Energy_meter_moduleAdmin)


class Energy_meter_peak_measureAdmin(UserAdminMixin, import_export_admin.ImportExportModelAdmin):
    resource_class = resources.Energy_meter_peak_measureResource
    formats = (
        import_export_admin_formats.base_formats.XLS,
        import_export_admin_formats.base_formats.CSV,
        import_export_admin_formats.base_formats.JSON,
    )

    # fieldsets = (
    #     # (_('general information'), {
    #     #    'fields': ()
    #     # }),
    #     (_('visualization admin'), {
    #         'classes': ('collapse',),
    #         'fields': ('ordering', 'status')
    #     }),
    #     (_('logs admin'), {
    #         'classes': ('collapse',),
    #         'fields': ('creator', 'created_date', 'last_modifier', 'last_modified_date')
    #     }),
    # )
    list_display = ('get_status_display', 'ordering')
    readonly_fields = ('creator', 'created_date', 'last_modifier', 'last_modified_date')


admin.site.register(models.Energy_meter_peak_measure, Energy_meter_peak_measureAdmin)


class Error_light_level_and_adc_mismatchAdmin(UserAdminMixin, import_export_admin.ImportExportModelAdmin):
    resource_class = resources.Error_light_level_and_adc_mismatchResource
    formats = (
        import_export_admin_formats.base_formats.XLS,
        import_export_admin_formats.base_formats.CSV,
        import_export_admin_formats.base_formats.JSON,
    )

    # fieldsets = (
    #     # (_('general information'), {
    #     #    'fields': ()
    #     # }),
    #     (_('visualization admin'), {
    #         'classes': ('collapse',),
    #         'fields': ('ordering', 'status')
    #     }),
    #     (_('logs admin'), {
    #         'classes': ('collapse',),
    #         'fields': ('creator', 'created_date', 'last_modifier', 'last_modified_date')
    #     }),
    # )
    list_display = ('get_status_display', 'ordering')
    readonly_fields = ('creator', 'created_date', 'last_modifier', 'last_modified_date')


admin.site.register(models.Error_light_level_and_adc_mismatch,
                    Error_light_level_and_adc_mismatchAdmin)


class Error_light_level_and_power_mismatchAdmin(UserAdminMixin, import_export_admin.ImportExportModelAdmin):
    resource_class = resources.Error_light_level_and_power_mismatchResource
    formats = (
        import_export_admin_formats.base_formats.XLS,
        import_export_admin_formats.base_formats.CSV,
        import_export_admin_formats.base_formats.JSON,
    )

    # fieldsets = (
    #     # (_('general information'), {
    #     #    'fields': ()
    #     # }),
    #     (_('visualization admin'), {
    #         'classes': ('collapse',),
    #         'fields': ('ordering', 'status')
    #     }),
    #     (_('logs admin'), {
    #         'classes': ('collapse',),
    #         'fields': ('creator', 'created_date', 'last_modifier', 'last_modified_date')
    #     }),
    # )
    list_display = ('get_status_display', 'ordering')
    readonly_fields = ('creator', 'created_date', 'last_modifier', 'last_modified_date')


admin.site.register(models.Error_light_level_and_power_mismatch, Error_light_level_and_power_mismatchAdmin)


class Error_node_offlineAdmin(UserAdminMixin, import_export_admin.ImportExportModelAdmin):
    resource_class = resources.Error_node_offlineResource
    formats = (
        import_export_admin_formats.base_formats.XLS,
        import_export_admin_formats.base_formats.CSV,
        import_export_admin_formats.base_formats.JSON,
    )

    # fieldsets = (
    #     # (_('general information'), {
    #     #    'fields': ()
    #     # }),
    #     (_('visualization admin'), {
    #         'classes': ('collapse',),
    #         'fields': ('ordering', 'status')
    #     }),
    #     (_('logs admin'), {
    #         'classes': ('collapse',),
    #         'fields': ('creator', 'created_date', 'last_modifier', 'last_modified_date')
    #     }),
    # )
    list_display = ('get_status_display', 'ordering')
    readonly_fields = ('creator', 'created_date', 'last_modifier', 'last_modified_date')


admin.site.register(models.Error_node_offline, Error_node_offlineAdmin)


class GatewayAdmin(UserAdminMixin, import_export_admin.ImportExportModelAdmin):
    resource_class = resources.GatewayResource
    formats = (
        import_export_admin_formats.base_formats.XLS,
        import_export_admin_formats.base_formats.CSV,
        import_export_admin_formats.base_formats.JSON,
    )

    # fieldsets = (
    #     # (_('general information'), {
    #     #    'fields': ()
    #     # }),
    #     (_('visualization admin'), {
    #         'classes': ('collapse',),
    #         'fields': ('ordering', 'status')
    #     }),
    #     (_('logs admin'), {
    #         'classes': ('collapse',),
    #         'fields': ('creator', 'created_date', 'last_modifier', 'last_modified_date')
    #     }),
    # )
    list_display = ('get_status_display', 'ordering')
    readonly_fields = ('creator', 'created_date', 'last_modifier', 'last_modified_date')


admin.site.register(models.Gateway, GatewayAdmin)


class Ime_power_counterAdmin(UserAdminMixin, import_export_admin.ImportExportModelAdmin):
    resource_class = resources.Ime_power_counterResource
    formats = (
        import_export_admin_formats.base_formats.XLS,
        import_export_admin_formats.base_formats.CSV,
        import_export_admin_formats.base_formats.JSON,
    )

    # fieldsets = (
    #     # (_('general information'), {
    #     #    'fields': ()
    #     # }),
    #     (_('visualization admin'), {
    #         'classes': ('collapse',),
    #         'fields': ('ordering', 'status')
    #     }),
    #     (_('logs admin'), {
    #         'classes': ('collapse',),
    #         'fields': ('creator', 'created_date', 'last_modifier', 'last_modified_date')
    #     }),
    # )
    list_display = ('get_status_display', 'ordering')
    readonly_fields = ('creator', 'created_date', 'last_modifier', 'last_modified_date')


admin.site.register(models.Ime_power_counter, Ime_power_counterAdmin)


class Ime_power_measureAdmin(UserAdminMixin, import_export_admin.ImportExportModelAdmin):
    resource_class = resources.Ime_power_measureResource
    formats = (
        import_export_admin_formats.base_formats.XLS,
        import_export_admin_formats.base_formats.CSV,
        import_export_admin_formats.base_formats.JSON,
    )

    fieldsets = (
        # (_('general information'), {
        #    'fields': ()
        # }),
        (_('visualization admin'), {
            'classes': ('collapse',),
            'fields': ('ordering', 'status')
        }),
        (_('logs admin'), {
            'classes': ('collapse',),
            'fields': ('creator', 'created_date', 'last_modifier', 'last_modified_date')
        }),
    )
    list_display = ('get_status_display', 'ordering')
    readonly_fields = ('creator', 'created_date', 'last_modifier', 'last_modified_date')


admin.site.register(models.Ime_power_measure, Ime_power_measureAdmin)


class InstallationAdmin(UserAdminMixin, import_export_admin.ImportExportModelAdmin):
    resource_class = resources.InstallationResource
    formats = (
        import_export_admin_formats.base_formats.XLS,
        import_export_admin_formats.base_formats.CSV,
        import_export_admin_formats.base_formats.JSON,
    )

    # fieldsets = (
    #     # (_('general information'), {
    #     #    'fields': ()
    #     # }),
    #     (_('visualization admin'), {
    #         'classes': ('collapse',),
    #         'fields': ('ordering', 'status')
    #     }),
    #     (_('logs admin'), {
    #         'classes': ('collapse',),
    #         'fields': ('creator', 'created_date', 'last_modifier', 'last_modified_date')
    #     }),
    # )
    list_display = ('id', 'name', 'description', 'customer', 'address')
    readonly_fields = ('creator', 'created_date', 'last_modifier', 'last_modified_date')


admin.site.register(models.Installation, InstallationAdmin)


class Light_management_measureAdmin(UserAdminMixin, import_export_admin.ImportExportModelAdmin):
    resource_class = resources.Light_management_measureResource
    formats = (
        import_export_admin_formats.base_formats.XLS,
        import_export_admin_formats.base_formats.CSV,
        import_export_admin_formats.base_formats.JSON,
    )

    fieldsets = (
        # (_('general information'), {
        #    'fields': ()
        # }),
        (_('visualization admin'), {
            'classes': ('collapse',),
            'fields': ('ordering', 'status')
        }),
        (_('logs admin'), {
            'classes': ('collapse',),
            'fields': ('creator', 'created_date', 'last_modifier', 'last_modified_date')
        }),
    )
    list_display = ('get_status_display', 'ordering')
    readonly_fields = ('creator', 'created_date', 'last_modifier', 'last_modified_date')


admin.site.register(models.Light_management_measure, Light_management_measureAdmin)


class Light_management_moduleAdmin(UserAdminMixin, import_export_admin.ImportExportModelAdmin):
    resource_class = resources.Light_management_moduleResource
    formats = (
        import_export_admin_formats.base_formats.XLS,
        import_export_admin_formats.base_formats.CSV,
        import_export_admin_formats.base_formats.JSON,
    )

    fieldsets = (
        # (_('general information'), {
        #    'fields': ()
        # }),
        (_('visualization admin'), {
            'classes': ('collapse',),
            'fields': ('ordering', 'status')
        }),
        (_('logs admin'), {
            'classes': ('collapse',),
            'fields': ('creator', 'created_date', 'last_modifier', 'last_modified_date')
        }),
    )
    list_display = ('get_status_display', 'ordering')
    readonly_fields = ('creator', 'created_date', 'last_modifier', 'last_modified_date')


admin.site.register(models.Light_management_module, Light_management_moduleAdmin)


class Light_profileAdmin(UserAdminMixin, import_export_admin.ImportExportModelAdmin):
    resource_class = resources.Light_profileResource
    formats = (
        import_export_admin_formats.base_formats.XLS,
        import_export_admin_formats.base_formats.CSV,
        import_export_admin_formats.base_formats.JSON,
    )

    fieldsets = (
        # (_('general information'), {
        #    'fields': ()
        # }),
        (_('visualization admin'), {
            'classes': ('collapse',),
            'fields': ('ordering', 'status')
        }),
        (_('logs admin'), {
            'classes': ('collapse',),
            'fields': ('creator', 'created_date', 'last_modifier', 'last_modified_date')
        }),
    )
    list_display = ('get_status_display', 'ordering')
    readonly_fields = ('creator', 'created_date', 'last_modifier', 'last_modified_date')


admin.site.register(models.Light_profile, Light_profileAdmin)


class Light_profile_slotAdmin(UserAdminMixin, import_export_admin.ImportExportModelAdmin):
    resource_class = resources.Light_profile_slotResource
    formats = (
        import_export_admin_formats.base_formats.XLS,
        import_export_admin_formats.base_formats.CSV,
        import_export_admin_formats.base_formats.JSON,
    )

    fieldsets = (
        # (_('general information'), {
        #    'fields': ()
        # }),
        (_('visualization admin'), {
            'classes': ('collapse',),
            'fields': ('ordering', 'status')
        }),
        (_('logs admin'), {
            'classes': ('collapse',),
            'fields': ('creator', 'created_date', 'last_modifier', 'last_modified_date')
        }),
    )
    list_display = ('get_status_display', 'ordering')
    readonly_fields = ('creator', 'created_date', 'last_modifier', 'last_modified_date')


admin.site.register(models.Light_profile_slot, Light_profile_slotAdmin)


class Motion_eventAdmin(UserAdminMixin, import_export_admin.ImportExportModelAdmin):
    resource_class = resources.Motion_eventResource
    formats = (
        import_export_admin_formats.base_formats.XLS,
        import_export_admin_formats.base_formats.CSV,
        import_export_admin_formats.base_formats.JSON,
    )

    fieldsets = (
        # (_('general information'), {
        #    'fields': ()
        # }),
        (_('visualization admin'), {
            'classes': ('collapse',),
            'fields': ('ordering', 'status')
        }),
        (_('logs admin'), {
            'classes': ('collapse',),
            'fields': ('creator', 'created_date', 'last_modifier', 'last_modified_date')
        }),
    )
    list_display = ('get_status_display', 'ordering')
    readonly_fields = ('creator', 'created_date', 'last_modifier', 'last_modified_date')


admin.site.register(models.Motion_event, Motion_eventAdmin)


class NodeAdmin(UserAdminMixin, import_export_admin.ImportExportModelAdmin):
    resource_class = resources.NodeResource
    formats = (
        import_export_admin_formats.base_formats.XLS,
        import_export_admin_formats.base_formats.CSV,
        import_export_admin_formats.base_formats.JSON,
    )

    fieldsets = (
        # (_('general information'), {
        #    'fields': ()
        # }),
        (_('visualization admin'), {
            'classes': ('collapse',),
            'fields': ('ordering', 'status')
        }),
        (_('logs admin'), {
            'classes': ('collapse',),
            'fields': ('creator', 'created_date', 'last_modifier', 'last_modified_date')
        }),
    )
    list_display = ('get_status_display', 'ordering')
    readonly_fields = ('creator', 'created_date', 'last_modifier', 'last_modified_date')


admin.site.register(models.Node, NodeAdmin)


class Node_moduleAdmin(UserAdminMixin, import_export_admin.ImportExportModelAdmin):
    resource_class = resources.Node_moduleResource
    formats = (
        import_export_admin_formats.base_formats.XLS,
        import_export_admin_formats.base_formats.CSV,
        import_export_admin_formats.base_formats.JSON,
    )

    fieldsets = (
        # (_('general information'), {
        #    'fields': ()
        # }),
        (_('visualization admin'), {
            'classes': ('collapse',),
            'fields': ('ordering', 'status')
        }),
        (_('logs admin'), {
            'classes': ('collapse',),
            'fields': ('creator', 'created_date', 'last_modifier', 'last_modified_date')
        }),
    )
    list_display = ('get_status_display', 'ordering')
    readonly_fields = ('creator', 'created_date', 'last_modifier', 'last_modified_date')


admin.site.register(models.Node_module, Node_moduleAdmin)


class Wilamp_alertAdmin(UserAdminMixin, import_export_admin.ImportExportModelAdmin):
    resource_class = resources.Wilamp_alertResource
    formats = (
        import_export_admin_formats.base_formats.XLS,
        import_export_admin_formats.base_formats.CSV,
        import_export_admin_formats.base_formats.JSON,
    )

    fieldsets = (
        # (_('general information'), {
        #    'fields': ()
        # }),
        (_('visualization admin'), {
            'classes': ('collapse',),
            'fields': ('ordering', 'status')
        }),
        (_('logs admin'), {
            'classes': ('collapse',),
            'fields': ('creator', 'created_date', 'last_modifier', 'last_modified_date')
        }),
    )
    list_display = ('get_status_display', 'ordering')
    readonly_fields = ('creator', 'created_date', 'last_modifier', 'last_modified_date')


admin.site.register(models.Wilamp_alert, Wilamp_alertAdmin)


class Feeder_pillarAdmin(UserAdminMixin, import_export_admin.ImportExportModelAdmin):
    resource_class = resources.Feeder_pillarResource
    formats = (
        import_export_admin_formats.base_formats.XLS,
        import_export_admin_formats.base_formats.CSV,
        import_export_admin_formats.base_formats.JSON,
    )

    fieldsets = (
        # (_('general information'), {
        #    'fields': ()
        # }),
        (_('visualization admin'), {
            'classes': ('collapse',),
            'fields': ('ordering', 'status')
        }),
        (_('logs admin'), {
            'classes': ('collapse',),
            'fields': ('creator', 'created_date', 'last_modifier', 'last_modified_date')
        }),
    )
    list_display = ('get_status_display', 'ordering')
    readonly_fields = ('creator', 'created_date', 'last_modifier', 'last_modified_date')


admin.site.register(models.Feeder_pillar, Feeder_pillarAdmin)


class Twilight_management_moduleAdmin(UserAdminMixin, import_export_admin.ImportExportModelAdmin):
    resource_class = resources.Twilight_management_moduleResource
    formats = (
        import_export_admin_formats.base_formats.XLS,
        import_export_admin_formats.base_formats.CSV,
        import_export_admin_formats.base_formats.JSON,
    )

    fieldsets = (
        # (_('general information'), {
        #    'fields': ()
        # }),
        (_('visualization admin'), {
            'classes': ('collapse',),
            'fields': ('ordering', 'status')
        }),
        (_('logs admin'), {
            'classes': ('collapse',),
            'fields': ('creator', 'created_date', 'last_modifier', 'last_modified_date')
        }),
    )
    list_display = ('get_status_display', 'ordering')
    readonly_fields = ('creator', 'created_date', 'last_modifier', 'last_modified_date')


admin.site.register(models.Twilight_management_module, Twilight_management_moduleAdmin)


class Twilight_measureAdmin(UserAdminMixin, import_export_admin.ImportExportModelAdmin):
    resource_class = resources.Twilight_measureResource
    formats = (
        import_export_admin_formats.base_formats.XLS,
        import_export_admin_formats.base_formats.CSV,
        import_export_admin_formats.base_formats.JSON,
    )

    fieldsets = (
        # (_('general information'), {
        #    'fields': ()
        # }),
        (_('visualization admin'), {
            'classes': ('collapse',),
            'fields': ('ordering', 'status')
        }),
        (_('logs admin'), {
            'classes': ('collapse',),
            'fields': ('creator', 'created_date', 'last_modifier', 'last_modified_date')
        }),
    )
    list_display = ('get_status_display', 'ordering')
    readonly_fields = ('creator', 'created_date', 'last_modifier', 'last_modified_date')


admin.site.register(models.Twilight_measure, Twilight_measureAdmin)


class Motion_management_moduleAdmin(UserAdminMixin, import_export_admin.ImportExportModelAdmin):
    resource_class = resources.Motion_management_moduleResource
    formats = (
        import_export_admin_formats.base_formats.XLS,
        import_export_admin_formats.base_formats.CSV,
        import_export_admin_formats.base_formats.JSON,
    )

    fieldsets = (
        # (_('general information'), {
        #    'fields': ()
        # }),
        (_('visualization admin'), {
            'classes': ('collapse',),
            'fields': ('ordering', 'status')
        }),
        (_('logs admin'), {
            'classes': ('collapse',),
            'fields': ('creator', 'created_date', 'last_modifier', 'last_modified_date')
        }),
    )
    list_display = ('get_status_display', 'ordering')
    readonly_fields = ('creator', 'created_date', 'last_modifier', 'last_modified_date')


admin.site.register(models.Motion_management_module, Motion_management_moduleAdmin)






