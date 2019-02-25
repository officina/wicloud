import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse } from '@angular/common/http';
import { Subscription } from 'rxjs/Subscription';
import { JhiEventManager } from 'ng-jhipster';

import { LightFixtureWilamp } from './light-fixture-wilamp.model';
import { LightFixtureWilampService } from './light-fixture-wilamp.service';

@Component({
    selector: 'jhi-light-fixture-wilamp-detail',
    templateUrl: './light-fixture-wilamp-detail.component.html',
})
export class LightFixtureWilampDetailComponent implements OnInit, OnDestroy {

    lightFixture: LightFixtureWilamp;
    private subscription: Subscription;
    private eventSubscriber: Subscription;

    constructor(
        private eventManager: JhiEventManager,
        private lightFixtureService: LightFixtureWilampService,
        private route: ActivatedRoute,
    ) {
    }

    ngOnInit() {
        this.subscription = this.route.params.subscribe((params) => {
            this.load(params['id']);
        });
        this.registerChangeInLightFixtures();
    }

    load(id) {
        this.lightFixtureService.find(id)
            .subscribe((lightFixtureResponse: HttpResponse<LightFixtureWilamp>) => {
                this.lightFixture = lightFixtureResponse.body;
            });
    }
    previousState() {
        window.history.back();
    }

    ngOnDestroy() {
        this.subscription.unsubscribe();
        this.eventManager.destroy(this.eventSubscriber);
    }

    registerChangeInLightFixtures() {
        this.eventSubscriber = this.eventManager.subscribe(
            'lightFixtureListModification',
            (response) => this.load(this.lightFixture.id),
        );
    }
}
