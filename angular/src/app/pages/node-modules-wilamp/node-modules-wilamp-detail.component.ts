import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse } from '@angular/common/http';
import { Subscription } from 'rxjs';
import { JhiEventManager } from 'ng-jhipster';

import { NodeModulesWilamp } from './node-modules-wilamp.model';
import { NodeModulesWilampService } from './node-modules-wilamp.service';

@Component({
    selector: 'jhi-node-modules-wilamp-detail',
    templateUrl: './node-modules-wilamp-detail.component.html',
})
export class NodeModulesWilampDetailComponent implements OnInit, OnDestroy {

    nodeModules: NodeModulesWilamp;
    private subscription: Subscription;
    private eventSubscriber: Subscription;

    constructor(
        private eventManager: JhiEventManager,
        private nodeModulesService: NodeModulesWilampService,
        private route: ActivatedRoute,
    ) {
    }

    ngOnInit() {
        this.subscription = this.route.params.subscribe((params) => {
            this.load(params['id']);
        });
        this.registerChangeInNodeModules();
    }

    load(id) {
        this.nodeModulesService.find(id)
            .subscribe((nodeModulesResponse: HttpResponse<NodeModulesWilamp>) => {
                this.nodeModules = nodeModulesResponse.body;
            });
    }
    previousState() {
        window.history.back();
    }

    ngOnDestroy() {
        this.subscription.unsubscribe();
        this.eventManager.destroy(this.eventSubscriber);
    }

    registerChangeInNodeModules() {
        this.eventSubscriber = this.eventManager.subscribe(
            'nodeModulesListModification',
            (response) => this.load(this.nodeModules.id),
        );
    }
}
