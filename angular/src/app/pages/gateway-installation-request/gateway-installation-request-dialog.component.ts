import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse, HttpErrorResponse } from '@angular/common/http';

import { Observable } from 'rxjs';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager, JhiAlertService } from 'ng-jhipster';

import { GatewayInstallationRequest } from './gateway-installation-request.model';
import { GatewayInstallationRequestPopupService } from './gateway-installation-request-popup.service';
import { GatewayInstallationRequestService } from './gateway-installation-request.service';
import { GatewayWilamp, GatewayWilampService } from '../gateway-wilamp';

@Component({
    selector: 'jhi-gateway-installation-request-dialog',
    templateUrl: './gateway-installation-request-dialog.component.html',
})
export class GatewayInstallationRequestDialogComponent implements OnInit {

    gatewayInstallationRequest: GatewayInstallationRequest;
    isSaving: boolean;

    gateways: GatewayWilamp[];

    constructor(
        public activeModal: NgbActiveModal,
        private jhiAlertService: JhiAlertService,
        private gatewayInstallationRequestService: GatewayInstallationRequestService,
        private gatewayService: GatewayWilampService,
        private eventManager: JhiEventManager,
    ) {
    }

    ngOnInit() {
        this.isSaving = false;
        this.gatewayService
            .query({filter: 'gatewayinstallationrequest-is-null'})
            .subscribe((res: HttpResponse<GatewayWilamp[]>) => {
                if (!this.gatewayInstallationRequest.gatewayId) {
                    this.gateways = res.body;
                } else {
                    this.gatewayService
                        .find(this.gatewayInstallationRequest.gatewayId)
                        .subscribe((subRes: HttpResponse<GatewayWilamp>) => {
                            this.gateways = [subRes.body].concat(res.body);
                        }, (subRes: HttpErrorResponse) => this.onError(subRes.message));
                }
            }, (res: HttpErrorResponse) => this.onError(res.message));
    }

    clear() {
        this.activeModal.dismiss('cancel');
    }

    save() {
        this.isSaving = true;
        if (this.gatewayInstallationRequest.id !== undefined) {
            this.subscribeToSaveResponse(
                this.gatewayInstallationRequestService.update(this.gatewayInstallationRequest));
        } else {
            this.subscribeToSaveResponse(
                this.gatewayInstallationRequestService.create(this.gatewayInstallationRequest));
        }
    }

    private subscribeToSaveResponse(result: Observable<HttpResponse<GatewayInstallationRequest>>) {
        result.subscribe((res: HttpResponse<GatewayInstallationRequest>) =>
            this.onSaveSuccess(res.body), (res: HttpErrorResponse) => this.onSaveError());
    }

    private onSaveSuccess(result: GatewayInstallationRequest) {
        this.eventManager.broadcast({ name: 'gatewayInstallationRequestListModification', content: 'OK'});
        this.isSaving = false;
        this.activeModal.dismiss(result);
    }

    private onSaveError() {
        this.isSaving = false;
    }

    private onError(error: any) {
        this.jhiAlertService.error(error.message, null, null);
    }

    trackGatewayById(index: number, item: GatewayWilamp) {
        return item.id;
    }
}

@Component({
    selector: 'jhi-gateway-installation-request-popup',
    template: '',
})
export class GatewayInstallationRequestPopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private gatewayInstallationRequestPopupService: GatewayInstallationRequestPopupService,
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            if ( params['id'] ) {
                this.gatewayInstallationRequestPopupService
                    .open(GatewayInstallationRequestDialogComponent as Component, params['id']);
            } else {
                this.gatewayInstallationRequestPopupService
                    .open(GatewayInstallationRequestDialogComponent as Component);
            }
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
