import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse } from '@angular/common/http';
import { Subscription } from 'rxjs';
import { JhiEventManager } from 'ng-jhipster';

import { ShippingWilamp } from './shipping-wilamp.model';
import { ShippingWilampService } from './shipping-wilamp.service';

@Component({
    selector: 'jhi-shipping-wilamp-detail',
    templateUrl: './shipping-wilamp-detail.component.html',
})
export class ShippingWilampDetailComponent implements OnInit, OnDestroy {

    shipping: ShippingWilamp;
    private subscription: Subscription;
    private eventSubscriber: Subscription;

    constructor(
        private eventManager: JhiEventManager,
        private shippingService: ShippingWilampService,
        private route: ActivatedRoute,
    ) {
    }

    ngOnInit() {
        this.subscription = this.route.params.subscribe((params) => {
            this.load(params['id']);
        });
        this.registerChangeInShippings();
    }

    load(id) {
        this.shippingService.find(id)
            .subscribe((shippingResponse: HttpResponse<ShippingWilamp>) => {
                this.shipping = shippingResponse.body;
            });
    }
    previousState() {
        window.history.back();
    }

    ngOnDestroy() {
        this.subscription.unsubscribe();
        this.eventManager.destroy(this.eventSubscriber);
    }

    registerChangeInShippings() {
        this.eventSubscriber = this.eventManager.subscribe(
            'shippingListModification',
            (response) => this.load(this.shipping.id),
        );
    }
}
