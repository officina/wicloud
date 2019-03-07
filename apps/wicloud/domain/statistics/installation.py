from typing import List, Optional

from apps.wicloud.domain.base import BaseDomainEntity


class InstallationGlobalStatistics(BaseDomainEntity):
    def __init__(self):
        self.byWeek = [] #type: List[Optional[WeeklyEnergyStatistics]]
        self.byMonth = []  #type: List[Optional[MonthlyEnergyStatistics]]
        super(InstallationGlobalStatistics, self).__init__(**kwargs)

class WeeklyEnergyStatistics(BaseDomainEntity):
    def __init__(self, **kwargs):
        self.year = 0
        self.weekNumber = 0
        self.dayOfWeek = 0
        self.hour = 0
        self.activePowerAverage = 0.0
        self.reactivePowerAverage = 0.0
        self.activeEnergySum = 0.0
        self.reactiveEnergySum = 0.0
        self.activeEnergyWithoutDimSum = 0.0
        self.activeEnergyWithoutControlSum = 0.0
        self.activeEnergyOldLampsSum = 0.0
        self.burningTimeAverage = 0.0
        self.nodeLifeAverage = 0.0
        super(WeeklyEnergyStatistics, self).__init__(**kwargs)



class MonthlyEnergyStatistics(BaseDomainEntity):
    def __init__(self, **kwargs):
        self.year = 0
        self.month = 0
        self.day = 0
        self.activePowerAverage = 0.0
        self.reactivePowerAverage = 0.0
        self.activeEnergySum = 0.0
        self.reactiveEnergySum = 0.0
        self.activeEnergyWithoutDimSum = 0.0
        self.activeEnergyWithoutControlSum = 0.0
        self.activeEnergyOldLampsSum = 0.0
        self.burningTimeAverage = 0.0
        self.nodeLifeAverage = 0.0
        super(MonthlyEnergyStatistics, self).__init__(**kwargs)
