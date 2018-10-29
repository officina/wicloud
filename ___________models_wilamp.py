# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Address(models.Model):
    id = models.BigIntegerField(primary_key=True)
    address_description = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    street = models.CharField(max_length=255, blank=True, null=True)
    house_number = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    lat = models.CharField(max_length=255, blank=True, null=True)
    lng = models.CharField(max_length=255, blank=True, null=True)
    timezone_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address'


class Contact(models.Model):
    id = models.BigIntegerField(primary_key=True)
    contact_description = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    customer = models.ForeignKey('Customer', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact'


class ContactAddress(models.Model):
    addresses = models.ForeignKey(Address, models.DO_NOTHING)
    contacts = models.ForeignKey(Contact, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'contact_address'
        unique_together = (('contacts', 'addresses'),)


class Customer(models.Model):
    id = models.BigIntegerField(primary_key=True)
    company_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class CustomerUsers(models.Model):
    users = models.ForeignKey('JhiUser', models.DO_NOTHING)
    customers = models.ForeignKey(Customer, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'customer_users'
        unique_together = (('customers', 'users'),)


class Databasechangelog(models.Model):
    id = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    dateexecuted = models.DateTimeField()
    orderexecuted = models.IntegerField()
    exectype = models.CharField(max_length=10)
    md5sum = models.CharField(max_length=35, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    tag = models.CharField(max_length=255, blank=True, null=True)
    liquibase = models.CharField(max_length=20, blank=True, null=True)
    contexts = models.CharField(max_length=255, blank=True, null=True)
    labels = models.CharField(max_length=255, blank=True, null=True)
    deployment_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'databasechangelog'


class Databasechangeloglock(models.Model):
    id = models.IntegerField(primary_key=True)
    locked = models.BooleanField()
    lockgranted = models.DateTimeField(blank=True, null=True)
    lockedby = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'databasechangeloglock'


class DefaultSlot(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    pw_0 = models.FloatField(blank=True, null=True)
    pw_1 = models.FloatField(blank=True, null=True)
    pw_2 = models.FloatField(blank=True, null=True)
    pw_3 = models.FloatField(blank=True, null=True)
    fade_in = models.FloatField(blank=True, null=True)
    flags = models.IntegerField(blank=True, null=True)
    motion_delay = models.FloatField(blank=True, null=True)
    motion_duration = models.FloatField(blank=True, null=True)
    motion_light_level = models.FloatField(blank=True, null=True)
    motion_fade_in = models.FloatField(blank=True, null=True)
    motion_fade_out = models.FloatField(blank=True, null=True)
    dim_0_off = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'default_slot'


class EnergyInterval(models.Model):
    id = models.BigIntegerField(primary_key=True)
    mac = models.CharField(max_length=255)
    light_management_module_id = models.BigIntegerField()
    installation_id = models.BigIntegerField(blank=True, null=True)
    start_interval = models.DateTimeField()
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
        managed = False
        db_table = 'energy_interval'
        unique_together = (('light_management_module_id', 'start_interval', 'end_interval'),)


class EnergyMeterModule(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    iac_calibration = models.FloatField(blank=True, null=True)
    vac_calibration = models.FloatField(blank=True, null=True)
    pat_calibration = models.FloatField(blank=True, null=True)
    pre_calibration = models.CharField(max_length=255, blank=True, null=True)
    nominal_power = models.FloatField(blank=True, null=True)
    old_lamp_power = models.FloatField(blank=True, null=True)
    power_losses = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'energy_meter_module'


class EnergyMeterPeakMeasure(models.Model):
    id = models.BigIntegerField(primary_key=True)
    mac = models.CharField(max_length=255)
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
    installation_id = models.BigIntegerField(blank=True, null=True)
    energy_meter_module = models.ForeignKey(EnergyMeterModule, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'energy_meter_peak_measure'
        unique_together = (('mac', 'measure_timestamp'),)


class ErrorLightLevelAndAdcMismatch(models.Model):
    id = models.BigIntegerField(primary_key=True)
    error_timestamp = models.DateTimeField(blank=True, null=True)
    error_resolved_timestamp = models.DateTimeField(blank=True, null=True)
    is_in_error = models.BooleanField(blank=True, null=True)
    light_level_value = models.FloatField(blank=True, null=True)
    adc_value = models.FloatField(blank=True, null=True)
    active_power = models.FloatField(blank=True, null=True)
    jhi_current = models.FloatField(blank=True, null=True)
    voltage = models.FloatField(blank=True, null=True)
    logged_entity = models.BigIntegerField(blank=True, null=True)
    logged_entity_mac = models.CharField(max_length=255, blank=True, null=True)
    entity_json = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'error_light_level_and_adc_mismatch'


class ErrorLightLevelAndPowerMismatch(models.Model):
    id = models.BigIntegerField(primary_key=True)
    error_timestamp = models.DateTimeField(blank=True, null=True)
    error_resolved_timestamp = models.DateTimeField(blank=True, null=True)
    is_in_error = models.BooleanField(blank=True, null=True)
    light_level_value = models.FloatField(blank=True, null=True)
    adc_value = models.FloatField(blank=True, null=True)
    active_power = models.FloatField(blank=True, null=True)
    jhi_current = models.FloatField(blank=True, null=True)
    voltage = models.FloatField(blank=True, null=True)
    logged_entity = models.BigIntegerField(blank=True, null=True)
    logged_entity_mac = models.CharField(max_length=255, blank=True, null=True)
    entity_json = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'error_light_level_and_power_mismatch'


class ErrorNodeOffline(models.Model):
    id = models.BigIntegerField(primary_key=True)
    error_timestamp = models.DateTimeField(blank=True, null=True)
    error_resolved_timestamp = models.DateTimeField(blank=True, null=True)
    is_in_error = models.BooleanField(blank=True, null=True)
    logged_entity = models.BigIntegerField(blank=True, null=True)
    logged_entity_mac = models.CharField(max_length=255, blank=True, null=True)
    entity_json = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'error_node_offline'


class FeederPillar(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    reference_code = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    max_power = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feeder_pillar'


class Gateway(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    gateway_uuid = models.CharField(unique=True, max_length=255)
    gateway_hostname = models.CharField(max_length=255)
    gateway_type = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    creation_date = models.DateTimeField(blank=True, null=True)
    serial_number = models.CharField(unique=True, max_length=255, blank=True, null=True)
    device_name = models.CharField(max_length=255, blank=True, null=True)
    hardware_model = models.CharField(max_length=255, blank=True, null=True)
    mac_address = models.CharField(max_length=255, blank=True, null=True)
    coordinator_mac = models.CharField(max_length=255, blank=True, null=True)
    file_name_encryption_info = models.CharField(max_length=255, blank=True, null=True)
    hardware_informations = models.CharField(max_length=255, blank=True, null=True)
    ready_to_receive_data = models.BooleanField(blank=True, null=True)
    installation = models.ForeignKey('Installation', models.DO_NOTHING, blank=True, null=True)
    shipping = models.ForeignKey('Shipping', models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey('JhiOrder', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gateway'


class GatewayConfig(models.Model):
    id = models.BigIntegerField(primary_key=True)
    gateway_uuid = models.CharField(max_length=255, blank=True, null=True)
    json_config = models.CharField(max_length=255, blank=True, null=True)
    created_timestamp = models.DateTimeField(blank=True, null=True)
    gateway_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gateway_config'


class GatewayInstallationRequest(models.Model):
    id = models.BigIntegerField(primary_key=True)
    mac_address = models.CharField(unique=True, max_length=255)
    gateway_uuid = models.CharField(unique=True, max_length=255)
    gateway_ip = models.CharField(max_length=255, blank=True, null=True)
    gateway_type = models.CharField(max_length=255, blank=True, null=True)
    fw_version = models.CharField(max_length=255, blank=True, null=True)
    creation_date = models.DateTimeField(blank=True, null=True)
    device_name = models.CharField(max_length=255, blank=True, null=True)
    hardware_model = models.CharField(max_length=255, blank=True, null=True)
    hardware_informations = models.CharField(max_length=255, blank=True, null=True)
    ready_to_install = models.BooleanField(blank=True, null=True)
    start_installation_timestamp = models.DateTimeField(blank=True, null=True)
    end_installation_timestamp = models.DateTimeField(blank=True, null=True)
    current_installation_step = models.CharField(max_length=255, blank=True, null=True)
    error_message = models.CharField(max_length=500, blank=True, null=True)
    error_detected = models.BooleanField(blank=True, null=True)
    installation_concluded = models.BooleanField(blank=True, null=True)
    gateway = models.ForeignKey(Gateway, models.DO_NOTHING, unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gateway_installation_request'


class ImePowerCounter(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    gateway_uuid = models.CharField(max_length=255, blank=True, null=True)
    installation_id = models.BigIntegerField(blank=True, null=True)
    counter_id = models.CharField(unique=True, max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    rs_485_bus = models.CharField(max_length=255, blank=True, null=True)
    rs_485_address = models.CharField(max_length=255, blank=True, null=True)
    address = models.ForeignKey(Address, models.DO_NOTHING, blank=True, null=True)
    gateway = models.ForeignKey(Gateway, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ime_power_counter'


class ImePowerMeasure(models.Model):
    id = models.BigIntegerField(primary_key=True)
    power_counter_id = models.CharField(max_length=255, blank=True, null=True)
    jhi_timestamp = models.DateTimeField(blank=True, null=True)
    installation_id = models.BigIntegerField(blank=True, null=True)
    voltage = models.FloatField(blank=True, null=True)
    jhi_current = models.FloatField(blank=True, null=True)
    active_power = models.FloatField(blank=True, null=True)
    power_factor = models.FloatField(blank=True, null=True)
    power_factor_sector = models.FloatField(blank=True, null=True)
    freq = models.FloatField(blank=True, null=True)
    active_energy = models.FloatField(blank=True, null=True)
    partial_active_energy = models.FloatField(blank=True, null=True)
    operating_time_counter = models.FloatField(blank=True, null=True)
    ime_power_counter = models.ForeignKey(ImePowerCounter, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ime_power_measure'


class Installation(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    preparation_date = models.DateTimeField(blank=True, null=True)
    installation_date = models.DateTimeField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    address = models.ForeignKey(Address, models.DO_NOTHING, unique=True, blank=True, null=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'installation'


class JhiAuthority(models.Model):
    name = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'jhi_authority'


class JhiOrder(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    order_date = models.DateTimeField(blank=True, null=True)
    preparation_date = models.DateTimeField(blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jhi_order'


class JhiPersistentAuditEvent(models.Model):
    event_id = models.BigIntegerField(primary_key=True)
    principal = models.CharField(max_length=50)
    event_date = models.DateTimeField(blank=True, null=True)
    event_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jhi_persistent_audit_event'


class JhiPersistentAuditEvtData(models.Model):
    event = models.ForeignKey(JhiPersistentAuditEvent, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=150)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jhi_persistent_audit_evt_data'
        unique_together = (('event', 'name'),)


class JhiUser(models.Model):
    id = models.BigIntegerField(primary_key=True)
    login = models.CharField(unique=True, max_length=50)
    password_hash = models.CharField(max_length=60, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)
    image_url = models.CharField(max_length=256, blank=True, null=True)
    activated = models.BooleanField()
    lang_key = models.CharField(max_length=6, blank=True, null=True)
    activation_key = models.CharField(max_length=20, blank=True, null=True)
    reset_key = models.CharField(max_length=20, blank=True, null=True)
    created_by = models.CharField(max_length=50)
    created_date = models.DateTimeField()
    reset_date = models.DateTimeField(blank=True, null=True)
    last_modified_by = models.CharField(max_length=50, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jhi_user'


class JhiUserAuthority(models.Model):
    user = models.ForeignKey(JhiUser, models.DO_NOTHING, primary_key=True)
    authority_name = models.ForeignKey(JhiAuthority, models.DO_NOTHING, db_column='authority_name')

    class Meta:
        managed = False
        db_table = 'jhi_user_authority'
        unique_together = (('user', 'authority_name'),)


class LastEnergyInterval(models.Model):
    id = models.BigIntegerField(primary_key=True)
    mac = models.CharField(max_length=255)
    light_management_module_id = models.BigIntegerField()
    installation_id = models.BigIntegerField(blank=True, null=True)
    start_interval = models.DateTimeField()
    end_interval = models.DateTimeField(blank=True, null=True)
    start_interval_measure_timestamp = models.DateTimeField(blank=True, null=True)
    end_interval_measure_timestamp = models.DateTimeField(blank=True, null=True)
    active_power = models.FloatField(blank=True, null=True)
    reactive_power = models.FloatField(blank=True, null=True)
    start_interval_active_energy_counter_value = models.FloatField(blank=True, null=True)
    end_interval_active_energy_counter_value = models.FloatField(blank=True, null=True)
    start_interval_reactive_energy_counter_value = models.FloatField(blank=True, null=True)
    end_interval_reactive_energy_counter_value = models.FloatField(blank=True, null=True)
    current_active_energy_counter_value = models.FloatField(blank=True, null=True)
    current_reactive_energy_counter_value = models.FloatField(blank=True, null=True)
    current_active_energy_accumulated_mty_0 = models.FloatField(blank=True, null=True)
    current_active_energy_accumulated_mty_1 = models.FloatField(blank=True, null=True)
    current_active_energy_accumulated_mty_2 = models.FloatField(blank=True, null=True)
    current_active_energy_accumulated_mty_3 = models.FloatField(blank=True, null=True)
    last_dim_level = models.FloatField(blank=True, null=True)
    start_interval_burning_time = models.FloatField(blank=True, null=True)
    current_burning_time = models.FloatField(blank=True, null=True)
    calculated_burning_time = models.FloatField(blank=True, null=True)
    start_interval_node_life = models.FloatField(blank=True, null=True)
    current_node_life = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'last_energy_interval'
        unique_together = (('light_management_module_id', 'start_interval', 'end_interval'),)


class LightManagementMeasure(models.Model):
    id = models.BigIntegerField(primary_key=True)
    mac = models.CharField(max_length=255)
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
    installation_id = models.BigIntegerField(blank=True, null=True)
    light_management_module = models.ForeignKey('LightManagementModule', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'light_management_measure'
        unique_together = (('mac', 'measure_timestamp'),)


class LightManagementModule(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    device_type = models.IntegerField()
    lamp_type = models.IntegerField()
    timer_auto_mode = models.IntegerField()
    timer_hps_protection = models.IntegerField()
    light_zone = models.IntegerField(blank=True, null=True)
    light_profile_id = models.BigIntegerField(blank=True, null=True)
    light_profile_crc = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'light_management_module'


class LightProfile(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    jhi_type = models.CharField(max_length=255, blank=True, null=True)
    reference = models.CharField(max_length=255, blank=True, null=True)
    profile_crc = models.FloatField(blank=True, null=True)
    light_profile_id = models.IntegerField(blank=True, null=True)
    gateway_id = models.IntegerField(blank=True, null=True)
    enabled = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'light_profile'


class LightProfileSlot(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    don = models.IntegerField(blank=True, null=True)
    dof = models.IntegerField(blank=True, null=True)
    ton = models.CharField(max_length=255, blank=True, null=True)
    tof = models.CharField(max_length=255, blank=True, null=True)
    eas = models.BooleanField(blank=True, null=True)
    ecr = models.BooleanField(blank=True, null=True)
    emo = models.BooleanField(blank=True, null=True)
    edw = models.IntegerField(blank=True, null=True)
    enabled = models.BooleanField(blank=True, null=True)
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
    light_profile = models.ForeignKey(LightProfile, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'light_profile_slot'


class LmMeasureProcessingInfo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    mac_address = models.CharField(max_length=255, blank=True, null=True)
    light_management_module_id = models.BigIntegerField(blank=True, null=True)
    last_measure_id_processed_with_mty_0 = models.BigIntegerField(blank=True, null=True)
    last_measure_id_processed_with_mty_1 = models.BigIntegerField(blank=True, null=True)
    last_measure_id_processed_with_mty_2 = models.BigIntegerField(blank=True, null=True)
    last_measure_id_processed_with_mty_3 = models.BigIntegerField(blank=True, null=True)
    last_energy_interval_id_processed_with_mty_0 = models.BigIntegerField(blank=True, null=True)
    last_energy_interval_id_processed_with_mty_1 = models.BigIntegerField(blank=True, null=True)
    last_energy_interval_id_processed_with_mty_2 = models.BigIntegerField(blank=True, null=True)
    last_energy_interval_id_processed_with_mty_3 = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lm_measure_processing_info'


class LogEntry(models.Model):
    id = models.BigIntegerField(primary_key=True)
    log_timestamp = models.DateTimeField(blank=True, null=True)
    module = models.CharField(max_length=255, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    jhi_level = models.FloatField(blank=True, null=True)
    jhi_comment = models.CharField(max_length=255, blank=True, null=True)
    log_class = models.CharField(max_length=255, blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_entry'


class MotionEvent(models.Model):
    id = models.BigIntegerField(primary_key=True)
    mac = models.CharField(max_length=255)
    motion_mode = models.IntegerField(blank=True, null=True)
    motion_group = models.IntegerField(blank=True, null=True)
    motion_broadcast = models.IntegerField(blank=True, null=True)
    measure_timestamp = models.DateTimeField(blank=True, null=True)
    motion_management_module = models.ForeignKey('MotionManagementModule', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'motion_event'


class MotionManagementModule(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    motion_mode = models.IntegerField()
    motion_type = models.IntegerField()
    motion_group = models.IntegerField()
    delay_after = models.FloatField()
    retrigger_time = models.FloatField()
    trigger_delay = models.FloatField()
    mi_0 = models.FloatField()
    mi_1 = models.FloatField()
    mi_2 = models.FloatField()
    mi_3 = models.FloatField()
    fade_in = models.FloatField()
    fade_out = models.FloatField()
    created_timestamp = models.DateTimeField(blank=True, null=True)
    adc_in_channel = models.IntegerField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'motion_management_module'


class Node(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    node_type = models.IntegerField(blank=True, null=True)
    mac = models.CharField(unique=True, max_length=255)
    log_time_ist = models.IntegerField()
    log_time_0 = models.IntegerField()
    log_time_1 = models.IntegerField()
    log_time_2 = models.IntegerField()
    log_time_3 = models.IntegerField()
    time_zone = models.IntegerField()
    time_zone_code = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    modules = models.ForeignKey('NodeModules', models.DO_NOTHING, unique=True, blank=True, null=True)
    gateway = models.ForeignKey(Gateway, models.DO_NOTHING, blank=True, null=True)
    shipping = models.ForeignKey('Shipping', models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey(JhiOrder, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'node'


class NodeModules(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    light_management = models.ForeignKey(LightManagementModule, models.DO_NOTHING, unique=True, blank=True, null=True)
    energy_meter = models.ForeignKey(EnergyMeterModule, models.DO_NOTHING, unique=True, blank=True, null=True)
    twilight_management = models.ForeignKey('TwilightManagementModule', models.DO_NOTHING, unique=True, blank=True, null=True)
    motion_management = models.ForeignKey(MotionManagementModule, models.DO_NOTHING, unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'node_modules'


class Shipping(models.Model):
    id = models.BigIntegerField(primary_key=True)
    courier = models.CharField(max_length=255, blank=True, null=True)
    tracking_code = models.CharField(max_length=255, blank=True, null=True)
    shipping_date = models.CharField(max_length=255, blank=True, null=True)
    estimated_arrival = models.CharField(max_length=255, blank=True, null=True)
    transport_document = models.CharField(max_length=255, blank=True, null=True)
    is_arrived = models.BooleanField(blank=True, null=True)
    shipping_contact = models.ForeignKey(Contact, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipping'


class ShippingOrder(models.Model):
    orders = models.ForeignKey(JhiOrder, models.DO_NOTHING)
    shippings = models.ForeignKey(Shipping, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'shipping_order'
        unique_together = (('shippings', 'orders'),)


class SubscriptionType(models.Model):
    id = models.BigIntegerField(primary_key=True)
    subscription_type = models.CharField(max_length=255, blank=True, null=True)
    entity_id = models.BigIntegerField(blank=True, null=True)
    entity_uuid = models.CharField(max_length=255, blank=True, null=True)
    wanted_severity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription_type'


class SubscriptionTypeUser(models.Model):
    users = models.ForeignKey(JhiUser, models.DO_NOTHING)
    subscription_types = models.ForeignKey(SubscriptionType, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'subscription_type_user'
        unique_together = (('subscription_types', 'users'),)


class TimeSwitch(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    time_switch_active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'time_switch'


class TwilightManagementModule(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    tw_mode = models.IntegerField()
    tw_type = models.IntegerField()
    tw_group = models.IntegerField()
    valid_period = models.IntegerField()
    ths_sunset_on = models.FloatField()
    ths_sunset_off = models.FloatField()
    ths_sunrise_on = models.FloatField()
    ths_sunrise_off = models.FloatField()
    persistence_period = models.IntegerField()
    delay_offset = models.IntegerField()
    voltagem_v = models.FloatField()
    lux_measured = models.FloatField()
    sampling_period = models.IntegerField()
    number_average_measures = models.IntegerField()
    adc_in_channel = models.IntegerField()
    programming_status = models.IntegerField()
    created_timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'twilight_management_module'


class TwilightMeasure(models.Model):
    id = models.BigIntegerField(primary_key=True)
    lux_value = models.FloatField(blank=True, null=True)
    adc_value = models.FloatField(blank=True, null=True)
    measure_timestamp = models.DateTimeField(blank=True, null=True)
    twilight_management_module = models.ForeignKey(TwilightManagementModule, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'twilight_measure'


class VpnConfiguration(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    vpn_name = models.CharField(max_length=255, blank=True, null=True)
    vpn_server = models.CharField(max_length=255, blank=True, null=True)
    vpn_type = models.CharField(max_length=255)
    certificate_name = models.CharField(max_length=255)
    certificate_pwd = models.CharField(max_length=255, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_pwd = models.CharField(max_length=255, blank=True, null=True)
    vpn_ip_address = models.CharField(max_length=255, blank=True, null=True)
    pk_12_certificate = models.CharField(max_length=255, blank=True, null=True)
    vpn_configuration = models.CharField(max_length=255, blank=True, null=True)
    private_key = models.CharField(max_length=255, blank=True, null=True)
    public_key = models.CharField(max_length=255, blank=True, null=True)
    ca_certificate = models.CharField(max_length=255, blank=True, null=True)
    gateway = models.ForeignKey(Gateway, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vpn_configuration'


class WilampAlert(models.Model):
    id = models.BigIntegerField(primary_key=True)
    alert_timestamp = models.DateTimeField(blank=True, null=True)
    jhi_type = models.IntegerField(blank=True, null=True)
    severity = models.IntegerField(blank=True, null=True)
    logger_entity_id = models.CharField(max_length=255, blank=True, null=True)
    logger_name = models.CharField(max_length=255, blank=True, null=True)
    module = models.CharField(max_length=255, blank=True, null=True)
    logged_entity_id = models.CharField(max_length=255, blank=True, null=True)
    logged_entity = models.CharField(max_length=255, blank=True, null=True)
    message = models.CharField(max_length=1000, blank=True, null=True)
    jhi_comment = models.CharField(max_length=5000, blank=True, null=True)
    log_class = models.CharField(max_length=1000, blank=True, null=True)
    note = models.CharField(max_length=5000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wilamp_alert'
