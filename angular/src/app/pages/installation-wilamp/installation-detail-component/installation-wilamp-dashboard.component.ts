/* tslint:disable:no-unused-expression */
import {AfterViewInit, Component, OnDestroy, OnInit} from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {ScriptLoaderService} from '../../../_services/script-loader.service';
import {JhiEventManager} from 'ng-jhipster';
import {MapHelpers} from '../../../shared/maps/map.helpers';
import {MapOptions} from '../../../shared/maps/map.models';
import {AmChart, AmChartsService} from '@amcharts/amcharts3-angular';
import {Helpers, Principal} from '../../../shared';
import {Subscription} from 'rxjs/Rx';
import {
    InstallationWilampService,
} from '../../installation-wilamp/installation-wilamp.service';

import {
    EnergyStatistics, EnergyStatisticsRowByInterval, GlobalStatistics, InstallationRuntimeParameters,
} from '../../installation-wilamp/installation-wilamp.model';
import {CustomerWilamp, CustomerWilampService} from '../../customer-wilamp';
import {AddressWilamp, AddressWilampService} from '../../address-wilamp';
import {NodeWilamp, NodeWilampService} from '../../node-wilamp';
import {GatewayWilamp, GatewayWilampService} from '../../gateway-wilamp';
import {latLng} from 'leaflet';
import {
    GLOBALDATABASE__GATEWAYS_FETCHED,
    GLOBALDATABASE__INSTALLATION_FETCHED,
    GLOBALDATABASE__INSTALLATION_STATISTICS_BY_NODEID_FETCHED,
    GLOBALDATABASE__INSTALLATION_WEEKLY_STATISTICS_FETCHED, GLOBALDATABASE__INSTALLATION_WEEKLY_STATISTICS_FETCHING,
    GLOBALDATABASE__LIGHT_FIXTURES_FETCHED,
    INSTALLATION__LIST_MODIFICATION,
    INSTALLATION__SELECTED_ID_CHANGED,
    INSTALLATION_DASHBOARD__DAILY_STATISTICS_FETCHED,
    INSTALLATION_DASHBOARD__MONTHLY_STATISTICS_FETCHED,
    INSTALLATION_DASHBOARD__WEEKLY_STATISTICS_FETCHED,
} from '../../../shared/constants/events.constants';
import {GlobalDatabaseService} from '../../../shared/global-database/global-database.service';
import {KWprice, KWtoCO2Factor} from '../../../shared/constants/graph.constants';
import * as SunCalc from 'suncalc';
import 'moment-timezone/builds/moment-timezone-with-data-2012-2022';
import * as moment from 'moment-timezone';

declare var Dashboard: any;
declare var Chart: any;
declare var mUtil: any;
declare var Chartist: any;
declare var Morris: any;
declare var mApp: any;
declare var google: any;
declare const toastr: any;
declare var window: any;

@Component({
    selector: '.m-grid__item.m-grid__item--fluid.m-wrapper',
    templateUrl: './installation-wilamp-dashboard.component.html',
    styleUrls: ['installation-wilamp-dashboard.component.css'],
})
export class InstallationWilampDashboardComponent implements OnInit, OnDestroy, AfterViewInit {

    private chart_weeklyAvgPower: AmChart;
    Dashboard: any;
    Math: any;
    energyStatistics: EnergyStatistics;
    /*installation: InstallationWilamp;
    customer: CustomerWilamp;
    address: AddressWilamp;
    nodes: NodeWilamp[];
    nodesCount: number;
    gateways: GatewayWilamp[];
    gatewaysHM: {String, GatewayWilamp}[];
    gatewaysCount: number;
    */
    runtimeParameters: InstallationRuntimeParameters;
    mapOptions: MapOptions;
    itemsPerPage: number;
    links: any;
    page: any;
    predicate: any;
    reverse: any;
    totalItems: number;
    public currentAnalyzedDate: Date;
    public startInterval: Date;
    public endInterval: Date;
    private eventSubscriberInstallationFetched: Subscription;
    private eventSubscriberInstallationIdChanged: Subscription;
    private eventSubscriberNodesFetched: Subscription;
    private eventSubscriberGatewaysFetched: Subscription;
    private eventSubscriberWeeklyStatisticsByInstallationIdFetched: Subscription;
    private eventSubscriberStatisticsByNodeIdAndInstallationIdFetched: Subscription;
    private eventSubscriberInstallationWeeklyStatistics: Subscription;
    private googleMapsLoaded = false;
    private subscription: Subscription;
    private googleGeocoder: any;
    private timeAgo: any;
    public dailyEnergyConsumption: any;
    public weeklyEnergyConsumption: any;
    public monthlyEnergyConsumption: any;
    public dailyEnergyConsumptionOptions: any;
    public weeklyEnergyConsumptionOptions: any;
    public monthlyEnergyConsumptionOptions: any;
    public dailyEnergyConsumptionAvg = 0.0;
    public weeklyEnergyConsumptionAvg = 0.0;
    public lastWeekEnergyConsumptionAvg = 0.0;
    public monthlyEnergyConsumptionAvg = 0.0;
    public lastMonthEnergyConsumptionAvg = 0.0;
    public dailyEnergyConsumptionMax = 0.0;
    public weeklyEnergyConsumptionMax = 0.0;
    public lastWeekEnergyConsumptionMax = 0.0;
    public monthlyEnergyConsumptionMax = 0.0;
    public lastMonthEnergyConsumptionMax = 0.0;
    public lastMeasureReceivedTimestamp: Date;
    public lastMeasureReceivedTimeAgo = 'n/a';
    public totalEnergyConsumption = 0.0;
    public totalEnergyConsumptionWithoutDimming = 0.0;
    public totalEnergyConsumptionOldInstallation = 0.0;
    public absorbedPowerEstimation = 0.0;
    public averageDimming = 0.0;
    public plantPower = 0.0;
    public monthlyEnergySaved = 0.0;
    public lastMonthEnergySaved = 0.0;
    public totalEnergySaved = 0.0;
    public monthlyCo2Saved = 0.0;
    public lastMonthCo2Saved = 0.0;
    public totalCo2Saved = 0.0;
    public monthlyEarnings = 0.0;
    public lastMonthEarnings = 0.0;
    public totalEarnings = 0.0;
    public dataFetchingStatus = {
        isFetchingInstallation : true,
        isFetchingAddress: true,
        isFetchingNodes: true,
        isFetchingDailyStatistics: true,
        isFetchingWeeklyStatistics: true,
        isFetchingMonthlyStatistics: true,
        isFetchingGlobalStatistics: true,
        isFetchingIntervalStatistics: true,
        isFetchingLastMeasures: true,
        isFetchingMeasuresByNodeId: true,
    };

