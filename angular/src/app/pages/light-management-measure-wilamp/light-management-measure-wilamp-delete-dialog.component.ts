import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager } from 'ng-jhipster';

import { LightManagementMeasureWilamp } from './light-management-measure-wilamp.model';
import { LightManagementMeasureWilampPopupService } from './light-management-measure-wilamp-popup.service';
import { LightManagementMeasureWilampService } from './light-management-measure-wilamp.service';

@Component({
    selector: 'jhi-light-management-measure-wilamp-delete-dialog',
    templateUrl: './light-management-measure-wilamp-delete-dialog.component.html',
})
export class LightManagementMeasureWilampDeleteDialogComponent {

    lightManagementMeasure: LightManagementMeasureWilamp;

    constructor(
        private lightManagementMeasureService: LightManagementMeasureWilampService,
        public activeModal: NgbActiveModal,
        private eventManager: JhiEventManager,
    ) {
    }

    clear() {
        this.activeModal.dismiss('cancel');
    }

    confirmDelete(id: number) {
        this.lightManagementMeasureService.delete(id).subscribe((response) => {
            this.eventManager.broadcast({
                name: 'lightManagementMeasureListModification',
                content: 'Deleted an lightManagementMeasure',
            });
            this.activeModal.dismiss(true);
        });
    }
}

@Component({
    selector: 'jhi-light-management-measure-wilamp-delete-popup',
    template: '',
})
export class LightManagementMeasureWilampDeletePopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private lightManagementMeasurePopupService: LightManagementMeasureWilampPopupService,
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            this.lightManagementMeasurePopupService
                .open(LightManagementMeasureWilampDeleteDialogComponent as Component, params['id']);
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
