import {
    AbsorbedPowerEstimation,
    EnergyStatisticsByResourceId,
    EnergyStatisticsRowByInterval,
    InstallationWilamp,
} from '../../pages/installation-wilamp/installation-wilamp.model';
import {CustomerWilamp} from '../../pages/customer-wilamp';
import {AddressWilamp} from '../../pages/address-wilamp';
import {NodeWilamp} from '../../pages/node-wilamp';
import {GatewayWilamp} from '../../pages/gateway-wilamp';
import {Helpers} from '../helpers';
import {LightFixtureWilamp} from '../../pages/light-fixture-wilamp';

/**
 * TODO: Implement with https://netbasal.com/introducing-akita-a-new-state-management-pattern-for-angular-applications-f2f0fab5a8
 * Interval Energy consumption could contain sub intervals, in the content variable.
 * This is useful to model, for example, the statisticsByWeek, where data contains the vector with the values of each day of week and
 * average and total contains the value of the measures of the full week.
 * In this case content variable will contain 7 IntervalEnergyConsumptions each with the daily consumption, where data contains the vector with
 * the values for each hour of that day and average and total the sum of the measures of the full day.
 */

export interface IIntervalEnergyConsumptionParams {
        day?: number,
        dayOfWeek?: number,
        month?: number,
        year?: number,
        weekNumber?: number,
        hour?: number,
        numberOfSubIntervalForAverage?: number,
        energyStatisticRow?: EnergyStatisticsRowByInterval,
}

export class IntervalEnergyConsumption {
    public data = [];
    public activePowerAverage = 0.0;
    public burningTimeAverage = 0.0;
    public burningTimeTotal = 0.0;
    public activeEnergyAverage = 0.0;
    public activeEnergyTotal = 0.0;
    public activeEnergyWithoutDimAverage = 0.0;
    public activeEnergyWithoutDimTotal = 0.0;
    public activeEnergyWithoutControlAverage = 0.0;
    public activeEnergyWithoutControlTotal = 0.0;
    public activeEnergyOldLampsAverage = 0.0;
    public activeEnergyOldLampsTotal = 0.0;
    public timestamp = null;
    public content: Map<number, IntervalEnergyConsumption> = new Map<number, IntervalEnergyConsumption>();
    public numberOfSubIntervalForAverage = 0;
    public day: number;
    public dayOfWeek: number;
    public month: number;
    public year: number;
    public weekNumber: number;
    public hour: number;

    constructor(
        params?: IIntervalEnergyConsumptionParams,
    ) {
        if (params.energyStatisticRow) {
            this.day = params.energyStatisticRow.day;
            this.dayOfWeek = params.energyStatisticRow.dayOfWeek;
            this.month = params.energyStatisticRow.month;
            this.year = params.energyStatisticRow.year;
            this.weekNumber = params.energyStatisticRow.weekNumber;
            this.hour = params.energyStatisticRow.hour;
            this.activePowerAverage = params.energyStatisticRow.activePowerAverage;
            this.burningTimeAverage = params.energyStatisticRow.burningTimeAverage;
            this.burningTimeTotal = params.energyStatisticRow.burningTimeAverage;
            this.activeEnergyAverage = params.energyStatisticRow.activeEnergySum;
            this.activeEnergyTotal = params.energyStatisticRow.activeEnergySum;
            this.activeEnergyWithoutDimAverage = params.energyStatisticRow.activeEnergyWithoutDimSum;
            this.activeEnergyWithoutDimTotal = params.energyStatisticRow.activeEnergyWithoutDimSum;
            this.activeEnergyWithoutControlAverage = params.energyStatisticRow.activeEnergyWithoutControlSum;
            this.activeEnergyWithoutControlTotal = params.energyStatisticRow.activeEnergyWithoutControlSum;
            this.activeEnergyOldLampsAverage = params.energyStatisticRow.activeEnergyOldLampsSum;
            this.activeEnergyOldLampsTotal = params.energyStatisticRow.activeEnergyOldLampsSum;
        }

        /* Override date/time informations if present */
        if (params.day != null) { this.day = params.day; }
        if (params.dayOfWeek != null) { this.dayOfWeek = params.dayOfWeek; }
        if (params.month != null) { this.month = params.month; }
        if (params.year != null) { this.year = params.year; }
        if (params.weekNumber != null) { this.weekNumber = params.weekNumber; }
        if (params.hour != null) { this.hour = params.hour; }
        if (params.numberOfSubIntervalForAverage != null) { this.numberOfSubIntervalForAverage = params.numberOfSubIntervalForAverage; }
    }