    public sunriseTime = '';
    public sunsetTime = '';
    public localTime = '';
    public localIsDayTime = true;

    public averageBurningTime = 0.0;
    public minBurningTime = 0.0;
    public maxBurningTime = 0.0;
    public timezoneCode = 'America/Los_Angeles';

    constructor(
        private AmCharts: AmChartsService,
        private eventManager: JhiEventManager,
        private installationService: InstallationWilampService,
        private customerService: CustomerWilampService,
        private addressService: AddressWilampService,
        private nodeService: NodeWilampService,
        private gatewayService: GatewayWilampService,
        private route: ActivatedRoute,
        private _script: ScriptLoaderService,
        private principal: Principal,
        public globalDatabase: GlobalDatabaseService,
    ) {
        this.Math = Math;
        this.endInterval = new Date();
        this.startInterval = new Date();
        this.currentAnalyzedDate = new Date();
        this.startInterval.setFullYear(this.startInterval.getFullYear() - 1);
        this.itemsPerPage = 100;
        this.page = 0;
        this.links = {
            last: 0,
        };
        this.predicate = 'id';
        this.reverse = true;
        this.mapOptions = new MapOptions();
    }

    ngOnInit() {
        this.subscription = this.route.params.subscribe((params) => {
            this.load(params['id']);
        });

        this.mapOptions.center = latLng(2.71241353356395, 101.99271440506);
        this.waitForEntities();
        this.registerChangeInInstallations();
        this.Dashboard = function() {
            const e = function(el1, t, a, r) {
                if (0 !== el1.length) {
                    const o = {
                        type: 'line',
                        data: {
                            labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October'],
                            datasets: [{
                                label: '',
                                borderColor: a,
                                borderWidth: r,
                                pointHoverRadius: 4,
                                pointHoverBorderWidth: 12,
                                pointBackgroundColor: Chart.helpers.color('#000000').alpha(0).rgbString(),
                                pointBorderColor: Chart.helpers.color('#000000').alpha(0).rgbString(),
                                pointHoverBackgroundColor: mUtil.getColor('danger'),
                                pointHoverBorderColor: Chart.helpers.color('#000000').alpha(.1).rgbString(),
                                fill: !1,
                                data: t,
                            }],
                        },
                        options: {
                            title: {display: !1},
                            tooltips: {
                                enabled: !1,
                                intersect: !1,
                                mode: 'nearest',
                                xPadding: 10,
                                yPadding: 10,
                                caretPadding: 10,
                            },
                            legend: {display: !1, labels: {usePointStyle: !1}},
                            responsive: !0,
                            maintainAspectRatio: !0,
                            hover: {mode: 'index'},
                            scales: {
                                xAxes: [{display: !1, gridLines: !1, scaleLabel: {display: !0, labelString: 'Month'}}],
                                yAxes: [{
                                    display: !1,
                                    gridLines: !1,
                                    scaleLabel: {display: !0, labelString: 'Value'},
                                    ticks: {beginAtZero: !0},
                                }],
                            },
                            elements: {point: {radius: 4, borderWidth: 12}},
                            layout: {padding: {left: 0, right: 10, top: 5, bottom: 0}},
                        },
                    };
                    return new Chart(el1, o);
                }
            };
            return {
                initChartSerialByDayOfWeek(energyStatisticsByDayOfWeek: EnergyStatisticsRowByInterval[][], graphTitle: String, labelField: any, valueField: any, baloonText: String, chartDivElement: String) {
                    try {
                        if (0 !== $('#' + chartDivElement).length) {

                            const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
                            const labels = [];
                            for (let k = 0; k < 24; k++) {
                                labels.push(k);
                            }
                            const chartData = [];
                            const graphs = [];

                            for (let hour = 0; hour < 24; hour++) {
                                for (let day = 0; day < 7; day++) {
                                    if (energyStatisticsByDayOfWeek[day][hour][valueField] < 0) {
                                        energyStatisticsByDayOfWeek[day][hour][valueField] = 0;
                                    }
                                    if (day === 0) {
                                        // first round
                                        const rowDefinition = {
                                            date: energyStatisticsByDayOfWeek[day][hour][labelField],
                                        };
                                        chartData[hour] = rowDefinition;
                                    }
                                    if (hour === 0) {
                                        const graph = {
                                            'balloonText': baloonText,
                                            'lineThickness': 2,
                                            'title': days[day],
                                            'valueField': valueField + '_' + day,
                                        };
                                        graphs.push(graph);
                                    }
                                    chartData[hour][valueField + '_' + day] = Math.round(energyStatisticsByDayOfWeek[day][hour][valueField] * 100) / 100;
                                }
                            }
                            const serialGraphDefinition = {
                                'type': 'serial',
                                'theme': 'light',
                                'marginRight': 0,
                                'marginLeft': 0,
                                'dataDateFormat': 'HH',
                                'dataProvider': chartData,
                                'valueAxes': [{
                                    'axisAlpha': 0,
                                    'guides': [{
                                        'fillAlpha': 0.1,
                                        'fillColor': '#888888',
                                        'lineAlpha': 0,
                                        'toValue': 16,
                                        'value': 10,
                                    }],
                                    'position': 'left',
                                    'tickLength': 0,
                                }],
                                'graphs': graphs,
                                'zoomOutButtonRollOverAlpha': 0.15,
                                'chartCursor': {
                                    'categoryBalloonDateFormat': 'MMM DD JJ:NN',
                                    'cursorPosition': 'mouse',
                                    'showNextAvailable': true,
                                },
                                'columnWidth': 1,
                                'categoryField': 'date',
                                'categoryAxis': {
                                    'minPeriod': 'hh',
                                    'parseDates': false,
                                },
                                /*'legend': {}*/
                            };
                            const chart = this.AmCharts.makeChart(chartDivElement, serialGraphDefinition);
                        }
                    } catch (Exception) {
                        console.warn(Exception);
                    }
                },
                initChartSerialByWeekNumber(energyStatisticsByWeekNumber: {}, graphTitle: String, labelField: any, valueField: any, baloonText: String, chartDivElement: String) {
                    if (0 !== $('#' + chartDivElement).length) {
                        const chartData = [];
                        for (const currentYear of Object.keys(energyStatisticsByWeekNumber)) {
                            for (const weekNumber of Object.keys(energyStatisticsByWeekNumber[currentYear])) {
                                chartData.push(energyStatisticsByWeekNumber[currentYear][weekNumber]);
                            }
                        }
                        let graphs = [
                            {
                                'balloonText': baloonText,
                                'lineThickness': 2,
                                'title': 'Measure count',
                                'valueField': 'measuresNumber',
                            }];

                        switch (valueField ) {
                            case 'activeEnergy': graphs = [
                                {
                                    'balloonText': baloonText,
                                    'lineThickness': 2,
                                    'title': 'Energy consumption',
                                    'valueField': 'sumEnergy',
                                },
                                {
                                    'balloonText': baloonText,
                                    'lineThickness': 2,
                                    'title': 'Energy consumption without dim',
                                    'valueField': 'sumEnergyWithoutDim',
                                },
                                {
                                    'balloonText': baloonText,
                                    'lineThickness': 2,
                                    'title': 'Energy consumption without control',
                                    'valueField': 'sumEnergyWithoutControl',
                                },
                                {
                                    'balloonText': baloonText,
                                    'lineThickness': 2,
                                    'title': 'Energy consumption previous installation',
                                    'valueField': 'sumEnergyOldLamps',
                                },
                            ];
                            break;
                            case 'measureCount': graphs = [
                                {
                                    'balloonText': baloonText,
                                    'lineThickness': 2,
                                    'title': 'Measures number',
                                    'valueField': 'measuresNumber',
                                },
                            ];
                            break;
                            case 'activePower': graphs = [
                                {
                                    'balloonText': baloonText,
                                    'lineThickness': 2,
                                    'title': 'Average power',
                                    'valueField': 'avgPower',
                                },
                            ];
                            break;
                            case 'burningTime': graphs = [
                                {
                                    'balloonText': baloonText,
                                    'lineThickness': 2,
                                    'title': 'Burning time',
                                    'valueField': 'burningTime',
                                },
                            ];
                                break;

                        }

                        const serialGraphDefinition = {
                            'type': 'serial',
                            'theme': 'light',
                            'marginRight': 0,
                            'marginLeft': 0,
                            'dataDateFormat': 'HH',
                            'dataProvider': chartData,
                            'valueAxes': [{
                                'axisAlpha': 0,
                                'guides': [{
                                    'fillAlpha': 0.1,
                                    'fillColor': '#888888',
                                    'lineAlpha': 0,
                                    'toValue': 16,
                                    'value': 10,
                                }],
                                'position': 'left',
                                'tickLength': 0,
                            }],
                            'graphs': graphs,
                            'zoomOutButtonRollOverAlpha': 0.15,
                            'chartCursor': {
                                'categoryBalloonDateFormat': 'MMM DD JJ:NN',
                                'cursorPosition': 'mouse',
                                'showNextAvailable': true,
                            },
                            'columnWidth': 1,
                            'categoryField': 'weekNumber',
                            'categoryAxis': {
                                'minPeriod': 'hh',
                                'parseDates': false,
                            },
                        };
                        const chart = this.AmCharts.makeChart(chartDivElement, serialGraphDefinition);
                    }
                },
                initChartConsumptionBullet(energyStatisticsByWeekNumber: GlobalStatistics, graphTitle: String, chartDivElement: String) {
                    if (0 !== $('#' + chartDivElement).length) {

                        const serialGraphDefinition = {
                            'addClassNames': true,
                            'type': 'serial',
                            'theme': 'light',
                            'autoMargins': true,
                            'marginTop': 0,
                            'marginLeft': 20,
                            'marginBottom': 50,
                            'marginRight': 40,
                            'usePrefixes': true,
                            'prefixesOfBigNumbers': [{number: 1e+3, prefix: 'k'}, {number: 1e+6, prefix: 'M'}, {number: 1e+9, prefix: 'G'}, {number: 1e+12, prefix: 'T'}, {number: 1e+15, prefix: 'P'}, {number: 1e+18, prefix: 'E'}, {number: 1e+21, prefix: 'Z'}, {number: 1e+24, prefix: 'Y'}],
                            'dataProvider': [ energyStatisticsByWeekNumber ],
                            'valueAxes': [ {
                                'minimum': 0,
                                'maximum': energyStatisticsByWeekNumber.sumEnergyOldLamps,
                                'stackType': 'regular',
                                'gridAlpha': 0,
                            } ],
                            'startDuration': 1,
                            'graphs': [
                                {
                                    'valueField': 'sumEnergyOldLamps',
                                    'classNameField': 'bulletClass',
                                    'clustered': false,
                                    'columnWidth': 0.7,
                                    'fillAlphas': 1,
                                    'stackable': false,
                                    'type': 'column',
                                    'cornerRadiusTop': 10,
                                    'lineColor': '#D1CDCD',
                                    'balloonText': '[[value]] KWh',
                                },
                                {
                                    'clustered': false,
                                    'columnWidth': 0.7,
                                    'fillAlphas': 0.5,
                                    'stackable': false,
                                    'type': 'column',
                                    'valueField': 'sumEnergyWithoutControl',
                                    'cornerRadiusTop': 10,
                                    'lineThickness': 0,
                                    'lineColor': '#F95E10',
                                    'balloonText': '[[value]] KWh',
                                }, {
                                    'clustered': false,
                                    'columnWidth': 0.7,
                                    'fillAlphas': 0.8,
                                    'stackable': false,
                                    'type': 'column',
                                    'valueField': 'sumEnergyWithoutDim',
                                    'cornerRadiusTop': 10,
                                    'lineColor': '#FCD410',
                                    'balloonText': '[[value]] KWh',
                                },
                                {
                                    'clustered': false,
                                    'columnWidth': 0.7,
                                    'fillAlphas': 0.8,
                                    'stackable': false,
                                    'type': 'column',
                                    'valueField': 'sumEnergy',
                                    'cornerRadiusTop': 10,
                                    'lineThickness': 0,
                                    'lineColor': '#1EC622',
                                    'balloonText': '[[value]] KWh',

                                },
                                {
                                    'columnWidth': 0.5,
                                    'lineColor': '#000000',
                                    'lineThickness': 3,
                                    'noStepRisers': true,
                                    'stackable': false,
                                    'type': 'step',
                                    'valueField': 'limit',
                                },
                            ],
                            'rotate': true,
                            'columnWidth': 0.1,
                            'categoryAxis': {
                                'gridAlpha': 0,
                                'position': 'left',
                                'categoryFunction': () => '',
                            },
                        };

                        const chart = this.AmCharts.makeChart(chartDivElement, serialGraphDefinition);
                    }
                },
                initChartEnergyStatistics(energyStatistics: EnergyStatistics) {
                    this.initChartSerialByDayOfWeek( energyStatistics.statisticsByDayOfWeek,  'Average power by day of week', 'hour', 'activePower', '[[title]]: [[value]]', 'char_day_of_week_avgpwr');
                    this.initChartSerialByDayOfWeek( energyStatistics.statisticsByDayOfWeek,  'Consumption by day of week', 'hour', 'activeEnergy', '[[title]]: [[value]]', 'char_day_of_week_energy_intervals');
                    this.initChartSerialByDayOfWeek( energyStatistics.statisticsByDayOfWeek,  'Number of measures by day of week', 'hour', 'measureCount', '[[title]]: [[value]]', 'char_day_of_week_measure_count');
                    this.initChartSerialByDayOfWeek( energyStatistics.statisticsByDayOfWeek,  'Number of measures by day of week', 'hour', 'burningTime', '[[title]]: [[value]]', 'char_day_of_week_burning_time');

                    this.initChartSerialByWeekNumber( energyStatistics.statisticsByWeekNumber,  'Average power by week number', 'hour', 'activePower', '[[title]]: [[value]]', 'char_weekly_avgpwr');
                    this.initChartSerialByWeekNumber( energyStatistics.statisticsByWeekNumber,  'Consumption by week number', 'hour', 'activeEnergy', '[[title]]: [[value]]', 'char_weekly_energy_intervals');
                    this.initChartSerialByWeekNumber( energyStatistics.statisticsByWeekNumber,  'Number of measures by week number', 'hour', 'measureCount', '[[title]]: [[value]]', 'char_weekly_measure_count');
                    this.initChartSerialByWeekNumber( energyStatistics.statisticsByWeekNumber,  'Burning time by week number', 'hour', 'burningTime', '[[title]]: [[value]]', 'char_weekly_burning_time');

                    this.initChartConsumptionBullet( energyStatistics.globalEnergyConsumption, 'Global consumption', 'chart_global_consumption' );
                    this.initChartConsumptionBullet( energyStatistics.currentIntervalEnergyConsumption, 'Global consumption', 'chart_current_interval_consumption' );
                },
            };
        }();
        this.Dashboard.AmCharts = this.AmCharts;
        this.resetInstallationData();
    }

