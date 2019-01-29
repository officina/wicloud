import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager } from 'ng-jhipster';

import { EnergyMeterModuleWilamp } from './energy-meter-module-wilamp.model';
import { EnergyMeterModuleWilampPopupService } from './energy-meter-module-wilamp-popup.service';
import { EnergyMeterModuleWilampService } from './energy-meter-module-wilamp.service';

@Component({
    selector: 'jhi-energy-meter-module-wilamp-delete-dialog',
    templateUrl: './energy-meter-module-wilamp-delete-dialog.component.html'
})
export class EnergyMeterModuleWilampDeleteDialogComponent {

    energyMeterModule: EnergyMeterModuleWilamp;

    constructor(
        private energyMeterModuleService: EnergyMeterModuleWilampService,
        public activeModal: NgbActiveModal,
        private eventManager: JhiEventManager
    ) {
    }

    clear() {
        this.activeModal.dismiss('cancel');
    }

    confirmDelete(id: number) {
        this.energyMeterModuleService.delete(id).subscribe((response) => {
            this.eventManager.broadcast({
                name: 'energyMeterModuleListModification',
                content: 'Deleted an energyMeterModule'
            });
            this.activeModal.dismiss(true);
        });
    }
}

@Component({
    selector: 'jhi-energy-meter-module-wilamp-delete-popup',
    template: ''
})
export class EnergyMeterModuleWilampDeletePopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private energyMeterModulePopupService: EnergyMeterModuleWilampPopupService
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            this.energyMeterModulePopupService
                .open(EnergyMeterModuleWilampDeleteDialogComponent as Component, params['id']);
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
