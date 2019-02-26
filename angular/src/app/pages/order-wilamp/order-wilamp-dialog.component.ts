import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager, JhiAlertService } from 'ng-jhipster';
import { OrderWilamp } from './order-wilamp.model';
import { OrderWilampPopupService } from './order-wilamp-popup.service';
import { OrderWilampService } from './order-wilamp.service';
import { CustomerWilamp, CustomerWilampService } from '../customer-wilamp';
import { ShippingWilamp, ShippingWilampService } from '../shipping-wilamp';

@Component({
    selector: 'jhi-order-wilamp-dialog',
    templateUrl: './order-wilamp-dialog.component.html',
})
export class OrderWilampDialogComponent implements OnInit {

    order: OrderWilamp;
    isSaving: boolean;

    customers: CustomerWilamp[];

    shippings: ShippingWilamp[];

    constructor(
        public activeModal: NgbActiveModal,
        private jhiAlertService: JhiAlertService,
        private orderService: OrderWilampService,
        private customerService: CustomerWilampService,
        private shippingService: ShippingWilampService,
        private eventManager: JhiEventManager,
    ) {
    }

    ngOnInit() {
        this.isSaving = false;
        this.customerService.query()
            .subscribe((res: HttpResponse<CustomerWilamp[]>) => { this.customers = res.body; }, (res: HttpErrorResponse) => this.onError(res.message));
        this.shippingService.query()
            .subscribe((res: HttpResponse<ShippingWilamp[]>) => { this.shippings = res.body; }, (res: HttpErrorResponse) => this.onError(res.message));
    }

    clear() {
        this.activeModal.dismiss('cancel');
    }

    save() {
        this.isSaving = true;
        if (this.order.id !== undefined) {
            this.subscribeToSaveResponse(
                this.orderService.update(this.order));
        } else {
            this.subscribeToSaveResponse(
                this.orderService.create(this.order));
        }
    }

    private subscribeToSaveResponse(result: Observable<HttpResponse<OrderWilamp>>) {
        result.subscribe((res: HttpResponse<OrderWilamp>) =>
            this.onSaveSuccess(res.body), (res: HttpErrorResponse) => this.onSaveError());
    }

    private onSaveSuccess(result: OrderWilamp) {
        this.eventManager.broadcast({ name: 'orderListModification', content: 'OK'});
        this.isSaving = false;
        this.activeModal.dismiss(result);
    }

    private onSaveError() {
        this.isSaving = false;
    }

    private onError(error: any) {
        this.jhiAlertService.error(error.message, null, null);
    }

    trackCustomerById(index: number, item: CustomerWilamp) {
        return item.id;
    }

    trackShippingById(index: number, item: ShippingWilamp) {
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
    selector: 'jhi-order-wilamp-popup',
    template: '',
})
export class OrderWilampPopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private orderPopupService: OrderWilampPopupService,
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            if ( params['id'] ) {
                this.orderPopupService
                    .open(OrderWilampDialogComponent as Component, params['id']);
            } else {
                this.orderPopupService
                    .open(OrderWilampDialogComponent as Component);
            }
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
