import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse, HttpErrorResponse } from '@angular/common/http';

import { Observable } from 'rxjs/Observable';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager, JhiAlertService } from 'ng-jhipster';

import { LightProfileSlotWilamp } from './light-profile-slot-wilamp.model';
import { LightProfileSlotWilampPopupService } from './light-profile-slot-wilamp-popup.service';
import { LightProfileSlotWilampService } from './light-profile-slot-wilamp.service';
import { LightProfileWilamp } from '../light-profile-wilamp/light-profile-wilamp.model';
import { LightProfileWilampService } from '../light-profile-wilamp/light-profile-wilamp.service';

@Component({
    selector: 'jhi-light-profile-slot-wilamp-dialog',
    templateUrl: './light-profile-slot-wilamp-dialog.component.html'
})
export class LightProfileSlotWilampDialogComponent implements OnInit {

    lightProfileSlot: LightProfileSlotWilamp;
    isSaving: boolean;

    lightprofiles: LightProfileWilamp[];

    constructor(
        public activeModal: NgbActiveModal,
        private jhiAlertService: JhiAlertService,
        private lightProfileSlotService: LightProfileSlotWilampService,
        private lightProfileService: LightProfileWilampService,
        private eventManager: JhiEventManager
    ) {
    }

    ngOnInit() {
        this.isSaving = false;
        this.lightProfileService.query()
            .subscribe((res: HttpResponse<LightProfileWilamp[]>) => { this.lightprofiles = res.body; }, (res: HttpErrorResponse) => this.onError(res.message));
    }

    clear() {
        this.activeModal.dismiss('cancel');
    }

    save() {
        this.isSaving = true;
        if (this.lightProfileSlot.id !== undefined) {
            this.subscribeToSaveResponse(
                this.lightProfileSlotService.update(this.lightProfileSlot));
        } else {
            this.subscribeToSaveResponse(
                this.lightProfileSlotService.create(this.lightProfileSlot));
        }
    }

    private subscribeToSaveResponse(result: Observable<HttpResponse<LightProfileSlotWilamp>>) {
        result.subscribe((res: HttpResponse<LightProfileSlotWilamp>) =>
            this.onSaveSuccess(res.body), (res: HttpErrorResponse) => this.onSaveError());
    }

    private onSaveSuccess(result: LightProfileSlotWilamp) {
        this.eventManager.broadcast({ name: 'lightProfileSlotListModification', content: 'OK'});
        this.isSaving = false;
        this.activeModal.dismiss(result);
    }

    private onSaveError() {
        this.isSaving = false;
    }

    private onError(error: any) {
        this.jhiAlertService.error(error.message, null, null);
    }

    trackLightProfileById(index: number, item: LightProfileWilamp) {
        return item.id;
    }
}

@Component({
    selector: 'jhi-light-profile-slot-wilamp-popup',
    template: ''
})
export class LightProfileSlotWilampPopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private lightProfileSlotPopupService: LightProfileSlotWilampPopupService
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            if ( params['id'] ) {
                this.lightProfileSlotPopupService
                    .open(LightProfileSlotWilampDialogComponent as Component, params['id']);
            } else {
                this.lightProfileSlotPopupService
                    .open(LightProfileSlotWilampDialogComponent as Component);
            }
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
