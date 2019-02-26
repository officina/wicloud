import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager } from 'ng-jhipster';

import { GatewayInstallationRequest } from './gateway-installation-request.model';
import { GatewayInstallationRequestPopupService } from './gateway-installation-request-popup.service';
import { GatewayInstallationRequestService } from './gateway-installation-request.service';

@Component({
    selector: 'jhi-gateway-installation-request-delete-dialog',
    templateUrl: './gateway-installation-request-delete-dialog.component.html',
})
export class GatewayInstallationRequestDeleteDialogComponent {

    gatewayInstallationRequest: GatewayInstallationRequest;

    constructor(
        private gatewayInstallationRequestService: GatewayInstallationRequestService,
        public activeModal: NgbActiveModal,
        private eventManager: JhiEventManager,
    ) {
    }

    clear() {
        this.activeModal.dismiss('cancel');
    }

    confirmDelete(id: number) {
        this.gatewayInstallationRequestService.delete(id).subscribe((response) => {
            this.eventManager.broadcast({
                name: 'gatewayInstallationRequestListModification',
                content: 'Deleted an gatewayInstallationRequest',
            });
            this.activeModal.dismiss(true);
        });
    }
}

@Component({
    selector: 'jhi-gateway-installation-request-delete-popup',
    template: '',
})
export class GatewayInstallationRequestDeletePopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private gatewayInstallationRequestPopupService: GatewayInstallationRequestPopupService,
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            this.gatewayInstallationRequestPopupService
                .open(GatewayInstallationRequestDeleteDialogComponent as Component, params['id']);
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
