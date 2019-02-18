from typing import List, Optional

from test_plus.test import TestCase
import logging
l = logging.getLogger('django.db.backends')
l.setLevel(logging.DEBUG)
l.addHandler(logging.StreamHandler())

from apps.wicloud.api.serializers import InstallationGlobalStatisticsSerializer
from apps.wicloud.domain.statistics.installation import InstallationGlobalStatistics, WeeklyEnergyStatistics, \
    MonthlyEnergyStatistics
from apps.wicloud.domain.statistics.installationQueries import InstallationQueries

l = logging.getLogger('django.db.backends')
l.setLevel(logging.DEBUG)
l.addHandler(logging.StreamHandler())

class TestInstallationQueries(TestCase):

    def loadInstallation(self):
        ""
    def test_getWeeklyEnergyStatisticsByInstallationAndDateInterval(self):
        installationId = 2
        data = InstallationQueries.getWeeklyEnergyStatisticsByInstallationAndDateInterval(installationId=installationId)

