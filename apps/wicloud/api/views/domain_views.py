# -*- coding: utf-8 -*-
import collections
import datetime
import dateutil.parser
from django.http import Http404, HttpResponseNotFound, HttpResponse, HttpResponseBadRequest, HttpResponseServerError

from rest_framework import generics, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)


from apps.wicloud.domain.statistics.installation import InstallationGlobalStatistics, WeeklyEnergyStatistics, \
    MonthlyEnergyStatistics
from apps.wicloud.domain.statistics.installationQueries import InstallationQueries, ObjectNotFoundException
from com.wi4b.wilamp.utilities.CommonUtils import Utils
from web.api import views
from apps.wicloud.api import serializers
from apps.wicloud import models
from django.db.models import Q, Sum, Avg, Min, Max


#https://github.com/linovia/drf-demo


class InstallationGlobalStatisticsViewSet(viewsets.ViewSet):
    # Required for the Browsable API renderer to have a nice form.
    serializer_class = serializers.InstallationGlobalStatisticsSerializer

    def retrieve(self, request, pk=None):
        try:
            import logging
            l = logging.getLogger('django.db.backends')
            l.setLevel(logging.DEBUG)
            if len(l.handlers)==0:
                l.addHandler(logging.StreamHandler())

            if "installationId" in request.query_params:
                installationId = request.query_params["installationId"]
                currentAnalyzedDate = request.query_params["currentAnalyzedDate"] if "currentAnalyzedDate" in request.query_params else datetime.datetime.utcnow().replace(hour=0,minute=0,second=0,microsecond=0)
                if isinstance(currentAnalyzedDate, str):
                    try:
                        currentAnalyzedDate = dateutil.parser.parse(request.query_params["currentAnalyzedDate"])
                    except:
                        return Response(data="currentAnalyzedDate is not in ISO DATE format", status=status.HTTP_400_BAD_REQUEST)
                installationId = request.query_params["installationId"]
                mondayPreviousWeek = (currentAnalyzedDate + datetime.timedelta(days=-currentAnalyzedDate.weekday(), weeks=-1)).replace(hour=0,minute=0,second=0,microsecond=0)
                sundayEndOfWeek = currentAnalyzedDate + datetime.timedelta(days=-currentAnalyzedDate.weekday() + 6)
                sundayEndOfWeek = sundayEndOfWeek.replace(hour=23,minute=59,second=59,microsecond=999999)
                beginningLastMonth = (currentAnalyzedDate.replace(day=1) + dateutil.relativedelta.relativedelta(months=-1)).replace(hour=0,minute=0,second=0,microsecond=0)
                endCurrentMonth = (currentAnalyzedDate.replace(day=1) + dateutil.relativedelta.relativedelta(months=+1, days=-1)).replace(hour=23,minute=59,second=59,microsecond=999999)
                startInterval = request.query_params["startInterval"] if "startInterval" in request.query_params else mondayPreviousWeek
                if isinstance(startInterval, str):
                    try:
                        startInterval = dateutil.parser.parse(request.query_params["startInterval"])
                    except:
                        return Response(data="startInterval is not in ISO DATE format", status=status.HTTP_400_BAD_REQUEST)
                endInterval = request.query_params["endInterval"] if "endInterval" in request.query_params else sundayEndOfWeek
                if isinstance(endInterval, str):
                    try:
                        endInterval = dateutil.parser.parse(request.query_params["endInterval"])
                    except:
                        return Response(data="endInterval is not in ISO DATE format", status=status.HTTP_400_BAD_REQUEST)


                installations = models.Installation.objects.all().filter(id=installationId)
                if installations.count() > 0:
                    installation = installations.first()  # type: models.Installation
                    weeklyEnergyIntervals = InstallationQueries.getWeeklyEnergyStatisticsByInstallationAndDateInterval(installationId=installationId,
                                                        startDate=mondayPreviousWeek, endDate=sundayEndOfWeek, installationObject=installation)

                    monthlyEnergyIntervals = InstallationQueries.getMonthlyEnergyStatisticsByInstallationAndDateInterval(
                        installationId=installationId,
                        startDate=beginningLastMonth, endDate=endCurrentMonth, installationObject=installation)

                    intervalEnergyStatistics = InstallationQueries.getGlobalEnergyStatistics(installationId=installationId,
                        startDate=startInterval, endDate=endInterval, installationObject=installation)

                    globalEnergyStatistics = InstallationQueries.getGlobalEnergyStatistics(
                        installationId=installationId, installationObject=installation)

                    absorbedPowerEstimation = InstallationQueries.getAbsorbedPowerEstimation(
                        installationId=installationId, calculationTimestamp=endInterval, installationObject=installation)

                    installationGlobalStatistics = InstallationGlobalStatistics()
                    installationGlobalStatistics.byWeek = weeklyEnergyIntervals
                    installationGlobalStatistics.byMonth = monthlyEnergyIntervals
                    installationGlobalStatistics.globalEnergyConsumption = globalEnergyStatistics
                    installationGlobalStatistics.currentIntervalEnergyConsumption = intervalEnergyStatistics
                    installationGlobalStatistics.absorbedPowerEstimation = absorbedPowerEstimation
                    serializer = serializers.InstallationGlobalStatisticsSerializer(instance=installationGlobalStatistics)
                    return Response(serializer.data)

                else:
                    Response(data="Could not find installation with id {}".format(installationId), status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(data="Missing parameter installationId", status=status.HTTP_400_BAD_REQUEST)

        except KeyError as ex:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ObjectNotFoundException as ex:
            return Response(data=ex.message, status=status.HTTP_404_NOT_FOUND)


