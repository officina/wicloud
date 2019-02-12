import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse } from '@angular/common/http';
import { Subscription } from 'rxjs';
import { JhiEventManager } from 'ng-jhipster';

import { EnergyMeterModuleWilamp } from './energy-meter-module-wilamp.model';
import { EnergyMeterModuleWilampService } from './energy-meter-module-wilamp.service';

@Component({
    selector: 'jhi-energy-meter-module-wilamp-detail',
    templateUrl: './energy-meter-module-wilamp-detail.component.html'
})
export class EnergyMeterModuleWilampDetailComponent implements OnInit, OnDestroy {

    energyMeterModule: EnergyMeterModuleWilamp;
    private subscription: Subscription;
    private eventSubscriber: Subscription;

    constructor(
        private eventManager: JhiEventManager,
        private energyMeterModuleService: EnergyMeterModuleWilampService,
        private route: ActivatedRoute
    ) {
    }

    ngOnInit() {
        this.subscription = this.route.params.subscribe((params) => {
            this.load(params['id']);
        });
        this.registerChangeInEnergyMeterModules();
    }

    load(id) {
        this.energyMeterModuleService.find(id)
            .subscribe((energyMeterModuleResponse: HttpResponse<EnergyMeterModuleWilamp>) => {
                this.energyMeterModule = energyMeterModuleResponse.body;
            });
    }
    previousState() {
        window.history.back();
    }

    ngOnDestroy() {
        this.subscription.unsubscribe();
        this.eventManager.destroy(this.eventSubscriber);
    }

    registerChangeInEnergyMeterModules() {
        this.eventSubscriber = this.eventManager.subscribe(
            'energyMeterModuleListModification',
            (response) => this.load(this.energyMeterModule.id)
        );
    }
}
