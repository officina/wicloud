import {AfterViewInit, Directive, ElementRef, HostListener, Input} from '@angular/core';

@Directive({
    selector: '[href]',
})
export class HrefPreventDefaultDirective implements AfterViewInit {
    @Input() href: string;

    constructor(private el: ElementRef) {

    }
    ngAfterViewInit() {

    }

    @HostListener('click')
    preventDefault(event) {
        if (this.href.length === 0 || this.href === '#') {
            event.preventDefault();
        }
    }

}
