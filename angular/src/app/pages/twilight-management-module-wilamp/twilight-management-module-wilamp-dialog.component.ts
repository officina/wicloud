import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse, HttpErrorResponse } from '@angular/common/http';

import { Observable, Subject } from 'rxjs';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager, JhiAlertService } from 'ng-jhipster';

import { TwilightManagementModuleWilamp } from './twilight-management-module-wilamp.model';
import { TwilightManagementModuleWilampPopupService } from './twilight-management-module-wilamp-popup.service';
import { TwilightManagementModuleWilampService } from './twilight-management-module-wilamp.service';
import { NodeModulesWilamp } from '../node-modules-wilamp/node-modules-wilamp.model';
import { NodeModulesWilampService } from '../node-modules-wilamp/node-modules-wilamp.service';

@Component({
    selector: 'jhi-twilight-management-module-wilamp-dialog',
    templateUrl: './twilight-management-module-wilamp-dialog.component.html',
})
export class TwilightManagementModuleWilampDialogComponent implements OnInit {

    twilightManagementModule: TwilightManagementModuleWilamp;
    isSaving: boolean;

    nodemodules: NodeModulesWilamp[];

    constructor(
        public activeModal: NgbActiveModal,
        private jhiAlertService: JhiAlertService,
        private twilightManagementModuleService: TwilightManagementModuleWilampService,
        private nodeModulesService: NodeModulesWilampService,
        private eventManager: JhiEventManager,
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
        if (this.twilightManagementModule.id !== undefined) {
            this.subscribeToSaveResponse(
                this.twilightManagementModuleService.update(this.twilightManagementModule));
        } else {
            this.subscribeToSaveResponse(
                this.twilightManagementModuleService.create(this.twilightManagementModule));
        }
    }

    private subscribeToSaveResponse(result: Observable<HttpResponse<TwilightManagementModuleWilamp>>) {
        result.subscribe((res: HttpResponse<TwilightManagementModuleWilamp>) =>
            this.onSaveSuccess(res.body), (res: HttpErrorResponse) => this.onSaveError());
    }

    private onSaveSuccess(result: TwilightManagementModuleWilamp) {
        this.eventManager.broadcast({ name: 'twilightManagementModuleListModification', content: 'OK'});
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
    selector: 'jhi-twilight-management-module-wilamp-popup',
    template: '',
})
export class TwilightManagementModuleWilampPopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private twilightManagementModulePopupService: TwilightManagementModuleWilampPopupService,
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            if ( params['id'] ) {
                this.twilightManagementModulePopupService
                    .open(TwilightManagementModuleWilampDialogComponent as Component, params['id']);
            } else {
                this.twilightManagementModulePopupService
                    .open(TwilightManagementModuleWilampDialogComponent as Component);
            }
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
