import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager } from 'ng-jhipster';

import { GatewayWilamp } from './gateway-wilamp.model';
import { GatewayWilampPopupService } from './gateway-wilamp-popup.service';
import { GatewayWilampService } from './gateway-wilamp.service';

@Component({
    selector: 'jhi-gateway-wilamp-delete-dialog',
    templateUrl: './gateway-wilamp-delete-dialog.component.html'
})
export class GatewayWilampDeleteDialogComponent {

    gateway: GatewayWilamp;

    constructor(
        private gatewayService: GatewayWilampService,
        public activeModal: NgbActiveModal,
        private eventManager: JhiEventManager
    ) {
    }

    clear() {
        this.activeModal.dismiss('cancel');
    }

    confirmDelete(id: number) {
        this.gatewayService.delete(id).subscribe((response) => {
            this.eventManager.broadcast({
                name: 'gatewayListModification',
                content: 'Deleted an gateway'
            });
            this.activeModal.dismiss(true);
        });
    }
}

@Component({
    selector: 'jhi-gateway-wilamp-delete-popup',
    template: ''
})
export class GatewayWilampDeletePopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private gatewayPopupService: GatewayWilampPopupService
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            this.gatewayPopupService
                .open(GatewayWilampDeleteDialogComponent as Component, params['id']);
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
