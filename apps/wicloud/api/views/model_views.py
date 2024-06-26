# -*- coding: utf-8 -*-
import collections

from django.db import transaction, IntegrityError
from django.http import Http404, HttpResponseNotFound, HttpResponse, HttpResponseBadRequest, HttpResponseServerError

from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from com.wi4b.wilamp.utilities.CommonUtils import Utils
from web.api import views
from apps.wicloud.api import serializers
from apps.wicloud import models
from django.db.models import Q

#https://dencode.com/date/iso8601

class  AddressListCreateAPIView(views.ThuxListCreateViewMixin, ListCreateAPIView):
    queryset = models.Address.objects.all()
    #permission_classes = (IsAuthenticated,)
    serializer_class = serializers.AddressListSerializer
    lookup_field = 'id'

class  AddressRetrieveUpdateDestroyAPIView(views.ThuxUpdateViewMixin, RetrieveUpdateDestroyAPIView):
    queryset = models.Address.objects.all()
    #permission_classes = (IsAuthenticated,)
    serializer_class = serializers.AddressRetrieveSerializer
    lookup_field = 'id'

class AddressSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single address
    """
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSetStatusSerializer


class AddressEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single address
    """
    queryset = models.Address.objects.filter(status=0)
    serializer_class = serializers.AddressStatusSerializer
    new_status = 1


class AddressDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single address
    """
    queryset = models.Address.objects.filter(status=1)
    serializer_class = serializers.AddressStatusSerializer
    new_status = 0

class Avg_power_measureListCreateAPIView(views.ThuxListCreateViewMixin, ListCreateAPIView):
    """
    Get all  avg_power_measures
    """
    queryset = models.Avg_power_measure.objects.all()
    serializer_class = serializers.Avg_power_measureListSerializer

    def create(self, request, *args, **kwargs):
        try:
            # with transaction.atomic():
            # Search the node the measure is belonging to
            if "mac" in request.data:
                b = models.Node.objects.filter(mac=request.data["mac"])
                try:
                   relatedNode = b.first()  #type: Node
                   if relatedNode:
                       with transaction.atomic():
                           # This code executes inside a transaction.
                           #Update nodeId etc..
                           request.data["_node"] = relatedNode.id
                           request.data["lightManagementModule"] = relatedNode.lightManagementModule.id if relatedNode.lightManagementModule else None
                           request.data["lightFixture"] = relatedNode.lightFixture.id if relatedNode.lightFixture else None
                           request.data["installation"] = relatedNode.lightFixture.installation.id if (relatedNode.lightFixture and relatedNode.lightFixture.installation) else None
                           # TODO: AT - create energy interval from measure
                           
                           #energyInterval = models.Energy_interval.objects.create(
                           # mac= request.data["mac"]
                           #)

                           serializer = self.get_serializer(data=request.data)
                           serializer.is_valid(raise_exception=True)
                           self.perform_create(serializer)
                           headers = self.get_success_headers(serializer.data)
                           result = Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
                           avgPowerMeasure = serializer.instance
                           energyInterval = models.Energy_interval.objects.create(
                                mac= request.data["mac"],
                                creator = self.user,
                                last_modifier = self.user,
                           )
                           # energyInterval.parseAvgPowerMeasure(avgPowerMeasure
                           
                           

                           result = super(Avg_power_measureListCreateAPIView, self).create(request, *args, **kwargs)
                           return result
                           #return super(Avg_power_measureListCreateAPIView, self).create(request, *args, **kwargs)

                   else:
                       return HttpResponse(content="Cannot find a node with this mac address: {}".format(request.data["mac"]), status=500)
                except ValidationError as ex:
                   raise HttpResponse(content=ex.detail, status=500)
                except Exception as ex:
                   raise HttpResponse(content=ex, status=500)
            else:
                return HttpResponse(content="Wrong number of parameters", status=500)
        except IntegrityError as err:
            return HttpResponse(content=err, status=500)

        except Exception as ex:
            return HttpResponse(content=ex, status=500)


class Avg_power_measureRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get a single avg_power_measure
    """
    queryset = models.Avg_power_measure.objects.all()
    serializer_class = serializers.Avg_power_measureRetrieveSerializer
    lookup_field = 'id'


class Avg_power_measureSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single avg_power_measure
    """
    queryset = models.Avg_power_measure.objects.all()
    serializer_class = serializers.Avg_power_measureSetStatusSerializer
    lookup_field = 'id'

class Avg_power_measureEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single avg_power_measure
    """
    queryset = models.Avg_power_measure.objects.filter(status=0)
    serializer_class = serializers.Avg_power_measureStatusSerializer
    new_status = 1


class Avg_power_measureDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single avg_power_measure
    """
    queryset = models.Avg_power_measure.objects.filter(status=1)
    serializer_class = serializers.Avg_power_measureStatusSerializer
    new_status = 0

class Connected_deviceListCreateAPIView(views.ThuxListCreateViewMixin, ListCreateAPIView):
    """
    Get all  energy_intervals
    """
    queryset = models.Connected_device.objects.all()
    serializer_class = serializers.Connected_deviceListSerializer


class Connected_deviceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get a single energy_interval
    """
    queryset = models.Connected_device.objects.all()
    serializer_class = serializers.Connected_deviceRetrieveSerializer
    lookup_field = 'id'


class Connected_deviceSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single energy_interval
    """
    queryset = models.Connected_device.objects.all()
    serializer_class = serializers.Connected_deviceSetStatusSerializer
    lookup_field = 'id'

class Connected_deviceEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single energy_interval
    """
    queryset = models.Connected_device.objects.filter(status=0)
    serializer_class = serializers.Connected_deviceStatusSerializer
    new_status = 1


