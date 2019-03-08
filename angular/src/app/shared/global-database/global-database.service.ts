import { Injectable } from '@angular/core';

import { Subject } from 'rxjs';
import {
    GLOBALDATABASE__GATEWAYS_FETCHED, GLOBALDATABASE__INSTALLATION_FETCHED,
    GLOBALDATABASE__INSTALLATION_STATISTICS_BY_NODEID_FETCHED,
    GLOBALDATABASE__INSTALLATION_WEEKLY_STATISTICS_FETCHED, GLOBALDATABASE__INSTALLATION_WEEKLY_STATISTICS_FETCHING,
    GLOBALDATABASE__LIGHT_FIXTURES_FETCHED,
    INSTALLATION__LIST_MODIFICATION,
    INSTALLATION__SELECTED_ID_CHANGED,
    INSTALLATION__SELECTED_INSTALLATION_CHANGED,
    INSTALLATION_DASHBOARD__DAILY_STATISTICS_FETCHED,
    INSTALLATION_DASHBOARD__MONTHLY_STATISTICS_FETCHED, INSTALLATION_DASHBOARD__WEEKLY_STATISTICS_FETCHED,
    MAP_INSTANCE_GETTER__MAP_OBTAINED,
} from '../constants/events.constants';
import {JhiEventManager} from 'ng-jhipster';
import {Subscription} from 'rxjs/Rx';
import {InstallationDatabase, IntervalEnergyConsumption} from './global-database.model';
import {Helpers, Principal} from '../';
import {KWtoCO2Factor} from '../constants/graph.constants';
import {LightProfileWilamp} from '../../pages/light-profile-wilamp/light-profile-wilamp.model';
import {LightProfileWilampService} from '../../pages/light-profile-wilamp/light-profile-wilamp.service';
import {EnergyStatistics} from '../../pages/installation-wilamp/installation-wilamp.model';
import {InstallationWilampService} from '../../pages/installation-wilamp/installation-wilamp.service';
import {NodeWilampService} from '../../pages/node-wilamp/node-wilamp.service';
import {CustomerWilampService} from '../../pages/customer-wilamp/customer-wilamp.service';
import {AddressWilampService} from '../../pages/address-wilamp/address-wilamp.service';
import {GatewayWilampService} from '../../pages/gateway-wilamp/gateway-wilamp.service';
import {LightFixtureWilampService} from '../../pages/light-fixture-wilamp/light-fixture-wilamp.service';
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
        private lightFixtureService: LightFixtureWilampService,
        private customerService: CustomerWilampService,
        private addressService: AddressWilampService,
        private gatewayService: GatewayWilampService,
        private lightProfilesService: LightProfileWilampService,
        private eventManager: JhiEventManager,
        private principal: Principal,
        ) {
        this.init();
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
                if (installation.customer != null) {
                    this.customerService.find(installation.customer).subscribe((customer) => {
                        this.selectedInstallation.customer = customer.body;
                        this.installationDatabase[id].customer = customer.body;
                    });
                }
                if (installation.address != null) {
                    this.addressService.find(installation.address).subscribe((address) => {
                        this.selectedInstallation.address = address.body;
                        this.installationDatabase[id].address = address.body;
                        this.eventManager.broadcast({
                            name: GLOBALDATABASE__INSTALLATION_FETCHED,
                            content: 'Sending Selected Installation Fetched event',
                        });
                    });
                }
                this.fetchGateways(id, 1, 100);
                this.fetchLightFixtures(id, 1, 100);
                const startInterval = new Date();
                startInterval.setFullYear(1990);
                this.fetchEnergyStatisticsByInstallationId(id, startInterval, new Date(), new Date());
                this.fetchEnergyStatisticsByNodeId(id, null, startInterval, new Date(), new Date());

                // this.fetchEnergyStatisticsByNodeId(id);
            });
        }
        this.eventManager.broadcast({
            name: INSTALLATION__SELECTED_INSTALLATION_CHANGED,
            content: 'Sending Selected Installation Changed event',
        });

    }

    fetchGateways(installationId, page, size) {
        this.gatewayService.findByInstallation(installationId, {
            page,
            size,
            sort: ['id,asc'],
        }).subscribe((res) => {
            if (page === 1) {
                this.selectedInstallation.gatewaysCount = parseInt(res.headers.get('X-Total-Count'), 10);
                this.selectedInstallation.gateways = res.body;

            } else {
                this.selectedInstallation.gateways.push.apply(this.selectedInstallation.gateways, res.body);
            }
            const totalPages = parseInt(res.headers.get('x-total-pages'), 10);
            if (page === totalPages) {
                this.installationDatabase[installationId].gateways = this.selectedInstallation.gateways;
                this.eventManager.broadcast({
                    name: GLOBALDATABASE__GATEWAYS_FETCHED,
                    content: 'Sending fetch event',
                });
            } else {
                this.fetchGateways(installationId, page + 1, size);
            }
        });
    }

    fetchLightFixtures(installationId, page, size) {
        this.lightFixtureService.findByInstallation(installationId, {
            page,
            size,
            sort: ['id,asc'],
        }).subscribe((res) => {
            if (page === 1) {
                this.selectedInstallation.nodesCount = parseInt(res.headers.get('X-Total-Count'), 10);
                this.selectedInstallation.lightFixtures = res.body;
            } else {
                this.selectedInstallation.lightFixtures.push.apply(this.selectedInstallation.lightFixtures, res.body);
            }
            const totalPages = parseInt(res.headers.get('x-total-pages'), 10);
            if (page === totalPages) {
                this.installationDatabase[installationId].lightFixtures = this.selectedInstallation.lightFixtures;
                this.eventManager.broadcast({
                    name: GLOBALDATABASE__LIGHT_FIXTURES_FETCHED,
                    content: 'Sending fetch event',
                });
            } else {
                this.fetchLightFixtures(installationId, page + 1, size);
            }
        });
    }



    fetchNodes(installationId, page, size) {
        this.nodeService.findByInstallation(installationId, {
            page,
            size,
            sort: ['id,asc'],
        }).subscribe((res) => {
            if (page === 1) {
                this.selectedInstallation.nodesCount = parseInt(res.headers.get('X-Total-Count'), 10);
                this.selectedInstallation.nodes = res.body;
            } else {
                this.selectedInstallation.nodes.push.apply(this.selectedInstallation.nodes, res.body);
            }
            const totalPages = parseInt(res.headers.get('x-total-pages'), 10);
            if (page === totalPages) {
                this.installationDatabase[installationId].nodes = this.selectedInstallation.nodes;
                this.eventManager.broadcast({
                    name: GLOBALDATABASE__LIGHT_FIXTURES_FETCHED,
                    content: 'Sending fetch event',
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
                content: 'Sending fetch event',
            });

        });
    }

    fetchDimAndPowerAtTimestampByNodeId(installationId, timestamp) {
        this.installationService.getDimAndPowerAtTimestampByNodeId(installationId, timestamp).subscribe((statisticsByNodeId) => {
            this.selectedInstallation.statisticsByNodeId = statisticsByNodeId.body;
            this.eventManager.broadcast({
                name: GLOBALDATABASE__INSTALLATION_STATISTICS_BY_NODEID_FETCHED,
                content: 'Sending fetch event',
            });

        });
    }

    fetchEnergyStatisticsByInstallationId(installationId, startInterval, endInterval, currentAnalyzedDate) {
        this.eventManager.broadcast({
            name: GLOBALDATABASE__INSTALLATION_WEEKLY_STATISTICS_FETCHING,
            content: 'Sending fetch event',
        });
        this.installationService.getEnergyStatistics(installationId, startInterval, endInterval, currentAnalyzedDate).subscribe((energyStatistics) => {
            this.populateSelectedInstallationWithEnergyStatistics(energyStatistics);
            this.eventManager.broadcast({
                name: GLOBALDATABASE__INSTALLATION_WEEKLY_STATISTICS_FETCHED,
                content: 'Sending fetch event',
            });
            });
    }

    registerEvents() {
        this.eventSubscriber = this.eventManager.subscribe(
            INSTALLATION__LIST_MODIFICATION,
            (response) => this.load(this.principal.selectedInstallationId),
        );
        this.eventSubscriberSelectedIdChanged = this.eventManager.subscribe(
            INSTALLATION__SELECTED_ID_CHANGED,
            (response) => this.load(this.principal.selectedInstallationId),
        );
    }

    unregisterEvents() {
        this.eventManager.destroy(this.eventSubscriber);
        this.eventManager.destroy(this.eventSubscriberSelectedIdChanged);
    }

    populateSelectedInstallationWithEnergyStatistics(energyStatistics: EnergyStatistics) {
        try {
            this.selectedInstallation.energyStatisticsByInstallationId = energyStatistics;
            this.selectedInstallation.energyStatistics.totalEnergyConsumption = energyStatistics.globalEnergyConsumption.sumEnergy;
            this.selectedInstallation.energyStatistics.totalEnergyConsumptionWithoutDimming = energyStatistics.globalEnergyConsumption.sumEnergyWithoutDim;
            this.selectedInstallation.energyStatistics.totalEnergyConsumptionWithoutControl = energyStatistics.globalEnergyConsumption.sumEnergyWithoutControl;
            this.selectedInstallation.energyStatistics.totalEnergyConsumptionOldInstallation = energyStatistics.globalEnergyConsumption.sumEnergyOldLamps;
            this.selectedInstallation.energyStatistics.lastMeasureReceivedTimestamp = energyStatistics.globalEnergyConsumption.lastIntervalTimestamp;
            this.selectedInstallation.energyStatistics.absorbedPowerEstimation = energyStatistics.absorbedPowerEstimation;
            if (energyStatistics.byWeek.length > 0) {
                const weeklyEnergyConsumption: Map<string, IntervalEnergyConsumption> = new Map<string, IntervalEnergyConsumption>();
                let databaseKey = '';

                energyStatistics.byWeek.forEach((hourEnergyInterval) => {
                    databaseKey = hourEnergyInterval.year + '_' + hourEnergyInterval.weekNumber;
                    if (!weeklyEnergyConsumption.has(databaseKey)) {
                        weeklyEnergyConsumption.set(databaseKey, new IntervalEnergyConsumption({
                            year: hourEnergyInterval.year,
                            weekNumber: hourEnergyInterval.weekNumber,
                            numberOfSubIntervalForAverage: 7,
                        }));
                    }
                    if (!weeklyEnergyConsumption.get(databaseKey).content.has(hourEnergyInterval.dayOfWeek)) {
                        weeklyEnergyConsumption.get(databaseKey).content.set(hourEnergyInterval.dayOfWeek, new IntervalEnergyConsumption({
                            year: hourEnergyInterval.year,
                            weekNumber: hourEnergyInterval.weekNumber,
                            dayOfWeek: hourEnergyInterval.dayOfWeek,
                            numberOfSubIntervalForAverage: 24,
                        }));
                    }
                    weeklyEnergyConsumption.get(databaseKey).content.get(hourEnergyInterval.dayOfWeek).content.set(hourEnergyInterval.hour, new IntervalEnergyConsumption({energyStatisticRow: hourEnergyInterval}));
                });
                weeklyEnergyConsumption.forEach((singleWeekEnergyConsumption, key) => {
                    const result = IntervalEnergyConsumption.populateAveragesFromSubIntervals(singleWeekEnergyConsumption);
                    this.selectedInstallation.energyStatistics.statisticsByWeek.set(key, result);
                });
            }
        } catch (Exception) {
            console.warn(Exception);
        }

        try {
            this.selectedInstallation.energyStatisticsByInstallationId = energyStatistics;
            if (energyStatistics.byMonth.length > 0) {
                const monthlyEnergyConsumptions: Map<string, IntervalEnergyConsumption> = new Map<string, IntervalEnergyConsumption>();
                let databaseKey = '';

                energyStatistics.byMonth.forEach((dayEnergyInterval) => {
                    databaseKey = dayEnergyInterval.year + '_' + dayEnergyInterval.month;
                    if (!monthlyEnergyConsumptions.has(databaseKey)) {
                        monthlyEnergyConsumptions.set(databaseKey, new IntervalEnergyConsumption({
                            year: dayEnergyInterval.year,
                            month: dayEnergyInterval.month,
                            numberOfSubIntervalForAverage: new Date(dayEnergyInterval.year, dayEnergyInterval.month, 0).getDate(),
                        }));
                    }
                    monthlyEnergyConsumptions.get(databaseKey).content.set(dayEnergyInterval.day, new IntervalEnergyConsumption({energyStatisticRow: dayEnergyInterval}));
                });
                monthlyEnergyConsumptions.forEach((dayEnergyConsumption, key) => {
                    const result = IntervalEnergyConsumption.populateAveragesFromSubIntervals(dayEnergyConsumption);
                    this.selectedInstallation.energyStatistics.statisticsByMonth.set(key, result);
                });
            }
        } catch (Exception) {
            console.warn(Exception);
        }
    }

}
