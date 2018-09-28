# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
import admin_tools
from admin_tools.dashboard import modules, AppIndexDashboard
from jmb.core.admin import dashboard as jmb_dashboard


class DefaultDashboard(modules.Group):
    def __init__(self, **kwargs):
        kwargs.update({
            'title': _("wicloud"),
            'display': "tabs",
            'children': [Models()]
        })
        super(DefaultDashboard, self).__init__(**kwargs)


class MainDashboard(modules.Group):
    def __init__(self, **kwargs):
        kwargs.update({
            'title': _("wicloud"),
            'display': "tabs",
            'children': [Models()]
        })
        super(MainDashboard, self).__init__(**kwargs)


class Models(modules.ModelList):
    def __init__(self, **kwargs):
        kwargs.update({
            'title': _("main models"),
            'models': (
                'wicloud.models.Address',
                'wicloud.models.Customer',
                'wicloud.models.Energy_interval',
                'wicloud.models.Energy_meter_module',
                'wicloud.models.Energy_meter_peak_measure',
                'wicloud.models.Error_light_level_and_adc_mismatch',
                'wicloud.models.Error_light_level_and_power_mismatch',
                'wicloud.models.Error_node_offline',
                'wicloud.models.Gateway',
                'wicloud.models.Ime_power_counter',
                'wicloud.models.Ime_power_measure',
                'wicloud.models.Installation',
                'wicloud.models.Light_management_measure',
                'wicloud.models.Light_management_module',
                'wicloud.models.Light_profile',
                'wicloud.models.Light_profile_slot',
                'wicloud.models.Motion_event',
                'wicloud.models.Node',
                'wicloud.models.Node_module',
                'wicloud.models.Wilamp_alert',
                'wicloud.models.Feeder_pillar',
                'wicloud.models.Twilight_management_module',
                'wicloud.models.Twilight_measure',
                'wicloud.models.Motion_management_module',
                'wicloud.models.',
            ),
        })
        super(Models, self).__init__(**kwargs)


class DefaultAppDashboard(AppIndexDashboard):
    def __init__(self, app_title, models, **kwargs):
        AppIndexDashboard.__init__(self, app_title, models, **kwargs)
        self.columns = 3

    def init_with_context(self, context):
        self.children.append(DefaultDashboard(), )


jmb_dashboard.register_group(MainDashboard, 'wicloud')
admin_tools.dashboard.register(DefaultAppDashboard, 'wicloud')