class Connected_deviceDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single energy_interval
    """
    queryset = models.Connected_device.objects.filter(status=1)
    serializer_class = serializers.Connected_deviceStatusSerializer
    new_status = 0

class CustomerListCreateAPIView(views.ThuxListCreateViewMixin, ListCreateAPIView):
    """
    Get all  customers
    """
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerListSerializer
    lookup_field = 'id'

class CustomerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get a single customer
    """
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerRetrieveSerializer
    lookup_field = 'id'


class CustomerSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single customer
    """
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSetStatusSerializer


class CustomerEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single customer
    """
    queryset = models.Customer.objects.filter(status=0)
    serializer_class = serializers.CustomerStatusSerializer
    new_status = 1


class CustomerDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single customer
    """
    queryset = models.Customer.objects.filter(status=1)
    serializer_class = serializers.CustomerStatusSerializer
    new_status = 0


class Energy_intervalListCreateAPIView(views.ThuxListCreateViewMixin, ListCreateAPIView):
    """
    Get all  energy_intervals
    """
    queryset = models.Energy_interval.objects.all()
    serializer_class = serializers.Energy_intervalListSerializer


class Energy_intervalRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get a single energy_interval
    """
    queryset = models.Energy_interval.objects.all()
    serializer_class = serializers.Energy_intervalRetrieveSerializer
    lookup_field = 'id'


class Energy_intervalSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single energy_interval
    """
    queryset = models.Energy_interval.objects.all()
    serializer_class = serializers.Energy_intervalSetStatusSerializer
    lookup_field = 'id'

class Energy_intervalEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single energy_interval
    """
    queryset = models.Energy_interval.objects.filter(status=0)
    serializer_class = serializers.Energy_intervalStatusSerializer
    new_status = 1


class Energy_intervalDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single energy_interval
    """
    queryset = models.Energy_interval.objects.filter(status=1)
    serializer_class = serializers.Energy_intervalStatusSerializer
    new_status = 0


class Energy_meter_moduleListCreateAPIView(views.ThuxListCreateViewMixin, ListCreateAPIView):
    """
    Get all  energy_meter_modules
    """
    queryset = models.Energy_meter_module.objects.all()
    serializer_class = serializers.Energy_meter_moduleListSerializer
    lookup_field = 'id'

class Energy_meter_moduleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get a single energy_meter_module
    """
    queryset = models.Energy_meter_module.objects.all()
    serializer_class = serializers.Energy_meter_moduleRetrieveSerializer
    lookup_field = 'id'

class Energy_meter_moduleByMacRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get a single energy_meter_module by mac
    """
    serializer_class = serializers.Energy_meter_moduleRetrieveSerializer
    lookup_field = 'id'

    def get_object(self):
        mac = self.kwargs['id']
        user = self.request.user
        b = models.Node.objects.filter(mac=mac).select_related('energyMeterModule').order_by('-created_date')
        try:
            try:
                result = b.first()
                if result and result.energyMeterModule:
                    return result.energyMeterModule
                raise Http404()
            except:
                raise Http404()
        except:
            raise Http404()

class Energy_meter_moduleSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single energy_meter_module
    """
    queryset = models.Energy_meter_module.objects.all()
    serializer_class = serializers.Energy_meter_moduleSetStatusSerializer


class Energy_meter_moduleEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single energy_meter_module
    """
    queryset = models.Energy_meter_module.objects.filter(status=0)
    serializer_class = serializers.Energy_meter_moduleStatusSerializer
    new_status = 1


class Energy_meter_moduleDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single energy_meter_module
    """
    queryset = models.Energy_meter_module.objects.filter(status=1)
    serializer_class = serializers.Energy_meter_moduleStatusSerializer
    new_status = 0


class Energy_meter_peak_measureListCreateAPIView(views.ThuxListCreateViewMixin, ListCreateAPIView):
    """
    Get all  energy_meter_peak_measures
    """
    queryset = models.Energy_meter_peak_measure.objects.all()
    serializer_class = serializers.Energy_meter_peak_measureListSerializer
    lookup_field = 'id'

class Energy_meter_peak_measureRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get a single energy_meter_peak_measure
    """
    queryset = models.Energy_meter_peak_measure.objects.all()
    serializer_class = serializers.Energy_meter_peak_measureRetrieveSerializer
    lookup_field = 'id'


class Energy_meter_peak_measureSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single energy_meter_peak_measure
    """
    queryset = models.Energy_meter_peak_measure.objects.all()
    serializer_class = serializers.Energy_meter_peak_measureSetStatusSerializer


class Energy_meter_peak_measureEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single energy_meter_peak_measure
    """
    queryset = models.Energy_meter_peak_measure.objects.filter(status=0)
    serializer_class = serializers.Energy_meter_peak_measureStatusSerializer
    new_status = 1


class Energy_meter_peak_measureDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single energy_meter_peak_measure
    """
    queryset = models.Energy_meter_peak_measure.objects.filter(status=1)
    serializer_class = serializers.Energy_meter_peak_measureStatusSerializer
    new_status = 0


class Error_light_level_and_adc_mismatchListCreateAPIView(views.ThuxListCreateViewMixin, ListCreateAPIView):
    """
    Get all  error_light_level_and_adc_mismatchs
    """
    queryset = models.Error_light_level_and_adc_mismatch.objects.all()
    serializer_class = serializers.Error_light_level_and_adc_mismatchListSerializer
    lookup_field = 'id'

