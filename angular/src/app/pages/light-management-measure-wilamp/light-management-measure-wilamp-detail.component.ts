import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse } from '@angular/common/http';
import { Subscription } from 'rxjs';
import { JhiEventManager } from 'ng-jhipster';

import { LightManagementMeasureWilamp } from './light-management-measure-wilamp.model';
import { LightManagementMeasureWilampService } from './light-management-measure-wilamp.service';

@Component({
    selector: 'jhi-light-management-measure-wilamp-detail',
    templateUrl: './light-management-measure-wilamp-detail.component.html'
})
export class LightManagementMeasureWilampDetailComponent implements OnInit, OnDestroy {

    lightManagementMeasure: LightManagementMeasureWilamp;
    private subscription: Subscription;
    private eventSubscriber: Subscription;

    constructor(
        private eventManager: JhiEventManager,
        private lightManagementMeasureService: LightManagementMeasureWilampService,
        private route: ActivatedRoute
    ) {
    }

    ngOnInit() {
        this.subscription = this.route.params.subscribe((params) => {
            this.load(params['id']);
        });
        this.registerChangeInLightManagementMeasures();
    }

    load(id) {
        this.lightManagementMeasureService.find(id)
            .subscribe((lightManagementMeasureResponse: HttpResponse<LightManagementMeasureWilamp>) => {
                this.lightManagementMeasure = lightManagementMeasureResponse.body;
            });
    }
    previousState() {
        window.history.back();
    }

    ngOnDestroy() {
        this.subscription.unsubscribe();
        this.eventManager.destroy(this.eventSubscriber);
    }

    registerChangeInLightManagementMeasures() {
        this.eventSubscriber = this.eventManager.subscribe(
            'lightManagementMeasureListModification',
            (response) => this.load(this.lightManagementMeasure.id)
        );
    }
}
