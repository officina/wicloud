import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager } from 'ng-jhipster';

import { LightManagementModuleWilamp } from './light-management-module-wilamp.model';
import { LightManagementModuleWilampPopupService } from './light-management-module-wilamp-popup.service';
import { LightManagementModuleWilampService } from './light-management-module-wilamp.service';

@Component({
    selector: 'jhi-light-management-module-wilamp-delete-dialog',
    templateUrl: './light-management-module-wilamp-delete-dialog.component.html'
})
export class LightManagementModuleWilampDeleteDialogComponent {

    lightManagementModule: LightManagementModuleWilamp;

    constructor(
        private lightManagementModuleService: LightManagementModuleWilampService,
        public activeModal: NgbActiveModal,
        private eventManager: JhiEventManager
    ) {
    }

    clear() {
        this.activeModal.dismiss('cancel');
    }

    confirmDelete(id: number) {
        this.lightManagementModuleService.delete(id).subscribe((response) => {
            this.eventManager.broadcast({
                name: 'lightManagementModuleListModification',
                content: 'Deleted an lightManagementModule'
            });
            this.activeModal.dismiss(true);
        });
    }
}

@Component({
    selector: 'jhi-light-management-module-wilamp-delete-popup',
    template: ''
})
export class LightManagementModuleWilampDeletePopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private lightManagementModulePopupService: LightManagementModuleWilampPopupService
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            this.lightManagementModulePopupService
                .open(LightManagementModuleWilampDeleteDialogComponent as Component, params['id']);
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
