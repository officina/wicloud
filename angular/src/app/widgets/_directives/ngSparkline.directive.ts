import {AfterViewInit, Directive, ElementRef, HostListener, Input} from '@angular/core';
require('jquery-sparkline');
declare var sparkline: any;

@Directive({
    selector: '[sparkline]',
})
export class NgSparklineDirective implements AfterViewInit {
    @Input() data: any;
    @Input() options: any;

    constructor(private el: ElementRef) {
        this.el = el.nativeElement;

    }
    ngAfterViewInit() {
        if (!this.data) { this.data = []; }
        if (!this.options) { this.options = {}; }

        if ((this.data.constructor === Array) && (this.options.constructor === Array)) {
            for (let i = 0; i < this.data.length; i++) {
                (<any>$(this.el)).sparkline(this.data[i], this.options[i]);
            }
        } else {
            (<any>$(this.el)).sparkline(this.data, this.options);
        }

    }

}
