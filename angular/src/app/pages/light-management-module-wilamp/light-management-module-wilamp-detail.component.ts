import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import {JhiAlertService, JhiEventManager} from 'ng-jhipster';
import { HttpResponse } from '@angular/common/http';
import { Subscription } from 'rxjs';

import { LightManagementModuleWilamp } from './light-management-module-wilamp.model';
import { LightManagementModuleWilampService } from './light-management-module-wilamp.service';
import { LightManagementMeasureWilampService } from '../light-management-measure-wilamp/light-management-measure-wilamp.service';
import { EnergyInterval } from '../energy-interval/energy-interval.model';
import { EnergyIntervalService} from '../energy-interval/energy-interval.service';
import {LightManagementMeasureWilamp} from '../light-management-measure-wilamp/light-management-measure-wilamp.model';
import {AmChart, AmChartsService} from '@amcharts/amcharts3-angular';
import {graph_measure_types} from '../../shared/constants/graph.constants';
import {EntityResponseType} from '../energy-interval/energy-interval.service';
import {Helpers} from '../../shared';

@Component({
    selector: 'jhi-light-management-module-wilamp-detail',
    templateUrl: './light-management-module-wilamp-detail.component.html',
})
export class LightManagementModuleWilampDetailComponent implements OnInit, OnDestroy {

    lightManagementModule: LightManagementModuleWilamp;
    lightManagementMeasures: LightManagementMeasureWilamp[];
    lightManagementMeasuresCount = 0;
    energyIntervals: EnergyInterval[];
    energyMeterIntervalsCount = 0;
    private subscription: Subscription;
    private eventSubscriber: Subscription;

    Dashboard = null;
    statsWeeklyCycleAvg = 0;
    statsWeeklyCycleProductivity = 0;
    statsWeeklyPlannedCycles = 0;
    statsIssues = 0;
    statsTotalCycles = 0;
    statsWeeklyDelivered = 0;
    statsWeeklyInProgress = 0;
    statsPhaseDurations = null;
    logEntries = null;
    itemsPerPage: number;
    links: any;
    page: any;
    predicate: any;
    reverse: any;
    totalItems: number;
    private chartLightManagementMeasuresPat: AmChart;
    private chartLightManagementMeasuresCea: AmChart;
    private chartEnergyIntervals: AmChart;
    private chartEnergyIntervalsBurningTime: AmChart;
    private lightManagementMeasuresChartData = [];
    public measureTypes = graph_measure_types;
    public light_management_measures_graph__start_date = '2017-12-01T17:13:47.477Z';
    public light_management_measures_graph__end_date = '2018-02-20T22:13:47.477Z';
    public light_management_measures_graph__mty = 3;

    constructor(
        private eventManager: JhiEventManager,
        private lightManagementModuleService: LightManagementModuleWilampService,
        private lightManagementMeasureService: LightManagementMeasureWilampService,
        private energyIntervalService: EnergyIntervalService,
        private route: ActivatedRoute,
        private jhiAlertService: JhiAlertService,
        private AmCharts: AmChartsService,
    ) {
        this.lightManagementMeasures = [];
        this.energyIntervals = [];
        this.itemsPerPage = 100;
        this.page = 1;
        this.links = {
            last: 0,
        };
        this.predicate = 'id';
        this.reverse = true;

    }

    ngOnInit() {
        this.subscription = this.route.params.subscribe((params) => {
            this.load(params['id']);
        });
        this.registerChangeInLightManagementModules();
    }

    load(id) {
        this.lightManagementModuleService.find(id)
            .subscribe((lightManagementModuleResponse: HttpResponse<LightManagementModuleWilamp>) => {
                this.lightManagementModule = lightManagementModuleResponse.body;

                /*this.lightManagementMeasureService.getByLightModuleAndInterval(this.lightManagementModule.id,1,"2017-12-20T17:13:47.477Z","2017-12-25T22:13:47.477Z",{
                    page: this.page,
                    size: this.itemsPerPage,
                    sort: this.sort()
                }).subscribe(
                    (res: ResponseWrapper) => this.onSuccess(res.json, res.headers),
                    (res: ResponseWrapper) => this.onError(res.json)
                );
                */
                this.fetchLightManagementMeasures(this.lightManagementModule.id, this.light_management_measures_graph__mty,
                    this.light_management_measures_graph__start_date, this.light_management_measures_graph__end_date, 0, 100);

                this.fetchEnergyIntervals(this.lightManagementModule.id, this.light_management_measures_graph__start_date, this.light_management_measures_graph__end_date, 0, 100);

            });
    }

