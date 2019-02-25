import {
    EnergyStatisticsByResourceId,
    EnergyStatisticsRowByInterval,
    InstallationWilamp
} from '../../pages/installation-wilamp';
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
    public content: IntervalEnergyConsumption[] = [];
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

    public lastMeasureReceivedTimestamp: Date;
    public totalEnergyConsumption = 0.0;
    public totalEnergyConsumptionWithoutDimming = 0.0;
    public totalEnergyConsumptionWithoutControl = 0.0;
    public totalEnergyConsumptionOldInstallation = 0.0;
    public absorbedPowerEstimation = 0.0;
    public averageDimming = 0.0;
    public plantPower = 0.0;
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
    public weeklyEnergyStatisticsByInstallationId: any;
    private ___calculatedOnlineNodes = null;
    private ___calculatedOnlineGateways = null;
    private ___statisticsByNodeId: EnergyStatisticsByResourceId[];

    constructor(
        public installationId
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

