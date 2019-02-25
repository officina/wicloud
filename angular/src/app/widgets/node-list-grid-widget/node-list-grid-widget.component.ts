import {Component, Input, OnInit, AfterViewInit, OnDestroy} from '@angular/core';
import {NodeWilamp} from '../../pages/node-wilamp';
import { DomSanitizer } from '@angular/platform-browser';
import {
    GLOBALDATABASE__INSTALLATION_WEEKLY_STATISTICS_FETCHED, GLOBALDATABASE__INSTALLATION_WEEKLY_STATISTICS_FETCHING,
    GLOBALDATABASE__NODES_FETCHED,
    INSTALLATION__SELECTED_INSTALLATION_CHANGED,
    INSTALLATION_DASHBOARD__DAILY_STATISTICS_FETCHED,
    INSTALLATION_DASHBOARD__MONTHLY_STATISTICS_FETCHED,
    INSTALLATION_DASHBOARD__WEEKLY_STATISTICS_FETCHED,
} from '../../shared/constants/events.constants';
import {KWtoCO2Factor} from '../../shared/constants/graph.constants';
import {GlobalDatabaseService} from '../../shared/global-database/global-database.service';
import DateTimeFormat = Intl.DateTimeFormat;
import {JhiEventManager} from 'ng-jhipster';
import {Subscription} from 'rxjs/Rx';
import {ScriptLoaderService} from '../../_services/script-loader.service';
declare var dhtmlXGridObject, dhtmlxEvent: any;

@Component({
  selector: 'node-list-grid-widget',
  templateUrl: './node-list-grid-widget.component.html',
  styleUrls: ['node-list-grid-widget.component.css'],

})
export class NodeListGridWidgetComponent implements OnInit, AfterViewInit, OnDestroy {
    @Input() nodes: NodeWilamp[];
    public nodesFetchedSubscriber: Subscription;
    public installationChangedSubscriber: Subscription;
    public eventSubscriberInstallationWeeklyStatistics: Subscription;
    public isFetchingData = true;

    public nodesGridOptions = {
        groupBy: 2,
    };
    public nodesGrid: any;
    public numRows: number;
    public numColumns: number;
    public numTables: number;
    public rowsPerPage: number;
    public data: any[];
    public colDef: any[];
    public colWidth: any[];
    public colAlign: any[];
    public colTypes: any[];
    public colNames: any[];
    public eXcell_details: any;
    public showStyle = false;
    public eventwatch = GLOBALDATABASE__NODES_FETCHED;

    constructor(
        private _script: ScriptLoaderService,
        private _DomSanitizationService: DomSanitizer,
        public globalDatabase: GlobalDatabaseService,
        private eventManager: JhiEventManager,
    ) {

        this.numRows = 20;
        this.numTables = 1;
        this.rowsPerPage = 10;
        this.colNames = ['Mac', 'Name', 'Description', 'Type', 'Lamp', 'KWh', 'Lamp life', 'Node life'];
        this.data = [];
        this.colDef = [];
        this.colWidth = [];
        this.colAlign = [];
        this.colTypes = [];
        this.numColumns = this.colNames.length;

    }

    ngOnInit() {
        this.registerEvents();
    }

    ngAfterViewInit() {
        console.warn('Initializing jquery');
        $('.test').hide();
        console.warn('tested');
        /*$('<link/>', {
            rel: 'stylesheet',
            type: 'text/css',
            href: '/assets/app/js/libs/dhtmlxsuite/dhtmlx.css'
        }).appendTo('head');*/
        this.initializeXgrid();
        this.createXgrid();

        /*$.getScript( '/assets/app/js/libs/dhtmlxsuite/dhtmlx.js' )
            .done(function( script, textStatus ) {
                console.warn('DHTMLX loaded!');
                this.initializeXgrid();
                this.createXgrid();
            }.bind(this))
            .fail(function( jqxhr, settings, exception ) {
                console.warn( 'Triggered ajaxError handler.' );
            }.bind(this));*/
        /*this._script.load('body',
            '/assets/app/js/libs/dhtmlxsuite/dhtmlx.js')
            .then((result) => {
                console.warn('DHTMLX loaded!');
                // this.initializeXgrid();
                // this.createXgrid();
            });*/
    }

