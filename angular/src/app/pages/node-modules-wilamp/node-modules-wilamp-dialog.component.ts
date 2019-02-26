import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse, HttpErrorResponse } from '@angular/common/http';

import { Observable, Subject } from 'rxjs';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager, JhiAlertService } from 'ng-jhipster';

import { NodeModulesWilamp } from './node-modules-wilamp.model';
import { NodeModulesWilampPopupService } from './node-modules-wilamp-popup.service';
import { NodeModulesWilampService } from './node-modules-wilamp.service';
import { LightManagementModuleWilamp } from '../light-management-module-wilamp/light-management-module-wilamp.model';
import { LightManagementModuleWilampService } from '../light-management-module-wilamp/light-management-module-wilamp.service';
import { EnergyMeterModuleWilamp } from '../energy-meter-module-wilamp/energy-meter-module-wilamp.model';
import { EnergyMeterModuleWilampService } from '../energy-meter-module-wilamp/energy-meter-module-wilamp.service';
import { TwilightManagementModuleWilamp } from '../twilight-management-module-wilamp/twilight-management-module-wilamp.model';
import { TwilightManagementModuleWilampService } from '../twilight-management-module-wilamp/twilight-management-module-wilamp.service';
import { MotionManagementModuleWilamp } from '../motion-management-module-wilamp/motion-management-module-wilamp.model';
import { MotionManagementModuleWilampService } from '../motion-management-module-wilamp/motion-management-module-wilamp.service';
import { NodeWilamp } from '../node-wilamp/node-wilamp.model';
import { NodeWilampService } from '../node-wilamp/node-wilamp.service';

@Component({
    selector: 'jhi-node-modules-wilamp-dialog',
    templateUrl: './node-modules-wilamp-dialog.component.html',
})
export class NodeModulesWilampDialogComponent implements OnInit {

    nodeModules: NodeModulesWilamp;
    isSaving: boolean;

    lightmanagements: LightManagementModuleWilamp[];

    energymeters: EnergyMeterModuleWilamp[];

    twilightmanagements: TwilightManagementModuleWilamp[];

    motionmanagements: MotionManagementModuleWilamp[];

    nodes: NodeWilamp[];

    constructor(
        public activeModal: NgbActiveModal,
        private jhiAlertService: JhiAlertService,
        private nodeModulesService: NodeModulesWilampService,
        private lightManagementModuleService: LightManagementModuleWilampService,
        private energyMeterModuleService: EnergyMeterModuleWilampService,
        private twilightManagementModuleService: TwilightManagementModuleWilampService,
        private motionManagementModuleService: MotionManagementModuleWilampService,
        private nodeService: NodeWilampService,
        private eventManager: JhiEventManager,
    ) {
    }

    ngOnInit() {
        this.isSaving = false;
        this.lightManagementModuleService
            .query({filter: 'nodemodules(name)-is-null'})
            .subscribe((res: HttpResponse<LightManagementModuleWilamp[]>) => {
                if (!this.nodeModules.lightManagementId) {
                    this.lightmanagements = res.body;
                } else {
                    this.lightManagementModuleService
                        .find(this.nodeModules.lightManagementId)
                        .subscribe((subRes: HttpResponse<LightManagementModuleWilamp>) => {
                            this.lightmanagements = [subRes.body].concat(res.body);
                        }, (subRes: HttpErrorResponse) => this.onError(subRes.message));
                }
            }, (res: HttpErrorResponse) => this.onError(res.message));
        this.energyMeterModuleService
            .query({filter: 'nodemodules(name)-is-null'})
            .subscribe((res: HttpResponse<EnergyMeterModuleWilamp[]>) => {
                if (!this.nodeModules.energyMeterId) {
                    this.energymeters = res.body;
                } else {
                    this.energyMeterModuleService
                        .find(this.nodeModules.energyMeterId)
                        .subscribe((subRes: HttpResponse<EnergyMeterModuleWilamp>) => {
                            this.energymeters = [subRes.body].concat(res.body);
                        }, (subRes: HttpErrorResponse) => this.onError(subRes.message));
                }
            }, (res: HttpErrorResponse) => this.onError(res.message));
        this.twilightManagementModuleService
            .query({filter: 'nodemodules(name)-is-null'})
            .subscribe((res: HttpResponse<TwilightManagementModuleWilamp[]>) => {
                if (!this.nodeModules.twilightManagementId) {
                    this.twilightmanagements = res.body;
                } else {
                    this.twilightManagementModuleService
                        .find(this.nodeModules.twilightManagementId)
                        .subscribe((subRes: HttpResponse<TwilightManagementModuleWilamp>) => {
                            this.twilightmanagements = [subRes.body].concat(res.body);
                        }, (subRes: HttpErrorResponse) => this.onError(subRes.message));
                }
            }, (res: HttpErrorResponse) => this.onError(res.message));
        this.motionManagementModuleService
            .query({filter: 'nodemodules(name)-is-null'})
            .subscribe((res: HttpResponse<MotionManagementModuleWilamp[]>) => {
                if (!this.nodeModules.motionManagementId) {
                    this.motionmanagements = res.body;
                } else {
                    this.motionManagementModuleService
                        .find(this.nodeModules.motionManagementId)
                        .subscribe((subRes: HttpResponse<MotionManagementModuleWilamp>) => {
                            this.motionmanagements = [subRes.body].concat(res.body);
                        }, (subRes: HttpErrorResponse) => this.onError(subRes.message));
                }
            }, (res: HttpErrorResponse) => this.onError(res.message));
        this.nodeService.query()
            .subscribe((res: HttpResponse<NodeWilamp[]>) => { this.nodes = res.body; }, (res: HttpErrorResponse) => this.onError(res.message));
    }

    clear() {
        this.activeModal.dismiss('cancel');
    }

    save() {
        this.isSaving = true;
        if (this.nodeModules.id !== undefined) {
            this.subscribeToSaveResponse(
                this.nodeModulesService.update(this.nodeModules));
        } else {
            this.subscribeToSaveResponse(
                this.nodeModulesService.create(this.nodeModules));
        }
    }

    private subscribeToSaveResponse(result: Observable<HttpResponse<NodeModulesWilamp>>) {
        result.subscribe((res: HttpResponse<NodeModulesWilamp>) =>
            this.onSaveSuccess(res.body), (res: HttpErrorResponse) => this.onSaveError());
    }

    private onSaveSuccess(result: NodeModulesWilamp) {
        this.eventManager.broadcast({ name: 'nodeModulesListModification', content: 'OK'});
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

    trackEnergyMeterModuleById(index: number, item: EnergyMeterModuleWilamp) {
        return item.id;
    }

    trackTwilightManagementModuleById(index: number, item: TwilightManagementModuleWilamp) {
        return item.id;
    }

    trackMotionManagementModuleById(index: number, item: MotionManagementModuleWilamp) {
        return item.id;
    }

    trackNodeById(index: number, item: NodeWilamp) {
        return item.id;
    }
}

@Component({
    selector: 'jhi-node-modules-wilamp-popup',
    template: '',
})
export class NodeModulesWilampPopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private nodeModulesPopupService: NodeModulesWilampPopupService,
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            if ( params['id'] ) {
                this.nodeModulesPopupService
                    .open(NodeModulesWilampDialogComponent as Component, params['id']);
            } else {
                this.nodeModulesPopupService
                    .open(NodeModulesWilampDialogComponent as Component);
            }
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
