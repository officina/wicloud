import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager } from 'ng-jhipster';

import { ShippingWilamp } from './shipping-wilamp.model';
import { ShippingWilampPopupService } from './shipping-wilamp-popup.service';
import { ShippingWilampService } from './shipping-wilamp.service';

@Component({
    selector: 'jhi-shipping-wilamp-delete-dialog',
    templateUrl: './shipping-wilamp-delete-dialog.component.html',
})
export class ShippingWilampDeleteDialogComponent {

    shipping: ShippingWilamp;

    constructor(
        private shippingService: ShippingWilampService,
        public activeModal: NgbActiveModal,
        private eventManager: JhiEventManager,
    ) {
    }

    clear() {
        this.activeModal.dismiss('cancel');
    }

    confirmDelete(id: number) {
        this.shippingService.delete(id).subscribe((response) => {
            this.eventManager.broadcast({
                name: 'shippingListModification',
                content: 'Deleted an shipping',
            });
            this.activeModal.dismiss(true);
        });
    }
}

@Component({
    selector: 'jhi-shipping-wilamp-delete-popup',
    template: '',
})
export class ShippingWilampDeletePopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private shippingPopupService: ShippingWilampPopupService,
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            this.shippingPopupService
                .open(ShippingWilampDeleteDialogComponent as Component, params['id']);
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