    fetchLightManagementMeasures(lightManagementId, mty, startDate, endDate, page, size) {
        this.lightManagementMeasureService.getByLightModuleAndMtyAndInterval(lightManagementId, mty, startDate, endDate, {
            page,
            size,
            sort: this.sort(),
        }).subscribe((res: HttpResponse<LightManagementModuleWilamp[]>) => {
            if (page === 0) {
                this.lightManagementMeasuresCount = parseInt(res.headers.get('X-Total-Count'), 10);
                this.lightManagementMeasures = res.body;
            } else {
                this.lightManagementMeasures.push.apply(this.lightManagementMeasures, res.body);
            }
            if (res.body.length === 0) {
                this.createLightManagementMeasuresChart();
            } else {
                this.fetchLightManagementMeasures(lightManagementId, mty, startDate, endDate, page + 1, size);
            }
        });
    }

    fetchEnergyIntervals(lightManagementId, startDate, endDate, page, size) {
        this.energyIntervalService.getByLightModuleAndInterval(lightManagementId, startDate, endDate, {
            page,
            size,
            sort: this.sort(),
        }).subscribe((res: HttpResponse<LightManagementModuleWilamp[]>) => {
            if (page === 0) {
                this.energyMeterIntervalsCount = parseInt(res.headers.get('X-Total-Count'), 10);
                this.energyIntervals = res.body;
            } else {
                this.energyIntervals.push.apply(this.energyIntervals, res.body);
            }
            if (res.body.length === 0) {
                this.createEnergyIntervalsChart();
            } else {
                this.fetchEnergyIntervals(lightManagementId, startDate, endDate, page + 1, size);
            }
        });

        this.lightManagementModuleService.find(lightManagementId)
            .subscribe((lightManagementModuleResponse: HttpResponse<LightManagementModuleWilamp>) => {
                this.lightManagementModule = lightManagementModuleResponse.body;
            });
    }

    updateLightManagementMeasuresChartWithMty() {
        this.fetchLightManagementMeasures(this.lightManagementModule.id, this.light_management_measures_graph__mty,
            this.light_management_measures_graph__start_date, this.light_management_measures_graph__end_date, 0, 100);
    }

    /*
    this.lightManagementMeasureService.getByMacAndMtyAndInterval("00158D0000FE27A7",3,"2017-12-23T17:13:47.477Z","2017-12-23T22:13:47.477Z",{
                page: this.page,
                size: this.itemsPerPage,
                sort: this.sort()
            }).subscribe(
                (res: ResponseWrapper) => {console.log(res.json)},
                (res: ResponseWrapper) => this.onError(res.json)
            );

     */

    private onSuccess(data, headers) {
        this.totalItems = headers.get('X-Total-Count');
        for (let i = 0; i < data.length; i++) {
            this.lightManagementMeasures.push(data[i]);
            const measure = Helpers.toDictionary(data[i], (num, key) =>  key, (num) => num);
            this.lightManagementMeasuresChartData.push(measure);
        }
        this.createLightManagementMeasuresChart();
    }

    private onError(error) {
        this.jhiAlertService.error(error.message, null, null);
    }

    sort() {
        const result = [this.predicate + ',' + (this.reverse ? 'asc' : 'desc')];
        if (this.predicate !== 'id') {
            result.push('id');
        }
        return result;
    }

    previousState() {
        window.history.back();
    }

    ngOnDestroy() {
        this.subscription.unsubscribe();
        this.eventManager.destroy(this.eventSubscriber);
    }

    registerChangeInLightManagementModules() {
        this.eventSubscriber = this.eventManager.subscribe(
            'lightManagementModuleListModification',
            (response) => this.load(this.lightManagementModule.id),
        );
    }

