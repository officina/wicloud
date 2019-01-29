import {Component, OnInit, OnDestroy, ViewChild} from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse } from '@angular/common/http';
import { Subscription } from 'rxjs';
import { JhiEventManager } from 'ng-jhipster';

import { CustomerWilamp } from './customer-wilamp.model';
import { CustomerWilampService } from './customer-wilamp.service';

@Component({
    selector: 'jhi-customer-wilamp-detail',
    templateUrl: './customer-wilamp-detail.component.html',
    styleUrls: [ './customer-wilamp.css' ]
})
export class CustomerWilampDetailComponent implements OnInit, OnDestroy {

    customer: CustomerWilamp;
    private subscription: Subscription;
    private eventSubscriber: Subscription;

    // google maps zoom level
    zoom = 8;

    // initial center position for the map
    lat = 51.673858;
    lng = 7.815982;

    constructor(
        private eventManager: JhiEventManager,
        private customerService: CustomerWilampService,
        private route: ActivatedRoute
    ) {
    }

    ngOnInit() {
        this.subscription = this.route.params.subscribe((params) => {
            this.load(params['id']);
        });
        this.registerChangeInCustomers();
    }

    load(id) {
        this.customerService.find(id)
            .subscribe((customerResponse: HttpResponse<CustomerWilamp>) => {
                this.customer = customerResponse.body;
            });
    }
    previousState() {
        window.history.back();
    }

    ngOnDestroy() {
        this.subscription.unsubscribe();
        this.eventManager.destroy(this.eventSubscriber);
    }

    registerChangeInCustomers() {
        this.eventSubscriber = this.eventManager.subscribe(
            'customerListModification',
            (response) => this.load(this.customer.id)
        );
    }
}
