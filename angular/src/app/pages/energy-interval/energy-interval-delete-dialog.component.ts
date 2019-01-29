import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager } from 'ng-jhipster';

import { EnergyInterval } from './energy-interval.model';
import { EnergyIntervalPopupService } from './energy-interval-popup.service';
import { EnergyIntervalService } from './energy-interval.service';

@Component({
    selector: 'jhi-energy-interval-delete-dialog',
    templateUrl: './energy-interval-delete-dialog.component.html'
})
export class EnergyIntervalDeleteDialogComponent {

    energyInterval: EnergyInterval;

    constructor(
        private energyIntervalService: EnergyIntervalService,
        public activeModal: NgbActiveModal,
        private eventManager: JhiEventManager
    ) {
    }

    clear() {
        this.activeModal.dismiss('cancel');
    }

    confirmDelete(id: number) {
        this.energyIntervalService.delete(id).subscribe((response) => {
            this.eventManager.broadcast({
                name: 'energyIntervalListModification',
                content: 'Deleted an energyInterval'
            });
            this.activeModal.dismiss(true);
        });
    }
}

@Component({
    selector: 'jhi-energy-interval-delete-popup',
    template: ''
})
export class EnergyIntervalDeletePopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private energyIntervalPopupService: EnergyIntervalPopupService
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            this.energyIntervalPopupService
                .open(EnergyIntervalDeleteDialogComponent as Component, params['id']);
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
