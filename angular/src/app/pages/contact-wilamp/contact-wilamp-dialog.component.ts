import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager, JhiAlertService } from 'ng-jhipster';
import { ContactWilamp } from './contact-wilamp.model';
import { ContactWilampPopupService } from './contact-wilamp-popup.service';
import { ContactWilampService } from './contact-wilamp.service';
import { AddressWilamp } from '../address-wilamp/address-wilamp.model';
import { AddressWilampService } from '../address-wilamp/address-wilamp.service';
import { CustomerWilamp } from '../customer-wilamp/customer-wilamp.model';
import { CustomerWilampService } from '../customer-wilamp/customer-wilamp.service';

@Component({
    selector: 'jhi-contact-wilamp-dialog',
    templateUrl: './contact-wilamp-dialog.component.html'
})
export class ContactWilampDialogComponent implements OnInit {

    contact: ContactWilamp;
    isSaving: boolean;

    addresses: AddressWilamp[];

    customers: CustomerWilamp[];

    constructor(
        public activeModal: NgbActiveModal,
        private jhiAlertService: JhiAlertService,
        private contactService: ContactWilampService,
        private addressService: AddressWilampService,
        private customerService: CustomerWilampService,
        private eventManager: JhiEventManager
    ) {
    }

    ngOnInit() {
        this.isSaving = false;
        this.addressService.query()
            .subscribe((res: HttpResponse<AddressWilamp[]>) => { this.addresses = res.body; }, (res: HttpErrorResponse) => this.onError(res.message));
        this.customerService.query()
            .subscribe((res: HttpResponse<CustomerWilamp[]>) => { this.customers = res.body; }, (res: HttpErrorResponse) => this.onError(res.message));
    }

    clear() {
        this.activeModal.dismiss('cancel');
    }

    save() {
        this.isSaving = true;
        if (this.contact.id !== undefined) {
            this.subscribeToSaveResponse(
                this.contactService.update(this.contact));
        } else {
            this.subscribeToSaveResponse(
                this.contactService.create(this.contact));
        }
    }

    private subscribeToSaveResponse(result: Observable<HttpResponse<ContactWilamp>>) {
        result.subscribe((res: HttpResponse<ContactWilamp>) =>
            this.onSaveSuccess(res.body), (res: HttpErrorResponse) => this.onSaveError());
    }

    private onSaveSuccess(result: ContactWilamp) {
        this.eventManager.broadcast({ name: 'contactListModification', content: 'OK'});
        this.isSaving = false;
        this.activeModal.dismiss(result);
    }

    private onSaveError() {
        this.isSaving = false;
    }

    private onError(error: any) {
        this.jhiAlertService.error(error.message, null, null);
    }

    trackAddressById(index: number, item: AddressWilamp) {
        return item.id;
    }

    trackCustomerById(index: number, item: CustomerWilamp) {
        return item.id;
    }

    getSelected(selectedVals: Array<any>, option: any) {
        if (selectedVals) {
            for (let i = 0; i < selectedVals.length; i++) {
                if (option.id === selectedVals[i].id) {
                    return selectedVals[i];
                }
            }
        }
        return option;
    }
}

@Component({
    selector: 'jhi-contact-wilamp-popup',
    template: ''
})
export class ContactWilampPopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private contactPopupService: ContactWilampPopupService
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            if ( params['id'] ) {
                this.contactPopupService
                    .open(ContactWilampDialogComponent as Component, params['id']);
            } else {
                this.contactPopupService
                    .open(ContactWilampDialogComponent as Component);
            }
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
