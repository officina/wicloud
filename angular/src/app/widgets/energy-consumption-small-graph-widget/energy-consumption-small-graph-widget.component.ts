import {Component, Input, OnInit, OnDestroy} from '@angular/core';
import {NodeWilamp} from '../../pages/node-wilamp';
import { DomSanitizer } from '@angular/platform-browser';
import {
    GLOBALDATABASE__INSTALLATION_WEEKLY_STATISTICS_FETCHED,
    GLOBALDATABASE__INSTALLATION_WEEKLY_STATISTICS_FETCHING,
    INSTALLATION__SELECTED_INSTALLATION_CHANGED,
    INSTALLATION_DASHBOARD__DAILY_STATISTICS_FETCHED,
    INSTALLATION_DASHBOARD__MONTHLY_STATISTICS_FETCHED,
    INSTALLATION_DASHBOARD__WEEKLY_STATISTICS_FETCHED
} from '../../shared/constants/events.constants';
import {KWtoCO2Factor} from '../../shared/constants/graph.constants';
import {GlobalDatabaseService} from '../../shared/global-database/global-database.service';
import DateTimeFormat = Intl.DateTimeFormat;
import {JhiEventManager} from 'ng-jhipster';
import {Helpers} from '../../shared';
import {Subscription} from 'rxjs/Rx';

@Component({
  selector: 'energy-consumption-small-graph-widget',
  templateUrl: './energy-consumption-small-graph-widget.component.html',
  styleUrls: ['energy-consumption-small-graph-widget.component.css']

})
export class EnergyConsumptionSmallGraphWidgetComponent implements OnInit, OnDestroy {
    @Input() chartType = 'daily';
    @Input() currentDate: Date;
    @Input() eventwatch: string;

    public chartData: any;
    public chartDataYMaxValue = 40.0;
    public chartOptions: any;
    public flotEventToGenerate = Helpers.makeid();
    public legendId = Helpers.makeid();
    public graphTitle: string;
    public graphBottomLeftSPData: any;
    public graphBottomRightSPData: any;
    public graphBottomLeftSPOptions: any;
    public graphBottomRightSPOptions: any;
    public isFetchingData = true;
    public graphBottomLeftTitle = '';
    public graphBottomLeftValue = 0.0;
    public graphBottomRightTitle = '';
    public graphBottomRightValue = 0.0;
    private eventSubscriber: Subscription;
    private selectedInstallationChange: Subscription;
    private eventSubscriberInstallationWeeklyStatistics: Subscription;

    constructor(
        private _DomSanitizationService: DomSanitizer,
        public globalDatabase: GlobalDatabaseService,
        private eventManager: JhiEventManager
    ) { }

