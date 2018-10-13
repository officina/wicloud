# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from web.core.models import UserModel, DateModel, StatusModel, OrderedModel, CleanModel


class Address(CleanModel, UserModel, DateModel, StatusModel, OrderedModel):

    description = models.CharField(max_length=255, null=True)
    full_name = models.CharField(max_length=255,null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    house_number = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    lat = models.CharField(max_length=255, blank=True, null=True)
    lng = models.CharField(max_length=255, blank=True, null=True)
    timezone_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = _('address')
        verbose_name_plural = _('addresses')
        ordering = ('ordering',)
        permissions = (
            ("list_address", "Can list address"),
            ("detail_address", "Can detail address"),
            ("disable_address", "Can disable address"),
        )

    def __str__(self):
        return self.description


class Customer(CleanModel, UserModel, DateModel, StatusModel, OrderedModel):

    company_name = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = _('customer')
        verbose_name_plural = _('customers')
        ordering = ('ordering',)
        permissions = (
            ("list_customer", "Can list customer"),
            ("detail_customer", "Can detail customer"),
            ("disable_customer", "Can disable customer"),
        )

    def __str__(self):
        return self.description


class Energy_interval(CleanModel, UserModel, DateModel, StatusModel, OrderedModel):

    mac = models.CharField(max_length=255, null=True)
    light_management_module = models.ForeignKey('Light_management_module', models.DO_NOTHING, blank=True, null=True)
    installation = models.ForeignKey('Installation', models.DO_NOTHING, blank=True, null=True)
    start_interval = models.DateTimeField(null=True)
    end_interval = models.DateTimeField(blank=True, null=True)
    start_interval_measure_timestamp = models.DateTimeField(blank=True, null=True)
    end_interval_measure_timestamp = models.DateTimeField(blank=True, null=True)
    active_power = models.FloatField(blank=True, null=True)
    reactive_power = models.FloatField(blank=True, null=True)
    start_interval_active_energy_counter_value = models.FloatField(blank=True, null=True)
    end_interval_active_energy_counter_value = models.FloatField(blank=True, null=True)
    active_energy = models.FloatField(blank=True, null=True)
    start_interval_reactive_energy_counter_value = models.FloatField(blank=True, null=True)
    end_interval_reactive_energy_counter_value = models.FloatField(blank=True, null=True)
    reactive_energy = models.FloatField(blank=True, null=True)
    active_energy_mty_0 = models.FloatField(blank=True, null=True)
    active_energy_mty_1 = models.FloatField(blank=True, null=True)
    active_energy_mty_2 = models.FloatField(blank=True, null=True)
    active_energy_mty_3 = models.FloatField(blank=True, null=True)
    active_energy_without_dim = models.FloatField(blank=True, null=True)
    active_energy_without_control = models.FloatField(blank=True, null=True)
    active_energy_old_lamps = models.FloatField(blank=True, null=True)
    burning_time = models.FloatField(blank=True, null=True)
    node_life = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name = _('energy_interval')
        verbose_name_plural = _('energy_intervals')
        ordering = ('ordering',)
        permissions = (
            ("list_energy_interval", "Can list energy_interval"),
            ("detail_energy_interval", "Can detail energy_interval"),
            ("disable_energy_interval", "Can disable energy_interval"),
        )

    def __str__(self):
        return 'Energy_interval'


class Energy_meter_module(CleanModel, UserModel, DateModel, StatusModel, OrderedModel):

    name = models.CharField(max_length=255,null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    iac_calibration = models.FloatField(blank=True, null=True)
    vac_calibration = models.FloatField(blank=True, null=True)
    pat_calibration = models.FloatField(blank=True, null=True)
    pre_calibration = models.CharField(max_length=255, blank=True, null=True)
    nominal_power = models.FloatField(blank=True, null=True)
    old_lamp_power = models.FloatField(blank=True, null=True)
    power_losses = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name = _('energy_meter_module')
        verbose_name_plural = _('energy_meter_modules')
        ordering = ('ordering',)
        permissions = (
            ("list_energy_meter_module", "Can list energy_meter_module"),
            ("detail_energy_meter_module", "Can detail energy_meter_module"),
            ("disable_energy_meter_module", "Can disable energy_meter_module"),
        )

    def __str__(self):
        return 'Energy_meter_module'


class Energy_meter_peak_measure(CleanModel, UserModel, DateModel, StatusModel, OrderedModel):

    mac = models.CharField(max_length=255,null=True)
    node_date = models.CharField(max_length=255, blank=True, null=True)
    node_hms = models.CharField(max_length=255, blank=True, null=True)
    vac_rms_low = models.FloatField(blank=True, null=True)
    vac_rms_high = models.FloatField(blank=True, null=True)
    vac_peak = models.FloatField(blank=True, null=True)
    vac_rms_absolute_max = models.FloatField(blank=True, null=True)
    vac_rms_absolute_min = models.FloatField(blank=True, null=True)
    iac_high = models.FloatField(blank=True, null=True)
    iac_low = models.FloatField(blank=True, null=True)
    iac_peak = models.FloatField(blank=True, null=True)
    iac_hh = models.FloatField(blank=True, null=True)
    iac_ll = models.FloatField(blank=True, null=True)
    measure_timestamp = models.DateTimeField(blank=True, null=True)
    created_timestamp = models.DateTimeField(blank=True, null=True)
    source_module = models.CharField(max_length=255, blank=True, null=True)
    installation = models.ForeignKey('Installation', models.DO_NOTHING, blank=True, null=True)
    energy_meter_module = models.ForeignKey(Energy_meter_module, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        verbose_name = _('energy_meter_peak_measure')
        verbose_name_plural = _('energy_meter_peak_measures')
        ordering = ('ordering',)
        permissions = (
            ("list_energy_meter_peak_measure", "Can list energy_meter_peak_measure"),
            ("detail_energy_meter_peak_measure", "Can detail energy_meter_peak_measure"),
            ("disable_energy_meter_peak_measure", "Can disable energy_meter_peak_measure"),
        )

    def __str__(self):
        return 'Energy_meter_peak_measure'


class Error_light_level_and_adc_mismatch(CleanModel, UserModel, DateModel, StatusModel, OrderedModel):

    error_timestamp = models.DateTimeField(blank=True, null=True)
    error_resolved_timestamp = models.DateTimeField(blank=True, null=True)
    is_in_error = models.BooleanField(blank=True, default=False)
    light_level_value = models.FloatField(blank=True, null=True)
    adc_value = models.FloatField(blank=True, null=True)
    active_power = models.FloatField(blank=True, null=True)
    jhi_current = models.FloatField(blank=True, null=True)
    voltage = models.FloatField(blank=True, null=True)
    logged_entity = models.BigIntegerField(blank=True, null=True)
    logged_entity_mac = models.CharField(max_length=255, blank=True, null=True)
    entity_json = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = _('error_light_level_and_adc_mismatch')
        verbose_name_plural = _('error_light_level_and_adc_mismatchs')
        ordering = ('ordering',)
        permissions = (
            ("list_error_light_level_and_adc_mismatch", "Can list error_light_level_and_adc_mismatch"),
            ("detail_error_light_level_and_adc_mismatch",
             "Can detail error_light_level_and_adc_mismatch"),
            ("disable_error_light_level_and_adc_mismatch",
             "Can disable error_light_level_and_adc_mismatch"),
        )

    def __str__(self):
        return 'Error_light_level_and_adc_mismatch'


class Error_light_level_and_power_mismatch(CleanModel, UserModel, DateModel, StatusModel, OrderedModel):

    error_timestamp = models.DateTimeField(blank=True, null=True)
    error_resolved_timestamp = models.DateTimeField(blank=True, null=True)
    is_in_error = models.BooleanField(blank=True, default=False)
    light_level_value = models.FloatField(blank=True, null=True)
    adc_value = models.FloatField(blank=True, null=True)
    active_power = models.FloatField(blank=True, null=True)
    jhi_current = models.FloatField(blank=True, null=True)
    voltage = models.FloatField(blank=True, null=True)
    logged_entity = models.BigIntegerField(blank=True, null=True)
    logged_entity_mac = models.CharField(max_length=255, blank=True, null=True)
    entity_json = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = _('error_light_level_and_power_mismatch')
        verbose_name_plural = _('error_light_level_and_power_mismatchs')
        ordering = ('ordering',)
        permissions = (
            ("list_error_light_level_and_power_mismatch", "Can list error_light_level_and_power_mismatch"),
            ("detail_error_light_level_and_power_mismatch", "Can detail error_light_level_and_power_mismatch"),
            ("disable_error_light_level_and_power_mismatch", "Can disable error_light_level_and_power_mismatch"),
        )

    def __str__(self):
        return 'Error_light_level_and_power_mismatch'


class Error_node_offline(CleanModel, UserModel, DateModel, StatusModel, OrderedModel):

    error_timestamp = models.DateTimeField(blank=True, null=True)
    error_resolved_timestamp = models.DateTimeField(blank=True, null=True)
    is_in_error = models.BooleanField(blank=True, default=False)
    logged_entity = models.BigIntegerField(blank=True, null=True)
    logged_entity_mac = models.CharField(max_length=255, blank=True, null=True)
    entity_json = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = _('error_node_offline')
        verbose_name_plural = _('error_node_offlines')
        ordering = ('ordering',)
        permissions = (
            ("list_error_node_offline", "Can list error_node_offline"),
            ("detail_error_node_offline", "Can detail error_node_offline"),
            ("disable_error_node_offline", "Can disable error_node_offline"),
        )

    def __str__(self):
        return 'Error_node_offline'


class Gateway(CleanModel, UserModel, DateModel, StatusModel, OrderedModel):

    name = models.CharField(max_length=255,blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    gateway_uuid = models.CharField(unique=True, max_length=255,null=True)
    gateway_hostname = models.CharField(max_length=255, blank=True, null=True)
    gateway_type = models.IntegerField(blank=True,  null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    creation_date = models.DateTimeField(blank=True, null=True)
    serial_number = models.CharField(unique=True, max_length=255, blank=True, null=True)
    device_name = models.CharField(max_length=255, blank=True, null=True)
    hardware_model = models.CharField(max_length=255, blank=True, null=True)
    mac_address = models.CharField(max_length=255, blank=True, null=True)
    coordinator_mac = models.CharField(max_length=255, blank=True, null=True)
    file_name_encryption_info = models.CharField(max_length=255, blank=True, null=True)
    hardware_informations = models.CharField(max_length=255, blank=True, null=True)
    ready_to_receive_data = models.BooleanField(blank=True, default=False)
    installation = models.ForeignKey('Installation', models.DO_NOTHING, blank=True, null=True)
    # shipping = models.ForeignKey('Shipping', models.DO_NOTHING, blank=True, null=True)
    # order = models.ForeignKey('JhiOrder', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        verbose_name = _('gateway')
        verbose_name_plural = _('gateways')
        ordering = ('ordering',)
        permissions = (
            ("list_gateway", "Can list gateway"),
            ("detail_gateway", "Can detail gateway"),
            ("disable_gateway", "Can disable gateway"),
        )

    def __str__(self):
        return 'Gateway'


class Ime_power_counter(CleanModel, UserModel, DateModel, StatusModel, OrderedModel):

    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    gateway_uuid = models.CharField(max_length=255, blank=True, null=True)
    installation = models.ForeignKey('Installation', models.DO_NOTHING, blank=True, null=True)
    counter_id = models.CharField(unique=True, max_length=255, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    rs_485_bus = models.CharField(max_length=255, blank=True, null=True)
    rs_485_address = models.CharField(max_length=255, blank=True, null=True)
    address = models.ForeignKey(Address, models.DO_NOTHING, blank=True, null=True)
    gateway = models.ForeignKey(Gateway, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        verbose_name = _('ime_power_counter')
        verbose_name_plural = _('ime_power_counters')
        ordering = ('ordering',)
        permissions = (
            ("list_ime_power_counter", "Can list ime_power_counter"),
            ("detail_ime_power_counter", "Can detail ime_power_counter"),
            ("disable_ime_power_counter", "Can disable ime_power_counter"),
        )

    def __str__(self):
        return 'Ime_power_counter'


class Ime_power_measure(CleanModel, UserModel, DateModel, StatusModel, OrderedModel):

    power_counter_id = models.CharField(max_length=255, blank=True, null=True)
    jhi_timestamp = models.DateTimeField(blank=True, null=True)
    installation = models.ForeignKey('Installation', models.DO_NOTHING, blank=True, null=True)
    voltage = models.FloatField(blank=True, null=True)
    jhi_current = models.FloatField(blank=True, null=True)
    active_power = models.FloatField(blank=True, null=True)
    power_factor = models.FloatField(blank=True, null=True)
    power_factor_sector = models.FloatField(blank=True, null=True)
    freq = models.FloatField(blank=True, null=True)
    active_energy = models.FloatField(blank=True, null=True)
    partial_active_energy = models.FloatField(blank=True, null=True)
    operating_time_counter = models.FloatField(blank=True, null=True)
    ime_power_counter = models.ForeignKey(Ime_power_counter, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        verbose_name = _('ime_power_measure')
        verbose_name_plural = _('ime_power_measures')
        ordering = ('ordering',)
        permissions = (
            ("list_ime_power_measure", "Can list ime_power_measure"),
            ("detail_ime_power_measure", "Can detail ime_power_measure"),
            ("disable_ime_power_measure", "Can disable ime_power_measure"),
        )

    def __str__(self):
        return 'Ime_power_measure'


class Installation(CleanModel, UserModel, DateModel, StatusModel, OrderedModel):

    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    preparation_date = models.DateTimeField(blank=True, null=True)
    installation_date = models.DateTimeField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    address = models.OneToOneField(Address, models.DO_NOTHING,  blank=True, null=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        verbose_name = _('installation')
        verbose_name_plural = _('installations')
        ordering = ('ordering',)
        permissions = (
            ("list_installation", "Can list installation"),
            ("detail_installation", "Can detail installation"),
            ("disable_installation", "Can disable installation"),
        )

    def __str__(self):
        return self.description


class Light_management_measure(CleanModel, UserModel, DateModel, StatusModel, OrderedModel):

    mac = models.CharField(max_length=255, blank=True, null=True)
    processing_status = models.IntegerField(blank=True, null=True)
    node_hms = models.CharField(max_length=255, blank=True, null=True)
    day_of_year = models.IntegerField(blank=True, null=True)
    measure_type = models.IntegerField(blank=True, null=True)
    parent_node = models.CharField(max_length=255, blank=True, null=True)
    lqi = models.FloatField(blank=True, null=True)
    vac = models.FloatField(blank=True, null=True)
    vcc = models.FloatField(blank=True, null=True)
    iac = models.FloatField(blank=True, null=True)
    active_power = models.FloatField(blank=True, null=True)
    reactive_power = models.FloatField(blank=True, null=True)
    active_energy_counter = models.FloatField(blank=True, null=True)
    reactive_energy_counter = models.FloatField(blank=True, null=True)
    light_level = models.FloatField(blank=True, null=True)
    pw_0 = models.FloatField(blank=True, null=True)
    pw_1 = models.FloatField(blank=True, null=True)
    pw_2 = models.FloatField(blank=True, null=True)
    pw_3 = models.FloatField(blank=True, null=True)
    node_temp = models.FloatField(blank=True, null=True)
    ad_0 = models.FloatField(blank=True, null=True)
    ad_1 = models.FloatField(blank=True, null=True)
    ad_2 = models.FloatField(blank=True, null=True)
    ad_3 = models.FloatField(blank=True, null=True)
    packets_sent = models.IntegerField(blank=True, null=True)
    packets_received = models.IntegerField(blank=True, null=True)
    packets_lost = models.IntegerField(blank=True, null=True)
    motion_status = models.IntegerField(blank=True, null=True)
    manual_status = models.IntegerField(blank=True, null=True)
    status_bitmask = models.IntegerField(blank=True, null=True)
    parameters_crc = models.FloatField(blank=True, null=True)
    profile_crc = models.FloatField(blank=True, null=True)
    measure_timestamp = models.DateTimeField(blank=True, null=True)
    created_timestamp = models.DateTimeField(blank=True, null=True)
    source_module = models.CharField(max_length=255, blank=True, null=True)
    node_fw_version = models.CharField(max_length=255, blank=True, null=True)
    lamp_life = models.FloatField(blank=True, null=True)
    node_life = models.FloatField(blank=True, null=True)
    active_power_counter = models.FloatField(blank=True, null=True)
    installation = models.ForeignKey('Installation', models.DO_NOTHING, blank=True, null=True)
    light_management_module = models.ForeignKey('Light_management_module', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        verbose_name = _('light_management_measure')
        verbose_name_plural = _('light_management_measures')
        ordering = ('ordering',)
        permissions = (
            ("list_light_management_measure", "Can list light_management_measure"),
            ("detail_light_management_measure", "Can detail light_management_measure"),
            ("disable_light_management_measure", "Can disable light_management_measure"),
        )

    def __str__(self):
        return f'Light_management_measure {self.id}'


class Light_management_module(CleanModel, UserModel, DateModel, StatusModel, OrderedModel):

    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    device_type = models.IntegerField(blank=True, null=True)
    lamp_type = models.IntegerField(blank=True, null=True)
    timer_auto_mode = models.IntegerField(blank=True, null=True)
    timer_hps_protection = models.IntegerField(blank=True, null=True)
    light_zone = models.IntegerField(blank=True, null=True)
    light_profile_id = models.BigIntegerField(blank=True, null=True)
    light_profile_crc = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name = _('light_management_module')
        verbose_name_plural = _('light_management_module')
        ordering = ('ordering',)
        permissions = (
            ("list_light_management_module", "Can list light_management_module"),
            ("detail_light_management_module", "Can detail light_management_module"),
            ("disable_light_management_module", "Can disable light_management_module"),
        )

    def __str__(self):
        return 'Light_management_module'


class Light_profile(CleanModel, UserModel, DateModel, StatusModel, OrderedModel):

    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    jhi_type = models.CharField(max_length=255, blank=True, null=True)
    reference = models.CharField(max_length=255, blank=True, null=True)
    profile_crc = models.FloatField(blank=True, null=True)
    light_profile_id = models.IntegerField(blank=True, null=True)
    gateway = models.ForeignKey('Gateway', models.DO_NOTHING, blank=True, null=True)
    enabled = models.BooleanField(blank=True, default=False)

    class Meta:
        verbose_name = _('light_profile')
        verbose_name_plural = _('light_profiles')
        ordering = ('ordering',)
        permissions = (
            ("list_light_profile", "Can list light_profile"),
            ("detail_light_profile", "Can detail light_profile"),
            ("disable_light_profile", "Can disable light_profile"),
        )

    def __str__(self):
        return 'Light_profile'


class Light_profile_slot(CleanModel, UserModel, DateModel, StatusModel, OrderedModel):

    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    don = models.IntegerField(blank=True, null=True)
    dof = models.IntegerField(blank=True, null=True)
    ton = models.CharField(max_length=255, blank=True, null=True)
    tof = models.CharField(max_length=255, blank=True, null=True)
    eas = models.BooleanField(blank=True, default=False)
    ecr = models.BooleanField(blank=True, default=False)
    emo = models.BooleanField(blank=True, default=False)
    edw = models.IntegerField(blank=True, null=True)
    enabled = models.BooleanField(blank=True, default=False)
    light_profile_index = models.IntegerField(blank=True, null=True)
    pw_0 = models.FloatField(blank=True, null=True)
    pw_1 = models.FloatField(blank=True, null=True)
    pw_2 = models.FloatField(blank=True, null=True)
    pw_3 = models.FloatField(blank=True, null=True)
    fade_in = models.FloatField(blank=True, null=True)
    fade_out = models.FloatField(blank=True, null=True)
    slot = models.IntegerField(blank=True, null=True)
    created_timestamp = models.DateTimeField(blank=True, null=True)
    motion_duration = models.FloatField(blank=True, null=True)
    motion_delay = models.FloatField(blank=True, null=True)
    mi_0 = models.FloatField(blank=True, null=True)
    mi_1 = models.FloatField(blank=True, null=True)
    mi_2 = models.FloatField(blank=True, null=True)
    mi_3 = models.FloatField(blank=True, null=True)
    motion_fade_in = models.FloatField(blank=True, null=True)
    motion_fade_out = models.FloatField(blank=True, null=True)
    light_profile = models.ForeignKey(Light_profile, models.DO_NOTHING, blank=True, null=True)
    

    class Meta:
        verbose_name = _('light_profile_slot')
        verbose_name_plural = _('light_profile_slots')
        ordering = ('ordering',)
        permissions = (
            ("list_light_profile_slot", "Can list light_profile_slot"),
            ("detail_light_profile_slot", "Can detail light_profile_slot"),
            ("disable_light_profile_slot", "Can disable light_profile_slot"),
        )

    def __str__(self):
        return 'Light_profile_slot'


class Motion_event(CleanModel, UserModel, DateModel, StatusModel, OrderedModel):

    mac = models.CharField(max_length=255, blank=True, null=True)
    motion_mode = models.IntegerField(blank=True, null=True)
    motion_group = models.IntegerField(blank=True, null=True)
    motion_broadcast = models.IntegerField(blank=True, null=True)
    measure_timestamp = models.DateTimeField(blank=True, null=True)
    motion_management_module = models.ForeignKey('Motion_management_module', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        verbose_name = _('motion_event')
        verbose_name_plural = _('motion_events')
        ordering = ('ordering',)
        permissions = (
            ("list_motion_event", "Can list motion_event"),
            ("detail_motion_event", "Can detail motion_event"),
            ("disable_motion_event", "Can disable motion_event"),
        )

    def __str__(self):
        return 'Motion_event'




class Node(CleanModel, UserModel, DateModel, StatusModel, OrderedModel):

    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    node_type = models.IntegerField(blank=True, null=True)
    mac = models.CharField(unique=True, max_length=255, blank=True, null=True)
    log_time_ist = models.IntegerField(blank=True, null=True)
    log_time_0 = models.IntegerField(blank=True, null=True)
    log_time_1 = models.IntegerField(blank=True, null=True)
    log_time_2 = models.IntegerField(blank=True, null=True)
    log_time_3 = models.IntegerField(blank=True, null=True)
    time_zone = models.IntegerField(blank=True, null=True)
    time_zone_code = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    modules = models.OneToOneField('Node_module', models.DO_NOTHING, blank=True, null=True)
    gateway = models.ForeignKey(Gateway, models.DO_NOTHING, blank=True, null=True)
    # shipping = models.ForeignKey('Shipping', models.DO_NOTHING, blank=True, null=True)
    # order = models.ForeignKey(JhiOrder, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        verbose_name = _('node')
        verbose_name_plural = _('nodes')
        ordering = ('ordering',)
        permissions = (
            ("list_node", "Can list node"),
            ("detail_node", "Can detail node"),
            ("disable_node", "Can disable node"),
        )

    def __str__(self):
        return 'Node'


class Node_module(CleanModel, UserModel, DateModel, StatusModel, OrderedModel):

    name = models.CharField(max_length=255, blank=True, null=True)
    light_management = models.OneToOneField(Light_management_module, models.DO_NOTHING,  blank=True, null=True)
    energy_meter = models.OneToOneField(Energy_meter_module, models.DO_NOTHING,  blank=True, null=True)
    twilight_management = models.OneToOneField('Twilight_management_module', models.DO_NOTHING,  blank=True,
                                            null=True)
    motion_management = models.OneToOneField('Motion_management_module', models.DO_NOTHING,blank=True, null=True)

    class Meta:
        verbose_name = _('node_module')
        verbose_name_plural = _('node_modules')
        ordering = ('ordering',)
        permissions = (
            ("list_node_module", "Can list node_module"),
            ("detail_node_module", "Can detail node_module"),
            ("disable_node_module", "Can disable node_module"),
        )

    def __str__(self):
        return 'Node_module'


class Wilamp_alert(CleanModel, UserModel, DateModel, StatusModel, OrderedModel):

    alert_timestamp = models.DateTimeField(blank=True, null=True)
    jhi_type = models.IntegerField(blank=True, null=True)
    severity = models.IntegerField(blank=True, null=True)
    logger_entity_id = models.CharField(max_length=255, blank=True, null=True)
    logger_name = models.CharField(max_length=255, blank=True, null=True)
    module = models.CharField(max_length=255, blank=True, null=True)
    logged_entity_id = models.CharField(max_length=255, blank=True, null=True)
    logged_entity = models.CharField(max_length=255, blank=True, null=True)
    message = models.CharField(max_length=1000, blank=True, null=True)
    comment = models.CharField(max_length=5000, blank=True, null=True)
    log_class = models.CharField(max_length=1000, blank=True, null=True)
    note = models.CharField(max_length=5000, blank=True, null=True)

    class Meta:
        verbose_name = _('wilamp_alert')
        verbose_name_plural = _('wilamp_alerts')
        ordering = ('ordering',)
        permissions = (
            ("list_wilamp_alert", "Can list wilamp_alert"),
            ("detail_wilamp_alert", "Can detail wilamp_alert"),
            ("disable_wilamp_alert", "Can disable wilamp_alert"),
        )

    def __str__(self):
        return 'Wilamp_alert'


class Feeder_pillar(CleanModel, UserModel, DateModel, StatusModel, OrderedModel):

    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    reference_code = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    max_power = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name = _('feeder_pillar')
        verbose_name_plural = _('feeder_pillars')
        ordering = ('ordering',)
        permissions = (
            ("list_feeder_pillar", "Can list feeder_pillar"),
            ("detail_feeder_pillar", "Can detail feeder_pillar"),
            ("disable_feeder_pillar", "Can disable feeder_pillar"),
        )

    def __str__(self):
        return 'Feeder_pillar'


class Twilight_management_module(CleanModel, UserModel, DateModel, StatusModel, OrderedModel):

    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    tw_mode = models.IntegerField(blank=True, null=True)
    tw_type = models.IntegerField(blank=True, null=True)
    tw_group = models.IntegerField(blank=True, null=True)
    valid_period = models.IntegerField(blank=True, null=True)
    ths_sunset_on = models.FloatField(blank=True, null=True)
    ths_sunset_off = models.FloatField(blank=True, null=True)
    ths_sunrise_on = models.FloatField(blank=True, null=True)
    ths_sunrise_off = models.FloatField(blank=True, null=True)
    persistence_period = models.IntegerField(blank=True, null=True)
    delay_offset = models.IntegerField(blank=True, null=True)
    voltagem_v = models.FloatField(blank=True, null=True)
    lux_measured = models.FloatField(blank=True, null=True)
    sampling_period = models.IntegerField(blank=True, null=True)
    number_average_measures = models.IntegerField(blank=True, null=True)
    adc_in_channel = models.IntegerField(blank=True, null=True)
    programming_status = models.IntegerField(blank=True, null=True)
    created_timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = _('twilight_management_module')
        verbose_name_plural = _('twilight_management_modules')
        ordering = ('ordering',)
        permissions = (
            ("list_twilight_management_module", "Can list twilight_management_module"),
            ("detail_twilight_management_module", "Can detail twilight_management_module"),
            ("disable_twilight_management_module", "Can disable twilight_management_module"),
        )

    def __str__(self):
        return 'Twilight_management_module'


class Twilight_measure(CleanModel, UserModel, DateModel, StatusModel, OrderedModel):

    lux_value = models.FloatField(blank=True, null=True)
    adc_value = models.FloatField(blank=True, null=True)
    measure_timestamp = models.DateTimeField(blank=True, null=True)
    twilight_management_module = models.ForeignKey(Twilight_management_module, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        verbose_name = _('twilight_measure')
        verbose_name_plural = _('twilight_measure')
        ordering = ('ordering',)
        permissions = (
            ("list_twilight_measure", "Can list twilight_measure"),
            ("detail_twilight_measure", "Can detail twilight_measure"),
            ("disable_twilight_measure", "Can disable twilight_measure"),
        )

    def __str__(self):
        return 'Twilight_measure'


class Motion_management_module(CleanModel, UserModel, DateModel, StatusModel, OrderedModel):

    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    motion_mode = models.IntegerField(blank=True, null=True)
    motion_type = models.IntegerField(blank=True, null=True)
    motion_group = models.IntegerField(blank=True, null=True)
    delay_after = models.FloatField(default=0)
    retrigger_time = models.FloatField(blank=True, null=True)
    trigger_delay = models.FloatField(blank=True, null=True)
    mi_0 = models.FloatField(blank=True, null=True)
    mi_1 = models.FloatField(blank=True, null=True)
    mi_2 = models.FloatField(blank=True, null=True)
    mi_3 = models.FloatField(blank=True, null=True)
    fade_in = models.FloatField(default=0)
    fade_out = models.FloatField(default=0)
    created_timestamp = models.DateTimeField(blank=True, null=True)
    adc_in_channel = models.IntegerField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name = _('motion_management_module')
        verbose_name_plural = _('motion_management_modules')
        ordering = ('ordering',)
        permissions = (
            ("list_motion_management_module", "Can list motion_management_module"),
            ("detail_motion_management_module", "Can detail motion_management_module"),
            ("disable_motion_management_module", "Can disable motion_management_module"),
        )

    def __str__(self):
        return 'Motion_management_module'