    initializeTimeAndSunrise() {
        try {
            if (this.globalDatabase.selectedInstallation && this.globalDatabase.selectedInstallation.address) {
                const timeZoneCode = this.globalDatabase.selectedInstallation.address.timezoneCode;
                const options = {
                    timeZone: timeZoneCode,
                    year: 'numeric', month: 'numeric', day: 'numeric',
                    hour: 'numeric', minute: 'numeric', second: 'numeric',
                }, formatter = new Intl.DateTimeFormat([], options);
                this.localTime = moment().tz(timeZoneCode).format('YYYY-MM-DD HH:mm z');
                const sunriseSunset = SunCalc.getTimes(new Date(), this.globalDatabase.selectedInstallation.address.lat, this.globalDatabase.selectedInstallation.address.lng);
                this.sunriseTime = moment(sunriseSunset.sunrise).tz(timeZoneCode).format('HH:mm z');
                this.sunsetTime = moment(sunriseSunset.sunset).tz(timeZoneCode).format('HH:mm z');
                this.localIsDayTime = new Date() > sunriseSunset.sunrise && new Date() < sunriseSunset.sunset;
            }
        } catch (Exception) {
            console.warn(Exception);
        }
        try {
        } catch (Exception) {
            console.warn(Exception);
        }

    }

