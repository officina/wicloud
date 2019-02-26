import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager } from 'ng-jhipster';

import { MotionManagementModuleWilamp } from './motion-management-module-wilamp.model';
import { MotionManagementModuleWilampPopupService } from './motion-management-module-wilamp-popup.service';
import { MotionManagementModuleWilampService } from './motion-management-module-wilamp.service';

@Component({
    selector: 'jhi-motion-management-module-wilamp-delete-dialog',
    templateUrl: './motion-management-module-wilamp-delete-dialog.component.html',
})
export class MotionManagementModuleWilampDeleteDialogComponent {

    motionManagementModule: MotionManagementModuleWilamp;

    constructor(
        private motionManagementModuleService: MotionManagementModuleWilampService,
        public activeModal: NgbActiveModal,
        private eventManager: JhiEventManager,
    ) {
    }

    clear() {
        this.activeModal.dismiss('cancel');
    }

    confirmDelete(id: number) {
        this.motionManagementModuleService.delete(id).subscribe((response) => {
            this.eventManager.broadcast({
                name: 'motionManagementModuleListModification',
                content: 'Deleted an motionManagementModule',
            });
            this.activeModal.dismiss(true);
        });
    }
}

@Component({
    selector: 'jhi-motion-management-module-wilamp-delete-popup',
    template: '',
})
export class MotionManagementModuleWilampDeletePopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private motionManagementModulePopupService: MotionManagementModuleWilampPopupService,
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            this.motionManagementModulePopupService
                .open(MotionManagementModuleWilampDeleteDialogComponent as Component, params['id']);
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