    initializeXgrid() {
        try {
            this.nodesGrid = new dhtmlXGridObject('gridbox');
            this.nodesGrid.setImagePath('./imgs/');
            this.nodesGrid.setHeader(this.colNames.join(','));
            this.nodesGrid.setInitWidthsP('15,20,20,12,12,11,10,10');
            this.nodesGrid.setColAlign('left,left,left,right,center,left,left,left');
            this.nodesGrid.setColTypes('edtxt,edtxt,edtxt,edtxt,edtxt,edtxt,edtxt,edtxt');
            this.nodesGrid.setColSorting('na,str,str,int,int,int,str,str');
            this.nodesGrid.enableAutoHeight(true, 1000);
            // this.nodesGrid.enableAutoWidth(true);
            this.nodesGrid.enableResizing('true,true,true,true,true,true,true,true');
            this.nodesGrid.init();
            const start = new Date().getTime();
            dhtmlxEvent(window, 'resize', (function() {
                this.nodesGrid.setSizes();
            }).bind(this));
        } catch (e) {
            console.warn(e);
        }
    }

    createXgrid() {
        this.nodesGrid.clearAll();
        this.globalDatabase.selectedInstallation.nodes.forEach( (node) => {
            const rowDefinition = [node.mac, node.name, node.description, node.nodeType];
            if (!isNaN(node.nominalPower) && node.nominalPower !== null) { rowDefinition.push(node.nominalPower + ' W'); } else { rowDefinition.push('n/a'); }
            const nodeStatistics = this.globalDatabase.selectedInstallation.statisticsByNodeIdHMap.get(node.id);
            if (nodeStatistics !== undefined) {
                rowDefinition.push(Math.round(nodeStatistics.sumEnergy) + ' KWh', Math.round(nodeStatistics.burningTime / 60) + ' h', Math.round(nodeStatistics.nodeLife / 60) + ' h');
            } else {
                rowDefinition.push('n/a', 'n/a', 'n/a');
            }
            this.nodesGrid.addRow(node.mac, rowDefinition );
        });

        this.nodesGrid.groupBy(3);

        // myGrid.addRow(start,["Sales","Book Title","Author","Price","In Store","Shipping","Bestseller","Date of Publication"] )
        // start = new Date().getTime();
        // var row = myGrid.getAllRowIds();
        // console.warn(row);
        /* myGrid.load("https://dhtmlx.com/docs/products/dhtmlxGrid/samples/common/grid.xml",function(){
            myGrid.groupBy(2);
              }); */

    }

    unGroupGrid() {
        this.nodesGrid.unGroup();
    }

    groupByChanged() {
        this.nodesGrid.groupBy(this.nodesGridOptions.groupBy);
    }

    getStyle() {
        if (this.showStyle) {
            return 'yellow';
        } else {
            return '';
        }
    }

    ngOnDestroy() {
        this.eventManager.destroy(this.nodesFetchedSubscriber);
        this.eventManager.destroy(this.installationChangedSubscriber);
        this.eventManager.destroy(this.eventSubscriberInstallationWeeklyStatistics);
    }

    registerEvents() {
        this.nodesFetchedSubscriber = this.eventManager.subscribe(
            GLOBALDATABASE__NODES_FETCHED,
            (response) => this.createXgrid(),
        );
        this.installationChangedSubscriber = this.eventManager.subscribe(
            INSTALLATION__SELECTED_INSTALLATION_CHANGED,
            (response) => this.createXgrid(),
        );
        this.eventSubscriberInstallationWeeklyStatistics = this.eventManager.subscribe(
            GLOBALDATABASE__INSTALLATION_WEEKLY_STATISTICS_FETCHING,
            (response) => {
                this.isFetchingData = true;
            },
        );
    }

}
