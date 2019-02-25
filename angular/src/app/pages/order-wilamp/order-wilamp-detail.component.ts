import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse } from '@angular/common/http';
import { Subscription } from 'rxjs';
import { JhiEventManager } from 'ng-jhipster';

import { OrderWilamp } from './order-wilamp.model';
import { OrderWilampService } from './order-wilamp.service';

@Component({
    selector: 'jhi-order-wilamp-detail',
    templateUrl: './order-wilamp-detail.component.html',
})
export class OrderWilampDetailComponent implements OnInit, OnDestroy {

    order: OrderWilamp;
    private subscription: Subscription;
    private eventSubscriber: Subscription;

    constructor(
        private eventManager: JhiEventManager,
        private orderService: OrderWilampService,
        private route: ActivatedRoute,
    ) {
    }

    ngOnInit() {
        this.subscription = this.route.params.subscribe((params) => {
            this.load(params['id']);
        });
        this.registerChangeInOrders();
    }

    load(id) {
        this.orderService.find(id)
            .subscribe((orderResponse: HttpResponse<OrderWilamp>) => {
                this.order = orderResponse.body;
            });
    }
    previousState() {
        window.history.back();
    }

    ngOnDestroy() {
        this.subscription.unsubscribe();
        this.eventManager.destroy(this.eventSubscriber);
    }

    registerChangeInOrders() {
        this.eventSubscriber = this.eventManager.subscribe(
            'orderListModification',
            (response) => this.load(this.order.id),
        );
    }
}
