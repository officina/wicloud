import { Injectable } from '@angular/core';

import { Subject } from 'rxjs';
import {
    GLOBALDATABASE__GATEWAYS_FETCHED, GLOBALDATABASE__INSTALLATION_FETCHED,
    GLOBALDATABASE__INSTALLATION_STATISTICS_BY_NODEID_FETCHED,
    GLOBALDATABASE__INSTALLATION_WEEKLY_STATISTICS_FETCHED, GLOBALDATABASE__INSTALLATION_WEEKLY_STATISTICS_FETCHING,
    GLOBALDATABASE__NODES_FETCHED,
    INSTALLATION__LIST_MODIFICATION,
    INSTALLATION__SELECTED_ID_CHANGED,
    INSTALLATION__SELECTED_INSTALLATION_CHANGED,
    INSTALLATION_DASHBOARD__DAILY_STATISTICS_FETCHED,
    INSTALLATION_DASHBOARD__MONTHLY_STATISTICS_FETCHED, INSTALLATION_DASHBOARD__WEEKLY_STATISTICS_FETCHED,
    MAP_INSTANCE_GETTER__MAP_OBTAINED
} from '../constants/events.constants';
import {JhiEventManager} from 'ng-jhipster';
import {Subscription} from 'rxjs/Rx';
import {InstallationDatabase, IntervalEnergyConsumption} from './global-database.model';
import {Helpers, Principal} from '../';
import {KWtoCO2Factor} from '../constants/graph.constants';
import {LightProfileWilamp, LightProfileWilampService} from '../../pages/light-profile-wilamp';
import {EnergyStatistics, InstallationWilampService} from '../../pages/installation-wilamp';
import {NodeWilampService} from '../../pages/node-wilamp';
import {CustomerWilampService} from '../../pages/customer-wilamp';
import {AddressWilampService} from '../../pages/address-wilamp';
import {GatewayWilampService} from '../../pages/gateway-wilamp';
declare var window: any;

/***
 * Used to Inject Global variables among Components. //TODO: AT
 */

@Injectable()
export class GlobalDatabaseService {
    /**
     * runtime fields, substituded or retrieved from server
     */
    selectedInstallation: InstallationDatabase;
    public installationDatabase: { [key: number]: InstallationDatabase; } = {};
    public lightProfiles = new Map<number, LightProfileWilamp>();
    private eventSubscriber: Subscription;
    private eventSubscriberSelectedIdChanged: Subscription;

    constructor(
        private installationService: InstallationWilampService,
        private nodeService: NodeWilampService,
        private customerService: CustomerWilampService,
        private addressService: AddressWilampService,
        private gatewayService: GatewayWilampService,
        private lightProfilesService: LightProfileWilampService,
        private eventManager: JhiEventManager,
        private principal: Principal
        ) {
    }

    init() {
        this.registerEvents();
        window.GlobalDatabase = this;
    }

    destroy() {
        this.unregisterEvents();
    }

    load(id, forceCloudFetch = false) {
        // Save old installation in the database
        if (this.selectedInstallation != null) {
            this.installationDatabase[this.selectedInstallation.installationId] = this.selectedInstallation;
        }
        this.selectedInstallation = null;
        let fetchFromCloud = true;
        if (!forceCloudFetch) {
            if (id in this.installationDatabase) {
                this.selectedInstallation = this.installationDatabase[id];
                fetchFromCloud = false;
                }
        }
        this.fetchLightProfiles();
        if (fetchFromCloud) {
            this.installationService.find(id).subscribe((res) => {
                const installation = res.body;
                this.selectedInstallation = new InstallationDatabase(id);
                this.selectedInstallation.installation = installation;
                if (this.installationDatabase[id] == null) {
                    this.installationDatabase[id] = new InstallationDatabase(id);
                    this.installationDatabase[id].installation = installation;
                }
                if (installation.customerId != null) {
                    this.customerService.find(installation.customerId).subscribe((customer) => {
                        this.selectedInstallation.customer = customer.body;
                        this.installationDatabase[id].customer = customer.body;
                    });
                }
                if (installation.addressId != null) {
                    this.addressService.find(installation.addressId).subscribe((address) => {
                        this.selectedInstallation.address = address.body;
                        this.installationDatabase[id].address = address.body;
                        this.eventManager.broadcast({
                            name: GLOBALDATABASE__INSTALLATION_FETCHED,
                            content: 'Sending Selected Installation Fetched event'
                        });
                    });
                }
                this.fetchGateways(id, 0, 100);
                this.fetchNodes(id, 0, 100);
                const startInterval = new Date();
                startInterval.setFullYear(1990);
                this.fetchWeeklyEnergyStatisticsByInstallationId(id, startInterval, new Date(), new Date());
                this.fetchEnergyStatisticsByNodeId(id, null, startInterval, new Date(), new Date());

                // this.fetchEnergyStatisticsByNodeId(id);
            });
        }
        this.eventManager.broadcast({
            name: INSTALLATION__SELECTED_INSTALLATION_CHANGED,
            content: 'Sending Selected Installation Changed event'
        });

    }

