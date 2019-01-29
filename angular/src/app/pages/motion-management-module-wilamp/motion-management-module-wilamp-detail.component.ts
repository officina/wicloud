import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse } from '@angular/common/http';
import { Subscription } from 'rxjs';
import { JhiEventManager } from 'ng-jhipster';

import { MotionManagementModuleWilamp } from './motion-management-module-wilamp.model';
import { MotionManagementModuleWilampService } from './motion-management-module-wilamp.service';

@Component({
    selector: 'jhi-motion-management-module-wilamp-detail',
    templateUrl: './motion-management-module-wilamp-detail.component.html'
})
export class MotionManagementModuleWilampDetailComponent implements OnInit, OnDestroy {

    motionManagementModule: MotionManagementModuleWilamp;
    private subscription: Subscription;
    private eventSubscriber: Subscription;

    constructor(
        private eventManager: JhiEventManager,
        private motionManagementModuleService: MotionManagementModuleWilampService,
        private route: ActivatedRoute
    ) {
    }

    ngOnInit() {
        this.subscription = this.route.params.subscribe((params) => {
            this.load(params['id']);
        });
        this.registerChangeInMotionManagementModules();
    }

    load(id) {
        this.motionManagementModuleService.find(id)
            .subscribe((motionManagementModuleResponse: HttpResponse<MotionManagementModuleWilamp>) => {
                this.motionManagementModule = motionManagementModuleResponse.body;
            });
    }
    previousState() {
        window.history.back();
    }

    ngOnDestroy() {
        this.subscription.unsubscribe();
        this.eventManager.destroy(this.eventSubscriber);
    }

    registerChangeInMotionManagementModules() {
        this.eventSubscriber = this.eventManager.subscribe(
            'motionManagementModuleListModification',
            (response) => this.load(this.motionManagementModule.id)
        );
    }
}
