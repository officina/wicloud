import {BaseEntity} from '../../_models/base-entity';

export class InstallationWilamp implements BaseEntity {
    constructor(
        public id?: number,
        public name?: string,
        public description?: string,
        public preparationDate?: any,
        public installationDate?: any,
        public notes?: string,
        public addressAddressDescription?: string,
        public addressId?: number,
        public customerCompanyName?: string,
        public customerId?: number,
        public gateways?: BaseEntity[],
    ) {
    }
}

export class InstallationRuntimeParameters implements BaseEntity {
    constructor(
        public id?: number,
        public installationId?: number,
        public startInterval?: any,
        public endInterval?: any,
        public averageDimLevel?: number,
        public averageActivePower?: number,
        public maximumActivePower?: number,
        public minimumActivePower?: number,
        public totalActivePower?: number,
        public averageBurningTime?: number,
        public currentPeriodPowerConsumption?: number,
        public currentPeriodOldLampsPowerConsumption?: number,
        public allTimePowerCosumption?: number,
        public allTimeOldLampsPowerCosumption?: number,
        public energySaved?: number,
        public co2Saved?: number,
        public actualSaving?: number,
        public savingTrget?: number,
        public numberOfAlerts?: number,
        public lightPoles?: BaseEntity[],
        public lastMeasures?: BaseEntity[],
        public gateways?: BaseEntity[],
    ) {
    }
}

export class EnergyStatistics implements BaseEntity {
    constructor(
        public id?: number,
        public globalEnergyConsumption?: GlobalStatistics,
        public currentIntervalEnergyConsumption?: GlobalStatistics,
        public statisticsByLightManagemenentId?: Map<number, EnergyStatisticsByResourceId>,
        public statisticsByNodeId?: Map<number, EnergyStatisticsByResourceId>,
        public energyStatisticsByWeekNumberDayOfWeekAndHour?: EnergyStatisticsRowByInterval[][][],
        public energyStatisticsByYearMonthAndDayOfMonthDTOS?: EnergyStatisticsRowByInterval[][][],
        public statisticsByDayOfWeek?: EnergyStatisticsRowByInterval[][],
        public statisticsByWeekNumber?: Map<number, Map<number, EnergyStatisticsRowByInterval>>,
        public statisticsOfTodayByHour?: EnergyStatisticsRowByInterval[],
        public statisticsOfTodayByDayOfWeek?: EnergyStatisticsRowByInterval[],
        public statisticsOfLastWeekByDayOfWeek?: EnergyStatisticsRowByInterval[],
        public statisticsOfTodayByDayOfMonth?: EnergyStatisticsRowByInterval[],
        public statisticsOfLastMonthByDayOfMonth?: EnergyStatisticsRowByInterval[],
    ) {
    }
}

export class EnergyStatisticsRowByInterval implements BaseEntity {
    constructor(
        public id?: number,
        public day?: number,
        public dayOfWeek?: number,
        public month?: number,
        public year?: number,
        public weekNumber?: number,
        public hour?: number,
        public sumEnergy?: number,
        public sumEnergyWithoutDim?: number,
        public sumEnergyWithoutControl?: number,
        public sumEnergyOldLamps?: number,
        public measureCount?: number,
        public activePower?: number,
        public burningTime?: number,
    ) {
    }
}

export class EnergyStatisticsByResourceId implements BaseEntity {
    constructor(
        public id?: number,
        public lightManagementModuleId?: number,
        public nodeId?: number,
        public sumEnergy?: number,
        public sumEnergyWithoutDim?: number,
        public sumEnergyWithoutControl?: number,
        public sumEnergyOldLamps?: number,
        public measureCount?: number,
        public activePower?: number,
        public avgPower?: number,
        public lightLevel?: number,
        public nominalPower?: number,
        public burningTime?: number,
        public nodeLife?: number,
        public lastMeasureTimestamp?: Date,
    ) {
    }
}

export class GlobalStatistics implements BaseEntity {
    constructor(
        public id?: number,
        public sumEnergy?: number,
        public sumEnergyWithoutDim?: number,
        public sumEnergyWithoutControl?: number,
        public sumEnergyOldLamps?: number,
        public burningTime?: number,
        public lastIntervalTimestamp?: Date,
    ) {
    }
}
