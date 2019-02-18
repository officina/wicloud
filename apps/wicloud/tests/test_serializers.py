from typing import List, Optional

from test_plus.test import TestCase

from apps.wicloud.api.serializers import InstallationGlobalStatisticsSerializer
from apps.wicloud.domain.statistics.installation import InstallationGlobalStatistics, WeeklyEnergyStatistics, \
    MonthlyEnergyStatistics


class TestInstallationGlobalStatisticsSerializer(TestCase):

    def test_InstallationGlobalStatisticsSerializer(self):

        serializer = InstallationGlobalStatisticsSerializer(data={"byWeek":[{"weekNumber":1,"dayOfWeek":1,"hour":0,"activePowerAverage":0,"reactivePowerAverage":0,"activeEnergy":0,"reactiveEnergy":0,"activeEnergyWithoutDim":0,"activeEnergyWithoutControl":0,"activeEnergyOldLamps":0,"burningTime":0,"nodeLife":0}],"byMonth":[{"month":1,"day":1,"activePowerAverage":0,"reactivePowerAverage":0,"activeEnergy":0,"reactiveEnergy":0,"activeEnergyWithoutDim":0,"activeEnergyWithoutControl":0,"activeEnergyOldLamps":0,"burningTime":0,"nodeLife":0}]})
        assert serializer.is_valid()
        output = serializer.save()
        assert isinstance(output, InstallationGlobalStatistics)
        assert isinstance(output.byWeek[0], WeeklyEnergyStatistics)
        assert isinstance(output.byMonth[0], MonthlyEnergyStatistics)
        assert output.byWeek[0].weekNumber == 1
        assert output.byWeek[0].dayOfWeek == 1
        assert output.byMonth[0].month == 1
        assert output.byMonth[0].day == 1


    def test_InstallationGlobalStatisticsSerializer_reverse(self):
        installationGlobalStatistics = InstallationGlobalStatistics()
        weektest = WeeklyEnergyStatistics()
        weektest.dayOfWeek = 2
        weektest.weekNumber = 2
        monthtest = MonthlyEnergyStatistics()
        monthtest.month = 2
        monthtest.day = 2
        installationGlobalStatistics.byWeek.append(weektest)
        installationGlobalStatistics.byMonth.append(monthtest)
        serializer = InstallationGlobalStatisticsSerializer(installationGlobalStatistics)

        reverseSerializer = InstallationGlobalStatisticsSerializer(data=serializer.data)
        assert reverseSerializer.is_valid()
        output = reverseSerializer.save()
        assert isinstance(output, InstallationGlobalStatistics)
        assert isinstance(output.byWeek[0], WeeklyEnergyStatistics)
        assert isinstance(output.byMonth[0], MonthlyEnergyStatistics)
        assert output.byWeek[0].weekNumber == 2
        assert output.byWeek[0].dayOfWeek == 2
        assert output.byMonth[0].month == 2
        assert output.byMonth[0].day == 2


