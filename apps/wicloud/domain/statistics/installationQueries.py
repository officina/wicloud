import datetime

from django.db.models import Avg, Sum, Count, Max, Min

from django.db.models import Avg
from django.db.models.functions import ExtractYear, ExtractMonth, ExtractWeek, ExtractDay, ExtractWeekDay, ExtractHour

from apps.wicloud import models
from apps.wicloud.domain.base import BaseDomainEntity
from apps.wicloud.domain.statistics.installation import WeeklyEnergyStatistics, MonthlyEnergyStatistics, \
    IntervalEnergyStatistics, AbsorbedPowerEstimation


class ObjectNotFoundException(Exception):
    def __init__(self, message):
        self.message = message

class InstallationQueries(BaseDomainEntity):

    @staticmethod
    def getWeeklyEnergyStatisticsByInstallationAndDateInterval(installationId, startDate, endDate, installationObject=None):
        if not installationObject:
            installations = models.Installation.objects.all().filter(id=installationId)
            if installations.count() > 0:
                installation = installations.first()  # type: models.Installation
            else:
                raise ObjectNotFoundException("Could not find installation with id {}".format(installationId))
        else: installation = installationObject
        energyIntervals = installation.energyIntervals.annotate(year=ExtractYear('startInterval'),
                                                                weekNumber=ExtractWeek('startInterval'),
                                                                dayOfWeek=ExtractWeekDay('startInterval'),
                                                                hour=ExtractHour('startInterval'),
                                                                activePowerAverage=Avg('activePower'),
                                                                reactivePowerAverage=Avg('reactivePower'),
                                                                activeEnergySum=Sum('activeEnergy'),
                                                                reactiveEnergySum=Sum('reactiveEnergy'),
                                                                activeEnergyWithoutDimSum=Sum('activeEnergyWithoutDim'),
                                                                activeEnergyWithoutControlSum=Sum('activeEnergyWithoutControl'),
                                                                activeEnergyOldLampsSum=Sum('activeEnergyOldLamps'),
                                                                burningTimeAverage=Avg('burningTime'),
                                                                nodeLifeAverage=Avg('nodeLife')).values(
            'year', 'weekNumber', 'dayOfWeek', 'hour', "activePowerAverage", "reactivePowerAverage",'activeEnergySum','reactiveEnergySum',
            'activeEnergyWithoutDimSum','activeEnergyWithoutControlSum','activeEnergyOldLampsSum','burningTimeAverage','nodeLifeAverage'
        ).filter(startInterval__gte=startDate).filter(startInterval__lte=endDate).order_by('year', 'weekNumber', 'dayOfWeek', 'hour').annotate(count=Count('pk'))
        result = []
        for energyInterval in energyIntervals.all():
            weeklyEnergyStatistics = WeeklyEnergyStatistics(dictObject=energyInterval)
            result.append(weeklyEnergyStatistics)
            #print("Year: {} Week number:{} DayOfWeek: {} Hour: {}".format(weeklyEnergyStatistics.year, weeklyEnergyStatistics.weekNumber, weeklyEnergyStatistics.dayOfWeek, weeklyEnergyStatistics.hour))
        return result


    @staticmethod
    def getMonthlyEnergyStatisticsByInstallationAndDateInterval(installationId, startDate, endDate, installationObject=None):
        if not installationObject:
            installations = models.Installation.objects.all().filter(id=installationId)
            if installations.count() > 0:
                installation = installations.first()  # type: models.Installation
            else:
                raise ObjectNotFoundException("Could not find installation with id {}".format(installationId))
        else: installation = installationObject

        energyIntervals = installation.energyIntervals.annotate(year=ExtractYear('startInterval'),
                                                                month=ExtractMonth('startInterval'),
                                                                day=ExtractDay('startInterval'),
                                                                activePowerAverage=Avg('activePower'),
                                                                reactivePowerAverage=Avg('reactivePower'),
                                                                activeEnergySum=Sum('activeEnergy'),
                                                                reactiveEnergySum=Sum('reactiveEnergy'),
                                                                activeEnergyWithoutDimSum=Sum('activeEnergyWithoutDim'),
                                                                activeEnergyWithoutControlSum=Sum('activeEnergyWithoutControl'),
                                                                activeEnergyOldLampsSum=Sum('activeEnergyOldLamps'),
                                                                burningTimeAverage=Avg('burningTime'),
                                                                nodeLifeAverage=Avg('nodeLife')).values(
            'year', 'month', 'day', "activePowerAverage", "reactivePowerAverage",'activeEnergySum','reactiveEnergySum',
            'activeEnergyWithoutDimSum','activeEnergyWithoutControlSum','activeEnergyOldLampsSum','burningTimeAverage','nodeLifeAverage'
        ).filter(startInterval__gte=startDate).filter(startInterval__lte=endDate).order_by('year', 'month', 'day').annotate(count=Count('pk'))
        result = []
        for energyInterval in energyIntervals.all():
            monthlyEnergyStatistics = MonthlyEnergyStatistics(dictObject=energyInterval)
            result.append(monthlyEnergyStatistics)
            #print("Year: {} Week number:{} DayOfWeek: {} Hour: {}".format(weeklyEnergyStatistics.year, weeklyEnergyStatistics.weekNumber, weeklyEnergyStatistics.dayOfWeek, weeklyEnergyStatistics.hour))
        return result


    @staticmethod
    def getGlobalEnergyStatistics(installationId, startDate=None, endDate=None, installationObject=None):
        if not installationObject:
            installations = models.Installation.objects.all().filter(id=installationId)
            if installations.count() > 0:
                installation = installations.first()  # type: models.Installation
            else:
                raise ObjectNotFoundException("Could not find installation with id {}".format(installationId))
        else: installation = installationObject

        if startDate:
            energyStatistics = installation.energyIntervals.annotate(startIntervalTimestamp=Min('startInterval'),
                                                                    endIntervalTimestamp=Max('endInterval'),
                                                                    sumEnergy=Sum('activeEnergy'),
                                                                    sumEnergyWithoutDim=Sum('activeEnergyWithoutDim'),
                                                                    sumEnergyWithoutControl=Sum('activeEnergyWithoutControl'),
                                                                    sumEnergyOldLamps=Sum('activeEnergyOldLamps'),
                                                                    lastMeasureIntervalTimestamp=Max('endIntervalMeasureTimestamp')).values(
                'startIntervalTimestamp', 'endIntervalTimestamp', 'sumEnergy', 'sumEnergyWithoutDim', 'sumEnergyWithoutControl', "sumEnergyOldLamps", "lastMeasureIntervalTimestamp").filter(startInterval__gte=startDate).filter(startInterval__lte=endDate).annotate(count=Count('pk')).first()
        else:
            energyStatistics = installation.energyIntervals.annotate(startIntervalTimestamp=Min('startInterval'),
                                                                    endIntervalTimestamp=Max('endInterval'),
                                                                    sumEnergy=Sum('activeEnergy'),
                                                                    sumEnergyWithoutDim=Sum('activeEnergyWithoutDim'),
                                                                    sumEnergyWithoutControl=Sum('activeEnergyWithoutControl'),
                                                                    sumEnergyOldLamps=Sum('activeEnergyOldLamps'),
                                                                    lastMeasureIntervalTimestamp=Max('endIntervalMeasureTimestamp')).values(
                'startIntervalTimestamp', 'endIntervalTimestamp', 'sumEnergy', 'sumEnergyWithoutDim', 'sumEnergyWithoutControl', "sumEnergyOldLamps", "lastMeasureIntervalTimestamp").annotate(count=Count('pk')).first()
        intervalEnergyStatistics = IntervalEnergyStatistics(dictObject=energyStatistics)
        return intervalEnergyStatistics

    @staticmethod
    def getAbsorbedPowerEstimation(installationId, calculationTimestamp=None, installationObject=None):
        if not installationObject:
            installations = models.Installation.objects.all().filter(id=installationId)
            if installations.count() > 0:
                installation = installations.first()  # type: models.Installation
            else:
                raise ObjectNotFoundException("Could not find installation with id {}".format(installationId))
        else: installation = installationObject
        if not calculationTimestamp: calculationTimestamp = datetime.datetime.utcnow()
        calculationTimestampEndOfHour = calculationTimestamp.replace(minute=0, second=0, microsecond=0)
        calculationTimestampBeginOfHour = calculationTimestampEndOfHour + datetime.timedelta(hours=-1)
        abdsorbedPowerEstimationObj = installation.energyIntervals.annotate(countMeasures=Count('*'),
                                                                startIntervalTimestamp=Min('startInterval'),
                                                                endIntervalTimestamp=Max('endInterval'),
                                                                avgDimLevel=Avg('dimLevel'),
                                                                avgAdc0Value=Avg('adc0Value'),
                                                                avgAdc1Value=Avg('adc1Value'),
                                                                sumActivePower=Sum('activePower'),
                                                                sumEnergy=Sum('activeEnergy'),
                                                                sumEnergyWithoutDim=Sum('activeEnergyWithoutDim'),
                                                                sumEnergyWithoutControl=Sum('activeEnergyWithoutControl'),
                                                                sumEnergyOldLamps=Sum('activeEnergyOldLamps'),
                                                                lastMeasureIntervalTimestamp=Max('endIntervalMeasureTimestamp')).values(
            'countMeasures', 'startIntervalTimestamp', 'endIntervalTimestamp', 'avgDimLevel', 'avgAdc0Value', 'avgAdc1Value', 'sumActivePower', 'sumEnergy', 'sumEnergyWithoutDim', 'sumEnergyWithoutControl', "sumEnergyOldLamps", "lastMeasureIntervalTimestamp").filter(startInterval__gte=calculationTimestampBeginOfHour).filter(endInterval__lte=calculationTimestampEndOfHour).annotate(count=Count('pk')).first()
        abdsorbedPowerEstimation = AbsorbedPowerEstimation(dictObject=abdsorbedPowerEstimationObj)
        return abdsorbedPowerEstimation
