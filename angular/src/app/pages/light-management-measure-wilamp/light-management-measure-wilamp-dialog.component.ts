import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse, HttpErrorResponse } from '@angular/common/http';

import { Observable, Subject } from 'rxjs';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager, JhiAlertService } from 'ng-jhipster';

import { LightManagementMeasureWilamp } from './light-management-measure-wilamp.model';
import { LightManagementMeasureWilampPopupService } from './light-management-measure-wilamp-popup.service';
import { LightManagementMeasureWilampService } from './light-management-measure-wilamp.service';
import { LightManagementModuleWilamp, LightManagementModuleWilampService } from '../light-management-module-wilamp';

@Component({
    selector: 'jhi-light-management-measure-wilamp-dialog',
    templateUrl: './light-management-measure-wilamp-dialog.component.html',
})
export class LightManagementMeasureWilampDialogComponent implements OnInit {

    lightManagementMeasure: LightManagementMeasureWilamp;
    isSaving: boolean;

    lightmanagementmodules: LightManagementModuleWilamp[];

    constructor(
        public activeModal: NgbActiveModal,
        private jhiAlertService: JhiAlertService,
        private lightManagementMeasureService: LightManagementMeasureWilampService,
        private lightManagementModuleService: LightManagementModuleWilampService,
        private eventManager: JhiEventManager,
    ) {
    }

    ngOnInit() {
        this.isSaving = false;
        this.lightManagementModuleService.query()
            .subscribe((res: HttpResponse<LightManagementModuleWilamp[]>) => { this.lightmanagementmodules = res.body; }, (res: HttpErrorResponse) => this.onError(res.message));
    }

    clear() {
        this.activeModal.dismiss('cancel');
    }

    save() {
        this.isSaving = true;
        if (this.lightManagementMeasure.id !== undefined) {
            this.subscribeToSaveResponse(
                this.lightManagementMeasureService.update(this.lightManagementMeasure));
        } else {
            this.subscribeToSaveResponse(
                this.lightManagementMeasureService.create(this.lightManagementMeasure));
        }
    }

    private subscribeToSaveResponse(result: Observable<HttpResponse<LightManagementMeasureWilamp>>) {
        result.subscribe((res: HttpResponse<LightManagementMeasureWilamp>) =>
            this.onSaveSuccess(res.body), (res: HttpErrorResponse) => this.onSaveError());
    }

    private onSaveSuccess(result: LightManagementMeasureWilamp) {
        this.eventManager.broadcast({ name: 'lightManagementMeasureListModification', content: 'OK'});
        this.isSaving = false;
        this.activeModal.dismiss(result);
    }

    private onSaveError() {
        this.isSaving = false;
    }

    private onError(error: any) {
        this.jhiAlertService.error(error.message, null, null);
    }

    trackLightManagementModuleById(index: number, item: LightManagementModuleWilamp) {
        return item.id;
    }
}

@Component({
    selector: 'jhi-light-management-measure-wilamp-popup',
    template: '',
})
export class LightManagementMeasureWilampPopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private lightManagementMeasurePopupService: LightManagementMeasureWilampPopupService,
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            if ( params['id'] ) {
                this.lightManagementMeasurePopupService
                    .open(LightManagementMeasureWilampDialogComponent as Component, params['id']);
            } else {
                this.lightManagementMeasurePopupService
                    .open(LightManagementMeasureWilampDialogComponent as Component);
            }
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