    createLightManagementMeasuresChart() {

        this.chartLightManagementMeasuresPat = this.AmCharts.makeChart('light_management_measures_line', {
            'type': 'serial',
            'theme': 'light',
            'marginTop': 0,
            'marginRight': 80,
            'dataProvider': this.lightManagementMeasures,
            'legend': {
                'equalWidths': false,
                'position': 'top',
                'valueAlign': 'left',
                'valueWidth': 100,
            },
            'categoryAxesSettings': {
                'minPeriod': 'fff',
            },
            'valueAxes': [{
                'axisAlpha': 0,
                'position': 'left',
            }],
            'graphs': [
                {
                    'id': 'g1',
                    'balloonText': '[[title]]<br><b><span style=\'font-size:14px;\'>[[value]] W</span></b>',
                    'bullet': 'round',
                    'title': 'Active Power (W).',
                    'bulletSize': 1,
                    'lineColor': '#6AB8DA',
                    'lineThickness': 1,
                    // 'negativeLineColor': '#637bb6',
                    'type': 'line',
                    'valueField': 'activePower',
                },
                {
                    'id': 'g2',
                    'balloonText': '[[title]]<br><b><span style=\'font-size:14px;\'>[[value]] mA</span></b>',
                    'bullet': 'round',
                    'title': 'Current (mA).',
                    'bulletSize': 1,
                    'lineColor': '#85B665',
                    'lineThickness': 1,
                    // 'negativeLineColor': '#637bb6',
                    'type': 'line',
                    'valueField': 'iac',
                },
                {
                    'id': 'g3',
                    'balloonText': '[[title]]<br><b><span style=\'font-size:14px;\'>[[value]] V</span></b>',
                    'title': 'AC Voltage (V)',
                    'bullet': 'round',
                    'bulletSize': 1,
                    'lineColor': '#FCD330',
                    'lineThickness': 1,
                    // 'negativeLineColor': '#637bb6',
                    'type': 'line',
                    'valueField': 'vac',
                },
            ],
            'chartScrollbar': {
                'graph': 'g1',
                'gridAlpha': 0,
                'color': '#888888',
                'scrollbarHeight': 55,
                'backgroundAlpha': 0,
                'selectedBackgroundAlpha': 0.1,
                'selectedBackgroundColor': '#888888',
                'graphFillAlpha': 0,
                'autoGridCount': true,
                'selectedGraphFillAlpha': 0,
                // 'graphLineAlpha':0.2,
                'graphLineColor': '#c2c2c2',
                'selectedGraphLineColor': '#888888',
                'selectedGraphLineAlpha': 1,

            },
            'chartCursor': {
                'categoryBalloonDateFormat': 'MMM DD HH:NN:SS',
                'cursorAlpha': 0,
                'valueLineEnabled': true,
                'valueLineBalloonEnabled': true,
                'valueLineAlpha': 0.5,
                'fullWidth': true,
            },
            'dataDateFormat': 'fff',
            'categoryField': 'measureTimestamp',
            'categoryAxis': {
                'minPeriod': 'fff',
                'parseDates': true,
                'minorGridAlpha': 0.1,
                'minorGridEnabled': true,
            },
            'export': {
                'enabled': true,
            },
        });
        // different zoom methods can be used - zoomToIndexes, zoomToDates, zoomToCategoryValues
        this.chartLightManagementMeasuresPat.zoomToIndexes(this.lightManagementMeasures.length - 40, this.lightManagementMeasures.length - 1);

        this.chartLightManagementMeasuresCea = this.AmCharts.makeChart('light_management_measures_line_cea', {
            'type': 'serial',
            'theme': 'light',
            'marginTop': 0,
            'marginRight': 80,
            'dataProvider': this.lightManagementMeasures,
            'legend': {
                'equalWidths': false,
                'position': 'top',
                'valueAlign': 'left',
                'valueWidth': 100,
            },
            'categoryAxesSettings': {
                'minPeriod': 'fff',
            },
            'valueAxes': [{
                'axisAlpha': 0,
                'position': 'left',
            }],
            'graphs': [
                {
                    'id': 'g1',
                    'balloonText': '[[title]]<br><b><span style=\'font-size:14px;\'>[[value]] Wh</span></b>',
                    'bullet': 'round',
                    'title': 'Active energy counter (Wh).',
                    'bulletSize': 1,
                    'lineColor': '#6AB8DA',
                    'lineThickness': 1,
                    // 'negativeLineColor': '#637bb6',
                    'type': 'line',
                    'valueField': 'activeEnergyCounter',
                },
                {
                    'id': 'g2',
                    'balloonText': '[[title]]<br><b><span style=\'font-size:14px;\'>[[value/60/10]] h</span></b>',
                    'bullet': 'round',
                    'title': 'Burning Time (dh).',
                    'bulletSize': 1,
                    'lineColor': '#85B665',
                    'lineThickness': 1,
                    // 'negativeLineColor': '#637bb6',
                    'type': 'line',
                    'valueField': 'lampLife',
                },
            ],
            'chartScrollbar': {
                'graph': 'g1',
                'gridAlpha': 0,
                'color': '#888888',
                'scrollbarHeight': 55,
                'backgroundAlpha': 0,
                'selectedBackgroundAlpha': 0.1,
                'selectedBackgroundColor': '#888888',
                'graphFillAlpha': 0,
                'autoGridCount': true,
                'selectedGraphFillAlpha': 0,
                // 'graphLineAlpha':0.2,
                'graphLineColor': '#c2c2c2',
                'selectedGraphLineColor': '#888888',
                'selectedGraphLineAlpha': 1,

            },
            'chartCursor': {
                'categoryBalloonDateFormat': 'MMM DD HH:NN:SS',
                'cursorAlpha': 0,
                'valueLineEnabled': true,
                'valueLineBalloonEnabled': true,
                'valueLineAlpha': 0.5,
                'fullWidth': true,
            },
            'dataDateFormat': 'fff',
            'categoryField': 'measureTimestamp',
            'categoryAxis': {
                'minPeriod': 'fff',
                'parseDates': true,
                'minorGridAlpha': 0.1,
                'minorGridEnabled': true,
            },
            'export': {
                'enabled': true,
            },
        });
        // different zoom methods can be used - zoomToIndexes, zoomToDates, zoomToCategoryValues
        this.chartLightManagementMeasuresCea.zoomToIndexes(this.lightManagementMeasures.length - 40, this.lightManagementMeasures.length - 1);

    }