class Error_light_level_and_adc_mismatchRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get a single error_light_level_and_adc_mismatch
    """
    queryset = models.Error_light_level_and_adc_mismatch.objects.all()
    serializer_class = serializers.Error_light_level_and_adc_mismatchRetrieveSerializer
    lookup_field = 'id'


class Error_light_level_and_adc_mismatchSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single error_light_level_and_adc_mismatch
    """
    queryset = models.Error_light_level_and_adc_mismatch.objects.all()
    serializer_class = serializers.Error_light_level_and_adc_mismatchSetStatusSerializer


class Error_light_level_and_adc_mismatchEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single error_light_level_and_adc_mismatch
    """
    queryset = models.Error_light_level_and_adc_mismatch.objects.filter(status=0)
    serializer_class = serializers.Error_light_level_and_adc_mismatchStatusSerializer
    new_status = 1


class Error_light_level_and_adc_mismatchDisableView(
        views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single error_light_level_and_adc_mismatch
    """
    queryset = models.Error_light_level_and_adc_mismatch.objects.filter(status=1)
    serializer_class = serializers.Error_light_level_and_adc_mismatchStatusSerializer
    new_status = 0


class Error_light_level_and_power_mismatchListCreateAPIView(views.ThuxListCreateViewMixin, ListCreateAPIView):
    """
    Get all  error_light_level_and_power_mismatchs
    """
    queryset = models.Error_light_level_and_power_mismatch.objects.all()
    serializer_class = serializers.Error_light_level_and_power_mismatchListSerializer
    lookup_field = 'id'

class Error_light_level_and_power_mismatchRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get a single error_light_level_and_power_mismatch
    """
    queryset = models.Error_light_level_and_power_mismatch.objects.all()
    serializer_class = serializers.Error_light_level_and_power_mismatchRetrieveSerializer
    lookup_field = 'id'

class Error_light_level_and_power_mismatchSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single error_light_level_and_power_mismatch
    """
    queryset = models.Error_light_level_and_power_mismatch.objects.all()
    serializer_class = serializers.Error_light_level_and_power_mismatchSetStatusSerializer


class Error_light_level_and_power_mismatchEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single error_light_level_and_power_mismatch
    """
    queryset = models.Error_light_level_and_power_mismatch.objects.filter(status=0)
    serializer_class = serializers.Error_light_level_and_power_mismatchStatusSerializer
    new_status = 1


class Error_light_level_and_power_mismatchDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single error_light_level_and_power_mismatch
    """
    queryset = models.Error_light_level_and_power_mismatch.objects.filter(status=1)
    serializer_class = serializers.Error_light_level_and_power_mismatchStatusSerializer
    new_status = 0


class Error_node_offlineListCreateAPIView(views.ThuxListCreateViewMixin, ListCreateAPIView):
    """
    Get all  error_node_offlines
    """
    queryset = models.Error_node_offline.objects.all()
    serializer_class = serializers.Error_node_offlineListSerializer
    lookup_field = 'id'

class Error_node_offlineRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get a single error_node_offline
    """
    queryset = models.Error_node_offline.objects.all()
    serializer_class = serializers.Error_node_offlineRetrieveSerializer
    lookup_field = 'id'


class Error_node_offlineSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single error_node_offline
    """
    queryset = models.Error_node_offline.objects.all()
    serializer_class = serializers.Error_node_offlineSetStatusSerializer


class Error_node_offlineEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single error_node_offline
    """
    queryset = models.Error_node_offline.objects.filter(status=0)
    serializer_class = serializers.Error_node_offlineStatusSerializer
    new_status = 1


class Error_node_offlineDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single error_node_offline
    """
    queryset = models.Error_node_offline.objects.filter(status=1)
    serializer_class = serializers.Error_node_offlineStatusSerializer
    new_status = 0


class GatewayListCreateAPIView(views.ThuxListCreateViewMixin, ListCreateAPIView):
    """
    Get all  gateways
    """
    queryset = models.Gateway.objects.all()
    serializer_class = serializers.GatewayListSerializer
    lookup_field = 'id'

class GatewayRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get a single gateway
    """
    queryset = models.Gateway.objects.all()
    serializer_class = serializers.GatewayRetrieveSerializer
    lookup_field = 'id'

class GatewayBySerialNumberRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get a single energy_meter_module by mac
    """
    serializer_class = serializers.GatewayRetrieveSerializer
    lookup_field = 'id'

    def get_object(self):
        serial = self.kwargs['id']
        b = models.Gateway.objects.filter(serialNumber=serial)
        try:
            result = b.first()
            if result: return result
            raise Http404()
        except:
            raise Http404()


class GatewayByInstallationListAPIView(views.ThuxListCreateViewMixin, ListCreateAPIView):
    """
    Get all  gateways by installation
    """
    queryset = models.Gateway.objects.all()
    serializer_class = serializers.GatewayListSerializer
    lookup_field = 'id'

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        installationId = int(self.kwargs["id"])
        return models.Gateway.objects.filter(installation=installationId)

class GatewaySetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single gateway
    """
    queryset = models.Gateway.objects.all()
    serializer_class = serializers.GatewaySetStatusSerializer


class GatewayEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single gateway
    """
    queryset = models.Gateway.objects.filter(status=0)
    serializer_class = serializers.GatewayStatusSerializer
    new_status = 1


class GatewayDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single gateway
    """
    queryset = models.Gateway.objects.filter(status=1)
    serializer_class = serializers.GatewayStatusSerializer
    new_status = 0


class Ime_power_counterListCreateAPIView(views.ThuxListCreateViewMixin, ListCreateAPIView):
    """
    Get all  ime_power_counters
    """
    queryset = models.Ime_power_counter.objects.all()
    serializer_class = serializers.Ime_power_counterListSerializer
    lookup_field = 'id'

class Ime_power_counterRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get a single ime_power_counter
    """
    queryset = models.Ime_power_counter.objects.all()
    serializer_class = serializers.Ime_power_counterRetrieveSerializer
    lookup_field = 'id'

class Ime_power_counterSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single ime_power_counter
    """
    queryset = models.Ime_power_counter.objects.all()
    serializer_class = serializers.Ime_power_counterSetStatusSerializer


class Ime_power_counterEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single ime_power_counter
    """
    queryset = models.Ime_power_counter.objects.filter(status=0)
    serializer_class = serializers.Ime_power_counterStatusSerializer
    new_status = 1


class Ime_power_counterDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single ime_power_counter
    """
    queryset = models.Ime_power_counter.objects.filter(status=1)
    serializer_class = serializers.Ime_power_counterStatusSerializer
    new_status = 0


class Ime_power_measureListCreateAPIView(views.ThuxListCreateViewMixin, ListCreateAPIView):
    """
    Get all  ime_power_measures
    """
    queryset = models.Ime_power_measure.objects.all()
    serializer_class = serializers.Ime_power_measureListSerializer
    lookup_field = 'id'

class Ime_power_measureRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get a single ime_power_measure
    """
    queryset = models.Ime_power_measure.objects.all()
    serializer_class = serializers.Ime_power_measureRetrieveSerializer
    lookup_field = 'id'


class Ime_power_measureSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single ime_power_measure
    """
    queryset = models.Ime_power_measure.objects.all()
    serializer_class = serializers.Ime_power_measureSetStatusSerializer


class Ime_power_measureEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single ime_power_measure
    """
    queryset = models.Ime_power_measure.objects.filter(status=0)
    serializer_class = serializers.Ime_power_measureStatusSerializer
    new_status = 1


class Ime_power_measureDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single ime_power_measure
    """
    queryset = models.Ime_power_measure.objects.filter(status=1)
    serializer_class = serializers.Ime_power_measureStatusSerializer
    new_status = 0


class InstallationListCreateAPIView(views.ThuxListCreateViewMixin, ListCreateAPIView):
    """
    Get all  installations
    """
    serializer_class = serializers.InstallationListSerializer
    lookup_field = 'id'

    def get_queryset(self):
        queryset = models.Installation.objects.all()
        user = self.request.user
        return queryset.distinct().filter(Q(installer=user) | Q(installationManagers__in=[user]) | Q(viewers__in=[user])
                               | Q(assetsManagers__in=[user]))


class InstallationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get a single installation
    """
    queryset = models.Installation.objects.all()
    serializer_class = serializers.InstallationRetrieveSerializer
    lookup_field = 'id'


class InstallationSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single installation
    """
    queryset = models.Installation.objects.all()
    serializer_class = serializers.InstallationSetStatusSerializer


class InstallationEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single installation
    """
    queryset = models.Installation.objects.filter(status=0)
    serializer_class = serializers.InstallationStatusSerializer
    new_status = 1


class InstallationDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single installation
    """
    queryset = models.Installation.objects.filter(status=1)
    serializer_class = serializers.InstallationStatusSerializer
    new_status = 0

class Light_fixtureListCreateAPIView(views.ThuxListCreateViewMixin, ListCreateAPIView):
    """
    Get all  light_fixtures
    """
    queryset = models.Light_fixture.objects.all()
    serializer_class = serializers.Light_fixtureListSerializer
    lookup_field = 'id'

class Light_fixtureRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get a single light_fixture
    """
    queryset = models.Light_fixture.objects.all()
    serializer_class = serializers.Light_fixtureRetrieveSerializer
    lookup_field = 'id'

class Light_fixtureBySerialNumberRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get a single energy_meter_module by mac
    """
    serializer_class = serializers.Light_fixtureRetrieveSerializer
    lookup_field = 'id'

    def get_object(self):
        serial = self.kwargs['id']
        b = models.Light_fixture.objects.filter(serialNumber=serial)
        try:
            result = b.first()
            if result: return result
            raise Http404()
        except:
            raise Http404()

class Light_fixtureByInstallationListAPIView(views.ThuxListCreateViewMixin, ListCreateAPIView):
    """
    Get all  gateways by installation
    """
    queryset = models.Light_fixture.objects.all()
    serializer_class = serializers.Light_fixtureListSerializer
    lookup_field = 'id'

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        installationId = int(self.kwargs["id"])
        return models.Light_fixture.objects.filter(installation=installationId)


class Light_fixtureSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single light_fixture
    """
    queryset = models.Light_fixture.objects.all()
    serializer_class = serializers.Light_fixtureSetStatusSerializer


class Light_fixtureEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single light_fixture
    """
    queryset = models.Light_fixture.objects.filter(status=0)
    serializer_class = serializers.Light_fixtureStatusSerializer
    new_status = 1


class Light_fixtureDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single light_fixture
    """
    queryset = models.Light_fixture.objects.filter(status=1)
    serializer_class = serializers.Light_fixtureStatusSerializer
    new_status = 0

class Light_management_measureListCreateAPIView(views.ThuxListCreateViewMixin, ListCreateAPIView):
    """
    Get all  light_management_measures
    """
    queryset = models.Light_management_measure.objects.all()
    serializer_class = serializers.Light_management_measureListSerializer
    lookup_field = 'id'

