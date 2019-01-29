import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse } from '@angular/common/http';
import { Subscription } from 'rxjs';
import { JhiEventManager } from 'ng-jhipster';

import { GatewayWilamp } from './gateway-wilamp.model';
import { GatewayWilampService } from './gateway-wilamp.service';

@Component({
    selector: '.m-grid__item.m-grid__item--fluid.m-wrapper',
    templateUrl: './gateway-wilamp-detail.component.html'
})
export class GatewayWilampDetailComponent implements OnInit, OnDestroy {

    gateway: GatewayWilamp;
    private subscription: Subscription;
    private eventSubscriber: Subscription;

    constructor(
        private eventManager: JhiEventManager,
        private gatewayService: GatewayWilampService,
        private route: ActivatedRoute
    ) {
    }

    ngOnInit() {
        this.subscription = this.route.params.subscribe((params) => {
            this.load(params['id']);
        });
        this.registerChangeInGateways();
    }

    load(id) {
        this.gatewayService.find(id)
            .subscribe((gatewayResponse: HttpResponse<GatewayWilamp>) => {
                this.gateway = gatewayResponse.body;
            });
    }
    previousState() {
        window.history.back();
    }

    ngOnDestroy() {
        this.subscription.unsubscribe();
        this.eventManager.destroy(this.eventSubscriber);
    }

    registerChangeInGateways() {
        this.eventSubscriber = this.eventManager.subscribe(
            'gatewayListModification',
            (response) => this.load(this.gateway.id)
        );
    }
}
