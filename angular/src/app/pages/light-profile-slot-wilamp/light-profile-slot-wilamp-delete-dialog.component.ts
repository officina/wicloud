import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager } from 'ng-jhipster';

import { LightProfileSlotWilamp } from './light-profile-slot-wilamp.model';
import { LightProfileSlotWilampPopupService } from './light-profile-slot-wilamp-popup.service';
import { LightProfileSlotWilampService } from './light-profile-slot-wilamp.service';

@Component({
    selector: 'jhi-light-profile-slot-wilamp-delete-dialog',
    templateUrl: './light-profile-slot-wilamp-delete-dialog.component.html',
})
export class LightProfileSlotWilampDeleteDialogComponent {

    lightProfileSlot: LightProfileSlotWilamp;

    constructor(
        private lightProfileSlotService: LightProfileSlotWilampService,
        public activeModal: NgbActiveModal,
        private eventManager: JhiEventManager,
    ) {
    }

    clear() {
        this.activeModal.dismiss('cancel');
    }

    confirmDelete(id: number) {
        this.lightProfileSlotService.delete(id).subscribe((response) => {
            this.eventManager.broadcast({
                name: 'lightProfileSlotListModification',
                content: 'Deleted an lightProfileSlot',
            });
            this.activeModal.dismiss(true);
        });
    }
}

@Component({
    selector: 'jhi-light-profile-slot-wilamp-delete-popup',
    template: '',
})
export class LightProfileSlotWilampDeletePopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private lightProfileSlotPopupService: LightProfileSlotWilampPopupService,
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            this.lightProfileSlotPopupService
                .open(LightProfileSlotWilampDeleteDialogComponent as Component, params['id']);
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
