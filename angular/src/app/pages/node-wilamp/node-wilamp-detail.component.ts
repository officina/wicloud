import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse } from '@angular/common/http';
import { Subscription } from 'rxjs';
import { JhiEventManager } from 'ng-jhipster';

import { NodeWilamp } from './node-wilamp.model';
import { NodeWilampService } from './node-wilamp.service';

@Component({
    selector: 'jhi-node-wilamp-detail',
    templateUrl: './node-wilamp-detail.component.html'
})
export class NodeWilampDetailComponent implements OnInit, OnDestroy {

    node: NodeWilamp;
    private subscription: Subscription;
    private eventSubscriber: Subscription;

    constructor(
        private eventManager: JhiEventManager,
        private nodeService: NodeWilampService,
        private route: ActivatedRoute
    ) {
    }

    ngOnInit() {
        this.subscription = this.route.params.subscribe((params) => {
            this.load(params['id']);
        });
        this.registerChangeInNodes();
    }

    load(id) {
        this.nodeService.find(id)
            .subscribe((nodeResponse: HttpResponse<NodeWilamp>) => {
                this.node = nodeResponse.body;
            });
    }
    previousState() {
        window.history.back();
    }

    ngOnDestroy() {
        this.subscription.unsubscribe();
        this.eventManager.destroy(this.eventSubscriber);
    }

    registerChangeInNodes() {
        this.eventSubscriber = this.eventManager.subscribe(
            'nodeListModification',
            (response) => this.load(this.node.id)
        );
    }
}
