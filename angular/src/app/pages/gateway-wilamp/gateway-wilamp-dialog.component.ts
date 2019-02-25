import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse, HttpErrorResponse } from '@angular/common/http';

import { Observable } from 'rxjs';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager, JhiAlertService } from 'ng-jhipster';

import { GatewayWilamp } from './gateway-wilamp.model';
import { GatewayWilampPopupService } from './gateway-wilamp-popup.service';
import { GatewayWilampService } from './gateway-wilamp.service';
import { InstallationWilamp } from '../installation-wilamp/installation-wilamp.model';
import { InstallationWilampService } from '../installation-wilamp/installation-wilamp.service';
import { ShippingWilamp } from '../shipping-wilamp/shipping-wilamp.model';
import { ShippingWilampService } from '../shipping-wilamp/shipping-wilamp.service';
import { OrderWilamp } from '../order-wilamp/order-wilamp.model';
import { OrderWilampService } from '../order-wilamp/order-wilamp.service';
import { GatewayInstallationRequest } from '../gateway-installation-request/gateway-installation-request.model';
import { GatewayInstallationRequestService } from '../gateway-installation-request/gateway-installation-request.service';

@Component({
    selector: 'jhi-gateway-wilamp-dialog',
    templateUrl: './gateway-wilamp-dialog.component.html'
})
export class GatewayWilampDialogComponent implements OnInit {

    gateway: GatewayWilamp;
    isSaving: boolean;

    installations: InstallationWilamp[];

    shippings: ShippingWilamp[];

    orders: OrderWilamp[];

    gatewayinstallationrequests: GatewayInstallationRequest[];

    constructor(
        public activeModal: NgbActiveModal,
        private jhiAlertService: JhiAlertService,
        private gatewayService: GatewayWilampService,
        private installationService: InstallationWilampService,
        private shippingService: ShippingWilampService,
        private orderService: OrderWilampService,
        private gatewayInstallationRequestService: GatewayInstallationRequestService,
        private eventManager: JhiEventManager
    ) {
    }

    ngOnInit() {
        this.isSaving = false;
        this.installationService.query()
            .subscribe((res: HttpResponse<InstallationWilamp[]>) => { this.installations = res.body; }, (res: HttpErrorResponse) => this.onError(res.message));
        this.shippingService.query()
            .subscribe((res: HttpResponse<ShippingWilamp[]>) => { this.shippings = res.body; }, (res: HttpErrorResponse) => this.onError(res.message));
        this.orderService.query()
            .subscribe((res: HttpResponse<OrderWilamp[]>) => { this.orders = res.body; }, (res: HttpErrorResponse) => this.onError(res.message));
        this.gatewayInstallationRequestService.query()
            .subscribe((res: HttpResponse<GatewayInstallationRequest[]>) => { this.gatewayinstallationrequests = res.body; }, (res: HttpErrorResponse) => this.onError(res.message));
    }

    clear() {
        this.activeModal.dismiss('cancel');
    }

    save() {
        this.isSaving = true;
        if (this.gateway.id !== undefined) {
            this.subscribeToSaveResponse(
                this.gatewayService.update(this.gateway));
        } else {
            this.subscribeToSaveResponse(
                this.gatewayService.create(this.gateway));
        }
    }

    private subscribeToSaveResponse(result: Observable<HttpResponse<GatewayWilamp>>) {
        result.subscribe((res: HttpResponse<GatewayWilamp>) =>
            this.onSaveSuccess(res.body), (res: HttpErrorResponse) => this.onSaveError());
    }

    private onSaveSuccess(result: GatewayWilamp) {
        this.eventManager.broadcast({ name: 'gatewayListModification', content: 'OK'});
        this.isSaving = false;
        this.activeModal.dismiss(result);
    }

    private onSaveError() {
        this.isSaving = false;
    }

    private onError(error: any) {
        this.jhiAlertService.error(error.message, null, null);
    }

    trackInstallationById(index: number, item: InstallationWilamp) {
        return item.id;
    }

    trackShippingById(index: number, item: ShippingWilamp) {
        return item.id;
    }

    trackOrderById(index: number, item: OrderWilamp) {
        return item.id;
    }

    trackGatewayInstallationRequestById(index: number, item: GatewayInstallationRequest) {
        return item.id;
    }
}

@Component({
    selector: 'jhi-gateway-wilamp-popup',
    template: ''
})
export class GatewayWilampPopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private gatewayPopupService: GatewayWilampPopupService
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            if ( params['id'] ) {
                this.gatewayPopupService
                    .open(GatewayWilampDialogComponent as Component, params['id']);
            } else {
                this.gatewayPopupService
                    .open(GatewayWilampDialogComponent as Component);
            }
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