    getLocalDateTime() {
        return new Date();
    }

    initializePortlet() {
        const e = (<any>$('#m_portlet_chart_burningTime')).mPortlet();
        e.on('beforeCollapse', function(element) {
            setTimeout(function() {
                toastr.info('Before collapse event fired!');
            }, 100);
        }), e.on('afterCollapse', function(element) {
            setTimeout(function() {
                toastr.warning('Before collapse event fired!');
            }, 2e3);
        }), e.on('beforeExpand', function(element) {
            setTimeout(function() {
                toastr.info('Before expand event fired!');
            }, 100);
        }), e.on('afterExpand', function(element) {
            setTimeout(function() {
                toastr.warning('After expand event fired!');
            }, 2e3);
        }), e.on('beforeRemove', function(element) {
            return toastr.info('Before remove event fired!'), confirm('Are you sure to remove this portlet ?');
        }), e.on('afterRemove', function(element) {
            setTimeout(function() {
                toastr.warning('After remove event fired!');
            }, 2e3);
        }), e.on('reload', function(element) {
            toastr.info('Leload event fired!'), mApp.block(e.getSelf(), {
                overlayColor: '#000000',
                type: 'spinner',
                state: 'brand',
                opacity: .05,
                size: 'lg',
            }), setTimeout(function() {
                mApp.unblock(e.getSelf());
            }, 2e3);
        });
    }

