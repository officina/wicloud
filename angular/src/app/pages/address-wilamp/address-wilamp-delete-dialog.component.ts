import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager } from 'ng-jhipster';

import { AddressWilamp } from './address-wilamp.model';
import { AddressWilampPopupService } from './address-wilamp-popup.service';
import { AddressWilampService } from './address-wilamp.service';

@Component({
    selector: 'jhi-address-wilamp-delete-dialog',
    templateUrl: './address-wilamp-delete-dialog.component.html',
})
export class AddressWilampDeleteDialogComponent {

    address: AddressWilamp;

    constructor(
        private addressService: AddressWilampService,
        public activeModal: NgbActiveModal,
        private eventManager: JhiEventManager,
    ) {
    }

    clear() {
        this.activeModal.dismiss('cancel');
    }

    confirmDelete(id: number) {
        this.addressService.delete(id).subscribe((response) => {
            this.eventManager.broadcast({
                name: 'addressListModification',
                content: 'Deleted an address',
            });
            this.activeModal.dismiss(true);
        });
    }
}

@Component({
    selector: 'jhi-address-wilamp-delete-popup',
    template: '',
})
export class AddressWilampDeletePopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private addressPopupService: AddressWilampPopupService,
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            this.addressPopupService
                .open(AddressWilampDeleteDialogComponent as Component, params['id']);
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
