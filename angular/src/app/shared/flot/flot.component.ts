import {
    Component,
    AfterViewInit,
    Input,
    ChangeDetectionStrategy,
    OnChanges,
    ElementRef,
    SimpleChanges, OnInit, HostListener, OnDestroy,
} from '@angular/core';
import {
    GLOBALDATABASE__INSTALLATION_WEEKLY_STATISTICS_FETCHED,
    INSTALLATION__LIST_MODIFICATION,
    INSTALLATION__SELECTED_ID_CHANGED,
} from '../constants/events.constants';
import {JhiEventManager} from 'ng-jhipster';
import {Subscription} from 'rxjs/Rx';

const jQuery: any = require('jquery');
require('flot/jquery.flot');
require('flot/jquery.flot.time');
require ('flot-spline');
declare var $: any;

@Component({
    selector: 'flot-graph',
    template: `<div>Loading...</div>`,
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class FlotGraphComponent implements OnChanges, OnInit, OnDestroy {
    static initialized = false;

    @Input() refresh: any;
    @Input() dataset: any;
    @Input() options: any;
    @Input() eventwatch: string;
    @Input() width: string | number = '100%';
    @Input() height: string | number = 220;
    private plotArea: any;
    private eventSubscriber: Subscription;

    constructor(
        private el: ElementRef,
        private eventManager: JhiEventManager,
    ) {
        this.el = el;
    }

    ngOnInit() {
        this.registerEvents();
        // if (!FlotGraphComponent.initialized) {
            this.plotArea = $(this.el.nativeElement).find('div').empty();
            this.plotArea.css({
                width: this.width,
                height: this.height,
            });
            this.plotGraph();

            /*$('#flot-graph').bind('plotclick', function(event, pos, item) {
                if (item) {
                    document.body.style.cursor = 'pointer';
                } else {
                    document.body.style.cursor = 'default';
                }
            });*/

            FlotGraphComponent.initialized = true;
        // }
    }

    plotGraph() {
        try {
            if (this.dataset && this.dataset.constructor === Function) {
                const datasetResult = this.dataset.call();
                $.plot(this.plotArea, datasetResult, this.options);
            } else {
                $.plot(this.plotArea, this.dataset, this.options);
            }
        } catch (Exception) {}
    }
    ngOnDestroy() {
        this.unregisterEvents();
    }

    public ngOnChanges(changes: SimpleChanges): void {
        if (changes['refresh'] && !changes['refresh'].isFirstChange() && FlotGraphComponent.initialized) {
            this.plotGraph();
        }
    }

    @HostListener('window:resize', ['$event'])
    onResize(event) {
        console.warn('Width: ' + event.target.innerWidth);
        if (FlotGraphComponent.initialized) {
            this.plotGraph();
        }
    }

    registerEvents() {
        try {
            if (this.eventwatch && this.eventwatch.constructor === String && this.eventwatch.constructor.length > 0) {
                this.eventSubscriber = this.eventManager.subscribe(
                    this.eventwatch,
                    (response) => {
                        if (FlotGraphComponent.initialized) {
                            if (response && response.hasOwnProperty('content')  && response.content.hasOwnProperty('dataset') && response.content.dataset.constructor === Array) {
                                this.dataset = response.content.dataset;
                                this.options = response.content.options;
                            }
                            this.plotGraph();
                        }
                    },
                );
            }
        } catch (Exception) { }
    }

    unregisterEvents() {
        if (this.eventwatch.constructor === String && this.eventwatch.constructor.length > 0) {
            this.eventManager.destroy(this.eventSubscriber);
        }
    }

}