    waitForEntities() {
        if (this.globalDatabase.selectedInstallation && this.globalDatabase.selectedInstallation.lightFixtures.length > 0) {
            this.updateMapBounds();
        } else {
            setTimeout(this.waitForEntities.bind(this), 250);
        }
    }

    startIntervalChanged(newInterval) {
        try {
            this.startInterval = new Date(newInterval);
            this.getRuntimeParameters(this.principal.selectedInstallationId);
        } catch (Exception) {
            console.warn(Exception);
        }
    }

    currentAnalyzedDateChanged(newInterval) {
        try {
            this.currentAnalyzedDate = new Date(newInterval);
            this.getRuntimeParameters(this.principal.selectedInstallationId);
        } catch (Exception) {
            console.warn(Exception);
        }
    }

    endIntervalChanged(newInterval) {
        try {
            this.endInterval = new Date(newInterval);
            this.getRuntimeParameters(this.principal.selectedInstallationId);
        } catch (Exception) {
            console.warn(Exception);
        }
    }

    sort() {
        const result = [this.predicate + ',' + (this.reverse ? 'asc' : 'desc')];
        if (this.predicate !== 'id') {
            result.push('id');
        }
        return result;
    }

    load(id) {
        this.globalDatabase.load(id);
        this.resetInstallationData();
        this.getRuntimeParameters(id);
        // this.getRuntimeParameters(id);
    }

    resetInstallationData() {
        this.dataFetchingStatus.isFetchingAddress = true;
        this.dataFetchingStatus.isFetchingDailyStatistics = true;
        this.dataFetchingStatus.isFetchingGlobalStatistics = true;
        this.dataFetchingStatus.isFetchingInstallation = true;
        this.dataFetchingStatus.isFetchingIntervalStatistics = true;
        this.dataFetchingStatus.isFetchingLastMeasures = true;
        this.dataFetchingStatus.isFetchingMeasuresByNodeId = true;
        this.dataFetchingStatus.isFetchingMonthlyStatistics = true;
        this.dataFetchingStatus.isFetchingNodes = true;
        this.dataFetchingStatus.isFetchingWeeklyStatistics = true;
        this.lastMeasureReceivedTimeAgo = 'n/a';
        this.lastMeasureReceivedTimestamp = null;
        this.localTime = 'n/a';
        this.sunriseTime = 'n/a';
        this.sunsetTime = 'n/a';
        this.absorbedPowerEstimation = 0;
        this.averageDimming = 0;
        this.plantPower = 0;
        this.monthlyEnergyConsumptionMax = 0;
        this.lastMonthEnergyConsumptionMax = 0;
        this.totalEnergyConsumption = 0;
        this.totalEnergyConsumption = 0;
        this.totalEnergyConsumptionWithoutDimming = 0;
        this.totalEnergyConsumptionOldInstallation = 0;
        this.monthlyEnergySaved = 0;
        this.lastMonthEnergySaved = 0;
        this.totalEnergySaved = 0;
        this.monthlyCo2Saved = 0;
        this.lastMonthCo2Saved = 0;
        this.totalCo2Saved = 0;
        this.monthlyEarnings = 0;
        this.lastMonthEarnings = 0;
        this.totalEarnings = 0;
    }

    updateRuntimeParameters() {
        if (this.principal.selectedInstallationId != null) {
            this.load(this.principal.selectedInstallationId);
        } else {
            setTimeout(this.updateRuntimeParameters.bind(this), 250);
        }
    }

    getRuntimeParameters(installationId) {
        this.resetInstallationData();
        this.installationService.getRuntimeParameters(installationId, this.startInterval, this.endInterval).subscribe((runtimeParameters) => {
            this.runtimeParameters = runtimeParameters;
            this.runtimeParameters.averageActivePower = Math.round(this.runtimeParameters.averageActivePower * 100) / 100;
            this.runtimeParameters.allTimePowerCosumption = Math.round(this.runtimeParameters.allTimePowerCosumption * 100) / 100;
            this.runtimeParameters.averageDimLevel = Math.round(this.runtimeParameters.averageDimLevel / 1023 * 100);

            if (isNaN(this.runtimeParameters.averageActivePower)) { this.runtimeParameters.averageActivePower = 0; }
            if (isNaN(this.runtimeParameters.allTimePowerCosumption)) { this.runtimeParameters.allTimePowerCosumption = 0; }
            if (isNaN(this.runtimeParameters.averageDimLevel)) { this.runtimeParameters.averageDimLevel = 0; }
        });
        // The following function will trigger an event (GLOBALDATABASE__INSTALLATION_WEEKLY_STATISTICS_FETCHED)
        // that will be managed by the function updateChartEnergyStatistics
        this.globalDatabase.fetchWeeklyEnergyStatisticsByInstallationId(installationId, this.startInterval, this.endInterval, this.currentAnalyzedDate);
        this.globalDatabase.fetchEnergyStatisticsByNodeId(installationId, null, this.startInterval, this.endInterval, this.currentAnalyzedDate);
        this.initializeTimeAndSunrise();
        // this.installationService.getWeeklyEnergyStatistics(installationId, null, this.startInterval, this.endInterval);
    }

    updateSelectedInstallationDetails() {
        this.dataFetchingStatus.isFetchingInstallation = false;
        this.dataFetchingStatus.isFetchingAddress = false;
        this.initializeTimeAndSunrise();
    }

