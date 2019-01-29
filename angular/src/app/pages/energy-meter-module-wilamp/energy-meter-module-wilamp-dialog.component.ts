import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse, HttpErrorResponse } from '@angular/common/http';

import { Observable, Subject } from 'rxjs';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager, JhiAlertService } from 'ng-jhipster';

import { EnergyMeterModuleWilamp } from './energy-meter-module-wilamp.model';
import { EnergyMeterModuleWilampPopupService } from './energy-meter-module-wilamp-popup.service';
import { EnergyMeterModuleWilampService } from './energy-meter-module-wilamp.service';
import { NodeModulesWilamp, NodeModulesWilampService } from '../node-modules-wilamp';

@Component({
    selector: 'jhi-energy-meter-module-wilamp-dialog',
    templateUrl: './energy-meter-module-wilamp-dialog.component.html'
})
export class EnergyMeterModuleWilampDialogComponent implements OnInit {

    energyMeterModule: EnergyMeterModuleWilamp;
    isSaving: boolean;

    nodemodules: NodeModulesWilamp[];

    constructor(
        public activeModal: NgbActiveModal,
        private jhiAlertService: JhiAlertService,
        private energyMeterModuleService: EnergyMeterModuleWilampService,
        private nodeModulesService: NodeModulesWilampService,
        private eventManager: JhiEventManager
    ) {
    }

    ngOnInit() {
        this.isSaving = false;
        this.nodeModulesService.query()
            .subscribe((res: HttpResponse<NodeModulesWilamp[]>) => { this.nodemodules = res.body; }, (res: HttpErrorResponse) => this.onError(res.message));
    }

    clear() {
        this.activeModal.dismiss('cancel');
    }

    save() {
        this.isSaving = true;
        if (this.energyMeterModule.id !== undefined) {
            this.subscribeToSaveResponse(
                this.energyMeterModuleService.update(this.energyMeterModule));
        } else {
            this.subscribeToSaveResponse(
                this.energyMeterModuleService.create(this.energyMeterModule));
        }
    }

    private subscribeToSaveResponse(result: Observable<HttpResponse<EnergyMeterModuleWilamp>>) {
        result.subscribe((res: HttpResponse<EnergyMeterModuleWilamp>) =>
            this.onSaveSuccess(res.body), (res: HttpErrorResponse) => this.onSaveError());
    }

    private onSaveSuccess(result: EnergyMeterModuleWilamp) {
        this.eventManager.broadcast({ name: 'energyMeterModuleListModification', content: 'OK'});
        this.isSaving = false;
        this.activeModal.dismiss(result);
    }

    private onSaveError() {
        this.isSaving = false;
    }

    private onError(error: any) {
        this.jhiAlertService.error(error.message, null, null);
    }

    trackNodeModulesById(index: number, item: NodeModulesWilamp) {
        return item.id;
    }
}

@Component({
    selector: 'jhi-energy-meter-module-wilamp-popup',
    template: ''
})
export class EnergyMeterModuleWilampPopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private energyMeterModulePopupService: EnergyMeterModuleWilampPopupService
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            if ( params['id'] ) {
                this.energyMeterModulePopupService
                    .open(EnergyMeterModuleWilampDialogComponent as Component, params['id']);
            } else {
                this.energyMeterModulePopupService
                    .open(EnergyMeterModuleWilampDialogComponent as Component);
            }
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
