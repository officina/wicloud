from typing import List, Optional

from apps.wicloud.domain.base import BaseDomainEntity


class InstallationGlobalStatistics(BaseDomainEntity):
    def __init__(self, **kwargs):
        self.globalEnergyConsumption = None #type: IntervalEnergyStatistics
        self.currentIntervalEnergyConsumption = None #type: IntervalEnergyStatistics
        self.absorbedPowerEstimation = None #type: AbsorbedPowerEstimation
        self.byWeek = [] #type: List[Optional[WeeklyEnergyStatistics]]
        self.byMonth = []  #type: List[Optional[MonthlyEnergyStatistics]]
        super(InstallationGlobalStatistics, self).__init__(**kwargs)

class IntervalEnergyStatistics(BaseDomainEntity):
    def __init__(self, **kwargs):
        self.startIntervalTimestamp = None
        self.endIntervalTimestamp = None
        self.sumEnergy = 0.0
        self.sumEnergyWithoutDim = 0.0
        self.sumEnergyWithoutControl = 0.0
        self.sumEnergyOldLamps = 0.0
        self.lastMeasureIntervalTimestamp = None
        super(IntervalEnergyStatistics, self).__init__(**kwargs)

class AbsorbedPowerEstimation(BaseDomainEntity):
    def __init__(self, **kwargs):
        self.countMeasures = 0
        self.startIntervalTimestamp = None
        self.endIntervalTimestamp = None
        self.avgDimLevel = 0.0
        self.avgAdc0Value = 0.0
        self.avgAdc1Value = 0.0
        self.sumActivePower = 0.0
        self.sumEnergy = 0.0
        self.sumEnergyWithoutDim = 0.0
        self.sumEnergyWithoutControl = 0.0
        self.sumEnergyOldLamps = 0.0
        self.lastMeasureIntervalTimestamp = None
        super(AbsorbedPowerEstimation, self).__init__(**kwargs)

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
