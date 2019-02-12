import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse } from '@angular/common/http';
import { Subscription } from 'rxjs';
import { JhiEventManager } from 'ng-jhipster';

import { EnergyInterval } from './energy-interval.model';
import { EnergyIntervalService } from './energy-interval.service';

@Component({
    selector: 'jhi-energy-interval-detail',
    templateUrl: './energy-interval-detail.component.html'
})
export class EnergyIntervalDetailComponent implements OnInit, OnDestroy {

    energyInterval: EnergyInterval;
    private subscription: Subscription;
    private eventSubscriber: Subscription;

    constructor(
        private eventManager: JhiEventManager,
        private energyIntervalService: EnergyIntervalService,
        private route: ActivatedRoute
    ) {
    }

    ngOnInit() {
        this.subscription = this.route.params.subscribe((params) => {
            this.load(params['id']);
        });
        this.registerChangeInEnergyIntervals();
    }

    load(id) {
        this.energyIntervalService.find(id)
            .subscribe((energyIntervalResponse: HttpResponse<EnergyInterval>) => {
                this.energyInterval = energyIntervalResponse.body;
            });
    }
    previousState() {
        window.history.back();
    }

    ngOnDestroy() {
        this.subscription.unsubscribe();
        this.eventManager.destroy(this.eventSubscriber);
    }

    registerChangeInEnergyIntervals() {
        this.eventSubscriber = this.eventManager.subscribe(
            'energyIntervalListModification',
            (response) => this.load(this.energyInterval.id)
        );
    }
}
