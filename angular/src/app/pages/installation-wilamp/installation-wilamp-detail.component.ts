/* tslint:disable:no-unused-expression */
import {Component, OnInit, OnDestroy, AfterViewInit} from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse } from '@angular/common/http';
import { Subscription } from 'rxjs';
import { JhiEventManager } from 'ng-jhipster';
import { AmChartsService, AmChart } from '@amcharts/amcharts3-angular';

import {
    InstallationRuntimeParameters, InstallationWilamp, EnergyStatistics,
    EnergyStatisticsRowByInterval, GlobalStatistics
} from './installation-wilamp.model';
import { InstallationWilampService } from './installation-wilamp.service';
import {ScriptLoaderService} from '../../_services/script-loader.service';
import {CustomerWilamp} from '../customer-wilamp/customer-wilamp.model';
import {CustomerWilampService} from '../customer-wilamp/customer-wilamp.service';
import {AddressWilamp} from '../address-wilamp/address-wilamp.model';
import {AddressWilampService} from '../address-wilamp/address-wilamp.service';
import {circle, latLng, polygon, tileLayer} from 'leaflet';
import {NodeWilamp} from '../node-wilamp/node-wilamp.model';
import {NodeWilampService} from '../node-wilamp/node-wilamp.service';
import {MapHelpers} from '../../shared/maps/map.helpers';
import {MapOptions} from '../../shared/maps/map.models';
import {GoogleMapsAPIWrapper, MapsAPILoader} from '@agm/core';
import {GatewayWilamp} from '../gateway-wilamp/gateway-wilamp.model';
import {GatewayWilampService} from '../gateway-wilamp/gateway-wilamp.service';

declare var Dashboard: any;
declare var Chart: any;
declare var mUtil: any;
declare var Chartist: any;
declare var Morris: any;
declare var moment: any;
declare var mApp: any;
declare var google: any;

