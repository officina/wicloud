# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from web.core.models import UserModel, DateModel, StatusModel, OrderedModel, CleanModel


class Address(CleanModel, UserModel, DateModel, StatusModel, OrderedModel):


    fullName = models.CharField(max_length=255, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    houseNumber = models.CharField(max_length=255, blank=True, null=True)
    zipCode = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    lat = models.CharField(max_length=255, blank=True, null=True)
    lng = models.CharField(max_length=255, blank=True, null=True)
    timezoneCode = models.CharField(max_length=255, blank=True, null=True)

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
        return f'{self.description}'


class Customer(CleanModel, UserModel, DateModel, StatusModel, OrderedModel):

    companyName = models.CharField(max_length=255, null=True)


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
    lightManagementModule = models.ForeignKey('Light_management_module', models.DO_NOTHING, blank=True, null=True)
    installation = models.ForeignKey('Installation', models.DO_NOTHING, blank=True, null=True)
    startInterval = models.DateTimeField(blank=True, null=True)
    endInterval = models.DateTimeField(blank=True, null=True)
    startIintervalMeasureTimestamp = models.DateTimeField(blank=True, null=True)
    endIntervalMeasureTimestamp = models.DateTimeField(blank=True, null=True)
    activePower = models.FloatField(blank=True, null=True)
    reactivePower = models.FloatField(blank=True, null=True)
    startIntervalActiveEnergyCounterValue = models.FloatField(blank=True, null=True)
    endIntervalActiveEnergyCounterValue = models.FloatField(blank=True, null=True)
    activeEnergy = models.FloatField(blank=True, null=True)
    startIntervalReactiveEnergyCounterValue = models.FloatField(blank=True, null=True)
    endIntervalReactiveEnergyCounterValue = models.FloatField(blank=True, null=True)
    reactiveEnergy = models.FloatField(blank=True, null=True)
    activeEnergyMty0 = models.FloatField(blank=True, null=True)
    activeEnergyMty1 = models.FloatField(blank=True, null=True)
    activeEnergyMty2 = models.FloatField(blank=True, null=True)
    activeEnergyMty3 = models.FloatField(blank=True, null=True)
    activeEnergyWithoutDim = models.FloatField(blank=True, null=True)
    activeEnergyWithoutControl = models.FloatField(blank=True, null=True)
    activeEnergyOldLamps = models.FloatField(blank=True, null=True)
    burningTime = models.FloatField(blank=True, null=True)
    nodeLife = models.FloatField(blank=True, null=True)

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

    name = models.CharField(max_length=255,  blank=True, null=True)

    iacCalibration = models.FloatField(blank=True, null=True)
    vacCalibration = models.FloatField(blank=True, null=True)
    patCalibration = models.FloatField(blank=True, null=True)
    preCalibration = models.CharField(max_length=255, blank=True, null=True)
    nominalPower = models.FloatField(blank=True, null=True)
    oldLampPower = models.FloatField(blank=True, null=True)
    powerLosses = models.FloatField(blank=True, null=True)

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
    nodeDate = models.CharField(max_length=255, blank=True, null=True)
    nodeHms = models.CharField(max_length=255, blank=True, null=True)
    vacRmsLow = models.FloatField(blank=True, null=True)
    vacRmsHigh = models.FloatField(blank=True, null=True)
    vacPeak = models.FloatField(blank=True, null=True)
    vacRMSAbsoluteMax = models.FloatField(blank=True, null=True)
    vacRMSAbsoluteMin = models.FloatField(blank=True, null=True)
    iacHigh = models.FloatField(blank=True, null=True)
    iacLow = models.FloatField(blank=True, null=True)
    iacPeak = models.FloatField(blank=True, null=True)
    iacHH = models.FloatField(blank=True, null=True)
    iacLL = models.FloatField(blank=True, null=True)
    measureTimestamp = models.DateTimeField(blank=True, null=True)
    createdTimestamp = models.DateTimeField(blank=True, null=True)
    sourceModule = models.CharField(max_length=255, blank=True, null=True)
    installation = models.ForeignKey('Installation', models.DO_NOTHING, blank=True, null=True)
    energyMeterModule = models.ForeignKey(Energy_meter_module, models.DO_NOTHING, blank=True, null=True)

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

    errorTimestamp = models.DateTimeField(blank=True, null=True)
    errorResolvedTimestamp = models.DateTimeField(blank=True, null=True)
    isInError = models.BooleanField(blank=True, default=False)
    lightLevelValue = models.FloatField(blank=True, null=True)
    adcValue = models.FloatField(blank=True, null=True)
    activePower = models.FloatField(blank=True, null=True)
    current = models.FloatField(blank=True, null=True)
    voltage = models.FloatField(blank=True, null=True)
    loggedEntity = models.BigIntegerField(blank=True, null=True)
    loggedEntityMac = models.CharField(max_length=255, blank=True, null=True)
    entityJson = models.CharField(max_length=255, blank=True, null=True)

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

    errorTimestamp = models.DateTimeField(blank=True, null=True)
    errorResolvedTimestamp = models.DateTimeField(blank=True, null=True)
    isInError = models.BooleanField(blank=True, default=False)
    lightLevelValue = models.FloatField(blank=True, null=True)
    adcValue = models.FloatField(blank=True, null=True)
    activePower = models.FloatField(blank=True, null=True)
    current = models.FloatField(blank=True, null=True)
    voltage = models.FloatField(blank=True, null=True)
    loggedEntity = models.BigIntegerField(blank=True, null=True)
    loggedEntityMac = models.CharField(max_length=255, blank=True, null=True)
    entityJson = models.CharField(max_length=255, blank=True, null=True)

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

    errorTimestamp = models.DateTimeField(blank=True, null=True)
    errorResolvedTimestamp = models.DateTimeField(blank=True, null=True)
    isInError = models.BooleanField(blank=True, default=False)
    loggedEntity = models.BigIntegerField(blank=True, null=True)
    loggedEntityMac = models.CharField(max_length=255, blank=True, null=True)
    entityJson = models.CharField(max_length=255, blank=True, null=True)

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

    gatewayUUID = models.CharField(unique=True, max_length=255,null=True)
    gatewayHostname = models.CharField(max_length=255, blank=True, null=True)
    gatewayType = models.IntegerField(blank=True,  null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    creationDate = models.DateTimeField(blank=True, null=True)
    serialNumber = models.CharField(unique=True, max_length=255, blank=True, null=True)
    deviceName = models.CharField(max_length=255, blank=True, null=True)
    hardwareModel = models.CharField(max_length=255, blank=True, null=True)
    macAddress = models.CharField(max_length=255, blank=True, null=True)
    coordinatorMac = models.CharField(max_length=255, blank=True, null=True)
    fileNameEncryptionInfo = models.CharField(max_length=255, blank=True, null=True)
    hardwareInformations = models.CharField(max_length=255, blank=True, null=True)
    readyToReceiveData = models.BooleanField(blank=True, default=False)
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
        return f'{self.description}'


class Ime_power_counter(CleanModel, UserModel, DateModel, StatusModel, OrderedModel):

    name = models.CharField(max_length=255, blank=True, null=True)

    gatewayUUID = models.CharField(max_length=255, blank=True, null=True)
    installation = models.ForeignKey('Installation', models.DO_NOTHING, blank=True, null=True)
    counterId = models.CharField(unique=True, max_length=255, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    rs485bus = models.CharField(max_length=255, blank=True, null=True)
    rs485address = models.CharField(max_length=255, blank=True, null=True)
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

    powerCounterId = models.CharField(max_length=255, blank=True, null=True)
    jhiTimestamp = models.DateTimeField(blank=True, null=True)
    installation = models.ForeignKey('Installation', models.DO_NOTHING, blank=True, null=True)
    voltage = models.FloatField(blank=True, null=True)
    current = models.FloatField(blank=True, null=True)
    activePower = models.FloatField(blank=True, null=True)
    powerFactor = models.FloatField(blank=True, null=True)
    powerFactorSector = models.FloatField(blank=True, null=True)
    freq = models.FloatField(blank=True, null=True)
    activeEnergy = models.FloatField(blank=True, null=True)
    partialActiveEnergy = models.FloatField(blank=True, null=True)
    operatingTimeCounter = models.FloatField(blank=True, null=True)
    imePowerCounter = models.ForeignKey(Ime_power_counter, models.DO_NOTHING, blank=True, null=True)

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

    preparationDate = models.DateTimeField(blank=True, null=True)
    installationDate = models.DateTimeField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    address = models.OneToOneField(Address, models.DO_NOTHING,  blank=True, null=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)

    installer = models.ForeignKey(User, models.SET_NULL, related_name='installator', blank=True, null=True)
    viewers = models.ManyToManyField(User, related_name='viewers', blank=True)
    installationManagers = models.ManyToManyField(User, related_name='installation_managers', blank=True)
    assetsManagers = models.ManyToManyField(User, related_name='assets_manager', blank=True)

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
        return f'{self.description}'

    @property
    def is_installer(self, user: User):
        return user == self.installer

    def is_installation_manager(self, user: User):
        for installation_manager in self.installation_managers:
            if installation_manager == user:
                return True
        return False

    def is_viewer(self, user: User):
        for viewer in self.viewers:
            if viewer == user:
                return True
        return False

    def is_assets_manager(self, user: User):
        for assets_manager in self.assets_managers:
            if assets_manager == user:
                return True
        return False


class Light_management_measure(CleanModel, UserModel, DateModel, StatusModel, OrderedModel):

    mac = models.CharField(max_length=255, blank=True, null=True)
    processingStatus = models.IntegerField(blank=True, null=True)
    nodeHMS = models.CharField(max_length=255, blank=True, null=True)
    dayOfYear = models.IntegerField(blank=True, null=True)
    measureType = models.IntegerField(blank=True, null=True)
    parentNode = models.CharField(max_length=255, blank=True, null=True)
    lqi = models.FloatField(blank=True, null=True)
    vac = models.FloatField(blank=True, null=True)
    vcc = models.FloatField(blank=True, null=True)
    iac = models.FloatField(blank=True, null=True)
    activePower = models.FloatField(blank=True, null=True)
    reactivePower = models.FloatField(blank=True, null=True)
    activeEnergyCounter = models.FloatField(blank=True, null=True)
    reactiveEnergyCounter = models.FloatField(blank=True, null=True)
    lightLevel = models.FloatField(blank=True, null=True)
    pw0 = models.FloatField(blank=True, null=True)
    pw1 = models.FloatField(blank=True, null=True)
    pw2 = models.FloatField(blank=True, null=True)
    pw3 = models.FloatField(blank=True, null=True)
    nodeTemp = models.FloatField(blank=True, null=True)
    ad0 = models.FloatField(blank=True, null=True)
    ad1 = models.FloatField(blank=True, null=True)
    ad2 = models.FloatField(blank=True, null=True)
    ad3 = models.FloatField(blank=True, null=True)
    packetsSent = models.IntegerField(blank=True, null=True)
    packetsReceived = models.IntegerField(blank=True, null=True)
    packetsLost = models.IntegerField(blank=True, null=True)
    motionStatus = models.IntegerField(blank=True, null=True)
    manualStatus = models.IntegerField(blank=True, null=True)
    statusBitmask = models.IntegerField(blank=True, null=True)
    parametersCRC = models.FloatField(blank=True, null=True)
    profileCRC = models.FloatField(blank=True, null=True)
    measureTimestamp = models.DateTimeField(blank=True, null=True)
    createdTimestamp = models.DateTimeField(blank=True, null=True)
    sourceModule = models.CharField(max_length=255, blank=True, null=True)
    nodeFwVersion = models.CharField(max_length=255, blank=True, null=True)
    lampLife = models.FloatField(blank=True, null=True)
    nodeLife = models.FloatField(blank=True, null=True)
    activePowerCounter = models.FloatField(blank=True, null=True)
    installation = models.ForeignKey('Installation', models.DO_NOTHING, blank=True, null=True)
    lightManagementModule = models.ForeignKey('Light_management_module', models.DO_NOTHING, blank=True, null=True)

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
    deviceType = models.IntegerField(blank=True, null=True)
    lampType = models.IntegerField(blank=True, null=True)
    timerAutoMode = models.IntegerField(blank=True, null=True)
    timerHPSProtection = models.IntegerField(blank=True, null=True)
    lightZone = models.IntegerField(blank=True, null=True)
    lightProfileId = models.BigIntegerField(blank=True, null=True)
    lightProfileCRC = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name = _('light_management_module')
        verbose_name_plural = _('light_management_modules')
        ordering = ('ordering',)
        permissions = (
            ("list_light_management_module", "Can list light_management_module"),
            ("detail_light_management_module", "Can detail light_management_module"),
            ("disable_light_management_module", "Can disable light_management_module"),
        )

    def __str__(self):
        return f'{self.name}'


class Light_profile(CleanModel, UserModel, DateModel, StatusModel, OrderedModel):

    name = models.CharField(max_length=255, blank=True, null=True)

    jhiType = models.CharField(max_length=255, blank=True, null=True)
    reference = models.CharField(max_length=255, blank=True, null=True)
    profileCRC = models.FloatField(blank=True, null=True)
    lightProfileId = models.IntegerField(blank=True, null=True)
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

    don = models.IntegerField(blank=True, null=True)
    dof = models.IntegerField(blank=True, null=True)
    ton = models.CharField(max_length=255, blank=True, null=True)
    tof = models.CharField(max_length=255, blank=True, null=True)
    eas = models.BooleanField(blank=True, default=False)
    ecr = models.BooleanField(blank=True, default=False)
    emo = models.BooleanField(blank=True, default=False)
    edw = models.IntegerField(blank=True, null=True)
    enabled = models.BooleanField(blank=True, default=False)
    lightProfileIndex = models.IntegerField(blank=True, null=True)
    pw0 = models.FloatField(blank=True, null=True)
    pw1 = models.FloatField(blank=True, null=True)
    pw2 = models.FloatField(blank=True, null=True)
    pw3 = models.FloatField(blank=True, null=True)
    fadeIn = models.FloatField(blank=True, null=True)
    fadeOut = models.FloatField(blank=True, null=True)
    slot = models.IntegerField(blank=True, null=True)
    createdTimestamp = models.DateTimeField(blank=True, null=True)
    motionDuration = models.FloatField(blank=True, null=True)
    motionDelay = models.FloatField(blank=True, null=True)
    mi0 = models.FloatField(blank=True, null=True)
    mi1 = models.FloatField(blank=True, null=True)
    mi2 = models.FloatField(blank=True, null=True)
    mi3 = models.FloatField(blank=True, null=True)
    motionFadeIn = models.FloatField(blank=True, null=True)
    motionFadeOut = models.FloatField(blank=True, null=True)
    lightProfile = models.ForeignKey(Light_profile, models.DO_NOTHING, blank=True, null=True)


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
    motionMode = models.IntegerField(blank=True, null=True)
    motionGroup = models.IntegerField(blank=True, null=True)
    motionBroadcast = models.IntegerField(blank=True, null=True)
    measureTimestamp = models.DateTimeField(blank=True, null=True)
    motionManagementModule = models.ForeignKey('Motion_management_module', models.DO_NOTHING, blank=True, null=True)

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

    nodeType = models.IntegerField(blank=True, null=True)
    mac = models.CharField(unique=True, max_length=255, blank=True, null=True)
    logTimeIst = models.IntegerField(blank=True, null=True)
    logTime0 = models.IntegerField(blank=True, null=True)
    logTime1 = models.IntegerField(blank=True, null=True)
    logTime2 = models.IntegerField(blank=True, null=True)
    logTime3 = models.IntegerField(blank=True, null=True)
    timeZone = models.IntegerField(blank=True, null=True)
    timeZoneCode = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.DecimalField(null=True,
                                    blank=True,
                                    decimal_places=15,
                                    max_digits=19,
                                    default=0)
    longitude = models.DecimalField(null=True,
                                    blank=True,
                                    decimal_places=15,
                                    max_digits=19,
                                    default=0)
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

    @property
    def location_field_indexing(self):
        """Location for indexing.

        Used in Elasticsearch indexing/tests of `geo_distance` native filter.
        """
        return {
            'lat': self.latitude,
            'lon': self.longitude,
        }


class Node_module(CleanModel, UserModel, DateModel, StatusModel, OrderedModel):

    name = models.CharField(max_length=255, blank=True, null=True)
    lightManagement = models.OneToOneField(Light_management_module, models.DO_NOTHING,  blank=True, null=True)
    energyMeter = models.OneToOneField(Energy_meter_module, models.DO_NOTHING,  blank=True, null=True)
    twilightManagement = models.OneToOneField('Twilight_management_module', models.DO_NOTHING,  blank=True,
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

    alertTimestamp = models.DateTimeField(blank=True, null=True)
    jhi_type = models.IntegerField(blank=True, null=True)
    severity = models.IntegerField(blank=True, null=True)
    loggerEntityId = models.CharField(max_length=255, blank=True, null=True)
    loggerName = models.CharField(max_length=255, blank=True, null=True)
    module = models.CharField(max_length=255, blank=True, null=True)
    loggedEntityId = models.CharField(max_length=255, blank=True, null=True)
    loggedEntity = models.CharField(max_length=255, blank=True, null=True)
    message = models.CharField(max_length=1000, blank=True, null=True)
    comment = models.CharField(max_length=5000, blank=True, null=True)
    logClass = models.CharField(max_length=1000, blank=True, null=True)
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

    referenceCode = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    maxPower = models.FloatField(blank=True, null=True)

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

    twMode = models.IntegerField(blank=True, null=True)
    twType = models.IntegerField(blank=True, null=True)
    twGroup = models.IntegerField(blank=True, null=True)
    validPeriod = models.IntegerField(blank=True, null=True)
    thsSunsetOn = models.FloatField(blank=True, null=True)
    thsSunsetOff = models.FloatField(blank=True, null=True)
    thsSunriseOn = models.FloatField(blank=True, null=True)
    thsSunriseOff = models.FloatField(blank=True, null=True)
    persistencePeriod = models.IntegerField(blank=True, null=True)
    delayOffset = models.IntegerField(blank=True, null=True)
    voltagemV = models.FloatField(blank=True, null=True)
    luxMeasured = models.FloatField(blank=True, null=True)
    samplingPeriod = models.IntegerField(blank=True, null=True)
    numberAverageMeasures = models.IntegerField(blank=True, null=True)
    adcInChannel = models.IntegerField(blank=True, null=True)
    programmingStatus = models.IntegerField(blank=True, null=True)
    createdTimestamp = models.DateTimeField(blank=True, null=True)

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

    luxValue = models.FloatField(blank=True, null=True)
    adcValue = models.FloatField(blank=True, null=True)
    measureTimestamp = models.DateTimeField(blank=True, null=True)
    twilightManagementModule = models.ForeignKey(Twilight_management_module, models.DO_NOTHING, blank=True, null=True)

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

    motionMode = models.IntegerField(blank=True, null=True)
    motionType = models.IntegerField(blank=True, null=True)
    motionGroup = models.IntegerField(blank=True, null=True)
    delayAfter = models.FloatField(default=0)
    retriggerTime = models.FloatField(blank=True, null=True)
    triggerDelay = models.FloatField(blank=True, null=True)
    mi0 = models.FloatField(blank=True, null=True)
    mi1 = models.FloatField(blank=True, null=True)
    mi2 = models.FloatField(blank=True, null=True)
    mi3 = models.FloatField(blank=True, null=True)
    fadeIn = models.FloatField(default=0)
    fadeOut = models.FloatField(default=0)
    createdTimestamp = models.DateTimeField(blank=True, null=True)
    adcInChannel = models.IntegerField(blank=True, null=True)
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



