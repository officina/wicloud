import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse } from '@angular/common/http';
import { Subscription } from 'rxjs';
import { JhiEventManager } from 'ng-jhipster';

import { GatewayInstallationRequest } from './gateway-installation-request.model';
import { GatewayInstallationRequestService } from './gateway-installation-request.service';

@Component({
    selector: 'jhi-gateway-installation-request-detail',
    templateUrl: './gateway-installation-request-detail.component.html'
})
export class GatewayInstallationRequestDetailComponent implements OnInit, OnDestroy {

    gatewayInstallationRequest: GatewayInstallationRequest;
    private subscription: Subscription;
    private eventSubscriber: Subscription;

    constructor(
        private eventManager: JhiEventManager,
        private gatewayInstallationRequestService: GatewayInstallationRequestService,
        private route: ActivatedRoute
    ) {
    }

    ngOnInit() {
        this.subscription = this.route.params.subscribe((params) => {
            this.load(params['id']);
        });
        this.registerChangeInGatewayInstallationRequests();
    }

    load(id) {
        this.gatewayInstallationRequestService.find(id)
            .subscribe((gatewayInstallationRequestResponse: HttpResponse<GatewayInstallationRequest>) => {
                this.gatewayInstallationRequest = gatewayInstallationRequestResponse.body;
            });
    }
    previousState() {
        window.history.back();
    }

    ngOnDestroy() {
        this.subscription.unsubscribe();
        this.eventManager.destroy(this.eventSubscriber);
    }

    registerChangeInGatewayInstallationRequests() {
        this.eventSubscriber = this.eventManager.subscribe(
            'gatewayInstallationRequestListModification',
            (response) => this.load(this.gatewayInstallationRequest.id)
        );
    }
}