@Component({
    selector: 'jhi-installation-wilamp-detail',
    templateUrl: './installation-wilamp-detail.component.html',
    styleUrls: ['installation-wilamp-detail.component.css']
})
export class InstallationWilampDetailComponent implements OnInit, OnDestroy, AfterViewInit {
    private chart_weeklyAvgPower: AmChart;
    Dashboard: any;
    Math: any;
    installation: InstallationWilamp;
    customer: CustomerWilamp;
    address: AddressWilamp;
    nodes: NodeWilamp[];
    nodesCount: number;
    gateways: GatewayWilamp[];
    gatewaysHM: {String, GatewayWilamp}[];
    gatewaysCount: number;
    runtimeParameters: InstallationRuntimeParameters;
    energyStatistics: EnergyStatistics;
    mapOptions: MapOptions;
    layersControl = {
        baseLayers: {
            'Open Street Map': tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 18, attribution: '...' }),
            'Open Cycle Map': tileLayer('http://{s}.tile.opencyclemap.org/{z}/{x}/{y}.png', { maxZoom: 18, attribution: '...' })
        },
        overlays: {
            'Big Circle': circle([ 46.95, -122 ], { radius: 5000 }),
            'Big Square': polygon([[ 46.8, -121.55 ], [ 46.9, -121.55 ], [ 46.9, -121.7 ], [ 46.8, -121.7 ]])
        }
    };
    itemsPerPage: number;
    links: any;
    page: any;
    predicate: any;
    reverse: any;
    totalItems: number;
    public startInterval: Date;
    public endInterval: Date;
    private subscription: Subscription;
    private eventSubscriber: Subscription;
    private googleMapsLoaded = false;
    private googleGeocoder: any;

    constructor(
        private mapsAPILoader: MapsAPILoader,
        private mapsAPIWrapper: GoogleMapsAPIWrapper,
        private AmCharts: AmChartsService,
        private eventManager: JhiEventManager,
        private installationService: InstallationWilampService,
        private customerService: CustomerWilampService,
        private addressService: AddressWilampService,
        private nodeService: NodeWilampService,
        private gatewayService: GatewayWilampService,
        private route: ActivatedRoute,
        private _script: ScriptLoaderService
    ) {
        this.Math = Math;
        this.endInterval = new Date();
        this.startInterval = new Date();
        this.startInterval.setMonth(this.startInterval.getMonth() - 1);
        this.itemsPerPage = 100;
        this.page = 1;
        this.links = {
            last: 0
        };
        this.predicate = 'id';
        this.reverse = true;
        this.mapOptions = new MapOptions();
        this.mapsAPILoader.load().then(() => {
            this.googleMapsLoaded = true;
            this.googleGeocoder = new google.maps.Geocoder();
        });

        // this.startInterval = this.startInterval.toISOString().slice(0, 16);
    }

    ngOnInit() {
        this.mapOptions.center = latLng(2.71241353356395, 101.99271440506);
        this.subscription = this.route.params.subscribe((params) => {
            this.load(params['id']);
        });
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
                                data: t
                            }]
                        },
                        options: {
                            title: {display: !1},
                            tooltips: {
                                enabled: !1,
                                intersect: !1,
                                mode: 'nearest',
                                xPadding: 10,
                                yPadding: 10,
                                caretPadding: 10
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
                                    ticks: {beginAtZero: !0}
                                }]
                            },
                            elements: {point: {radius: 4, borderWidth: 12}},
                            layout: {padding: {left: 0, right: 10, top: 5, bottom: 0}}
                        }
                    };
                    return new Chart(el1, o);
                }
            };
            return {
                initAllCharts() {
                    this.initChartWeeklyTrends();
                    this.initChartPhaseDistribution();
                    this.initChartTotalCycles();
                    this.initChartCyclesGrowth();
                    this.initChartWeeklyCycles();
                },
                initChartPhaseDistribution(phaseDurations) {
                    if (0 !== $('#m_chart_phase_distribution').length) {
                        const chartElement = new Chartist.Pie('#m_chart_phase_distribution', {
                            series: [{
                                value: phaseDurations.phase1,
                                className: 'custom',
                                meta: {color: mUtil.getColor('accent')}
                            },
                                {
                                    value: phaseDurations.phase2,
                                    className: 'custom',
                                    meta: {color: mUtil.getColor('warning')}
                                },
                                {
                                    value: phaseDurations.remaining,
                                    className: 'custom',
                                    meta: {color: mUtil.getColor('brand')}
                                }], labels: [1, 2, 3]
                        }, {donut: !0, donutWidth: 17, showLabel: !1});
                        chartElement.on('draw', function(elm) {
                            if ('slice' === elm.type) {
                                const t = elm.element._node.getTotalLength();
                                elm.element.attr({'stroke-dasharray': t + 'px ' + t + 'px'});
                                const a = {
                                    'stroke-dashoffset': {
                                        id: 'anim' + elm.index,
                                        dur: 1e3,
                                        from: -t + 'px',
                                        to: '0px',
                                        easing: Chartist.Svg.Easing.easeOutQuint,
                                        fill: 'freeze',
                                        stroke: elm.meta.color
                                    }
                                };
                                0 !== elm.index && ((<any>a['stroke-dashoffset']).begin = 'anim' + (elm.index - 1) + '.end'), elm.element.attr({
                                    'stroke-dashoffset': -t + 'px',
                                    stroke: elm.meta.color
                                }), elm.element.animate(a, !1);
                            }
                        }), chartElement.on('created', function() {
                            /* eslint-disable no-unused-expressions */
                            (<any>window).__anim21278907124 && (clearTimeout((<any>window).__anim21278907124), (<any>window).__anim21278907124 = null), (<any>window).__anim21278907124 = setTimeout(chartElement.update.bind(chartElement), 15e3);
                        });
                    }
                },
                initChartWeeklyTrends(weeklyTrends) {
                    const labels = weeklyTrends.map(function(idx, el) { return 'Week ' + el; });
                    const values = weeklyTrends.map(function(el) { return ' ' + el; });
                    const data = {
                        labels,
                        datasets: [{
                            backgroundColor: mUtil.getColor('success'),
                            data: values
                        }, {
                            backgroundColor: '#f3f3fb',
                            data: values
                        }]
                    }, t = $('#m_chart_daily_sales');
                    const result = 0 !== t.length && new Chart(t, {
                        type: 'bar',
                        data,
                        options: {
                            title: {display: !1},
                            tooltips: {intersect: !1, mode: 'nearest', xPadding: 10, yPadding: 10, caretPadding: 10},
                            legend: {display: !1},
                            responsive: !0,
                            maintainAspectRatio: !1,
                            barRadius: 4,
                            scales: {
                                xAxes: [{display: !1, gridLines: !1, stacked: !0}],
                                yAxes: [{display: !1, stacked: !0, gridLines: !1}]
                            },
                            layout: {padding: {left: 0, right: 0, top: 0, bottom: 0}}
                        }
                    });
                },

                initChartTotalCycles(monthlyTrends) {
                    const monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
                    const labels = monthlyTrends.map(function(idx, el) { return monthNames[el]; });
                    const values = monthlyTrends.map(function(el) { return ' ' + el; });

                    if (0 !== $('#m_chart_total_cycles').length) {
                        const chartElement = (<any>document.getElementById('m_chart_total_cycles')).getContext('2d'),
                            t = chartElement.createLinearGradient(0, 0, 0, 240);
                        t.addColorStop(0, Chart.helpers.color('#d1f1ec').alpha(1).rgbString()), t.addColorStop(1, Chart.helpers.color('#d1f1ec').alpha(.3).rgbString());
                        const a = {
                            type: 'line',
                            data: {
                                labels,
                                datasets: [{
                                    label: 'cycles',
                                    backgroundColor: t,
                                    borderColor: mUtil.getColor('success'),
                                    pointBackgroundColor: Chart.helpers.color('#000000').alpha(0).rgbString(),
                                    pointBorderColor: Chart.helpers.color('#000000').alpha(0).rgbString(),
                                    pointHoverBackgroundColor: mUtil.getColor('danger'),
                                    pointHoverBorderColor: Chart.helpers.color('#000000').alpha(.1).rgbString(),
                                    data: values
                                }]
                            },
                            options: {
                                title: {display: !1},
                                tooltips: {
                                    mode: 'nearest',
                                    intersect: !1,
                                    position: 'nearest',
                                    xPadding: 10,
                                    yPadding: 10,
                                    caretPadding: 10
                                },
                                legend: {display: !1},
                                responsive: !0,
                                maintainAspectRatio: !1,
                                scales: {
                                    xAxes: [{display: !1, gridLines: !1, scaleLabel: {display: !0, labelString: 'Month'}}],
                                    yAxes: [{
                                        display: !1,
                                        gridLines: !1,
                                        scaleLabel: {display: !0, labelString: 'Value'},
                                        ticks: {beginAtZero: !0}
                                    }]
                                },
                                elements: {line: {tension: 1e-7}, point: {radius: 4, borderWidth: 12}},
                                layout: {padding: {left: 0, right: 0, top: 10, bottom: 0}}
                            }
                        };
                        const newChart = new Chart(chartElement, a);
                    }
                },
                initChartCyclesGrowth() {
                    if (0 !== $('#m_chart_cycles_growth').length) {
                        const chartElement = (<any>document.getElementById('m_chart_cycles_growth')).getContext('2d'),
                            t = chartElement.createLinearGradient(0, 0, 0, 240);
                        t.addColorStop(0, Chart.helpers.color('#ffefce').alpha(1).rgbString()), t.addColorStop(1, Chart.helpers.color('#ffefce').alpha(.3).rgbString());
                        const a = {
                            type: 'line',
                            data: {
                                labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October'],
                                datasets: [{
                                    label: '% growth',
                                    backgroundColor: t,
                                    borderColor: mUtil.getColor('warning'),
                                    pointBackgroundColor: Chart.helpers.color('#000000').alpha(0).rgbString(),
                                    pointBorderColor: Chart.helpers.color('#000000').alpha(0).rgbString(),
                                    pointHoverBackgroundColor: mUtil.getColor('danger'),
                                    pointHoverBorderColor: Chart.helpers.color('#000000').alpha(.1).rgbString(),
                                    data: [8.2, 11.5, 9.8, 13.1, 7.4, 9, 10.7, 7.4, 10.7, 12.3]
                                    /*data: [10, 24, 36, 52, 61, 72, 85, 94, 107, 122]*/
                                }]
                            },
                            options: {
                                title: {display: !1},
                                tooltips: {
                                    mode: 'nearest',
                                    intersect: !1,
                                    position: 'nearest',
                                    xPadding: 10,
                                    yPadding: 10,
                                    caretPadding: 10
                                },
                                legend: {display: !1},
                                responsive: !0,
                                maintainAspectRatio: !1,
                                scales: {
                                    xAxes: [{display: !1, gridLines: !1, scaleLabel: {display: !0, labelString: 'Month'}}],
                                    yAxes: [{
                                        display: !1,
                                        gridLines: !1,
                                        scaleLabel: {display: !0, labelString: 'Value'},
                                        ticks: {beginAtZero: !0}
                                    }]
                                },
                                elements: {line: {tension: 1e-7}, point: {radius: 4, borderWidth: 12}},
                                layout: {padding: {left: 0, right: 0, top: 10, bottom: 0}}
                            }
                        };
                        const newChart = new Chart(chartElement, a);
                    }
                },
                initChartWeeklyCycles(dailyTrends) {
                    const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
                    const labels = dailyTrends.map(function(idx, el) { return days[el]; });
                    const values = dailyTrends.map(function(el) { return ' ' + el; });

                    if (0 !== $('#m_chart_weeklyAvgPower').length) {
                        const chartElement = (<any>document.getElementById('m_chart_initChartWeeklyCycles')).getContext('2d'),
                            t = chartElement.createLinearGradient(0, 0, 0, 240);
                        t.addColorStop(0, Chart.helpers.color('#e14c86').alpha(1).rgbString()), t.addColorStop(1, Chart.helpers.color('#e14c86').alpha(.3).rgbString());
                        const a = {
                            type: 'line',
                            data: {
                                labels,
                                datasets: [{
                                    label: 'Weekly cycles',
                                    backgroundColor: t,
                                    borderColor: '#e13a58',
                                    pointBackgroundColor: Chart.helpers.color('#000000').alpha(0).rgbString(),
                                    pointBorderColor: Chart.helpers.color('#000000').alpha(0).rgbString(),
                                    pointHoverBackgroundColor: mUtil.getColor('light'),
                                    pointHoverBorderColor: Chart.helpers.color('#ffffff').alpha(.1).rgbString(),
                                    data: values
                                }]
                            },
                            options: {
                                title: {display: !1},
                                tooltips: {
                                    mode: 'nearest',
                                    intersect: !1,
                                    position: 'nearest',
                                    xPadding: 10,
                                    yPadding: 10,
                                    caretPadding: 10
                                },
                                legend: {display: !1},
                                responsive: !0,
                                maintainAspectRatio: !1,
                                scales: {
                                    xAxes: [{display: !1, gridLines: !1, scaleLabel: {display: !0, labelString: 'Month'}}],
                                    yAxes: [{
                                        display: !1,
                                        gridLines: !1,
                                        scaleLabel: {display: !0, labelString: 'Value'},
                                        ticks: {beginAtZero: !0}
                                    }]
                                },
                                elements: {line: {tension: 1e-7}, point: {radius: 4, borderWidth: 12}},
                                layout: {padding: {left: 0, right: 0, top: 10, bottom: 0}}
                            }
                        };
                        const newChart = new Chart(chartElement, a);
                    }
                },
                initChartSerialByDayOfWeek(energyStatisticsByDayOfWeek: EnergyStatisticsRowByInterval[][], graphTitle: String, labelField: any, valueField: any, baloonText: String, chartDivElement: String) {
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
                                        'valueField': valueField + '_' + day
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
                                    'value': 10
                                }],
                                'position': 'left',
                                'tickLength': 0
                            }],
                            'graphs': graphs,
                            'zoomOutButtonRollOverAlpha': 0.15,
                            'chartCursor': {
                                'categoryBalloonDateFormat': 'MMM DD JJ:NN',
                                'cursorPosition': 'mouse',
                                'showNextAvailable': true
                            },
                            'columnWidth': 1,
                            'categoryField': 'date',
                            'categoryAxis': {
                                'minPeriod': 'hh',
                                'parseDates': false
                            },
                            /*'legend': {}*/
                        };
                        const chart = this.AmCharts.makeChart(chartDivElement, serialGraphDefinition);
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

                        const graphs = [
                            {
                                'balloonText': baloonText,
                                'lineThickness': 2,
                                'title': 'Energy consumption',
                                'valueField': 'sumEnergy'
                            },
                            {
                                'balloonText': baloonText,
                                'lineThickness': 2,
                                'title': 'Energy consumption without dim',
                                'valueField': 'sumEnergyWithoutDim'
                            },
                            {
                                'balloonText': baloonText,
                                'lineThickness': 2,
                                'title': 'Energy consumption without control',
                                'valueField': 'sumEnergyWithoutControl'
                            },
                            {
                                'balloonText': baloonText,
                                'lineThickness': 2,
                                'title': 'Energy consumption previous installation',
                                'valueField': 'sumEnergyOldLamps'
                            },
                        ];
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
                                    'value': 10
                                }],
                                'position': 'left',
                                'tickLength': 0
                            }],
                            'graphs': graphs,
                            'zoomOutButtonRollOverAlpha': 0.15,
                            'chartCursor': {
                                'categoryBalloonDateFormat': 'MMM DD JJ:NN',
                                'cursorPosition': 'mouse',
                                'showNextAvailable': true
                            },
                            'columnWidth': 1,
                            'categoryField': 'weekNumber',
                            'categoryAxis': {
                                'minPeriod': 'hh',
                                'parseDates': false
                            }
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
                                'gridAlpha': 0
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
                                    'balloonText': '[[value]] KWh'
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
                                    'balloonText': '[[value]] KWh'

                                },
                                {
                                    'columnWidth': 0.5,
                                    'lineColor': '#000000',
                                    'lineThickness': 3,
                                    'noStepRisers': true,
                                    'stackable': false,
                                    'type': 'step',
                                    'valueField': 'limit'
                                }
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
                    this.initChartSerialByDayOfWeek( energyStatistics.statisticsByDayOfWeek,  'Energy by day of week', 'hour', 'activeEnergy', '[[title]]: [[value]]', 'char_day_of_week_energy_intervals');
                    this.initChartSerialByDayOfWeek( energyStatistics.statisticsByDayOfWeek,  'Number of measures by day of week', 'hour', 'measureCount', '[[title]]: [[value]]', 'char_day_of_week_measure_count');

                    this.initChartSerialByWeekNumber( energyStatistics.statisticsByWeekNumber,  'Average power by week number', 'hour', 'measureCount', '[[title]]: [[value]]', 'char_weekly_avgpwr');
                    this.initChartSerialByWeekNumber( energyStatistics.statisticsByWeekNumber,  'Average power by week number', 'hour', 'measureCount', '[[title]]: [[value]]', 'char_weekly_energy_intervals');

                    this.initChartConsumptionBullet( energyStatistics.globalEnergyConsumption, 'Global consumption', 'chart_global_consumption' );
                    this.initChartConsumptionBullet( energyStatistics.currentIntervalEnergyConsumption, 'Global consumption', 'chart_current_interval_consumption' );
                }
            };
        }();
        this.Dashboard.AmCharts = this.AmCharts;
    }

    startIntervalChanged(newInterval) {
        try {
            this.startInterval = new Date(newInterval);
            this.getRuntimeParameters(this.installation.id);
        } catch (Exception) {
            console.warn(Exception);
        }
    }

    endIntervalChanged(newInterval) {
        try {
            this.endInterval = new Date(newInterval);
            this.getRuntimeParameters(this.installation.id);
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
        this.installationService.find(id).subscribe((response) => {
            const installation = response.body;
            this.installation = installation;
            if (installation.customerId != null) {
                this.customerService.find(installation.customerId).subscribe((customer) => {
                    this.customer = customer.body;
                });
            }
            if (installation.addressId != null) {
                this.addressService.find(installation.addressId).subscribe((address) => {
                    this.address = address.body;
                });
            }
            this.getRuntimeParameters(id);
            this.fetchGateways(id, 0, 100);
            this.fetchNodes(id, 0, 100);
        });
    }

    getRuntimeParameters(installationId) {
        this.installationService.getRuntimeParameters(installationId, this.startInterval, this.endInterval).subscribe((runtimeParameters) => {
            this.runtimeParameters = runtimeParameters;
            this.runtimeParameters.averageActivePower = Math.round(this.runtimeParameters.averageActivePower * 100) / 100;
            this.runtimeParameters.allTimePowerCosumption = Math.round(this.runtimeParameters.allTimePowerCosumption * 100) / 100;
            this.runtimeParameters.averageDimLevel = Math.round(this.runtimeParameters.averageDimLevel / 1023 * 100);

            if (isNaN(this.runtimeParameters.averageActivePower)) { this.runtimeParameters.averageActivePower = 0; }
            if (isNaN(this.runtimeParameters.allTimePowerCosumption)) { this.runtimeParameters.allTimePowerCosumption = 0; }
            if (isNaN(this.runtimeParameters.averageDimLevel)) { this.runtimeParameters.averageDimLevel = 0; }
            /*this.Dashboard.initChartWeeklyTrends(
                [113, 334, 1212, 22, 313, 121, 33]
            );
            this.Dashboard.initChartWeeklyCycles(
                [113, 334, 1212, 22, 313, 121, 33]
            );
            this.Dashboard.initChartTotalCycles(
                [113, 334, 1212, 22, 313, 121, 33, 33, 13, 342, 12, 43]
            );*/
            // this.Dashboard.initChartPhaseDistribution(null);
        });
        /*
        this.installationService.getWeeklyEnergyStatistics(installationId, 0, this.startInterval, this.endInterval).subscribe((weeklyStatistics) => {
            this.weeklyStatistics = weeklyStatistics;
            this.Dashboard.initChartWeeklySerial( this.weeklyStatistics,  'Weekly average power MTY0', 'hour', 'activePower', '[[title]]: [[value]]', 'char_weekly_avgpwr');
            // this.Dashboard.initChartWeeklySerial( this.weeklyStatistics,  'Weekly average energy MTY0', 'hour', 'activeEnergy', '[[title]]: [[value]]', 'char_weekly_energy_intervals_mty0');
        });
        this.installationService.getWeeklyEnergyStatistics(installationId, 1, this.startInterval, this.endInterval).subscribe((weeklyStatistics) => {
            this.weeklyStatistics = weeklyStatistics;
            this.Dashboard.initChartWeeklySerial( this.weeklyStatistics,  'Weekly average power MTY1', 'hour', 'activePower', '[[title]]: [[value]]', 'char_weekly_avgpwr_mty1');
            this.Dashboard.initChartWeeklySerial( this.weeklyStatistics,  'Weekly average energy MTY1', 'hour', 'activeEnergy', '[[title]]: [[value]]', 'char_weekly_energy_intervals_mty1');

        });
        this.installationService.getWeeklyEnergyStatistics(installationId, 2, this.startInterval, this.endInterval).subscribe((weeklyStatistics) => {
            this.weeklyStatistics = weeklyStatistics;
            this.Dashboard.initChartWeeklySerial( this.weeklyStatistics,  'Weekly average power MTY2', 'hour', 'activePower', '[[title]]: [[value]]', 'char_weekly_avgpwr_mty2');
            this.Dashboard.initChartWeeklySerial( this.weeklyStatistics,  'Weekly average energy MTY2', 'hour', 'activeEnergy', '[[title]]: [[value]]', 'char_weekly_energy_intervals_mty2');

        });
        this.installationService.getWeeklyEnergyStatistics(installationId, 3, this.startInterval, this.endInterval).subscribe((weeklyStatistics) => {
            this.weeklyStatistics = weeklyStatistics;

        });
        */
        this.installationService.getWeeklyEnergyStatistics(installationId, null, this.startInterval, this.endInterval).subscribe((energyStatistics) => {
            this.energyStatistics = energyStatistics;
            this.Dashboard.initChartEnergyStatistics(energyStatistics);
        });
    }

    fetchGateways(installationId, page, size) {
        this.gatewayService.findByInstallation(installationId, {
            page,
            size,
            sort: this.sort()
        }).subscribe((res: HttpResponse<GatewayWilamp[]>) => {
            if (page === 0) {
                this.gatewaysCount = parseInt(res.headers.get('X-Total-Count'), 10);
                this.gateways = res.body;
            } else {
                this.gateways.push.apply(this.gateways, res.body);
            }
            if (res.body.length === 0) { } else {
                this.fetchGateways(installationId, page + 1, size);
            }
        });
    }

    fetchNodes(installationId, page, size) {
        this.nodeService.findByInstallation(installationId, {
            page,
            size,
            sort: this.sort()
        }).subscribe((res: HttpResponse<NodeWilamp[]>) => {
            if (page === 0) {
                this.nodesCount = parseInt(res.headers.get('X-Total-Count'), 10);
                this.nodes = res.body;
                this.updateMapBounds(this);
            } else {
                this.nodes.push.apply(this.nodes, res.body);
            }
            if (res.body.length === 0) { } else {
                this.fetchNodes(installationId, page + 1, size);
            }
        });
    }

    updateMapBounds(reference) {
        if (reference.googleMapsLoaded) {
            reference.mapOptions.bounds = MapHelpers.generateBounds(reference.nodes);
            /* this.mapOptions.center.lat = (this.mapOptions.bounds.northeast.latitude + this.mapOptions.bounds.southwest.latitude) / 2;
            this.mapOptions.center.lng = (this.mapOptions.bounds.northeast.longitude + this.mapOptions.bounds.southwest.longitude) / 2;

            this.mapsAPIWrapper.fitBounds(this.mapOptions.bounds);
            this.mapsAPIWrapper.getNativeMap().then((m) => {
                console.warn(google.maps);
                console.warn(m);
            }); */
        } else {
            setTimeout(reference.updateMapBounds.bind(null, reference), 250);
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
        this.subscription.unsubscribe();
        this.eventManager.destroy(this.eventSubscriber);
    }

    registerChangeInInstallations() {
        this.eventSubscriber = this.eventManager.subscribe(
            'installationListModification',
            (response) => this.load(this.installation.id)
        );
    }

    ngAfterViewInit() {
        this._script.load('.m-grid__item.m-grid__item--fluid.m-wrapper',
            'assets/app/js/dashboard.js');

    }
    getCurrentDateTime() {
        return new Date();
    }

}