    updateChartEnergyStatistics() {

        try {
            this.energyStatistics = this.globalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId;
        } catch (e) {
        }

        try {
            // RetrieupdateChartEnergyStatistics(reference) {ve data for badges

            const statisticsOfCurrentMonth = this.globalDatabase.selectedInstallation.energyStatistics.getStatisticsOfCurrentMonth(this.currentAnalyzedDate);
            if (statisticsOfCurrentMonth) {
                this.monthlyEnergyConsumptionMax = statisticsOfCurrentMonth.activeEnergyTotal;
                this.monthlyEnergySaved = Helpers.round(statisticsOfCurrentMonth.activeEnergyOldLampsTotal - statisticsOfCurrentMonth.activeEnergyTotal);
                this.monthlyCo2Saved = Helpers.round(this.monthlyEnergySaved * KWtoCO2Factor);
                this.monthlyEarnings = Helpers.round(this.monthlyEnergySaved * KWprice);
            }
            const statisticsOfLastMonth = this.globalDatabase.selectedInstallation.energyStatistics.getStatisticsOfPreviousMonth(this.currentAnalyzedDate);
            if (statisticsOfLastMonth) {
                this.lastMonthEnergyConsumptionMax = Helpers.round(statisticsOfLastMonth.activeEnergyTotal);
                this.lastMonthEnergySaved = Helpers.round(statisticsOfLastMonth.activeEnergyOldLampsTotal - statisticsOfLastMonth.activeEnergyTotal);
                this.lastMonthCo2Saved = Helpers.round(this.lastMonthEnergySaved * KWtoCO2Factor);
                this.lastMonthEarnings = Helpers.round(this.lastMonthEnergySaved * KWprice);
            }

            this.totalEnergyConsumption = Helpers.round(this.globalDatabase.selectedInstallation.energyStatistics.totalEnergyConsumption);
            this.totalEnergyConsumptionWithoutDimming = Helpers.round(this.globalDatabase.selectedInstallation.energyStatistics.totalEnergyConsumptionWithoutDimming);
            this.totalEnergyConsumptionOldInstallation = Helpers.round(this.globalDatabase.selectedInstallation.energyStatistics.totalEnergyConsumptionOldInstallation);
            this.totalEnergySaved = Helpers.round(this.globalDatabase.selectedInstallation.energyStatistics.totalEnergyConsumptionOldInstallation - this.globalDatabase.selectedInstallation.energyStatistics.totalEnergyConsumption);
            this.totalCo2Saved = Helpers.round(this.totalEnergySaved * KWtoCO2Factor);
            this.totalEarnings = Helpers.round(this.totalEnergySaved * KWprice);
            this.lastMeasureReceivedTimestamp = this.globalDatabase.selectedInstallation.energyStatistics.lastMeasureReceivedTimestamp;
            this.lastMeasureReceivedTimeAgo = moment(this.lastMeasureReceivedTimestamp).fromNow();
            this.dataFetchingStatus.isFetchingIntervalStatistics = false;
            this.dataFetchingStatus.isFetchingGlobalStatistics = false;
            this.dataFetchingStatus.isFetchingMonthlyStatistics = false;
            this.dataFetchingStatus.isFetchingDailyStatistics = false;
            this.dataFetchingStatus.isFetchingWeeklyStatistics = false;
            this.dataFetchingStatus.isFetchingAddress = false;
        } catch (Exception) {
            console.warn(Exception);
        }

        try {
            if (window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId && window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByHour.length > 0) {
                const todayData = Array();
                const currentDayOfWeek = (this.currentAnalyzedDate).getDay();
                let maxValue = 0.0;
                this.dailyEnergyConsumptionAvg = 0.0;
                this.dailyEnergyConsumptionMax = 0.0;
                for (let i = 0; i < window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByHour.length; i++) {
                    todayData[i] = [i, Math.round(window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByHour[i].activeEnergy * 10.0) / 10.0];
                    // if (window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByHour[i].day > 0) { currentDayOfWeek = window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByHour[i].day; }
                    this.dailyEnergyConsumptionAvg += todayData[i][1] / 24.0;
                    this.dailyEnergyConsumptionMax += todayData[i][1];
                    if (todayData[i][1] > maxValue) { maxValue = todayData[i][1]; }
                }
                const todayAvgData = Array();
                for (let i = 0; i < window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsByDayOfWeek[currentDayOfWeek].length; i++) {
                    todayAvgData[i] = [i, window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsByDayOfWeek[currentDayOfWeek][i].sumEnergy];
                    if (todayAvgData[i][1] > maxValue) { maxValue = todayAvgData[i][1]; }
                }
                this.dailyEnergyConsumptionAvg = Math.round(this.dailyEnergyConsumptionAvg);
                this.dailyEnergyConsumptionMax = Math.round(this.dailyEnergyConsumptionMax);
                this.dailyEnergyConsumptionOptions.yaxis.max = Math.round(maxValue) + 1;
                this.dailyEnergyConsumption[0].data = todayData;
                this.dailyEnergyConsumption[1].data = todayAvgData;
                this.eventManager.broadcast({
                    name: INSTALLATION_DASHBOARD__DAILY_STATISTICS_FETCHED,
                    content: { dataset: this.dailyEnergyConsumption, options: this.dailyEnergyConsumptionOptions },
                });
            }
        } catch (Exception) {
            console.warn(Exception);
        }

        try {
            if (window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId && window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByDayOfWeek.length > 0) {
                const todayData = Array();
                this.weeklyEnergyConsumptionAvg = 0.0;
                this.weeklyEnergyConsumptionMax = 0.0;
                this.lastWeekEnergyConsumptionAvg = 0.0;
                this.lastWeekEnergyConsumptionMax = 0.0;
                let maxValue = 0.0;
                for (let i = 0; i < window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByDayOfWeek.length; i++) {
                    todayData[i] = [i, Math.round(window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByDayOfWeek[i].sumEnergy * 10.0) / 10.0];
                    // if (window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByHour[i].day > 0) { currentDayOfWeek = window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByHour[i].day; }
                    this.weeklyEnergyConsumptionAvg += todayData[i][1] / 7.0;
                    this.weeklyEnergyConsumptionMax += todayData[i][1];
                    if (todayData[i][1] > maxValue) { maxValue = todayData[i][1]; }
                }
                const todayAvgData = Array();
                for (let i = 0; i < window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfLastWeekByDayOfWeek.length; i++) {
                    let sumEnergy = 0.0;
                    sumEnergy += window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfLastWeekByDayOfWeek[i].sumEnergy;
                    todayAvgData[i] = [i, sumEnergy];
                    if (todayAvgData[i][1] > maxValue) { maxValue = todayAvgData[i][1]; }
                    this.lastWeekEnergyConsumptionAvg += todayAvgData[i][1] / 7.0;
                    this.lastWeekEnergyConsumptionMax += todayAvgData[i][1];

                }
                this.weeklyEnergyConsumptionAvg = Math.round(this.weeklyEnergyConsumptionAvg);
                this.weeklyEnergyConsumptionMax = Math.round(this.weeklyEnergyConsumptionMax);
                this.lastWeekEnergyConsumptionAvg = Math.round(this.lastWeekEnergyConsumptionAvg);
                this.lastWeekEnergyConsumptionMax = Math.round(this.lastWeekEnergyConsumptionMax);
                this.weeklyEnergyConsumptionOptions.yaxis.max = Math.round(maxValue) + 1;
                this.weeklyEnergyConsumption[0].data = todayData;
                this.weeklyEnergyConsumption[1].data = todayAvgData;
                this.eventManager.broadcast({
                    name: INSTALLATION_DASHBOARD__WEEKLY_STATISTICS_FETCHED,
                    content: { dataset: this.weeklyEnergyConsumption, options: this.weeklyEnergyConsumptionOptions },
                });
            }
        } catch (Exception) {
            console.warn(Exception);
        }

        try {
            if (window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId && window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByDayOfMonth.length > 0) {
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
                for (let i = 0; i < window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByDayOfMonth.length; i++) {
                    todayData[i] = [i, Math.round(window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByDayOfMonth[i].sumEnergy * 10.0) / 10.0];
                    // if (window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByHour[i].day > 0) { currentDayOfWeek = window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByHour[i].day; }
                    this.monthlyEnergyConsumptionAvg += todayData[i][1] / daysInCurrentMonth;
                    this.monthlyEnergyConsumptionMax += todayData[i][1];
                    const energySaved = window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByDayOfMonth[i].sumEnergyOldLamps - window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfTodayByDayOfMonth[i].sumEnergy;
                    if (energySaved > 0) { this.monthlyEnergySaved += energySaved; }
                    if (todayData[i][1] > maxValue) { maxValue = todayData[i][1]; }
                }
                const todayAvgData = Array();
                for (let i = 0; i < window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfLastMonthByDayOfMonth.length; i++) {
                    let sumEnergy = 0.0;
                    sumEnergy += window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfLastMonthByDayOfMonth[i].sumEnergy;
                    todayAvgData[i] = [i, sumEnergy];
                    if (todayAvgData[i][1] > maxValue) { maxValue = todayAvgData[i][1]; }
                    this.lastMonthEnergyConsumptionAvg += todayAvgData[i][1] / daysInCurrentMonth;
                    this.lastMonthEnergyConsumptionMax += todayAvgData[i][1];
                    const energySaved = window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfLastMonthByDayOfMonth[i].sumEnergyOldLamps - window.GlobalDatabase.selectedInstallation.weeklyEnergyStatisticsByInstallationId.statisticsOfLastMonthByDayOfMonth[i].sumEnergy;
                    if (energySaved > 0) { this.lastMonthEnergySaved += energySaved; }
                }
                this.monthlyCo2Saved = this.monthlyEnergySaved * KWtoCO2Factor;
                this.monthlyCo2Saved = Math.round(this.monthlyCo2Saved);
                this.monthlyEnergySaved = Math.round(this.monthlyEnergySaved);
                this.lastMonthCo2Saved = this.lastMonthEnergySaved * KWtoCO2Factor;
                this.lastMonthCo2Saved = Math.round(this.lastMonthCo2Saved);
                this.lastMonthEnergySaved = Math.round(this.lastMonthEnergySaved);
                this.monthlyEnergyConsumptionAvg = Math.round(this.monthlyEnergyConsumptionAvg);
                this.monthlyEnergyConsumptionMax = Math.round(this.monthlyEnergyConsumptionMax);
                this.lastMonthEnergyConsumptionAvg = Math.round(this.lastMonthEnergyConsumptionAvg);
                this.lastMonthEnergyConsumptionMax = Math.round(this.lastMonthEnergyConsumptionMax);
                this.monthlyEnergyConsumptionOptions.yaxis.max = Math.round(maxValue) + 1;
                this.monthlyEnergyConsumption[0].data = todayData;
                this.monthlyEnergyConsumption[1].data = todayAvgData;
                this.eventManager.broadcast({
                    name: INSTALLATION_DASHBOARD__MONTHLY_STATISTICS_FETCHED,
                    content: { dataset: this.monthlyEnergyConsumption, options: this.monthlyEnergyConsumptionOptions },
                });
                this.dataFetchingStatus.isFetchingMonthlyStatistics = false;
            }
        } catch (Exception) {
            console.warn(Exception);
        }

        try {
            this.Dashboard.initChartEnergyStatistics(this.energyStatistics);
        } catch (Exception) {
            console.warn(Exception);
        }
    }

