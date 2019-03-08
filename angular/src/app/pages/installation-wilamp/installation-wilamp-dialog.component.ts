import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse, HttpErrorResponse } from '@angular/common/http';

import { Observable, Subject } from 'rxjs';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager, JhiAlertService } from 'ng-jhipster';

import { InstallationWilamp } from './installation-wilamp.model';
import { InstallationWilampPopupService } from './installation-wilamp-popup.service';
import { InstallationWilampService } from './installation-wilamp.service';
import { AddressWilamp, AddressWilampService } from '../address-wilamp';
import { CustomerWilamp, CustomerWilampService } from '../customer-wilamp';

@Component({
    selector: 'jhi-installation-wilamp-dialog',
    templateUrl: './installation-wilamp-dialog.component.html',
})
export class InstallationWilampDialogComponent implements OnInit {

    installation: InstallationWilamp;
    isSaving: boolean;

    addresses: AddressWilamp[];

    customers: CustomerWilamp[];

    constructor(
        public activeModal: NgbActiveModal,
        private jhiAlertService: JhiAlertService,
        private installationService: InstallationWilampService,
        private addressService: AddressWilampService,
        private customerService: CustomerWilampService,
        private eventManager: JhiEventManager,
    ) {
    }

    ngOnInit() {
        this.isSaving = false;
        this.addressService
            .query({filter: 'installation-is-null'})
            .subscribe((res: HttpResponse<AddressWilamp[]>) => {
                if (!this.installation.address) {
                    this.addresses = res.body;
                } else {
                    this.addressService
                        .find(this.installation.address)
                        .subscribe((subRes: HttpResponse<AddressWilamp>) => {
                            this.addresses = [subRes.body].concat(res.body);
                        }, (subRes: HttpErrorResponse) => this.onError(subRes.message));
                }
            }, (res: HttpErrorResponse) => this.onError(res.message));
        this.customerService.query()
            .subscribe((res: HttpResponse<CustomerWilamp[]>) => { this.customers = res.body; }, (res: HttpErrorResponse) => this.onError(res.message));
    }

    clear() {
        this.activeModal.dismiss('cancel');
    }

    save() {
        this.isSaving = true;
        if (this.installation.id !== undefined) {
            this.subscribeToSaveResponse(
                this.installationService.update(this.installation));
        } else {
            this.subscribeToSaveResponse(
                this.installationService.create(this.installation));
        }
    }

    private subscribeToSaveResponse(result: Observable<HttpResponse<InstallationWilamp>>) {
        result.subscribe((res: HttpResponse<InstallationWilamp>) =>
            this.onSaveSuccess(res.body), (res: HttpErrorResponse) => this.onSaveError());
    }

    private onSaveSuccess(result: InstallationWilamp) {
        this.eventManager.broadcast({ name: 'installationListModification', content: 'OK'});
        this.isSaving = false;
        this.activeModal.dismiss(result);
    }

    private onSaveError() {
        this.isSaving = false;
    }

    private onError(error: any) {
        this.jhiAlertService.error(error.message, null, null);
    }

    trackAddressById(index: number, item: AddressWilamp) {
        return item.id;
    }

    trackCustomerById(index: number, item: CustomerWilamp) {
        return item.id;
    }
}

@Component({
    selector: 'jhi-installation-wilamp-popup',
    template: '',
})
export class InstallationWilampPopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private installationPopupService: InstallationWilampPopupService,
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            if ( params['id'] ) {
                this.installationPopupService
                    .open(InstallationWilampDialogComponent as Component, params['id']);
            } else {
                this.installationPopupService
                    .open(InstallationWilampDialogComponent as Component);
            }
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
