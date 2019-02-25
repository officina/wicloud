import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager } from 'ng-jhipster';

import { InstallationWilamp } from './installation-wilamp.model';
import { InstallationWilampPopupService } from './installation-wilamp-popup.service';
import { InstallationWilampService } from './installation-wilamp.service';

@Component({
    selector: 'jhi-installation-wilamp-delete-dialog',
    templateUrl: './installation-wilamp-delete-dialog.component.html',
})
export class InstallationWilampDeleteDialogComponent {

    installation: InstallationWilamp;

    constructor(
        private installationService: InstallationWilampService,
        public activeModal: NgbActiveModal,
        private eventManager: JhiEventManager,
    ) {
    }

    clear() {
        this.activeModal.dismiss('cancel');
    }

    confirmDelete(id: number) {
        this.installationService.delete(id).subscribe((response) => {
            this.eventManager.broadcast({
                name: 'installationListModification',
                content: 'Deleted an installation',
            });
            this.activeModal.dismiss(true);
        });
    }
}

@Component({
    selector: 'jhi-installation-wilamp-delete-popup',
    template: '',
})
export class InstallationWilampDeletePopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private installationPopupService: InstallationWilampPopupService,
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            this.installationPopupService
                .open(InstallationWilampDeleteDialogComponent as Component, params['id']);
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
