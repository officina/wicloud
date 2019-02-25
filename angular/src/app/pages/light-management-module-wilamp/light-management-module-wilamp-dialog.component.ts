import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse, HttpErrorResponse } from '@angular/common/http';

import { Observable, Subject } from 'rxjs';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager, JhiAlertService } from 'ng-jhipster';

import { LightManagementModuleWilamp } from './light-management-module-wilamp.model';
import { LightManagementModuleWilampService } from './light-management-module-wilamp.service';
import { LightManagementModuleWilampPopupService } from './light-management-module-wilamp-popup.service';
import { NodeModulesWilamp } from '../node-modules-wilamp/node-modules-wilamp.model';
import { NodeModulesWilampService } from '../node-modules-wilamp/node-modules-wilamp.service';

@Component({
    selector: 'jhi-light-management-module-wilamp-dialog',
    templateUrl: './light-management-module-wilamp-dialog.component.html',
})
export class LightManagementModuleWilampDialogComponent implements OnInit {

    lightManagementModule: LightManagementModuleWilamp;
    isSaving: boolean;

    nodemodules: NodeModulesWilamp[];

    constructor(
        public activeModal: NgbActiveModal,
        private jhiAlertService: JhiAlertService,
        private lightManagementModuleService: LightManagementModuleWilampService,
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
        if (this.lightManagementModule.id !== undefined) {
            this.subscribeToSaveResponse(
                this.lightManagementModuleService.update(this.lightManagementModule));
        } else {
            this.subscribeToSaveResponse(
                this.lightManagementModuleService.create(this.lightManagementModule));
        }
    }

    private subscribeToSaveResponse(result: Observable<HttpResponse<LightManagementModuleWilamp>>) {
        result.subscribe((res: HttpResponse<LightManagementModuleWilamp>) =>
            this.onSaveSuccess(res.body), (res: HttpErrorResponse) => this.onSaveError());
    }

    private onSaveSuccess(result: LightManagementModuleWilamp) {
        this.eventManager.broadcast({ name: 'lightManagementModuleListModification', content: 'OK'});
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
    selector: 'jhi-light-management-module-wilamp-popup',
    template: '',
})
export class LightManagementModuleWilampPopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private lightManagementModulePopupService: LightManagementModuleWilampPopupService,
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            if ( params['id'] ) {
                this.lightManagementModulePopupService
                    .open(LightManagementModuleWilampDialogComponent as Component, params['id']);
            } else {
                this.lightManagementModulePopupService
                    .open(LightManagementModuleWilampDialogComponent as Component);
            }
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
