import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse } from '@angular/common/http';
import { Subscription } from 'rxjs';
import { JhiEventManager } from 'ng-jhipster';

import { TwilightManagementModuleWilamp } from './twilight-management-module-wilamp.model';
import { TwilightManagementModuleWilampService } from './twilight-management-module-wilamp.service';

@Component({
    selector: 'jhi-twilight-management-module-wilamp-detail',
    templateUrl: './twilight-management-module-wilamp-detail.component.html'
})
export class TwilightManagementModuleWilampDetailComponent implements OnInit, OnDestroy {

    twilightManagementModule: TwilightManagementModuleWilamp;
    private subscription: Subscription;
    private eventSubscriber: Subscription;

    constructor(
        private eventManager: JhiEventManager,
        private twilightManagementModuleService: TwilightManagementModuleWilampService,
        private route: ActivatedRoute
    ) {
    }

    ngOnInit() {
        this.subscription = this.route.params.subscribe((params) => {
            this.load(params['id']);
        });
        this.registerChangeInTwilightManagementModules();
    }

    load(id) {
        this.twilightManagementModuleService.find(id)
            .subscribe((twilightManagementModuleResponse: HttpResponse<TwilightManagementModuleWilamp>) => {
                this.twilightManagementModule = twilightManagementModuleResponse.body;
            });
    }
    previousState() {
        window.history.back();
    }

    ngOnDestroy() {
        this.subscription.unsubscribe();
        this.eventManager.destroy(this.eventSubscriber);
    }

    registerChangeInTwilightManagementModules() {
        this.eventSubscriber = this.eventManager.subscribe(
            'twilightManagementModuleListModification',
            (response) => this.load(this.twilightManagementModule.id)
        );
    }
}
