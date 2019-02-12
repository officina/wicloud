import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager } from 'ng-jhipster';

import { TwilightManagementModuleWilamp } from './twilight-management-module-wilamp.model';
import { TwilightManagementModuleWilampPopupService } from './twilight-management-module-wilamp-popup.service';
import { TwilightManagementModuleWilampService } from './twilight-management-module-wilamp.service';

@Component({
    selector: 'jhi-twilight-management-module-wilamp-delete-dialog',
    templateUrl: './twilight-management-module-wilamp-delete-dialog.component.html'
})
export class TwilightManagementModuleWilampDeleteDialogComponent {

    twilightManagementModule: TwilightManagementModuleWilamp;

    constructor(
        private twilightManagementModuleService: TwilightManagementModuleWilampService,
        public activeModal: NgbActiveModal,
        private eventManager: JhiEventManager
    ) {
    }

    clear() {
        this.activeModal.dismiss('cancel');
    }

    confirmDelete(id: number) {
        this.twilightManagementModuleService.delete(id).subscribe((response) => {
            this.eventManager.broadcast({
                name: 'twilightManagementModuleListModification',
                content: 'Deleted an twilightManagementModule'
            });
            this.activeModal.dismiss(true);
        });
    }
}

@Component({
    selector: 'jhi-twilight-management-module-wilamp-delete-popup',
    template: ''
})
export class TwilightManagementModuleWilampDeletePopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private twilightManagementModulePopupService: TwilightManagementModuleWilampPopupService
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            this.twilightManagementModulePopupService
                .open(TwilightManagementModuleWilampDeleteDialogComponent as Component, params['id']);
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