    static populateAveragesFromSubIntervals(intervalEnergyConsumption: IntervalEnergyConsumption): IntervalEnergyConsumption {
        if (intervalEnergyConsumption.content.size > 0) {
            intervalEnergyConsumption.content.forEach( subintervalEnergyConsumption => {
                if (subintervalEnergyConsumption.content.size > 0) {
                    const tempInterval = IntervalEnergyConsumption.populateAveragesFromSubIntervals(subintervalEnergyConsumption);
                    intervalEnergyConsumption.burningTimeAverage += tempInterval.burningTimeTotal / intervalEnergyConsumption.numberOfSubIntervalForAverage;
                    intervalEnergyConsumption.burningTimeTotal += tempInterval.burningTimeTotal;
                    intervalEnergyConsumption.activePowerAverage += tempInterval.activePowerAverage / intervalEnergyConsumption.numberOfSubIntervalForAverage;
                    intervalEnergyConsumption.activeEnergyAverage += tempInterval.activeEnergyTotal / intervalEnergyConsumption.numberOfSubIntervalForAverage;
                    intervalEnergyConsumption.activeEnergyTotal += tempInterval.activeEnergyTotal;
                    intervalEnergyConsumption.activeEnergyWithoutDimAverage += tempInterval.activeEnergyWithoutDimTotal / intervalEnergyConsumption.numberOfSubIntervalForAverage;
                    intervalEnergyConsumption.activeEnergyWithoutDimTotal += tempInterval.activeEnergyWithoutDimTotal;
                    intervalEnergyConsumption.activeEnergyWithoutControlAverage += tempInterval.activeEnergyWithoutControlTotal / intervalEnergyConsumption.numberOfSubIntervalForAverage;
                    intervalEnergyConsumption.activeEnergyWithoutControlTotal += tempInterval.activeEnergyWithoutControlTotal;
                    intervalEnergyConsumption.activeEnergyOldLampsAverage += tempInterval.activeEnergyOldLampsTotal / intervalEnergyConsumption.numberOfSubIntervalForAverage;
                    intervalEnergyConsumption.activeEnergyOldLampsTotal += tempInterval.activeEnergyOldLampsTotal;
                    return tempInterval;
                } else {
                    intervalEnergyConsumption.burningTimeAverage += subintervalEnergyConsumption.burningTimeTotal / intervalEnergyConsumption.numberOfSubIntervalForAverage;
                    intervalEnergyConsumption.burningTimeTotal += subintervalEnergyConsumption.burningTimeTotal;
                    intervalEnergyConsumption.activePowerAverage += subintervalEnergyConsumption.activePowerAverage / intervalEnergyConsumption.numberOfSubIntervalForAverage;
                    intervalEnergyConsumption.activeEnergyAverage += subintervalEnergyConsumption.activeEnergyTotal / intervalEnergyConsumption.numberOfSubIntervalForAverage;
                    intervalEnergyConsumption.activeEnergyTotal += subintervalEnergyConsumption.activeEnergyTotal;
                    intervalEnergyConsumption.activeEnergyWithoutDimAverage += subintervalEnergyConsumption.activeEnergyWithoutDimTotal / intervalEnergyConsumption.numberOfSubIntervalForAverage;
                    intervalEnergyConsumption.activeEnergyWithoutDimTotal += subintervalEnergyConsumption.activeEnergyWithoutDimTotal;
                    intervalEnergyConsumption.activeEnergyWithoutControlAverage += subintervalEnergyConsumption.activeEnergyWithoutControlTotal / intervalEnergyConsumption.numberOfSubIntervalForAverage;
                    intervalEnergyConsumption.activeEnergyWithoutControlTotal += subintervalEnergyConsumption.activeEnergyWithoutControlTotal;
                    intervalEnergyConsumption.activeEnergyOldLampsAverage += subintervalEnergyConsumption.activeEnergyOldLampsTotal / intervalEnergyConsumption.numberOfSubIntervalForAverage;
                    intervalEnergyConsumption.activeEnergyOldLampsTotal += subintervalEnergyConsumption.activeEnergyOldLampsTotal;
                }
            });
        }
        return intervalEnergyConsumption;
    }
}