class Light_management_measureRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get a single light_management_measure
    """
    queryset = models.Light_management_measure.objects.all()
    serializer_class = serializers.Light_management_measureRetrieveSerializer
    lookup_field = 'id'


class Light_management_measureSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single light_management_measure
    """
    queryset = models.Light_management_measure.objects.all()
    serializer_class = serializers.Light_management_measureSetStatusSerializer


class Light_management_measureEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single light_management_measure
    """
    queryset = models.Light_management_measure.objects.filter(status=0)
    serializer_class = serializers.Light_management_measureStatusSerializer
    new_status = 1


class Light_management_measureDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single light_management_measure
    """
    queryset = models.Light_management_measure.objects.filter(status=1)
    serializer_class = serializers.Light_management_measureStatusSerializer
    new_status = 0


class Light_management_moduleListCreateAPIView(views.ThuxListCreateViewMixin, ListCreateAPIView):
    """
    Get all  light_management_module
    """
    queryset = models.Light_management_module.objects.all()
    serializer_class = serializers.Light_management_moduleListSerializer
    lookup_field = 'id'

class Light_management_moduleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get a single light_management_module
    """
    queryset = models.Light_management_module.objects.all()
    serializer_class = serializers.Light_management_moduleRetrieveSerializer
    lookup_field = 'id'

class Light_management_moduleByMacRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get a single energy_meter_module by mac
    """
    serializer_class = serializers.Light_management_moduleRetrieveSerializer
    lookup_field = 'id'

    def get_object(self):
        mac = self.kwargs['id']
        user = self.request.user
        b = models.Node.objects.filter(mac=mac).select_related('lightManagementModule').order_by('-created_date')
        try:
            result = b.first()
            if result.lightManagementModule != None:
                return result.lightManagementModule
            raise Http404()
        except:
            raise Http404()

class Light_management_moduleSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single light_management_module
    """
    queryset = models.Light_management_module.objects.all()
    serializer_class = serializers.Light_management_moduleSetStatusSerializer


class Light_management_moduleEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single light_management_module
    """
    queryset = models.Light_management_module.objects.filter(status=0)
    serializer_class = serializers.Light_management_moduleStatusSerializer
    new_status = 1


class Light_management_moduleDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single light_management_module
    """
    queryset = models.Light_management_module.objects.filter(status=1)
    serializer_class = serializers.Light_management_moduleStatusSerializer
    new_status = 0


class Light_profile_replace_slots_CreateView(views.ThuxStatusViewMixin, generics.CreateAPIView):
    """
    Enable a single light_management_module
    """
    queryset = models.Light_management_module.objects.filter(status=1)
    serializer_class = serializers.Light_management_moduleStatusSerializer
    new_status = 0
    def create(self, request, *args, **kwargs):
        try:
            #Retrieve light profile
            light_profile_id = kwargs['id']

            light_profile = models.Light_profile.objects.filter(id=light_profile_id).first()
            if not light_profile:
                return HttpResponseNotFound()
            else:
                #delete existing light profile slots
                ""
                try:
                    models.Light_profile_slot.objects.filter(lightProfile=light_profile_id).delete()
                except Exception as ex:
                    print("Exce {}".format(ex))
                for lightProfileSlotDict in request.data:
                    try:
                        lightProfileSlot = models.Light_profile_slot(**lightProfileSlotDict)
                        lightProfileSlot.creator = request.user
                        lightProfileSlot.last_modifier = request.user
                        lightProfileSlot.lightProfile = light_profile
                        lightProfileSlot.eas = True if Utils.isTrue(lightProfileSlot.eas) else False
                        lightProfileSlot.ecr = True if Utils.isTrue(lightProfileSlot.ecr) else False
                        lightProfileSlot.emo = True if Utils.isTrue(lightProfileSlot.emo) else False
                        lightProfileSlot.edw = int(lightProfileSlot.edw)
                        lightProfileSlot.enabled = True if Utils.isTrue(lightProfileSlot.enabled) else False
                        lightProfileSlot.save()
                    except Exception as ex:
                        print ("Exception {}".format(ex))
                        return HttpResponseServerError(ex)
                return HttpResponse(status=200)
        except:
            raise Http404()


class Light_profileListCreateAPIView(views.ThuxListCreateViewMixin, ListCreateAPIView):
    """
    Get all  light_profiles
    """
    queryset = models.Light_profile.objects.all()
    serializer_class = serializers.Light_profileListSerializer
    lookup_field = 'id'


class Light_profileRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get a single light_profile
    """
    queryset = models.Light_profile.objects.all()
    serializer_class = serializers.Light_profileRetrieveSerializer
    lookup_field = 'id'

class Light_profileByReferenceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get a single energy_meter_module by mac
    """
    serializer_class = serializers.Light_profileRetrieveSerializer
    lookup_field = 'id'

    def get_object(self):
        reference = self.kwargs['id']
        user = self.request.user
        b = models.Light_profile.objects.filter(reference=reference)
        try:
            result =  b.first()
            if result:
                return result
            raise Http404()
        except:
            raise Http404()




class Light_profileSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single light_profile
    """
    queryset = models.Light_profile.objects.all()
    serializer_class = serializers.Light_profileSetStatusSerializer


class Light_profileEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single light_profile
    """
    queryset = models.Light_profile.objects.filter(status=0)
    serializer_class = serializers.Light_profileStatusSerializer
    new_status = 1


class Light_profileDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single light_profile
    """
    queryset = models.Light_profile.objects.filter(status=1)
    serializer_class = serializers.Light_profileStatusSerializer
    new_status = 0


