import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse, HttpErrorResponse } from '@angular/common/http';

import { Observable, Subject } from 'rxjs';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager, JhiAlertService } from 'ng-jhipster';

import { MotionManagementModuleWilamp } from './motion-management-module-wilamp.model';
import { MotionManagementModuleWilampPopupService } from './motion-management-module-wilamp-popup.service';
import { MotionManagementModuleWilampService } from './motion-management-module-wilamp.service';
import { NodeModulesWilamp, NodeModulesWilampService } from '../node-modules-wilamp';

@Component({
    selector: 'jhi-motion-management-module-wilamp-dialog',
    templateUrl: './motion-management-module-wilamp-dialog.component.html',
})
export class MotionManagementModuleWilampDialogComponent implements OnInit {

    motionManagementModule: MotionManagementModuleWilamp;
    isSaving: boolean;

    nodemodules: NodeModulesWilamp[];

    constructor(
        public activeModal: NgbActiveModal,
        private jhiAlertService: JhiAlertService,
        private motionManagementModuleService: MotionManagementModuleWilampService,
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
        if (this.motionManagementModule.id !== undefined) {
            this.subscribeToSaveResponse(
                this.motionManagementModuleService.update(this.motionManagementModule));
        } else {
            this.subscribeToSaveResponse(
                this.motionManagementModuleService.create(this.motionManagementModule));
        }
    }

    private subscribeToSaveResponse(result: Observable<HttpResponse<MotionManagementModuleWilamp>>) {
        result.subscribe((res: HttpResponse<MotionManagementModuleWilamp>) =>
            this.onSaveSuccess(res.body), (res: HttpErrorResponse) => this.onSaveError());
    }

    private onSaveSuccess(result: MotionManagementModuleWilamp) {
        this.eventManager.broadcast({ name: 'motionManagementModuleListModification', content: 'OK'});
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
    selector: 'jhi-motion-management-module-wilamp-popup',
    template: '',
})
export class MotionManagementModuleWilampPopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private motionManagementModulePopupService: MotionManagementModuleWilampPopupService,
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            if ( params['id'] ) {
                this.motionManagementModulePopupService
                    .open(MotionManagementModuleWilampDialogComponent as Component, params['id']);
            } else {
                this.motionManagementModulePopupService
                    .open(MotionManagementModuleWilampDialogComponent as Component);
            }
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
