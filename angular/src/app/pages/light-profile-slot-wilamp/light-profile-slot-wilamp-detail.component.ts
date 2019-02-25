import {Component, OnInit, OnDestroy, AfterViewInit} from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse } from '@angular/common/http';
import { Subscription } from 'rxjs';
import { JhiEventManager } from 'ng-jhipster';

import { LightProfileSlotWilamp } from './light-profile-slot-wilamp.model';
import { LightProfileSlotWilampService } from './light-profile-slot-wilamp.service';

@Component({
    selector: 'jhi-light-profile-slot-wilamp-detail',
    templateUrl: './light-profile-slot-wilamp-detail.component.html',
})
export class LightProfileSlotWilampDetailComponent implements OnInit, OnDestroy {

    lightProfileSlot: LightProfileSlotWilamp;
    private subscription: Subscription;
    private eventSubscriber: Subscription;

    constructor(
        private eventManager: JhiEventManager,
        private lightProfileSlotService: LightProfileSlotWilampService,
        private route: ActivatedRoute,
    ) {
    }

    ngOnInit() {
        this.subscription = this.route.params.subscribe((params) => {
            this.load(params['id']);
        });
        this.registerChangeInLightProfileSlots();
    }

    load(id) {
        this.lightProfileSlotService.find(id)
            .subscribe((lightProfileSlotResponse: HttpResponse<LightProfileSlotWilamp>) => {
                this.lightProfileSlot = lightProfileSlotResponse.body;
            });
    }
    previousState() {
        window.history.back();
    }

    ngOnDestroy() {
        this.subscription.unsubscribe();
        this.eventManager.destroy(this.eventSubscriber);
    }

    registerChangeInLightProfileSlots() {
        this.eventSubscriber = this.eventManager.subscribe(
            'lightProfileSlotListModification',
            (response) => this.load(this.lightProfileSlot.id),
        );
    }
}
