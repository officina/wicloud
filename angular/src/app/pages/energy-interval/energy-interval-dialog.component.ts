import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse, HttpErrorResponse } from '@angular/common/http';

import { Observable, Subject } from 'rxjs';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager } from 'ng-jhipster';

import { EnergyInterval } from './energy-interval.model';
import { EnergyIntervalPopupService } from './energy-interval-popup.service';
import { EnergyIntervalService } from './energy-interval.service';

@Component({
    selector: 'jhi-energy-interval-dialog',
    templateUrl: './energy-interval-dialog.component.html'
})
export class EnergyIntervalDialogComponent implements OnInit {

    energyInterval: EnergyInterval;
    isSaving: boolean;

    constructor(
        public activeModal: NgbActiveModal,
        private energyIntervalService: EnergyIntervalService,
        private eventManager: JhiEventManager
    ) {
    }

    ngOnInit() {
        this.isSaving = false;
    }

    clear() {
        this.activeModal.dismiss('cancel');
    }

    save() {
        this.isSaving = true;
        if (this.energyInterval.id !== undefined) {
            this.subscribeToSaveResponse(
                this.energyIntervalService.update(this.energyInterval));
        } else {
            this.subscribeToSaveResponse(
                this.energyIntervalService.create(this.energyInterval));
        }
    }

    private subscribeToSaveResponse(result: Observable<HttpResponse<EnergyInterval>>) {
        result.subscribe((res: HttpResponse<EnergyInterval>) =>
            this.onSaveSuccess(res.body), (res: HttpErrorResponse) => this.onSaveError());
    }

    private onSaveSuccess(result: EnergyInterval) {
        this.eventManager.broadcast({ name: 'energyIntervalListModification', content: 'OK'});
        this.isSaving = false;
        this.activeModal.dismiss(result);
    }

    private onSaveError() {
        this.isSaving = false;
    }
}

@Component({
    selector: 'jhi-energy-interval-popup',
    template: ''
})
export class EnergyIntervalPopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private energyIntervalPopupService: EnergyIntervalPopupService
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            if ( params['id'] ) {
                this.energyIntervalPopupService
                    .open(EnergyIntervalDialogComponent as Component, params['id']);
            } else {
                this.energyIntervalPopupService
                    .open(EnergyIntervalDialogComponent as Component);
            }
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
