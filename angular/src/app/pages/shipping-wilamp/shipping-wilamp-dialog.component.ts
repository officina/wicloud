import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse, HttpErrorResponse } from '@angular/common/http';

import { Observable, Subject } from 'rxjs';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager, JhiAlertService } from 'ng-jhipster';

import { ShippingWilamp } from './shipping-wilamp.model';
import { ShippingWilampPopupService } from './shipping-wilamp-popup.service';
import { ShippingWilampService } from './shipping-wilamp.service';
import { ContactWilamp } from '../contact-wilamp/contact-wilamp.model';
import { ContactWilampService } from '../contact-wilamp/contact-wilamp.service';
import { OrderWilamp } from '../order-wilamp/order-wilamp.model';
import { OrderWilampService } from '../order-wilamp/order-wilamp.service';

@Component({
    selector: 'jhi-shipping-wilamp-dialog',
    templateUrl: './shipping-wilamp-dialog.component.html'
})
export class ShippingWilampDialogComponent implements OnInit {

    shipping: ShippingWilamp;
    isSaving: boolean;

    contacts: ContactWilamp[];

    orders: OrderWilamp[];

    constructor(
        public activeModal: NgbActiveModal,
        private jhiAlertService: JhiAlertService,
        private shippingService: ShippingWilampService,
        private contactService: ContactWilampService,
        private orderService: OrderWilampService,
        private eventManager: JhiEventManager
    ) {
    }

    ngOnInit() {
        this.isSaving = false;
        this.contactService.query()
            .subscribe((res: HttpResponse<ContactWilamp[]>) => { this.contacts = res.body; }, (res: HttpErrorResponse) => this.onError(res.message));
        this.orderService.query()
            .subscribe((res: HttpResponse<OrderWilamp[]>) => { this.orders = res.body; }, (res: HttpErrorResponse) => this.onError(res.message));
    }

    clear() {
        this.activeModal.dismiss('cancel');
    }

    save() {
        this.isSaving = true;
        if (this.shipping.id !== undefined) {
            this.subscribeToSaveResponse(
                this.shippingService.update(this.shipping));
        } else {
            this.subscribeToSaveResponse(
                this.shippingService.create(this.shipping));
        }
    }

    private subscribeToSaveResponse(result: Observable<HttpResponse<ShippingWilamp>>) {
        result.subscribe((res: HttpResponse<ShippingWilamp>) =>
            this.onSaveSuccess(res.body), (res: HttpErrorResponse) => this.onSaveError());
    }

    private onSaveSuccess(result: ShippingWilamp) {
        this.eventManager.broadcast({ name: 'shippingListModification', content: 'OK'});
        this.isSaving = false;
        this.activeModal.dismiss(result);
    }

    private onSaveError() {
        this.isSaving = false;
    }

    private onError(error: any) {
        this.jhiAlertService.error(error.message, null, null);
    }

    trackContactById(index: number, item: ContactWilamp) {
        return item.id;
    }

    trackOrderById(index: number, item: OrderWilamp) {
        return item.id;
    }

    getSelected(selectedVals: Array<any>, option: any) {
        if (selectedVals) {
            for (let i = 0; i < selectedVals.length; i++) {
                if (option.id === selectedVals[i].id) {
                    return selectedVals[i];
                }
            }
        }
        return option;
    }
}

@Component({
    selector: 'jhi-shipping-wilamp-popup',
    template: ''
})
export class ShippingWilampPopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private shippingPopupService: ShippingWilampPopupService
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            if ( params['id'] ) {
                this.shippingPopupService
                    .open(ShippingWilampDialogComponent as Component, params['id']);
            } else {
                this.shippingPopupService
                    .open(ShippingWilampDialogComponent as Component);
            }
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