    fetchGateways(installationId, page, size) {
        this.gatewayService.findByInstallation(installationId, {
            page,
            size,
            sort: ['id,asc']
        }).subscribe((res) => {
            if (page === 0) {
                this.selectedInstallation.gatewaysCount = parseInt(res.headers.get('X-Total-Count'), 10);
                this.selectedInstallation.gateways = res.body;

            } else {
                this.selectedInstallation.gateways.push.apply(this.selectedInstallation.gateways, res.body);
            }
            if (res.body.length === 0) {
                this.installationDatabase[installationId].gateways = this.selectedInstallation.gateways;
                this.eventManager.broadcast({
                    name: GLOBALDATABASE__GATEWAYS_FETCHED,
                    content: 'Sending fetch event'
                });
            } else {
                this.fetchGateways(installationId, page + 1, size);
            }
        });
    }

    fetchNodes(installationId, page, size) {
        this.nodeService.findByInstallation(installationId, {
            page,
            size,
            sort: ['id,asc']
        }).subscribe((res) => {
            if (page === 0) {
                this.selectedInstallation.nodesCount = parseInt(res.headers.get('X-Total-Count'), 10);
                this.selectedInstallation.nodes = res.body;
            } else {
                this.selectedInstallation.nodes.push.apply(this.selectedInstallation.nodes, res.body);
            }
            if (res.body.length === 0) {
                this.installationDatabase[installationId].nodes = this.selectedInstallation.nodes;
                this.eventManager.broadcast({
                    name: GLOBALDATABASE__NODES_FETCHED,
                    content: 'Sending fetch event'
                });
            } else {
                this.fetchNodes(installationId, page + 1, size);
            }
        });
    }

    fetchLightProfiles() {
        this.lightProfilesService.query().subscribe((res) => {
            res.body.forEach( (lightProfile: LightProfileWilamp) => {
                this.lightProfiles.set(lightProfile.id, lightProfile);
            });
        });
    }

    fetchEnergyStatisticsByNodeId(installationId, measureType?: number, startInterval?: Date, endInterval?: Date, currentDate?: Date) {
        this.installationService.getStatisticsByNodeId(installationId, measureType, startInterval, endInterval, currentDate).subscribe((statisticsByNodeId) => {
            this.selectedInstallation.statisticsByNodeId = statisticsByNodeId.body;
            this.eventManager.broadcast({
                name: GLOBALDATABASE__INSTALLATION_STATISTICS_BY_NODEID_FETCHED,
                content: 'Sending fetch event'
            });

        });
    }

    fetchDimAndPowerAtTimestampByNodeId(installationId, timestamp) {
        this.installationService.getDimAndPowerAtTimestampByNodeId(installationId, timestamp).subscribe((statisticsByNodeId) => {
            this.selectedInstallation.statisticsByNodeId = statisticsByNodeId.body;
            this.eventManager.broadcast({
                name: GLOBALDATABASE__INSTALLATION_STATISTICS_BY_NODEID_FETCHED,
                content: 'Sending fetch event'
            });

        });
    }