export class IntervalEnergyConsumptionAverages {
    public activePowerAverage = 0.0;
    public burningTimeAverage = 0.0;
    public burningTimeTotal = 0.0;
    public activeEnergyAverage = 0.0;
    public activeEnergyTotal = 0.0;
    public activeEnergyWithoutDimAverage = 0.0;
    public activeEnergyWithoutDimTotal = 0.0;
    public activeEnergyWithoutControlAverage = 0.0;
    public activeEnergyWithoutControlTotal = 0.0;
    public activeEnergyOldLampsAverage = 0.0;
    public activeEnergyOldLampsTotal = 0.0;
}



export class RangeInterval {
    public min = 0.0;
    public max = 0.0;
    public average = 0.0;
}

export class ValueWithTimeContainer {
    public entityLabel = '';
    public current = 0.0;
    public lastMonth = 0.0;
    public total = 0.0;
}

export class StatisticsByMonth {
    private statisticsByMonth = new Map<string, IntervalEnergyConsumption>();

    has(key: string) {
        return this.statisticsByMonth.has(key);
    }

    set(key: string, value: IntervalEnergyConsumption) {
        return this.statisticsByMonth.set(key, value);
    }

    get(key: string): IntervalEnergyConsumption {
        return this.statisticsByMonth.get(key);
    }

    updateWithIntervalEnergyConsumption(value: EnergyStatisticsRowByInterval) {
        const key = value.year + '_' + value.month;
        let statisticsByMonth = new IntervalEnergyConsumption();
        if (this.statisticsByMonth.has(key)) {
            statisticsByMonth = this.statisticsByMonth.get(key);
        }

    }
}

export class InstallationEnergyStatistics {
    public installation: InstallationWilamp;

    /**
     * Key is in the form YEAR-WeekNumber e.g. statisticsByWeek['2018-39']
     */
    public statisticsByWeek = new Map<string, IntervalEnergyConsumption>();
    public statisticsByMonth = new StatisticsByMonth();
    public absorbedPowerEstimation = new AbsorbedPowerEstimation();
    public lastMeasureReceivedTimestamp: Date;
    public totalEnergyConsumption = 0.0;
    public totalEnergyConsumptionWithoutDimming = 0.0;
    public totalEnergyConsumptionWithoutControl = 0.0;
    public totalEnergyConsumptionOldInstallation = 0.0;
    public energySavel = new(ValueWithTimeContainer);
    public co2Saved = new(ValueWithTimeContainer);
    public burningTime = new RangeInterval();

    getStatisticsOfCurrentMonth(date: Date) {
        const currentMonthKey = date.getFullYear() + '_' + (date.getMonth() + 1);
        if (this.statisticsByMonth.has(currentMonthKey)) {
            return this.statisticsByMonth.get(currentMonthKey);
        } else { return null; }

    }

    getStatisticsOfPreviousMonth(date: Date) {
        const previousMonth = new Date(date);
        previousMonth.setMonth(previousMonth.getMonth() - 1);
        const previousMonthKey = previousMonth.getFullYear() + '_' + (previousMonth.getMonth() + 1);
        if (this.statisticsByMonth.has(previousMonthKey)) {
            return this.statisticsByMonth.get(previousMonthKey);
        } else { return null; }
    }

    getStatisticsOfCurrentWeek(date: Date) {
        const currentWeekKey = date.getFullYear() + '_' + Helpers.getWeekNumber(date)[1];
        if (this.statisticsByMonth.has(currentWeekKey)) {
            return this.statisticsByMonth.get(currentWeekKey);
        } else { return null; }

    }

    getStatisticsOfPreviousWeek(date: Date) {
        const previousWeek = new Date(date);
        previousWeek.setDate(previousWeek.getDate() - 7);
        const previousWeekKey = previousWeek.getFullYear() + '_' + Helpers.getWeekNumber(previousWeek)[1];
        if (this.statisticsByWeek.has(previousWeekKey)) {
            return this.statisticsByWeek.get(previousWeekKey);
        } else { return null; }

    }
}

