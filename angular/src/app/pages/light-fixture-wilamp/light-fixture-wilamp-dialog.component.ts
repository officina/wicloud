 import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse, HttpErrorResponse } from '@angular/common/http';

import { Observable } from 'rxjs/Observable';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager, JhiAlertService } from 'ng-jhipster';

import { LightFixtureWilamp } from './light-fixture-wilamp.model';
import { LightFixtureWilampPopupService } from './light-fixture-wilamp-popup.service';
import { LightFixtureWilampService } from './light-fixture-wilamp.service';
import { GatewayWilamp, GatewayWilampService } from '../gateway-wilamp';
import { InstallationWilamp, InstallationWilampService } from '../installation-wilamp';
import { LightProfileWilamp, LightProfileWilampService } from '../light-profile-wilamp';

@Component({
    selector: 'jhi-light-fixture-wilamp-dialog',
    templateUrl: './light-fixture-wilamp-dialog.component.html'
})
export class LightFixtureWilampDialogComponent implements OnInit {

    lightFixture: LightFixtureWilamp;
    isSaving: boolean;

    gateways: GatewayWilamp[];

    installations: InstallationWilamp[];

    lightprofiles: LightProfileWilamp[];

    constructor(
        public activeModal: NgbActiveModal,
        private jhiAlertService: JhiAlertService,
        private lightFixtureService: LightFixtureWilampService,
        private gatewayService: GatewayWilampService,
        private installationService: InstallationWilampService,
        private lightProfileService: LightProfileWilampService,
        private eventManager: JhiEventManager
    ) {
    }

    ngOnInit() {
        this.isSaving = false;
        this.gatewayService.query()
            .subscribe((res: HttpResponse<GatewayWilamp[]>) => { this.gateways = res.body; }, (res: HttpErrorResponse) => this.onError(res.message));
        this.installationService.query()
            .subscribe((res: HttpResponse<InstallationWilamp[]>) => { this.installations = res.body; }, (res: HttpErrorResponse) => this.onError(res.message));
        this.lightProfileService.query()
            .subscribe((res: HttpResponse<LightProfileWilamp[]>) => { this.lightprofiles = res.body; }, (res: HttpErrorResponse) => this.onError(res.message));
    }

    clear() {
        this.activeModal.dismiss('cancel');
    }

    save() {
        this.isSaving = true;
        if (this.lightFixture.id !== undefined) {
            this.subscribeToSaveResponse(
                this.lightFixtureService.update(this.lightFixture));
        } else {
            this.subscribeToSaveResponse(
                this.lightFixtureService.create(this.lightFixture));
        }
    }

    private subscribeToSaveResponse(result: Observable<HttpResponse<LightFixtureWilamp>>) {
        result.subscribe((res: HttpResponse<LightFixtureWilamp>) =>
            this.onSaveSuccess(res.body), (res: HttpErrorResponse) => this.onSaveError());
    }

    private onSaveSuccess(result: LightFixtureWilamp) {
        this.eventManager.broadcast({ name: 'lightFixtureListModification', content: 'OK'});
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

    trackInstallationById(index: number, item: InstallationWilamp) {
        return item.id;
    }

    trackLightProfileById(index: number, item: LightProfileWilamp) {
        return item.id;
    }
}

@Component({
    selector: 'jhi-light-fixture-wilamp-popup',
    template: ''
})
export class LightFixtureWilampPopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private lightFixturePopupService: LightFixtureWilampPopupService
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            if ( params['id'] ) {
                this.lightFixturePopupService
                    .open(LightFixtureWilampDialogComponent as Component, params['id']);
            } else {
                this.lightFixturePopupService
                    .open(LightFixtureWilampDialogComponent as Component);
            }
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