    fetchWeeklyEnergyStatisticsByInstallationId(installationId, startInterval, endInterval, currentAnalyzedDate) {
        this.eventManager.broadcast({
            name: GLOBALDATABASE__INSTALLATION_WEEKLY_STATISTICS_FETCHING,
            content: 'Sending fetch event'
        });
        this.installationService.getWeeklyEnergyStatistics(installationId, null, startInterval, endInterval, currentAnalyzedDate).subscribe((energyStatistics) => {
            this.populateSelectedInstallationWithEnergyStatistics(energyStatistics);
            this.eventManager.broadcast({
                name: GLOBALDATABASE__INSTALLATION_WEEKLY_STATISTICS_FETCHED,
                content: 'Sending fetch event'
            });
            });
    }

    registerEvents() {
        this.eventSubscriber = this.eventManager.subscribe(
            INSTALLATION__LIST_MODIFICATION,
            (response) => this.load(this.principal.selectedInstallationId)
        );
        this.eventSubscriberSelectedIdChanged = this.eventManager.subscribe(
            INSTALLATION__SELECTED_ID_CHANGED,
            (response) => this.load(this.principal.selectedInstallationId)
        );
    }

    unregisterEvents() {
        this.eventManager.destroy(this.eventSubscriber);
        this.eventManager.destroy(this.eventSubscriberSelectedIdChanged);
    }

