import {Component, Input, OnInit, OnDestroy} from '@angular/core';
import { DomSanitizer } from '@angular/platform-browser';
import {
    GLOBALDATABASE__INSTALLATION_WEEKLY_STATISTICS_FETCHED,
    GLOBALDATABASE__INSTALLATION_WEEKLY_STATISTICS_FETCHING,
    INSTALLATION__SELECTED_INSTALLATION_CHANGED,
    INSTALLATION_DASHBOARD__DAILY_STATISTICS_FETCHED,
    INSTALLATION_DASHBOARD__MONTHLY_STATISTICS_FETCHED,
    INSTALLATION_DASHBOARD__WEEKLY_STATISTICS_FETCHED,
} from '../../shared/constants/events.constants';
import {GlobalDatabaseService} from '../../shared/global-database/global-database.service';
import {JhiEventManager} from 'ng-jhipster';
import {Subscription} from 'rxjs/Rx';
import {AmChartsService} from '@amcharts/amcharts3-angular';
import {Helpers} from '../../shared';

@Component({
  selector: 'panel-chart-widget',
  templateUrl: './panel-chart-widget.component.html',
  styleUrls: ['panel-chart-widget.component.css'],

})
export class PanelChartWidgetComponent implements OnInit, OnDestroy {
    @Input() chartType = 'daily';
    @Input() currentDate: Date;
    @Input() eventwatch: string;
    @Input() subClass = 'subclass';

    public isFetchingData = true;
    public chartData: any;
    public chartGroupTitle = 'Charts';
    public chartGroupSubtitle = 'by day of week';
    public activePanels = 3;
    public chart1Title = 'Chart 1';
    public chart1Id = 'chart_' + Helpers.makeid();
    public chart2Title = 'Chart 2';
    public chart2Id = 'chart_' + Helpers.makeid();
    public chart3Title = 'Chart 3';
    public chart3Id = 'chart_' + Helpers.makeid();
    public panel1Id = 'panel_' + Helpers.makeid();
    public panel2Id = 'panel_' + Helpers.makeid();
    public panel3Id = 'panel_' + Helpers.makeid();
    private eventSubscriber: Subscription;
    private selectedInstallationChange: Subscription;
    private eventSubscriberInstallationWeeklyStatistics: Subscription;
    constructor(
        private _DomSanitizationService: DomSanitizer,
        public globalDatabase: GlobalDatabaseService,
        private eventManager: JhiEventManager,
        private AmCharts: AmChartsService,
    ) { }

    ngOnInit() {/*
        switch (this.chartType) {
            case 'daily':
                this.createDailySmallGraph();
                this.eventwatch = GLOBALDATABASE__INSTALLATION_WEEKLY_STATISTICS_FETCHED;
                break;
            case 'weekly':
                this.createWeeklySmallGraph();
                this.eventwatch = GLOBALDATABASE__INSTALLATION_WEEKLY_STATISTICS_FETCHED;
                break;
            case 'monthly':
                this.createMonthlySmallGraph();
                this.eventwatch = GLOBALDATABASE__INSTALLATION_WEEKLY_STATISTICS_FETCHED;
                break;
            default:
                this.createDailySmallGraph();
        }*/
        this.eventwatch = GLOBALDATABASE__INSTALLATION_WEEKLY_STATISTICS_FETCHED;
        this.registerEvents();
        this.updateChart();
    }

