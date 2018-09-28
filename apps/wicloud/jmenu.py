# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from admin_tools.menu import items
from jmb.core.admin.menu import register_menu

currency_menu_item = items.MenuItem(
    _('wicloud'),
    reverse('admin:app_list', kwargs={'app_label': 'wicloud'}),
    children=[
        items.MenuItem(_('add address'), reverse('admin:wicloud_address_add', )),
        items.MenuItem(_('list address'), reverse('admin:wicloud_address_changelist', )),
        items.MenuItem(_('add  customer'), reverse('admin:wicloud_customer_add', )),
        items.MenuItem(_('list  customer'), reverse('admin:wicloud_customer_changelist', )),
        items.MenuItem(_('add  energy_interval'), reverse('admin:wicloud_energy_interval_add', )),
        items.MenuItem(_('list  energy_interval'), reverse('admin:wicloud_energy_interval_changelist', )),
        items.MenuItem(_('add  energy_meter_module'), reverse('admin:wicloud_energy_meter_module_add', )),
        items.MenuItem(_('list  energy_meter_module'), reverse('admin:wicloud_energy_meter_module_changelist', )),
        items.MenuItem(_('add  energy_meter_peak_measure'), reverse('admin:wicloud_energy_meter_peak_measure_add', )),
        items.MenuItem(_('list  energy_meter_peak_measure'), reverse(
            'admin:wicloud_energy_meter_peak_measure_changelist', )),
        items.MenuItem(_('add  error_light_level_and_adc_mismatch'), reverse(
            'admin:wicloud_error_light_level_and_adc_mismatch_add', )),
        items.MenuItem(_('list  error_light_level_and_adc_mismatch'), reverse(
            'admin:wicloud_error_light_level_and_adc_mismatch_changelist', )),
        items.MenuItem(_('add  error_light_level_and_power_mismatch'), reverse(
            'admin:wicloud_error_light_level_and_power_mismatch_add', )),
        items.MenuItem(_('list  error_light_level_and_power_mismatch'), reverse(
            'admin:wicloud_error_light_level_and_power_mismatch_changelist', )),
        items.MenuItem(_('add  error_node_offline'), reverse('admin:wicloud_error_node_offline_add', )),
        items.MenuItem(_('list  error_node_offline'), reverse('admin:wicloud_error_node_offline_changelist', )),
        items.MenuItem(_('add  gateway'), reverse('admin:wicloud_gateway_add', )),
        items.MenuItem(_('list  gateway'), reverse('admin:wicloud_gateway_changelist', )),
        items.MenuItem(_('add  ime_power_counter'), reverse('admin:wicloud_ime_power_counter_add', )),
        items.MenuItem(_('list  ime_power_counter'), reverse('admin:wicloud_ime_power_counter_changelist', )),
        items.MenuItem(_('add  ime_power_measure'), reverse('admin:wicloud_ime_power_measure_add', )),
        items.MenuItem(_('list  ime_power_measure'), reverse('admin:wicloud_ime_power_measure_changelist', )),
        items.MenuItem(_('add  installation'), reverse('admin:wicloud_installation_add', )),
        items.MenuItem(_('list  installation'), reverse('admin:wicloud_installation_changelist', )),
        items.MenuItem(_('add  light_management_measure'), reverse('admin:wicloud_light_management_measure_add', )),
        items.MenuItem(_('list  light_management_measure'), reverse(
            'admin:wicloud_light_management_measure_changelist', )),
        items.MenuItem(_('add  light_management_module'), reverse('admin:wicloud_light_management_module_add', )),
        items.MenuItem(_('list  light_management_module'), reverse(
            'admin:wicloud_light_management_module_changelist', )),
        items.MenuItem(_('add  light_profile'), reverse('admin:wicloud_light_profile_add', )),
        items.MenuItem(_('list  light_profile'), reverse('admin:wicloud_light_profile_changelist', )),
        items.MenuItem(_('add  light_profile_slot'), reverse('admin:wicloud_light_profile_slot_add', )),
        items.MenuItem(_('list  light_profile_slot'), reverse('admin:wicloud_light_profile_slot_changelist', )),
        items.MenuItem(_('add  motion_event'), reverse('admin:wicloud_motion_event_add', )),
        items.MenuItem(_('list  motion_event'), reverse('admin:wicloud_motion_event_changelist', )),
        items.MenuItem(_('add  node'), reverse('admin:wicloud_node_add', )),
        items.MenuItem(_('list  node'), reverse('admin:wicloud_node_changelist', )),
        items.MenuItem(_('add  node_module'), reverse('admin:wicloud_node_module_add', )),
        items.MenuItem(_('list  node_module'), reverse('admin:wicloud_node_module_changelist', )),
        items.MenuItem(_('add  wilamp_alert'), reverse('admin:wicloud_wilamp_alert_add', )),
        items.MenuItem(_('list  wilamp_alert'), reverse('admin:wicloud_wilamp_alert_changelist', )),
        items.MenuItem(_('add  feeder_pillar'), reverse('admin:wicloud_feeder_pillar_add', )),
        items.MenuItem(_('list  feeder_pillar'), reverse('admin:wicloud_feeder_pillar_changelist', )),
        items.MenuItem(_('add  twilight_management_module'), reverse(
            'admin:wicloud_twilight_management_module_add', )),
        items.MenuItem(_('list  twilight_management_module'), reverse(
            'admin:wicloud_twilight_management_module_changelist', )),
        items.MenuItem(_('add  twilight_measure'), reverse('admin:wicloud_twilight_measure_add', )),
        items.MenuItem(_('list  twilight_measure'), reverse('admin:wicloud_twilight_measure_changelist', )),
        items.MenuItem(_('add  motion_management_module'), reverse('admin:wicloud_motion_management_module_add', )),
        items.MenuItem(_('list  motion_management_module'), reverse(
            'admin:wicloud_motion_management_module_changelist', )),
        items.MenuItem(_('add '), reverse('admin:wicloud__add', )),
        items.MenuItem(_('list '), reverse('admin:wicloud__changelist', )),
    ]
)

register_menu(currency_menu_item, 'wicloud')