class Light_profile_slotListCreateAPIView(views.ThuxListCreateViewMixin, ListCreateAPIView):
    """
    Get all  light_profile_slots
    """
    queryset = models.Light_profile_slot.objects.all()
    serializer_class = serializers.Light_profile_slotListSerializer
    lookup_field = 'id'

class Light_profile_slotRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get a single light_profile_slot
    """
    queryset = models.Light_profile_slot.objects.all()
    serializer_class = serializers.Light_profile_slotRetrieveSerializer
    lookup_field = 'id'


class Light_profile_slotSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single light_profile_slot
    """
    queryset = models.Light_profile_slot.objects.all()
    serializer_class = serializers.Light_profile_slotSetStatusSerializer


class Light_profile_slotEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single light_profile_slot
    """
    queryset = models.Light_profile_slot.objects.filter(status=0)
    serializer_class = serializers.Light_profile_slotStatusSerializer
    new_status = 1


class Light_profile_slotDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single light_profile_slot
    """
    queryset = models.Light_profile_slot.objects.filter(status=1)
    serializer_class = serializers.Light_profile_slotStatusSerializer
    new_status = 0


class Motion_eventListCreateAPIView(views.ThuxListCreateViewMixin, ListCreateAPIView):
    """
    Get all  motion_events
    """
    queryset = models.Motion_event.objects.all()
    serializer_class = serializers.Motion_eventListSerializer
    lookup_field = 'id'

class Motion_eventRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get a single motion_event
    """
    queryset = models.Motion_event.objects.all()
    serializer_class = serializers.Motion_eventRetrieveSerializer
    lookup_field = 'id'


class Motion_eventSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single motion_event
    """
    queryset = models.Motion_event.objects.all()
    serializer_class = serializers.Motion_eventSetStatusSerializer


class Motion_eventEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single motion_event
    """
    queryset = models.Motion_event.objects.filter(status=0)
    serializer_class = serializers.Motion_eventStatusSerializer
    new_status = 1


class Motion_eventDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single motion_event
    """
    queryset = models.Motion_event.objects.filter(status=1)
    serializer_class = serializers.Motion_eventStatusSerializer
    new_status = 0


class NodeListCreateAPIView(views.ThuxListCreateViewMixin, ListCreateAPIView):
    """
    Get all  nodes
    """
    queryset = models.Node.objects.all()
    serializer_class = serializers.NodeListSerializer
    lookup_field = 'id'

class NodeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get a single node
    """
    queryset = models.Node.objects.all()
    serializer_class = serializers.NodeRetrieveSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class NodeByMacRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get a single energy_meter_module by mac
    """
    serializer_class = serializers.NodeRetrieveSerializer
    lookup_field = 'id'

    def get_object(self):
        mac = self.kwargs['id']
        user = self.request.user
        b = models.Node.objects.filter(mac=mac)
        try:
            result = b.first()
            if result: return result
            raise Http404()
        except:
            raise Http404()

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class NodeSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single node
    """
    queryset = models.Node.objects.all()
    serializer_class = serializers.NodeSetStatusSerializer


class NodeEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single node
    """
    queryset = models.Node.objects.filter(status=0)
    serializer_class = serializers.NodeStatusSerializer
    new_status = 1


class NodeDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single node
    """
    queryset = models.Node.objects.filter(status=1)
    serializer_class = serializers.NodeStatusSerializer
    new_status = 0


# class Node_moduleListCreateAPIView(views.ThuxListCreateViewMixin, ListCreateAPIView):
#     """
#     Get all  node_modules
#     """
#     queryset = models.Node_module.objects.all()
#     serializer_class = serializers.Node_moduleListSerializer
#     lookup_field = 'id'
#
# class Node_moduleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     """
#     Get a single node_module
#     """
#     queryset = models.Node_module.objects.all()
#     serializer_class = serializers.Node_moduleRetrieveSerializer
#     lookup_field = 'id'
#
# class Node_moduleByMacRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     """
#     Get a single energy_meter_module by mac
#     """
#     serializer_class = serializers.Node_moduleRetrieveSerializer
#     lookup_field = 'id'
#
#     def get_object(self):
#         mac = self.kwargs['id']
#         user = self.request.user
#         b = models.Node.objects.filter(mac=mac).select_related('modules')
#         try:
#             if b.first().modules:
#                 return b.first().modules
#             else: raise Http404()
#         except:
#             raise Http404()
#
#
# class Node_moduleSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
#     """
#     Set Status for a single node_module
#     """
#     queryset = models.Node_module.objects.all()
#     serializer_class = serializers.Node_moduleSetStatusSerializer
#
#
# class Node_moduleEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
#     """
#     Enable a single node_module
#     """
#     queryset = models.Node_module.objects.filter(status=0)
#     serializer_class = serializers.Node_moduleStatusSerializer
#     new_status = 1
#
#
# class Node_moduleDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
#     """
#     Enable a single node_module
#     """
#     queryset = models.Node_module.objects.filter(status=1)
#     serializer_class = serializers.Node_moduleStatusSerializer
#     new_status = 0


class Wilamp_alertListCreateAPIView(views.ThuxListCreateViewMixin, ListCreateAPIView):
    """
    Get all  wilamp_alerts
    """
    queryset = models.Wilamp_alert.objects.all()
    serializer_class = serializers.Wilamp_alertListSerializer
    lookup_field = 'id'