    updateStatisticsByNodeId() {
        try {
            if (window.GlobalDatabase.selectedInstallation.statisticsByNodeId) {
                this.averageBurningTime = 0.0;
                this.minBurningTime = 0.0;
                this.maxBurningTime = 0.0;
                // this.lastMeasureReceivedTimestamp = new Date(0);
                window.GlobalDatabase.selectedInstallation.statisticsByNodeId.forEach((function(value) {
                    this.averageBurningTime += value.burningTime / window.GlobalDatabase.selectedInstallation.statisticsByNodeId.length;
                    if (value.burningTime > this.maxBurningTime) { this.maxBurningTime = value.burningTime; }
                    if (this.minBurningTime === 0.0) { this.minBurningTime = value.burningTime; }
                    if (value.burningTime < this.minBurningTime) { this.minBurningTime = value.burningTime; }
                    if (value.activePower) { this.absorbedPowerEstimation += value.activePower; }
                    if (value.lightLevel) { this.averageDimming += value.lightLevel / window.GlobalDatabase.selectedInstallation.statisticsByNodeId.length; }
                    this.plantPower += value.nominalPower;
                    // if (new Date(value.lastMeasureTimestamp) > this.lastMeasureReceivedTimestamp) { this.lastMeasureReceivedTimestamp = new Date(value.lastMeasureTimestamp); }
                }).bind(this));
                this.averageBurningTime = Math.round(this.averageBurningTime / 60.0);
                this.minBurningTime = Math.round(this.minBurningTime / 60.0);
                this.maxBurningTime = Math.round(this.maxBurningTime / 60.0);
                this.absorbedPowerEstimation =  Math.round(this.absorbedPowerEstimation / 1000.0);
                this.averageDimming =  Math.round(this.averageDimming * 100 / 1023);
                this.plantPower =  Math.round(this.plantPower / 1000.0 );
                // console.warn(date1.getTimezoneOffset());
                this.dataFetchingStatus.isFetchingMeasuresByNodeId = false;
            }
        } catch (Exception) {
            console.warn(Exception);
        }
    }