export class InstallationDatabase {
    public installation: InstallationWilamp;
    public customer: CustomerWilamp;
    public address: AddressWilamp;
    public nodes: NodeWilamp[] = [];
    public lightFixtures: LightFixtureWilamp[] = [];
    public nodesCount: number;
    public lightFixturesCount: number;
    public gateways: GatewayWilamp[] = [];
    public gatewaysCount: number;
    public energyStatistics = new InstallationEnergyStatistics();
    public statisticsByLightManagementModule = new Map<number, EnergyStatisticsByResourceId>();
    public statisticsByNodeIdHMap = new Map<number, EnergyStatisticsByResourceId>();
    public energyStatisticsByInstallationId: any;
    private ___calculatedOnlineNodes = null;
    private ___calculatedOnlineGateways = null;
    private ___statisticsByNodeId: EnergyStatisticsByResourceId[];
    private ___totalNominalPower = -1;

    constructor(
        public installationId,
    ) {
    }

    get statisticsByNodeId(): EnergyStatisticsByResourceId[] {
        return this.___statisticsByNodeId;
    }
    set statisticsByNodeId(statisticsByNodeId: EnergyStatisticsByResourceId[]) {
        this.___calculatedOnlineNodes = null;
        this.___calculatedOnlineGateways = null;
        this.___statisticsByNodeId = statisticsByNodeId;
        this.setGatewayOnlineStatus();
        this.___statisticsByNodeId.forEach((statistic) => {
            this.statisticsByNodeIdHMap.set(statistic.nodeId, statistic);
        });
    }

    getPlantPower() {
        if (this.___totalNominalPower >= 0.0) {
            return this.___totalNominalPower
        } else {
            if (this.lightFixtures && this.lightFixtures.length > 0) {
                let totalNominalPower = 0.0;
                this.lightFixtures.forEach(function (lightFixture) {
                    totalNominalPower += lightFixture.nominalPower;
                });
                this.___totalNominalPower = totalNominalPower;
                return this.___totalNominalPower;
            } else {
                return 0.0;
            }
        }
    }

    setGatewayOnlineStatus() {
        if (this.gateways && this.gateways.length > 0) {
            this.gateways.forEach(function(value) {
                value.gatewayOnline = false;
            });
        }
        if (this.statisticsByNodeId && this.statisticsByNodeId.length > 0) {
            this.statisticsByNodeId.forEach(function(value) {
                if (value.activePower && value.activePower > 0.0) {
                    this.setGatewayOnlineByNodeId( value.nodeId);
                }
            }.bind(this));
        }
    }

    setGatewayOnlineByNodeId(nodeId: number) {
        if (this.nodes && this.nodes.length > 0) {
            this.nodes.forEach(function(value) {
                if (value.id === nodeId) {
                    this.setGatewayOnlineByGatewayId(value.gatewayId);
                }
            }.bind(this));
        }
    }

    setGatewayOnlineByGatewayId(gatewayId: number) {
        if (this.gateways && this.gateways.length > 0) {
            this.gateways.forEach(function(value) {
                if (value.id === gatewayId) {
                    value.gatewayOnline = true;
                }
            });
        }
    }

    getGatewayNodes(gatewayId: number) {
        const nodes = [];
        this.nodes.forEach( (node: NodeWilamp) => {
            if (node.gatewayId === gatewayId) {
                nodes.push(node);
            }
        });
        return nodes;
    }

    onlineNodes() {
        if (this.___calculatedOnlineNodes) { return this.___calculatedOnlineNodes; }
        let onlineNodes = 0;
        if (this.statisticsByNodeId && this.statisticsByNodeId.length > 0) {
            this.statisticsByNodeId.forEach(function(value) {
                if (value.activePower && value.activePower > 0.0) { onlineNodes ++; }
            });
        }
        this.___calculatedOnlineNodes = onlineNodes;
        return onlineNodes;
    }

    onlineGateways() {
        let onlineGateways = 0;
        if (this.gateways && this.gateways.length > 0) {
            this.gateways.forEach(function(value) {
                if (value.gatewayOnline) {
                    onlineGateways++;
                }
            });
        }
        return onlineGateways;
    }

}