class Wilamp_alertRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get a single wilamp_alert
    """
    queryset = models.Wilamp_alert.objects.all()
    serializer_class = serializers.Wilamp_alertRetrieveSerializer
    lookup_field = 'id'

class Wilamp_alertSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single wilamp_alert
    """
    queryset = models.Wilamp_alert.objects.all()
    serializer_class = serializers.Wilamp_alertSetStatusSerializer


class Wilamp_alertEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single wilamp_alert
    """
    queryset = models.Wilamp_alert.objects.filter(status=0)
    serializer_class = serializers.Wilamp_alertStatusSerializer
    new_status = 1


class Wilamp_alertDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single wilamp_alert
    """
    queryset = models.Wilamp_alert.objects.filter(status=1)
    serializer_class = serializers.Wilamp_alertStatusSerializer
    new_status = 0


class Feeder_pillarListCreateAPIView(views.ThuxListCreateViewMixin, ListCreateAPIView):
    """
    Get all  feeder_pillars
    """
    queryset = models.Feeder_pillar.objects.all()
    serializer_class = serializers.Feeder_pillarListSerializer
    lookup_field = 'id'

class Feeder_pillarRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get a single feeder_pillar
    """
    queryset = models.Feeder_pillar.objects.all()
    serializer_class = serializers.Feeder_pillarRetrieveSerializer
    lookup_field = 'id'

class Feeder_pillarSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single feeder_pillar
    """
    queryset = models.Feeder_pillar.objects.all()
    serializer_class = serializers.Feeder_pillarSetStatusSerializer


class Feeder_pillarEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single feeder_pillar
    """
    queryset = models.Feeder_pillar.objects.filter(status=0)
    serializer_class = serializers.Feeder_pillarStatusSerializer
    new_status = 1


class Feeder_pillarDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single feeder_pillar
    """
    queryset = models.Feeder_pillar.objects.filter(status=1)
    serializer_class = serializers.Feeder_pillarStatusSerializer
    new_status = 0


class Twilight_management_moduleListCreateAPIView(views.ThuxListCreateViewMixin, ListCreateAPIView):
    """
    Get all  twilight_management_modules
    """
    queryset = models.Twilight_management_module.objects.all()
    serializer_class = serializers.Twilight_management_moduleListSerializer
    lookup_field = 'id'

class Twilight_management_moduleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get a single twilight_management_module
    """
    queryset = models.Twilight_management_module.objects.all()
    serializer_class = serializers.Twilight_management_moduleRetrieveSerializer
    lookup_field = 'id'


class Twilight_management_moduleSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single twilight_management_module
    """
    queryset = models.Twilight_management_module.objects.all()
    serializer_class = serializers.Twilight_management_moduleSetStatusSerializer


class Twilight_management_moduleEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single twilight_management_module
    """
    queryset = models.Twilight_management_module.objects.filter(status=0)
    serializer_class = serializers.Twilight_management_moduleStatusSerializer
    new_status = 1


class Twilight_management_moduleDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single twilight_management_module
    """
    queryset = models.Twilight_management_module.objects.filter(status=1)
    serializer_class = serializers.Twilight_management_moduleStatusSerializer
    new_status = 0


class Twilight_measureListCreateAPIView(views.ThuxListCreateViewMixin, ListCreateAPIView):
    """
    Get all  twilight_measure
    """
    queryset = models.Twilight_measure.objects.all()
    serializer_class = serializers.Twilight_measureListSerializer
    lookup_field = 'id'

class Twilight_measureRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get a single twilight_measure
    """
    queryset = models.Twilight_measure.objects.all()
    serializer_class = serializers.Twilight_measureRetrieveSerializer
    lookup_field = 'id'


class Twilight_measureSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single twilight_measure
    """
    queryset = models.Twilight_measure.objects.all()
    serializer_class = serializers.Twilight_measureSetStatusSerializer


class Twilight_measureEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single twilight_measure
    """
    queryset = models.Twilight_measure.objects.filter(status=0)
    serializer_class = serializers.Twilight_measureStatusSerializer
    new_status = 1


class Twilight_measureDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single twilight_measure
    """
    queryset = models.Twilight_measure.objects.filter(status=1)
    serializer_class = serializers.Twilight_measureStatusSerializer
    new_status = 0


class Motion_management_moduleListCreateAPIView(views.ThuxListCreateViewMixin, ListCreateAPIView):
    """
    Get all  motion_management_modules
    """
    queryset = models.Motion_management_module.objects.all()
    serializer_class = serializers.Motion_management_moduleListSerializer
    lookup_field = 'id'

class Motion_management_moduleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Get a single motion_management_module
    """
    queryset = models.Motion_management_module.objects.all()
    serializer_class = serializers.Motion_management_moduleRetrieveSerializer
    lookup_field = 'id'

class Motion_management_moduleSetStatusView(views.ThuxUpdateViewMixin, generics.UpdateAPIView):
    """
    Set Status for a single motion_management_module
    """
    queryset = models.Motion_management_module.objects.all()
    serializer_class = serializers.Motion_management_moduleSetStatusSerializer


class Motion_management_moduleEnableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single motion_management_module
    """
    queryset = models.Motion_management_module.objects.filter(status=0)
    serializer_class = serializers.Motion_management_moduleStatusSerializer
    new_status = 1


class Motion_management_moduleDisableView(views.ThuxStatusViewMixin, generics.RetrieveUpdateAPIView):
    """
    Enable a single motion_management_module
    """
    queryset = models.Motion_management_module.objects.filter(status=1)
    serializer_class = serializers.Motion_management_moduleStatusSerializer
    new_status = 0


