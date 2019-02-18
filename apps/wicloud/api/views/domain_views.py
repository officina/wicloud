# -*- coding: utf-8 -*-
import collections
import datetime

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
                today = datetime.date.today()
                datetime_object = today
                mondayPreviousWeek = datetime_object + datetime.timedelta(days=-datetime_object.weekday(), weeks=-1)
                sundayEndOfWeek = datetime_object + datetime.timedelta(days=-datetime_object.weekday() + 6)

                installations = models.Installation.objects.all().filter(id=installationId)
                if installations.count() > 0:
                    installation = installations.first()  # type: models.Installation
                    weeklyEnergyIntervals = InstallationQueries.getWeeklyEnergyStatisticsByInstallationAndDateInterval(installationId=installationId,
                                                        startDate=mondayPreviousWeek, endDate=sundayEndOfWeek, installationObject=installation)

                    monthlyEnergyIntervals = InstallationQueries.getMonthlyEnergyStatisticsByInstallationAndDateInterval(
                        installationId=installationId,
                        startDate=mondayPreviousWeek, endDate=sundayEndOfWeek, installationObject=installation)
                    installationGlobalStatistics = InstallationGlobalStatistics()
                    installationGlobalStatistics.byWeek = weeklyEnergyIntervals
                    installationGlobalStatistics.byMonth = monthlyEnergyIntervals
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