    ngOnInit() {
        this.graphBottomLeftSPData = [4, 3, 3, 1, 4, 3, 2, 2, 3, 10, 9, 6];
        this.graphBottomLeftSPOptions = {
            type: 'bar',
            height: '30px',
            barColor: '#428BCA'
        };

        this.graphBottomRightSPData = [9, 8, 8, 6, 9, 10, 6, 5, 6, 3, 4, 2];
        this.graphBottomRightSPOptions = {
            type: 'bar',
            height: '30px',
            barColor: '#999'
        };
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
        }
        this.registerEvents();
        this.isFetchingData = true;
    }

    createDailySmallGraph() {
        try {
            this.graphTitle = 'DAILY ENERGY CONSUMPTION';
            this.graphBottomLeftTitle = 'Hour average';
            this.graphBottomRightTitle = 'Total per day';

            this.chartData = [{
                data: [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0], [12, 0], [13, 0], [14, 0], [15, 0], [16, 0], [17, 0], [18, 0], [19, 0], [20, 0], [21, 0], [22, 0], [23, 0]],
                label: 'Today (' + Helpers.getWeekName(this.currentDate) + ')',
                color: '#905dd1'
            },
                {
                    data: [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0], [12, 0], [13, 0], [14, 0], [15, 0], [16, 0], [17, 0], [18, 0], [19, 0], [20, 0], [21, 0], [22, 0], [23, 0]],
                    label: 'Yesterday',
                    color: '#03c3c4'
                }];

            this.chartOptions = {
                series: {
                    lines: {
                        show: false
                    },
                    splines: {
                        show: true,
                        tension: 0.4,
                        lineWidth: 1,
                        fill: 0.4
                    },
                    shadowSize: 0
                },
                points: {
                    show: true,
                },
                legend: {
                    container: '#' + this.legendId,
                    noColumns: 0
                },
                grid: {
                    hoverable: true,
                    clickable: true,
                    borderColor: '#ddd',
                    borderWidth: 0,
                    labelMargin: 5,
                    backgroundColor: '#fff'
                },
                yaxis: {
                    min: 0,
                    max: this.chartDataYMaxValue + 1,
                    color: '#656565'
                },
                xaxis: {
                    color: '#656565'
                }
            };
            const currentWeekKey = this.currentDate.getFullYear() + '_' + Helpers.getWeekNumber(this.currentDate)[1];
            const yesterday = new Date(this.currentDate);
            yesterday.setDate(this.currentDate.getDate() - 1);
            const yesterdayKey = yesterday.getFullYear() + '_' + Helpers.getWeekNumber(yesterday)[1];
            // Extract values from the week statistics using the key
            if (this.globalDatabase.selectedInstallation.energyStatistics.statisticsByWeek.has(currentWeekKey)) {
                const weekStatistics = this.globalDatabase.selectedInstallation.energyStatistics.statisticsByWeek.get(currentWeekKey);
                this.chartData[0].data = weekStatistics.content[this.currentDate.getDay()].data;
                // Search for graph boundaries
                this.chartData[0].data.forEach( (valArray) => {
                   if (valArray[1] > this.chartDataYMaxValue) { this.chartDataYMaxValue = valArray[1]; }
                });
                this.graphBottomLeftValue = Math.round(weekStatistics.content[this.currentDate.getDay()].activeEnergyAverage);
                this.graphBottomRightValue = Math.round(weekStatistics.content[this.currentDate.getDay()].activeEnergyTotal);
            }
            if (this.globalDatabase.selectedInstallation.energyStatistics.statisticsByWeek.has(yesterdayKey)) {
                const weekStatistics = this.globalDatabase.selectedInstallation.energyStatistics.statisticsByWeek.get(yesterdayKey);
                this.chartData[1].data = weekStatistics.content[yesterday.getDay()].data;
                // Search for graph boundaries
                this.chartData[1].data.forEach( (valArray) => {
                    if (valArray[1] > this.chartDataYMaxValue) { this.chartDataYMaxValue = valArray[1]; }
                });
            }
            this.chartOptions.yaxis.max = this.chartDataYMaxValue + 1.0;
            this.eventManager.broadcast({
                name: this.flotEventToGenerate,
                content: { dataset: this.chartData, options: this.chartOptions }
            });
            this.isFetchingData = false;
        } catch (Exception) {
            console.warn(Exception);
        }
    }

    createWeeklySmallGraph() {
        try {
            this.graphTitle = 'WEEKLY ENERGY CONSUMPTION';
            this.graphBottomLeftTitle = 'Day average';
            this.graphBottomRightTitle = 'Total per week';

            this.chartData = [{
                data: [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0]],
                label: 'Current Week',
                color: '#b830b3'
            },
                {
                    data: [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0]],
                    label: 'Last week',
                    color: '#428bca'
                }];

            this.chartOptions = {
                series: {
                    lines: {
                        show: false
                    },
                    splines: {
                        show: true,
                        tension: 0.4,
                        lineWidth: 1,
                        fill: 0.4
                    },
                    shadowSize: 0
                },
                points: {
                    show: true,
                },
                legend: {
                    container: '#' + this.legendId,
                    noColumns: 0
                },
                grid: {
                    hoverable: true,
                    clickable: true,
                    borderColor: '#ddd',
                    borderWidth: 0,
                    labelMargin: 5,
                    backgroundColor: '#fff'
                },
                yaxis: {
                    min: 0,
                    max: this.chartDataYMaxValue + 1 ,
                    color: '#656565'
                },
                xaxis: {
                    color: '#656565',
                    ticks: [[0, 'Mon'], [1, 'Tue'], [2, 'Wed'], [3, 'Thu'], [4, 'Fri'], [5, 'Sat'], [6, 'Sun']]
                }
            };
            const currentWeekKey = this.currentDate.getFullYear() + '_' + Helpers.getWeekNumber(this.currentDate)[1];
            const previousWeek = new Date(this.currentDate);
            previousWeek.setDate(this.currentDate.getDate() - 7);
            const previousWeekKey = previousWeek.getFullYear() + '_' + Helpers.getWeekNumber(previousWeek)[1];
            // Extract values from the week statistics using the key
            if (this.globalDatabase.selectedInstallation.energyStatistics.statisticsByWeek.has(currentWeekKey)) {
                const weekStatistics = this.globalDatabase.selectedInstallation.energyStatistics.statisticsByWeek.get(currentWeekKey);
                this.chartData[0].data = weekStatistics.data;
                // Search for graph boundaries
                this.chartData[0].data.forEach( (valArray) => {
                    if (valArray[1] > this.chartDataYMaxValue) { this.chartDataYMaxValue = valArray[1]; }
                });
                this.graphBottomLeftValue = Math.round(weekStatistics.activeEnergyAverage);
                this.graphBottomRightValue = Math.round(weekStatistics.activeEnergyTotal);
            }
            if (this.globalDatabase.selectedInstallation.energyStatistics.statisticsByWeek.has(previousWeekKey)) {
                const weekStatistics = this.globalDatabase.selectedInstallation.energyStatistics.statisticsByWeek.get(previousWeekKey);
                this.chartData[1].data = weekStatistics.data;
                // Search for graph boundaries
                this.chartData[1].data.forEach( (valArray) => {
                    if (valArray[1] > this.chartDataYMaxValue) { this.chartDataYMaxValue = valArray[1]; }
                });
            }
            this.chartOptions.yaxis.max = this.chartDataYMaxValue + 1.0;
            this.eventManager.broadcast({
                name: this.flotEventToGenerate,
                content: { dataset: this.chartData, options: this.chartOptions }
            });
            this.isFetchingData = false;

        } catch (Exception) {
            console.warn(Exception);
        }
    }

    createMonthlySmallGraph() {
        try {
            this.graphTitle = 'MONTHLY ENERGY CONSUMPTION';
            this.graphBottomLeftTitle = 'Day average';
            this.graphBottomRightTitle = 'Total per month';

            this.chartData = [{
                data: [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0], [12, 0], [13, 0], [14, 0], [15, 0], [16, 0], [17, 0], [18, 0], [19, 0], [20, 0], [21, 0], [22, 0], [23, 0], [24, 0], [25, 0], [26, 0], [27, 0], [28, 0], [29, 0], [30, 0], [31, 0]],
                label: 'Current month',
                color: '#905dd1'
            },
                {
                    data: [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0], [12, 0], [13, 0], [14, 0], [15, 0], [16, 0], [17, 0], [18, 0], [19, 0], [20, 0], [21, 0], [22, 0], [23, 0], [24, 0], [25, 0], [26, 0], [27, 0], [28, 0], [29, 0], [30, 0], [31, 0]],
                    label: 'Last month',
                    color: '#428bca'
                }];

            this.chartOptions = {
                series: {
                    lines: {
                        show: false
                    },
                    splines: {
                        show: true,
                        tension: 0.4,
                        lineWidth: 1,
                        fill: 0.4
                    },
                    shadowSize: 0
                },
                points: {
                    show: true,
                },
                legend: {
                    container: '#' + this.legendId,
                    noColumns: 0
                },
                grid: {
                    hoverable: true,
                    clickable: true,
                    borderColor: '#ddd',
                    borderWidth: 0,
                    labelMargin: 5,
                    backgroundColor: '#fff'
                },
                yaxis: {
                    min: 0,
                    max: this.chartDataYMaxValue + 1 ,
                    color: '#656565'
                },
                xaxis: {
                    color: '#656565',
                    ticks: [[0, '1'], [1, '2'], [2, '3'], [3, '4'], [4, '5'], [5, '6'], [6, '7'], [7, '8'], [8, '9'], [9, '10'], [10, '11'], [11, '12'], [12, '13'], [13, '14'], [14, '15'], [15, '16'], [16, '17'], [17, '18'], [18, '19'], [19, '20'], [20, '21'], [21, '22'], [22, '23'], [23, '24'], [24, '25'], [25, '26'], [26, '27'], [27, '28'], [28, '29'], [29, '30'], [30, '31']]

                }
            };
            const currentMonthKey = this.currentDate.getFullYear() + '_' + (this.currentDate.getMonth() + 1);
            const previousMonth = new Date(this.currentDate);
            previousMonth.setMonth(previousMonth.getMonth() - 1);
            const previousMonthKey = previousMonth.getFullYear() + '_' + (previousMonth.getMonth() + 1);
            // Extract values from the week statistics using the key
            if (this.globalDatabase.selectedInstallation.energyStatistics.statisticsByMonth.has(currentMonthKey)) {
                const monthStatistics = this.globalDatabase.selectedInstallation.energyStatistics.statisticsByMonth.get(currentMonthKey);
                const chartData = [];
                monthStatistics.data.slice(1, 32).forEach( (val) => {
                    chartData.push([val[0] - 1, val[1]]);
                });
                this.chartData[0].data = chartData;
                // Search for graph boundaries
                this.chartData[0].data.forEach( (valArray) => {
                    if (valArray[1] > this.chartDataYMaxValue) { this.chartDataYMaxValue = valArray[1]; }
                });
                this.graphBottomLeftValue = Math.round(monthStatistics.activeEnergyAverage);
                this.graphBottomRightValue = Math.round(monthStatistics.activeEnergyTotal);
            }
            if (this.globalDatabase.selectedInstallation.energyStatistics.statisticsByMonth.has(previousMonthKey)) {
                const monthStatistics = this.globalDatabase.selectedInstallation.energyStatistics.statisticsByMonth.get(previousMonthKey);
                const chartData = [];
                monthStatistics.data.slice(1, 32).forEach( (val) => {
                    chartData.push([val[0] - 1, val[1]]);
                });
                this.chartData[1].data = chartData;
                // Search for graph boundaries
                this.chartData[1].data.forEach( (valArray) => {
                    if (valArray[1] > this.chartDataYMaxValue) { this.chartDataYMaxValue = valArray[1]; }
                });
            }
            this.chartOptions.yaxis.max = this.chartDataYMaxValue + 1.0;
            this.eventManager.broadcast({
                name: this.flotEventToGenerate,
                content: { dataset: this.chartData, options: this.chartOptions }
            });
            this.isFetchingData = false;
        } catch (Exception) {
            console.warn(Exception);
        }
    }

    updateChartEnergyStatistics(reference) {
        switch (this.chartType) {
            case 'daily':
                this.createDailySmallGraph();
                break;
            case 'weekly':
                this.createWeeklySmallGraph();
                break;
            case 'monthly':
                this.createMonthlySmallGraph();
                break;
            default:
                this.createDailySmallGraph();
        }
    }

    ngOnDestroy() {
        this.eventManager.destroy(this.eventSubscriber);
        this.eventManager.destroy(this.selectedInstallationChange);
        this.eventManager.destroy(this.eventSubscriberInstallationWeeklyStatistics);
    }

    registerEvents() {
        this.eventSubscriber = this.eventManager.subscribe(
            this.eventwatch,
            (response) => this.updateChartEnergyStatistics(this)
        );
        this.selectedInstallationChange = this.eventManager.subscribe(
            INSTALLATION__SELECTED_INSTALLATION_CHANGED,
            (response) => this.isFetchingData = true
        );
        this.eventSubscriberInstallationWeeklyStatistics = this.eventManager.subscribe(
            GLOBALDATABASE__INSTALLATION_WEEKLY_STATISTICS_FETCHING,
            (response) => {
                this.isFetchingData = true;
            }
        );
    }

    formatPowerConsumption(power) {
        return Helpers.formatPowerConsumption(power);
    }

}
