from django.db.models import Avg, Sum, Count

from django.db.models import Avg
from django.db.models.functions import ExtractYear, ExtractMonth, ExtractWeek, ExtractDay, ExtractWeekDay, ExtractHour

from apps.wicloud import models
from apps.wicloud.domain.base import BaseDomainEntity
from apps.wicloud.domain.statistics.installation import WeeklyEnergyStatistics, MonthlyEnergyStatistics



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

