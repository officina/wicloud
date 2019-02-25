import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager } from 'ng-jhipster';

import { LightProfileWilamp } from './light-profile-wilamp.model';
import { LightProfileWilampPopupService } from './light-profile-wilamp-popup.service';
import { LightProfileWilampService } from './light-profile-wilamp.service';

@Component({
    selector: 'jhi-light-profile-wilamp-delete-dialog',
    templateUrl: './light-profile-wilamp-delete-dialog.component.html',
})
export class LightProfileWilampDeleteDialogComponent {

    lightProfile: LightProfileWilamp;

    constructor(
        private lightProfileService: LightProfileWilampService,
        public activeModal: NgbActiveModal,
        private eventManager: JhiEventManager,
    ) {
    }

    clear() {
        this.activeModal.dismiss('cancel');
    }

    confirmDelete(id: number) {
        this.lightProfileService.delete(id).subscribe((response) => {
            this.eventManager.broadcast({
                name: 'lightProfileListModification',
                content: 'Deleted an lightProfile',
            });
            this.activeModal.dismiss(true);
        });
    }
}

@Component({
    selector: 'jhi-light-profile-wilamp-delete-popup',
    template: '',
})
export class LightProfileWilampDeletePopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private lightProfilePopupService: LightProfileWilampPopupService,
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            this.lightProfilePopupService
                .open(LightProfileWilampDeleteDialogComponent as Component, params['id']);
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