    initChartSmoothSerialByHourAndDayOfWeek(chartDivElement: string, valueField: string, unit: string) {
        try {
            const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
            const labels = [];
            for (let k = 0; k < 24; k++) {
                labels.push(k);
            }
            const chartData = [];
            const graphs = [];
            const lineAlpha = 1;
            const fillAlpha = 0.05;
            const bulletSize = 6;
            const lineThickness = 1;
            const graphType = 'smoothedLine';
            const balloonText = '<b>[[title]]</b><br><span style=\'font-size:14px\'>h [[category]]: <b>[[value]] ' + unit + '</b></span>';

            for (let i = 0; i < days.length; i++) {
                const graph = {
                    'lineAlpha': lineAlpha,
                    'fillAlpha': fillAlpha,
                    'bullet': 'round',
                    'bulletSize': bulletSize,
                    'lineThickness': lineThickness,
                    'balloonText': balloonText,
                    'type': graphType,
                    'title': days[i],
                    'valueField': valueField + '_' + i,
                };
                graphs.push(graph);
            }
            if (this.globalDatabase.selectedInstallation &&
                this.globalDatabase.selectedInstallation.energyStatistics != null) {
                const statisticsOfPreviousWeek = this.globalDatabase.selectedInstallation.energyStatistics.getStatisticsOfPreviousWeek(this.currentDate);
                if (statisticsOfPreviousWeek != null) {
                    for (let hour = 0; hour < 24; hour++) {
                        for (let day = 0; day < 7; day++) {
                            if (statisticsOfPreviousWeek.content.get(day).content.get(hour)[valueField] < 0) { // TODO AT CHECK
                                statisticsOfPreviousWeek.content.get(day).content.get(hour)[valueField] = 0;
                            }
                            if (day === 0) {
                                // first round
                                const rowDefinition = {
                                    date: hour,
                                };
                                chartData[hour] = rowDefinition;
                            }
                            chartData[hour][valueField + '_' + day] = Math.round(statisticsOfPreviousWeek.content.get(day).content.get(hour)[valueField] * 100) / 100;
                        }
                    }
                }
            }
            if (chartData.length === 0) {
                for (let hour = 0; hour < 24; hour++) {
                    for (let day = 0; day < 7; day++) {
                        if (day === 0) {
                            // first round
                            const rowDefinition = {
                                date: hour,
                            };
                            chartData[hour] = rowDefinition;
                        }
                        chartData[hour][valueField + '_' + day] = 0;
                    }
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
                    'axisAlpha': 0.3,
                    'gridAlpha': 0,
                    /*'guides': [{
                        'fillAlpha': 0.1,
                        'fillColor': '#888888',
                        'lineAlpha': 0,
                        'toValue': 16,
                        'value': 10
                    }],
                    'position': 'left',
                    'tickLength': 0*/
                }],
                'graphs': graphs,
                'zoomOutButtonRollOverAlpha': 0.15,
                'chartCursor': {
                    /*'categoryBalloonDateFormat': 'MMM DD JJ:NN',*/
                    'cursorPosition': 'mouse',
                    'showNextAvailable': true,
                    'categoryBalloonEnabled': false,
                    'oneBalloonOnly': true,
                },
                'columnWidth': 1,
                'categoryField': 'date',
                'categoryAxis': {
                    'minPeriod': 'hh',
                    'parseDates': false,
                    'gridPosition': 'start',
                    'axisAlpha': 0,
                    'gridAlpha': 0,
                    'position': 'left',
                },
                'legend': {
                    'horizontalGap': 0,
                    'maxColumns': 1,
                    'position': 'right',
                    'useGraphSettings': true,
                    'markerSize': 10,
                    'valueText': '[[value]] KWh',
                    'valueWidth': 70,
                },
                'export': {
                    'enabled': true,
                },

            };
            const chart = this.AmCharts.makeChart(chartDivElement, serialGraphDefinition);
        } catch (Exception) {
            console.warn(Exception);
        }
    }

    initChartStackedEnergyByDayAndMonth(chartDivElement: string) {
        try {
            const chartData = [];
            const graphDefinitions = [
                {
                    'field': 'activeEnergyOldLampsAverage',
                    'title': 'Fluorescent / HPS',
                }, {
                    'field': 'activeEnergyWithoutControlAverage',
                    'title': 'LED',
                }, {
                    'field': 'activeEnergyAverage',
                    'title': 'Smart lights',
                },
            ];
            const graphs = [];
            const valueField = '';
            const unit = 'KWh';
            const lineAlpha = 0.3;
            const fillAlpha = 0.8;
            const bulletSize = 6;
            const lineThickness = 1;
            const graphType = 'column';
            const balloonText = '<b>[[title]]</b><br><span style=\'font-size:14px\'>[[category]]: <b>[[value]] ' + unit + '</b></span>';

            for (let i = 0; i < graphDefinitions.length; i++) {
                const graphDefinition = graphDefinitions[i];
                const graph = {
                    'lineAlpha': lineAlpha,
                    'fillAlphas': fillAlpha,
                    /*'bulletSize': bulletSize,*/
                    /*'lineThickness': lineThickness,*/
                    'balloonText': balloonText,
                    'type': graphType,
                    'title': graphDefinition['title'],
                    'valueField': graphDefinition['field'],
                    'color': '#000000',
                    'numberFormatter': {
                        'precision': 1,
                        /*"decimalSeparator": ",",*/
                        'thousandsSeparator': '',
                        'numberFormat': '#.0a',
                    },
                };
                graphs.push(graph);
            }
            let lastTimestamp = new Date(1900);
            if (this.globalDatabase.selectedInstallation &&
                this.globalDatabase.selectedInstallation.energyStatistics != null) {
                const statisticsOfCurrentMonth = this.globalDatabase.selectedInstallation.energyStatistics.getStatisticsOfCurrentMonth(this.currentDate);
                if (statisticsOfCurrentMonth != null) {
                    for (let i = 0; i < statisticsOfCurrentMonth.content.size; i++) { // TODO AT: better implementation
                        const dayStatistics = statisticsOfCurrentMonth.content.get(i);
                        if (lastTimestamp < dayStatistics.timestamp) {
                            lastTimestamp = dayStatistics.timestamp;
                            chartData.push(dayStatistics);
                        }
                    }
                }
            }
            if (chartData.length === 0) {
                for (let i = 0; i < 31; i++) {
                    const today = new Date(this.currentDate);
                    today.setMonth(today.getMonth() - 1);
                    today.setDate(today.getDate() + i);

                    const dayStatistics = {
                        'activeEnergyOldLampsAverage': 0,
                        'activeEnergyWithoutControlAverage': 0,
                        'activeEnergyAverage': 0,
                        'timestamp': today,
                    };
                    chartData.push(dayStatistics);
                }
            }
            const serialGraphDefinition = {
                'type': 'serial',
                'theme': 'light',
                'legend': {
                    'horizontalGap': 0,
                    'maxColumns': 1,
                    'position': 'right',
                    'useGraphSettings': true,
                    'markerSize': 10,
                    'valueText': '[[value]] KWh',
                    'valueWidth': 70,
                },
                'dataProvider': chartData,
                'valueAxes': [{
                    'stackType': '3d',
                    'axisAlpha': 0.3,
                    'gridAlpha': 0,
                    'precision': 0,
                    'unit': 'KWh',
                    'usePrefixes': false,

                }],
                'graphs': graphs,
                'categoryField': 'timestamp',
                'categoryAxis': {
                    'parseDates': true,
                    'gridPosition': 'start',
                    'axisAlpha': 0,
                    'gridAlpha': 0,
                    'position': 'left',
                },
                'chartCursor': {
                    /*'categoryBalloonDateFormat': 'MMM DD JJ:NN',*/
                    'cursorPosition': 'mouse',
                    'showNextAvailable': true,
                    'categoryBalloonEnabled': false,
                    'oneBalloonOnly': true,
                },
                'export': {
                    'enabled': true,
                },

            };
            const chart = this.AmCharts.makeChart(chartDivElement, serialGraphDefinition);
        } catch (Exception) {
            console.warn(Exception);
        }
    }

    updateChart() {
        /*
        this.initChartSerialByHourAndDayOfWeek(this.chart1Id, 'activeEnergyAverage', 'hour', '[[title]]: [[value]] KWh');
        this.initChartSerialByHourAndDayOfWeek(this.chart2Id, 'activePowerAverage', 'hour', '[[title]]: [[value]] W');
        this.initChartSerialByHourAndDayOfWeek(this.chart3Id, 'burningTimeAverage', 'hour', '[[title]]: [[value]] min');
        */

        switch (this.chartType) {
            case 'daily':
                this.chartGroupTitle = 'Daily power consumption';
                this.chartGroupSubtitle = 'by day of week';
                this.chart1Title = 'Active energy';
                this.chart2Title = 'Active power';
                // this.chart3Title = 'Burning time';
                this.activePanels = 2;
                this.initChartSmoothSerialByHourAndDayOfWeek(this.chart1Id, 'activeEnergyAverage',  'KWh');
                this.initChartSmoothSerialByHourAndDayOfWeek(this.chart2Id, 'activePowerAverage',  'W');
                // this.initChartSmoothSerialByHourAndDayOfWeek(this.chart3Id, 'burningTimeAverage',  'min');
                break;
            case 'weekly':
                this.chartGroupTitle = 'Last 7 days consumption comparison';
                this.chartGroupSubtitle = 'by type of lamp';
                this.chart1Title = 'Active energy';
                this.chart2Title = 'Active power';
                this.chart3Title = 'Burning time';
                this.activePanels = 2;
                this.initChartSmoothSerialByHourAndDayOfWeek(this.chart1Id, 'activeEnergyAverage',  'KWh');
                this.initChartSmoothSerialByHourAndDayOfWeek(this.chart2Id, 'activePowerAverage',  'W');
                this.initChartSmoothSerialByHourAndDayOfWeek(this.chart3Id, 'burningTimeAverage',  'min');
                break;
            case 'monthly':
                this.chartGroupTitle = 'Last 30 days consumption comparison';
                this.chartGroupSubtitle = 'by type of lamp';
                this.chart1Title = 'Active energy';
                this.activePanels = 1;
                this.initChartStackedEnergyByDayAndMonth(this.chart1Id);
                // this.initChartStackedEnergyByDayAndMonth(this.chart1Id);
                // this.initChartSmoothSerialByDayAndMonth(this.chart3Id, 'activePowerAverage',  'min');
                break;
            default:
                this.initChartSmoothSerialByHourAndDayOfWeek(this.chart2Id, 'activePowerAverage',  'W');
                this.initChartSmoothSerialByHourAndDayOfWeek(this.chart3Id, 'burningTimeAverage',  'min');
        }
        this.isFetchingData = false;
    }

    ngOnDestroy() {
        this.eventManager.destroy(this.eventSubscriber);
        this.eventManager.destroy(this.selectedInstallationChange);
        this.eventManager.destroy(this.eventSubscriberInstallationWeeklyStatistics);
    }

    registerEvents() {
        this.eventSubscriber = this.eventManager.subscribe(
            this.eventwatch,
            (response) => this.updateChart(),
        );
        this.selectedInstallationChange = this.eventManager.subscribe(
            INSTALLATION__SELECTED_INSTALLATION_CHANGED,
            (response) => this.isFetchingData = true,
        );
        this.eventSubscriberInstallationWeeklyStatistics = this.eventManager.subscribe(
            GLOBALDATABASE__INSTALLATION_WEEKLY_STATISTICS_FETCHING,
            (response) => {
                this.isFetchingData = true;
            },
        );
    }

}