class UserChangePasswordView(generics.UpdateAPIView):
    serializer_class = serializers.ChangePasswordSerializer

    def get_object(self, queryset=None):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response("Success.", status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from apps.wicloud.documents import *
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer





from apps.wicloud.documents import InstallationDocument
from apps.wicloud.api.serializers import InstallationDocumentSerializer
from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_TERMS,
    LOOKUP_FILTER_RANGE,
    LOOKUP_FILTER_PREFIX,
    LOOKUP_FILTER_WILDCARD,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
    LOOKUP_QUERY_EXCLUDE,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    IdsFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    SearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet

from apps.wicloud.documents import InstallationDocument, GatewayDocument, NodeDocument
from apps.wicloud.api.serializers import InstallationDocumentSerializer, GatewayDocumentSerializer, NodeDocumentSerializer

class InstallationSearchView(BaseDocumentViewSet):
    """The InstallationDocument view."""

    document = InstallationDocument
    serializer_class = InstallationDocumentSerializer

    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]
    # Define search fields
    search_fields = (
        'name',
        'description',
        'notes',
    )
    # Define filter fields
    filter_fields = {
        'id': {
            'field': 'id',
            # Note, that we limit the lookups of id field in this example,
            # to `range`, `in`, `gt`, `gte`, `lt` and `lte` filters.
            'lookups': [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_IN,
            ],
        },
        'name': {
            'field': 'name.raw',
            'lookups': [
                LOOKUP_FILTER_TERMS,
                LOOKUP_FILTER_PREFIX,
                LOOKUP_FILTER_WILDCARD,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_EXCLUDE,
            ],

        },
        'description': {
            'field': 'description.raw',
            'lookups': [
                LOOKUP_FILTER_TERMS,
                LOOKUP_FILTER_PREFIX,
                LOOKUP_FILTER_WILDCARD,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_EXCLUDE,
            ],

        },
        'notes': {
            'field': 'notes.raw',
            'lookups': [
                LOOKUP_FILTER_TERMS,
                LOOKUP_FILTER_PREFIX,
                LOOKUP_FILTER_WILDCARD,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_EXCLUDE,
            ],

        },


    }
    # Define ordering fields
    ordering_fields = {
        'id': 'id',
        'name': 'name.raw',
        'description': 'description.raw',
        'notes': 'notes.raw',

    }
    # Specify default ordering
    ordering = ('id',)

class GatewaySearchView(BaseDocumentViewSet):
    """The Gateway search view."""

    document = GatewayDocument
    serializer_class = GatewayDocumentSerializer

    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]
    # Define search fields
    search_fields = (
        'name',
        'description',
        'notes',
    )
    # Define filter fields
    filter_fields = {
        'id': {
            'field': 'id',
            # Note, that we limit the lookups of id field in this example,
            # to `range`, `in`, `gt`, `gte`, `lt` and `lte` filters.
            'lookups': [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_IN,
            ],
        },
        'name': {
            'field': 'name.raw',
            'lookups': [
                LOOKUP_FILTER_TERMS,
                LOOKUP_FILTER_PREFIX,
                LOOKUP_FILTER_WILDCARD,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_EXCLUDE,
            ],

        },
        'description': {
            'field': 'description.raw',
            'lookups': [
                LOOKUP_FILTER_TERMS,
                LOOKUP_FILTER_PREFIX,
                LOOKUP_FILTER_WILDCARD,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_EXCLUDE,
            ],

        },
        'notes': {
            'field': 'notes.raw',
            'lookups': [
                LOOKUP_FILTER_TERMS,
                LOOKUP_FILTER_PREFIX,
                LOOKUP_FILTER_WILDCARD,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_EXCLUDE,
            ],

        },


    }
    # Define ordering fields
    ordering_fields = {
        'id': 'id',
        'name': 'name.raw',
        'description': 'description.raw',
        'notes': 'notes.raw',

    }
    # Specify default ordering
    ordering = ('id',)

class NodeSearchView(BaseDocumentViewSet):
    """The Node search view."""

    document = NodeDocument
    serializer_class = NodeDocumentSerializer

    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]
    # Define search fields
    search_fields = (
        'name',
        'description',
        'notes',
    )
    # Define filter fields
    filter_fields = {
        'id': {
            'field': 'id',
            # Note, that we limit the lookups of id field in this example,
            # to `range`, `in`, `gt`, `gte`, `lt` and `lte` filters.
            'lookups': [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_IN,
            ],
        },
        'name': {
            'field': 'name.raw',
            'lookups': [
                LOOKUP_FILTER_TERMS,
                LOOKUP_FILTER_PREFIX,
                LOOKUP_FILTER_WILDCARD,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_EXCLUDE,
            ],

        },
        'description': {
            'field': 'description.raw',
            'lookups': [
                LOOKUP_FILTER_TERMS,
                LOOKUP_FILTER_PREFIX,
                LOOKUP_FILTER_WILDCARD,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_EXCLUDE,
            ],

        },
        'notes': {
            'field': 'notes.raw',
            'lookups': [
                LOOKUP_FILTER_TERMS,
                LOOKUP_FILTER_PREFIX,
                LOOKUP_FILTER_WILDCARD,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_EXCLUDE,
            ],

        },


    }
    # Define ordering fields
    ordering_fields = {
        'id': 'id',
        'name': 'name.raw',
        'description': 'description.raw',
        'notes': 'notes.raw',

    }
    # Specify default ordering
    ordering = ('id',)


