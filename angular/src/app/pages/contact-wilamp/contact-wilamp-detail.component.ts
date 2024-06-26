import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse } from '@angular/common/http';
import { Subscription } from 'rxjs';
import { JhiEventManager } from 'ng-jhipster';

import { ContactWilamp } from './contact-wilamp.model';
import { ContactWilampService } from './contact-wilamp.service';

@Component({
    selector: 'jhi-contact-wilamp-detail',
    templateUrl: './contact-wilamp-detail.component.html',
})
export class ContactWilampDetailComponent implements OnInit, OnDestroy {

    contact: ContactWilamp;
    private subscription: Subscription;
    private eventSubscriber: Subscription;

    constructor(
        private eventManager: JhiEventManager,
        private contactService: ContactWilampService,
        private route: ActivatedRoute,
    ) {
    }

    ngOnInit() {
        this.subscription = this.route.params.subscribe((params) => {
            this.load(params['id']);
        });
        this.registerChangeInContacts();
    }

    load(id) {
        this.contactService.find(id)
            .subscribe((contactResponse: HttpResponse<ContactWilamp>) => {
                this.contact = contactResponse.body;
            });
    }
    previousState() {
        window.history.back();
    }

    ngOnDestroy() {
        this.subscription.unsubscribe();
        this.eventManager.destroy(this.eventSubscriber);
    }

    registerChangeInContacts() {
        this.eventSubscriber = this.eventManager.subscribe(
            'contactListModification',
            (response) => this.load(this.contact.id),
        );
    }
}