    updateMapBounds() {
        if (this.googleMapsLoaded) {
            this.mapOptions.bounds = MapHelpers.generateBounds(this.globalDatabase.selectedInstallation.lightFixtures);
            /* this.mapOptions.center.lat = (this.mapOptions.bounds.northeast.latitude + this.mapOptions.bounds.southwest.latitude) / 2;
            this.mapOptions.center.lng = (this.mapOptions.bounds.northeast.longitude + this.mapOptions.bounds.southwest.longitude) / 2;

            this.mapsAPIWrapper.fitBounds(this.mapOptions.bounds);
            this.mapsAPIWrapper.getNativeMap().then((m) => {
                console.warn(google.maps);
                console.warn(m);
            }); */
        } else {
            setTimeout(this.updateMapBounds.bind(this), 250);
        }
    }

    getIconForNode(node: NodeWilamp) {
        if (node.nodeType != null) {
            switch (node.nodeType) {
                case 10:
                    // Coordinator
                    return '/assets/app/media/img/wilamp-icons/1x/coordinator.png';
                default:
                    return '/assets/app/media/img/wilamp-icons/1x/light_on.png';
            }
        }
        return '/assets/app/media/img/wilamp-icons/light_on.png';
    }

    previousState() {
        window.history.back();
    }

    ngOnDestroy() {
        this.eventManager.destroy(this.eventSubscriberNodesFetched);
        this.eventManager.destroy(this.eventSubscriberGatewaysFetched);
        this.eventManager.destroy(this.eventSubscriberWeeklyStatisticsByInstallationIdFetched);
        this.eventManager.destroy(this.eventSubscriberInstallationIdChanged);
        this.eventManager.destroy(this.eventSubscriberInstallationFetched);
        this.eventManager.destroy(this.eventSubscriberStatisticsByNodeIdAndInstallationIdFetched);
        this.eventManager.destroy(this.eventSubscriberInstallationWeeklyStatistics);
    }

    registerChangeInInstallations() {
        this.eventSubscriberInstallationFetched = this.eventManager.subscribe(
            GLOBALDATABASE__INSTALLATION_FETCHED,
            (response) => this.updateSelectedInstallationDetails(),
        );
        this.eventSubscriberInstallationIdChanged = this.eventManager.subscribe(
            INSTALLATION__SELECTED_ID_CHANGED,
            (response) => this.load(this.principal.selectedInstallationId),
        );
        this.eventSubscriberNodesFetched = this.eventManager.subscribe(
            GLOBALDATABASE__GATEWAYS_FETCHED,
            (response) => this.updateMapBounds(),
        );
        this.eventSubscriberGatewaysFetched = this.eventManager.subscribe(
            GLOBALDATABASE__LIGHT_FIXTURES_FETCHED,
            (response) => this.updateMapBounds(),
        );
        this.eventSubscriberWeeklyStatisticsByInstallationIdFetched = this.eventManager.subscribe(
            GLOBALDATABASE__INSTALLATION_WEEKLY_STATISTICS_FETCHED,
            (response) => this.updateChartEnergyStatistics(),
        );
        this.eventSubscriberStatisticsByNodeIdAndInstallationIdFetched = this.eventManager.subscribe(
            GLOBALDATABASE__INSTALLATION_STATISTICS_BY_NODEID_FETCHED,
            (response) => this.updateStatisticsByNodeId(),
        );
        this.eventSubscriberInstallationWeeklyStatistics = this.eventManager.subscribe(
            GLOBALDATABASE__INSTALLATION_WEEKLY_STATISTICS_FETCHING,
            (response) => {
                this.dataFetchingStatus.isFetchingWeeklyStatistics = true;
                this.dataFetchingStatus.isFetchingDailyStatistics = true;
                this.dataFetchingStatus.isFetchingMonthlyStatistics = true;
            },
        );

    }

    formatPowerConsumption(power) {
        return Helpers.formatPowerConsumption(power);
    }

    ngAfterViewInit() {
        /*this._script.load('.m-grid__item.m-grid__item--fluid.m-wrapper',
            'assets/demo/default/custom/components/portlets/tools.js');
        */
        /*this._script.load('.m-grid__item.m-grid__item--fluid.m-wrapper',
            'assets/app/js/dashboard.js').then( (result) => {
                jQuery(document).ready(function() {
                    this.initializePortlet()
                });
            });*/
        this.updateChartEnergyStatistics();
    }

}
