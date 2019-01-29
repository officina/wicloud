import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager } from 'ng-jhipster';

import { ContactWilamp } from './contact-wilamp.model';
import { ContactWilampPopupService } from './contact-wilamp-popup.service';
import { ContactWilampService } from './contact-wilamp.service';

@Component({
    selector: 'jhi-contact-wilamp-delete-dialog',
    templateUrl: './contact-wilamp-delete-dialog.component.html'
})
export class ContactWilampDeleteDialogComponent {

    contact: ContactWilamp;

    constructor(
        private contactService: ContactWilampService,
        public activeModal: NgbActiveModal,
        private eventManager: JhiEventManager
    ) {
    }

    clear() {
        this.activeModal.dismiss('cancel');
    }

    confirmDelete(id: number) {
        this.contactService.delete(id).subscribe((response) => {
            this.eventManager.broadcast({
                name: 'contactListModification',
                content: 'Deleted an contact'
            });
            this.activeModal.dismiss(true);
        });
    }
}

@Component({
    selector: 'jhi-contact-wilamp-delete-popup',
    template: ''
})
export class ContactWilampDeletePopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private contactPopupService: ContactWilampPopupService
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            this.contactPopupService
                .open(ContactWilampDeleteDialogComponent as Component, params['id']);
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