    createEnergyIntervalsChart() {

        this.chartEnergyIntervals = this.AmCharts.makeChart('energy_meter_measures_line', {
            'type': 'serial',
            'theme': 'light',
            'marginTop': 0,
            'marginRight': 80,
            'dataProvider': this.energyIntervals,
            'legend': {
                'equalWidths': false,
                'position': 'top',
                'valueAlign': 'left',
                'valueWidth': 100,
            },
            'categoryAxesSettings': {
                'minPeriod': 'fff',
            },
            'valueAxes': [{
                'axisAlpha': 0,
                'position': 'left',
            }],
            'graphs': [
                {
                    'id': 'g1',
                    'balloonText': '[[title]]<br><b><span style=\'font-size:14px;\'>[[value]] KWh</span></b>',
                    'bullet': 'round',
                    'title': 'Active energy without dim(KWh).',
                    'bulletSize': 1,
                    'lineColor': '#6AB8DA',
                    'lineThickness': 1,
                    // 'negativeLineColor': '#637bb6',
                    'type': 'line',
                    'valueField': 'activeEnergyWithoutDim',
                },
                {
                    'id': 'g2',
                    'balloonText': '[[title]]<br><b><span style=\'font-size:14px;\'>[[value]] KWh</span></b>',
                    'bullet': 'round',
                    'title': 'Active energy (KWh).',
                    'bulletSize': 1,
                    'lineColor': '#85B665',
                    'lineThickness': 1,
                    // 'negativeLineColor': '#637bb6',
                    'type': 'line',
                    'valueField': 'activeEnergyMty3',
                },
                {
                    'id': 'g3',
                    'balloonText': '[[title]]<br><b><span style=\'font-size:14px;\'>[[value]] KWh</span></b>',
                    'title': 'Active energy old lamps(KWh).',
                    'bullet': 'round',
                    'bulletSize': 1,
                    'lineColor': '#FCD330',
                    'lineThickness': 1,
                    // 'negativeLineColor': '#637bb6',
                    'type': 'line',
                    'valueField': 'activeEnergyOldLamps',
                },
                {
                    'id': 'g4',
                    'balloonText': '[[title]]<br><b><span style=\'font-size:14px;\'>[[value]] KWh</span></b>',
                    'title': 'Active energy without control(KWh).',
                    'bullet': 'round',
                    'bulletSize': 1,
                    'lineColor': '#fc0b47',
                    'lineThickness': 1,
                    // 'negativeLineColor': '#637bb6',
                    'type': 'line',
                    'valueField': 'activeEnergyWithoutControl',
                },

            ],
            'chartScrollbar': {
                'graph': 'g1',
                'gridAlpha': 0,
                'color': '#888888',
                'scrollbarHeight': 55,
                'backgroundAlpha': 0,
                'selectedBackgroundAlpha': 0.1,
                'selectedBackgroundColor': '#888888',
                'graphFillAlpha': 0,
                'autoGridCount': true,
                'selectedGraphFillAlpha': 0,
                // 'graphLineAlpha':0.2,
                'graphLineColor': '#c2c2c2',
                'selectedGraphLineColor': '#888888',
                'selectedGraphLineAlpha': 1,

            },
            'chartCursor': {
                'categoryBalloonDateFormat': 'MMM DD HH:NN:SS',
                'cursorAlpha': 0,
                'valueLineEnabled': true,
                'valueLineBalloonEnabled': true,
                'valueLineAlpha': 0.5,
                'fullWidth': true,
            },
            'dataDateFormat': 'fff',
            'categoryField': 'startInterval',
            'categoryAxis': {
                'minPeriod': 'fff',
                'parseDates': true,
                'minorGridAlpha': 0.1,
                'minorGridEnabled': true,
            },
            'export': {
                'enabled': true,
            },
        });
        // different zoom methods can be used - zoomToIndexes, zoomToDates, zoomToCategoryValues
        this.chartEnergyIntervals.zoomToIndexes(this.energyIntervals.length - 40, this.energyIntervals.length - 1);

        this.chartEnergyIntervalsBurningTime = this.AmCharts.makeChart('energy_meter_measures_line_burning_time', {
            'type': 'serial',
            'theme': 'light',
            'marginTop': 0,
            'marginRight': 80,
            'dataProvider': this.energyIntervals,
            'legend': {
                'equalWidths': false,
                'position': 'top',
                'valueAlign': 'left',
                'valueWidth': 100,
            },
            'categoryAxesSettings': {
                'minPeriod': 'fff',
            },
            'valueAxes': [{
                'axisAlpha': 0,
                'position': 'left',
            }],
            'graphs': [
                {
                    'id': 'g1',
                    'balloonText': '[[title]]<br><b><span style=\'font-size:14px;\'>[[value/60]] h</span></b>',
                    'bullet': 'round',
                    'title': 'Burning time (h).',
                    'bulletSize': 1,
                    'lineColor': '#6AB8DA',
                    'lineThickness': 1,
                    // 'negativeLineColor': '#637bb6',
                    'type': 'line',
                    'valueField': 'burningTime',
                },
                {
                    'id': 'g2',
                    'balloonText': '[[title]]<br><b><span style=\'font-size:14px;\'>[[value]] KWh</span></b>',
                    'bullet': 'round',
                    'title': 'Active energy (KWh).',
                    'bulletSize': 1,
                    'lineColor': '#85B665',
                    'lineThickness': 1,
                    // 'negativeLineColor': '#637bb6',
                    'type': 'line',
                    'valueField': 'activeEnergyMty3',
                },
                {
                    'id': 'g3',
                    'balloonText': '[[title]]<br><b><span style=\'font-size:14px;\'>[[value]] W</span></b>',
                    'title': 'Active power (W).',
                    'bullet': 'round',
                    'bulletSize': 1,
                    'lineColor': '#FCD330',
                    'lineThickness': 1,
                    // 'negativeLineColor': '#637bb6',
                    'type': 'line',
                    'valueField': 'activePower',
                },
            ],
            'chartScrollbar': {
                'graph': 'g1',
                'gridAlpha': 0,
                'color': '#888888',
                'scrollbarHeight': 55,
                'backgroundAlpha': 0,
                'selectedBackgroundAlpha': 0.1,
                'selectedBackgroundColor': '#888888',
                'graphFillAlpha': 0,
                'autoGridCount': true,
                'selectedGraphFillAlpha': 0,
                // 'graphLineAlpha':0.2,
                'graphLineColor': '#c2c2c2',
                'selectedGraphLineColor': '#888888',
                'selectedGraphLineAlpha': 1,

            },
            'chartCursor': {
                'categoryBalloonDateFormat': 'MMM DD HH:NN:SS',
                'cursorAlpha': 0,
                'valueLineEnabled': true,
                'valueLineBalloonEnabled': true,
                'valueLineAlpha': 0.5,
                'fullWidth': true,
            },
            'dataDateFormat': 'fff',
            'categoryField': 'startInterval',
            'categoryAxis': {
                'minPeriod': 'fff',
                'parseDates': true,
                'minorGridAlpha': 0.1,
                'minorGridEnabled': true,
            },
            'export': {
                'enabled': true,
            },
        });
        // different zoom methods can be used - zoomToIndexes, zoomToDates, zoomToCategoryValues
        this.chartEnergyIntervalsBurningTime.zoomToIndexes(this.energyIntervals.length - 40, this.energyIntervals.length - 1);

    }

}