    populateSelectedInstallationWithEnergyStatistics(energyStatistics: EnergyStatistics) {
        try {
            this.selectedInstallation.weeklyEnergyStatisticsByInstallationId = energyStatistics;
            this.selectedInstallation.energyStatistics.totalEnergyConsumption = energyStatistics.globalEnergyConsumption.sumEnergy;
            this.selectedInstallation.energyStatistics.totalEnergyConsumptionWithoutDimming = energyStatistics.globalEnergyConsumption.sumEnergyWithoutDim;
            this.selectedInstallation.energyStatistics.totalEnergyConsumptionWithoutControl = energyStatistics.globalEnergyConsumption.sumEnergyWithoutControl;
            this.selectedInstallation.energyStatistics.totalEnergyConsumptionOldInstallation = energyStatistics.globalEnergyConsumption.sumEnergyOldLamps;
            this.selectedInstallation.energyStatistics.lastMeasureReceivedTimestamp = energyStatistics.globalEnergyConsumption.lastIntervalTimestamp;

            if (energyStatistics.energyStatisticsByWeekNumberDayOfWeekAndHour.length > 0) {
                energyStatistics.energyStatisticsByWeekNumberDayOfWeekAndHour.forEach((week) => {
                    let databaseKey = '';
                    const weeklyEnergyConsumption = new IntervalEnergyConsumption();
                    const allDaysEnergyConsumption = new IntervalEnergyConsumption();
                    week.forEach((dayArray) => {
                        let day = 0;
                        const dailyEnergyConsumption = new IntervalEnergyConsumption();
                        for (let i = 0; i < 24; i++) {
                            const hourEnergyStatistics = dayArray[i];
                            day = hourEnergyStatistics.dayOfWeek;
                            if (databaseKey === '') { databaseKey = hourEnergyStatistics.year + '_' + hourEnergyStatistics.weekNumber; }
                            // Create a new EnergyConsumptionInterval for the current Hour.
                            const hourlyEnergyConsumption = new IntervalEnergyConsumption();
                            hourlyEnergyConsumption.activePowerAverage = hourEnergyStatistics.activePower;
                            hourlyEnergyConsumption.activeEnergyAverage = hourEnergyStatistics.sumEnergy;
                            hourlyEnergyConsumption.activeEnergyTotal = hourEnergyStatistics.sumEnergy;
                            hourlyEnergyConsumption.activeEnergyWithoutDimAverage = hourEnergyStatistics.sumEnergyWithoutDim;
                            hourlyEnergyConsumption.activeEnergyWithoutDimTotal = hourEnergyStatistics.sumEnergyWithoutDim;
                            hourlyEnergyConsumption.activeEnergyWithoutControlAverage = hourEnergyStatistics.sumEnergyWithoutControl;
                            hourlyEnergyConsumption.activeEnergyWithoutControlTotal = hourEnergyStatistics.sumEnergyWithoutControl;
                            hourlyEnergyConsumption.activeEnergyOldLampsAverage = hourEnergyStatistics.sumEnergyOldLamps;
                            hourlyEnergyConsumption.activeEnergyOldLampsTotal = hourEnergyStatistics.sumEnergyOldLamps;
                            dailyEnergyConsumption.content.push(hourlyEnergyConsumption);
                            dailyEnergyConsumption.data[i] = [i, Math.round(hourEnergyStatistics.sumEnergy * 10.0) / 10.0];
                            // if (window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByHour[i].day > 0) { currentDayOfWeek = window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByHour[i].day; }

                            // Update the EnergyConsumptionInterval for the current Day.
                            dailyEnergyConsumption.activePowerAverage += hourlyEnergyConsumption.activePowerAverage / 24.0;
                            dailyEnergyConsumption.activeEnergyAverage += hourlyEnergyConsumption.activeEnergyAverage ;
                            dailyEnergyConsumption.activeEnergyTotal += hourlyEnergyConsumption.activeEnergyAverage;
                            dailyEnergyConsumption.activeEnergyWithoutDimAverage += hourlyEnergyConsumption.activeEnergyWithoutDimAverage ;
                            dailyEnergyConsumption.activeEnergyWithoutDimTotal += hourlyEnergyConsumption.activeEnergyWithoutDimAverage;
                            dailyEnergyConsumption.activeEnergyWithoutControlAverage += hourlyEnergyConsumption.activeEnergyWithoutControlAverage ;
                            dailyEnergyConsumption.activeEnergyWithoutControlTotal += hourlyEnergyConsumption.activeEnergyWithoutControlAverage;
                            dailyEnergyConsumption.activeEnergyOldLampsAverage += hourlyEnergyConsumption.activeEnergyOldLampsAverage;
                            dailyEnergyConsumption.activeEnergyOldLampsTotal += hourlyEnergyConsumption.activeEnergyOldLampsAverage;
                        }
                        weeklyEnergyConsumption.content.push(dailyEnergyConsumption);

                        // Update the EnergyConsumptionInterval for the current Week.
                        weeklyEnergyConsumption.activePowerAverage += dailyEnergyConsumption.activePowerAverage / 7.0;
                        weeklyEnergyConsumption.activeEnergyAverage += dailyEnergyConsumption.activeEnergyAverage / 7.0;
                        weeklyEnergyConsumption.activeEnergyTotal += dailyEnergyConsumption.activeEnergyTotal;
                        weeklyEnergyConsumption.activeEnergyWithoutDimAverage += dailyEnergyConsumption.activeEnergyWithoutDimAverage / 7.0;
                        weeklyEnergyConsumption.activeEnergyWithoutDimTotal += dailyEnergyConsumption.activeEnergyWithoutDimTotal;
                        weeklyEnergyConsumption.activeEnergyWithoutControlAverage += dailyEnergyConsumption.activeEnergyWithoutControlAverage / 7.0;
                        weeklyEnergyConsumption.activeEnergyWithoutControlTotal += dailyEnergyConsumption.activeEnergyWithoutControlTotal;
                        weeklyEnergyConsumption.activeEnergyOldLampsAverage += dailyEnergyConsumption.activeEnergyOldLampsAverage / 7.0;
                        weeklyEnergyConsumption.activeEnergyOldLampsTotal += dailyEnergyConsumption.activeEnergyOldLampsTotal;
                        weeklyEnergyConsumption.data[day] = [day, Math.round(dailyEnergyConsumption.activeEnergyTotal * 10.0) / 10.0];
                    });

                    weeklyEnergyConsumption.activePowerAverage = Helpers.round(weeklyEnergyConsumption.activeEnergyAverage);
                    weeklyEnergyConsumption.activeEnergyAverage = Helpers.round(weeklyEnergyConsumption.activeEnergyAverage);
                    weeklyEnergyConsumption.activeEnergyTotal = Helpers.round(weeklyEnergyConsumption.activeEnergyTotal);
                    weeklyEnergyConsumption.activeEnergyWithoutDimAverage = Helpers.round(weeklyEnergyConsumption.activeEnergyWithoutDimAverage);
                    weeklyEnergyConsumption.activeEnergyWithoutDimTotal = Helpers.round(weeklyEnergyConsumption.activeEnergyWithoutDimTotal);
                    weeklyEnergyConsumption.activeEnergyWithoutControlAverage = Helpers.round(weeklyEnergyConsumption.activeEnergyWithoutControlAverage);
                    weeklyEnergyConsumption.activeEnergyWithoutControlTotal = Helpers.round(weeklyEnergyConsumption.activeEnergyWithoutControlTotal);
                    weeklyEnergyConsumption.activeEnergyOldLampsAverage = Helpers.round(weeklyEnergyConsumption.activeEnergyOldLampsAverage);
                    weeklyEnergyConsumption.activeEnergyOldLampsTotal = Helpers.round(weeklyEnergyConsumption.activeEnergyOldLampsTotal);
                    this.selectedInstallation.energyStatistics.statisticsByWeek.set(databaseKey, weeklyEnergyConsumption);
                });
                /*
                for (let i = 0; i < this.selectedInstallation.weeklyEnergyStatisticsByInstallationId.energyStatisticsByWeekNumberDayOfWeekAndHour.length; i++) {
                    const weekNumber = this.selectedInstallation.weeklyEnergyStatisticsByInstallationId.energyStatisticsByWeekNumberDayOfWeekAndHour[i]

                    todayData[i] = [i, Math.round(this.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByHour[i].sumEnergy * 10.0) / 10.0];

                    // if (window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByHour[i].day > 0) { currentDayOfWeek = window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByHour[i].day; }
                    this.dailyEnergyConsumptionAvg += todayData[i][1] / 24.0;
                    this.dailyEnergyConsumptionMax += todayData[i][1];
                    if (todayData[i][1] > maxValue) { maxValue = todayData[i][1]; }
                }
                const todayAvgData = Array();
                for (let i = 0; i < this.globalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsByDayOfWeek[currentDayOfWeek].length; i++) {
                    todayAvgData[i] = [i, this.globalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsByDayOfWeek[currentDayOfWeek][i].sumEnergy];
                    if (todayAvgData[i][1] > maxValue) { maxValue = todayAvgData[i][1]; }
                }
                this.dailyEnergyConsumptionAvg = Math.round(this.dailyEnergyConsumptionAvg * 10.0) / 10.0;
                this.dailyEnergyConsumptionMax = Math.round(this.dailyEnergyConsumptionMax * 10.0) / 10.0;
                this.dailyEnergyConsumptionOptions.yaxis.max = Math.round(maxValue) + 1;
                this.dailyEnergyConsumption[0].data = todayData;
                this.dailyEnergyConsumption[1].data = todayAvgData;
                this.eventManager.broadcast({
                    name: INSTALLATION_DASHBOARD__DAILY_STATISTICS_FETCHED,
                    content: { dataset: this.dailyEnergyConsumption, options: this.dailyEnergyConsumptionOptions }
                }); */
            }
        } catch (Exception) {
            console.warn(Exception);
        }

        try {
            this.selectedInstallation.weeklyEnergyStatisticsByInstallationId = energyStatistics;

            if (energyStatistics.energyStatisticsByYearMonthAndDayOfMonthDTOS.length > 0) {
                energyStatistics.energyStatisticsByYearMonthAndDayOfMonthDTOS.forEach((yearArray) => {
                    yearArray.forEach((monthArray) => {
                        let day = 0;
                        let databaseKey = '';
                        let numberOfMeasuresForAverage = 0.0;
                        const monthlyEnergyConsumption = new IntervalEnergyConsumption();
                        for (let i = 1; i <= 31; i++) {
                            const dayEnergyStatistics = monthArray[i];
                            day = dayEnergyStatistics.day;
                            if (databaseKey === '') {
                                databaseKey = dayEnergyStatistics.year + '_' + dayEnergyStatistics.month;
                            }

                            const dailyEnergyConsumption = new IntervalEnergyConsumption();
                            const dayDate = new Date(dayEnergyStatistics.year, dayEnergyStatistics.month, dayEnergyStatistics.day);

                            dailyEnergyConsumption.activeEnergyAverage = dayEnergyStatistics.sumEnergy;
                            dailyEnergyConsumption.activeEnergyTotal = dayEnergyStatistics.sumEnergy;
                            dailyEnergyConsumption.activeEnergyWithoutDimAverage = dayEnergyStatistics.sumEnergyWithoutDim;
                            dailyEnergyConsumption.activeEnergyWithoutDimTotal = dayEnergyStatistics.sumEnergyWithoutDim;
                            dailyEnergyConsumption.activeEnergyWithoutControlAverage = dayEnergyStatistics.sumEnergyWithoutControl;
                            dailyEnergyConsumption.activeEnergyWithoutControlTotal = dayEnergyStatistics.sumEnergyWithoutControl;
                            dailyEnergyConsumption.activeEnergyOldLampsAverage = dayEnergyStatistics.sumEnergyOldLamps;
                            dailyEnergyConsumption.activeEnergyOldLampsTotal = dayEnergyStatistics.sumEnergyOldLamps;
                            dailyEnergyConsumption.timestamp = new Date(dayEnergyStatistics.year, (dayEnergyStatistics.month - 1), dayEnergyStatistics.day);
                            monthlyEnergyConsumption.data[i] = [i, Math.round(dayEnergyStatistics.sumEnergy * 10.0) / 10.0];
                            monthlyEnergyConsumption.content.push(dailyEnergyConsumption);

                            // if (window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByHour[i].day > 0) { currentDayOfWeek = window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByHour[i].day; }
                            if (monthlyEnergyConsumption.data[i][1] > 0) { numberOfMeasuresForAverage++; }

                            monthlyEnergyConsumption.activeEnergyTotal += dailyEnergyConsumption.activeEnergyTotal;
                            monthlyEnergyConsumption.activeEnergyWithoutDimTotal += dailyEnergyConsumption.activeEnergyWithoutDimTotal;
                            monthlyEnergyConsumption.activeEnergyWithoutControlTotal += dailyEnergyConsumption.activeEnergyWithoutControlTotal;
                            monthlyEnergyConsumption.activeEnergyOldLampsTotal += dailyEnergyConsumption.activeEnergyOldLampsTotal;
                        }
                        if (numberOfMeasuresForAverage > 0) {
                            monthlyEnergyConsumption.activeEnergyAverage = monthlyEnergyConsumption.activeEnergyTotal / numberOfMeasuresForAverage;
                            monthlyEnergyConsumption.activeEnergyWithoutDimAverage = monthlyEnergyConsumption.activeEnergyWithoutDimTotal / numberOfMeasuresForAverage;
                            monthlyEnergyConsumption.activeEnergyOldLampsAverage = monthlyEnergyConsumption.activeEnergyOldLampsTotal / numberOfMeasuresForAverage;
                            monthlyEnergyConsumption.activeEnergyWithoutControlAverage = monthlyEnergyConsumption.activeEnergyWithoutControlTotal / numberOfMeasuresForAverage;

                        }
                        monthlyEnergyConsumption.activeEnergyAverage = Math.round(monthlyEnergyConsumption.activeEnergyAverage * 10.0) / 10.0;
                        monthlyEnergyConsumption.activeEnergyWithoutDimAverage = Math.round(monthlyEnergyConsumption.activeEnergyWithoutDimAverage * 10.0) / 10.0;
                        monthlyEnergyConsumption.activeEnergyOldLampsAverage = Math.round(monthlyEnergyConsumption.activeEnergyOldLampsAverage * 10.0) / 10.0;
                        monthlyEnergyConsumption.activeEnergyWithoutControlAverage = Math.round(monthlyEnergyConsumption.activeEnergyWithoutControlAverage * 10.0) / 10.0;
                        monthlyEnergyConsumption.activeEnergyTotal = Math.round(monthlyEnergyConsumption.activeEnergyTotal * 10.0) / 10.0;
                        monthlyEnergyConsumption.activeEnergyWithoutDimTotal = Math.round(monthlyEnergyConsumption.activeEnergyWithoutDimTotal * 10.0) / 10.0;
                        monthlyEnergyConsumption.activeEnergyWithoutControlTotal = Math.round(monthlyEnergyConsumption.activeEnergyWithoutControlTotal * 10.0) / 10.0;
                        monthlyEnergyConsumption.activeEnergyOldLampsTotal = Math.round(monthlyEnergyConsumption.activeEnergyOldLampsTotal * 10.0) / 10.0;
                        this.selectedInstallation.energyStatistics.statisticsByMonth.set(databaseKey, monthlyEnergyConsumption);
                    });
                });
            }
        } catch (Exception) {
            console.warn(Exception);
        }

    /*
    try {
        if (this.globalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId && this.globalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByDayOfWeek.length > 0) {
            const todayData = Array();
            this.weeklyEnergyConsumptionAvg = 0.0;
            this.weeklyEnergyConsumptionMax = 0.0;
            this.lastWeekEnergyConsumptionAvg = 0.0;
            this.lastWeekEnergyConsumptionMax = 0.0;
            let maxValue = 0.0;
            for (let i = 0; i < this.globalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByDayOfWeek.length; i++) {
                todayData[i] = [i, Math.round(this.globalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByDayOfWeek[i].sumEnergy * 10.0) / 10.0];
                // if (window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByHour[i].day > 0) { currentDayOfWeek = window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByHour[i].day; }
                this.weeklyEnergyConsumptionAvg += todayData[i][1] / 7.0;
                this.weeklyEnergyConsumptionMax += todayData[i][1];
                if (todayData[i][1] > maxValue) { maxValue = todayData[i][1]; }
            }
            const todayAvgData = Array();
            for (let i = 0; i < this.globalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfLastWeekByDayOfWeek.length; i++) {
                let sumEnergy = 0.0;
                sumEnergy += this.globalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfLastWeekByDayOfWeek[i].sumEnergy;
                todayAvgData[i] = [i, sumEnergy];
                if (todayAvgData[i][1] > maxValue) { maxValue = todayAvgData[i][1]; }
                this.lastWeekEnergyConsumptionAvg += todayAvgData[i][1] / 7.0;
                this.lastWeekEnergyConsumptionMax += todayAvgData[i][1];

            }
            this.weeklyEnergyConsumptionAvg = Math.round(this.weeklyEnergyConsumptionAvg * 10.0) / 10.0;
            this.weeklyEnergyConsumptionMax = Math.round(this.weeklyEnergyConsumptionMax * 10.0) / 10.0;
            this.lastWeekEnergyConsumptionAvg = Math.round(this.lastWeekEnergyConsumptionAvg * 10.0) / 10.0;
            this.lastWeekEnergyConsumptionMax = Math.round(this.lastWeekEnergyConsumptionMax * 10.0) / 10.0;
            this.weeklyEnergyConsumptionOptions.yaxis.max = Math.round(maxValue) + 1;
            this.weeklyEnergyConsumption[0].data = todayData;
            this.weeklyEnergyConsumption[1].data = todayAvgData;
            this.eventManager.broadcast({
                name: INSTALLATION_DASHBOARD__WEEKLY_STATISTICS_FETCHED,
                content: { dataset: this.weeklyEnergyConsumption, options: this.weeklyEnergyConsumptionOptions }
            });
        }
    } catch (Exception) {
        console.log(Exception);
    }

    try {
        if (this.globalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId && this.globalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByDayOfMonth.length > 0) {
            const todayData = Array();
            const daysInCurrentMonth = new Date((this.currentAnalyzedDate).getFullYear(), (this.currentAnalyzedDate).getMonth(), 0).getDate();
            this.monthlyEnergyConsumptionAvg = 0.0;
            this.monthlyEnergyConsumptionMax = 0.0;
            this.lastMonthEnergyConsumptionMax = 0.0;
            this.lastMonthEnergyConsumptionAvg = 0.0;
            this.lastMonthEnergySaved = 0.0;
            this.lastMonthCo2Saved = 0.0;
            this.monthlyEnergySaved = 0.0;
            this.monthlyCo2Saved = 0.0;
            let maxValue = 0.0;
            for (let i = 0; i < this.globalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByDayOfMonth.length; i++) {
                todayData[i] = [i, Math.round(this.globalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByDayOfMonth[i].sumEnergy * 10.0) / 10.0];
                // if (window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByHour[i].day > 0) { currentDayOfWeek = window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByHour[i].day; }
                this.monthlyEnergyConsumptionAvg += todayData[i][1] / daysInCurrentMonth;
                this.monthlyEnergyConsumptionMax += todayData[i][1];
                const energySaved = this.globalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByDayOfMonth[i].sumEnergyOldLamps - window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByDayOfMonth[i].sumEnergy;
                if (energySaved > 0) { this.monthlyEnergySaved += energySaved; }
                if (todayData[i][1] > maxValue) { maxValue = todayData[i][1]; }
            }
            const todayAvgData = Array();
            for (let i = 0; i < this.globalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfLastMonthByDayOfMonth.length; i++) {
                let sumEnergy = 0.0;
                sumEnergy += this.globalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfLastMonthByDayOfMonth[i].sumEnergy;
                todayAvgData[i] = [i, sumEnergy];
                if (todayAvgData[i][1] > maxValue) { maxValue = todayAvgData[i][1]; }
                this.lastMonthEnergyConsumptionAvg += todayAvgData[i][1] / daysInCurrentMonth;
                this.lastMonthEnergyConsumptionMax += todayAvgData[i][1];
                const energySaved = this.globalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfLastMonthByDayOfMonth[i].sumEnergyOldLamps - window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfLastMonthByDayOfMonth[i].sumEnergy;
                if (energySaved > 0) { this.lastMonthEnergySaved += energySaved; }
            }
            this.monthlyCo2Saved = this.monthlyEnergySaved * KWtoCO2Factor;
            this.monthlyCo2Saved = Math.round(this.monthlyCo2Saved * 10.0) / 10.0;
            this.monthlyEnergySaved = Math.round(this.monthlyEnergySaved * 10.0) / 10.0;
            this.lastMonthCo2Saved = this.lastMonthEnergySaved * KWtoCO2Factor;
            this.lastMonthCo2Saved = Math.round(this.lastMonthCo2Saved * 10.0) / 10.0;
            this.lastMonthEnergySaved = Math.round(this.lastMonthEnergySaved * 10.0) / 10.0;
            this.monthlyEnergyConsumptionAvg = Math.round(this.monthlyEnergyConsumptionAvg * 10.0) / 10.0;
            this.monthlyEnergyConsumptionMax = Math.round(this.monthlyEnergyConsumptionMax * 10.0) / 10.0;
            this.lastMonthEnergyConsumptionAvg = Math.round(this.lastMonthEnergyConsumptionAvg * 10.0) / 10.0;
            this.lastMonthEnergyConsumptionMax = Math.round(this.lastMonthEnergyConsumptionMax * 10.0) / 10.0;
            this.monthlyEnergyConsumptionOptions.yaxis.max = Math.round(maxValue) + 1;
            this.monthlyEnergyConsumption[0].data = todayData;
            this.monthlyEnergyConsumption[1].data = todayAvgData;
            this.eventManager.broadcast({
                name: INSTALLATION_DASHBOARD__MONTHLY_STATISTICS_FETCHED,
                content: { dataset: this.monthlyEnergyConsumption, options: this.monthlyEnergyConsumptionOptions }
            });
        }
    } catch (Exception) {
        console.log(Exception);
    }

    this.Dashboard.initChartEnergyStatistics(this.energyStatistics);
    this.totalEnergyConsumption = this.energyStatistics.globalEnergyConsumption.sumEnergy;
    this.totalEnergyConsumptionWithoutDimming = this.energyStatistics.globalEnergyConsumption.sumEnergyWithoutDim;
    this.totalEnergyConsumptionOldInstallation = this.energyStatistics.globalEnergyConsumption.sumEnergyOldLamps;
    this.totalEnergySaved = this.totalEnergyConsumptionOldInstallation - this.totalEnergyConsumption;
    this.totalCo2Saved = this.totalEnergySaved * KWtoCO2Factor;

    this.totalEnergyConsumption = Math.round(this.totalEnergyConsumption);
    this.totalEnergyConsumptionWithoutDimming = Math.round(this.totalEnergyConsumptionWithoutDimming);
    this.totalEnergyConsumptionOldInstallation = Math.round(this.totalEnergyConsumptionOldInstallation);
    this.totalEnergySaved = Math.round(this.totalEnergySaved);
    this.totalCo2Saved = Math.round(this.totalCo2Saved);
    */
    }

}
