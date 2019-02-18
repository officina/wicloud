import { Component, OnInit, OnDestroy } from '@angular/core';
import { HttpResponse, HttpErrorResponse } from '@angular/common/http';
import { ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';
import { JhiEventManager, JhiAlertService } from 'ng-jhipster';

import { LightProfileWilamp } from './light-profile-wilamp.model';
import { LightProfileWilampService } from './light-profile-wilamp.service';
import { Principal } from '../../shared';

@Component({
    selector: 'jhi-light-profile-wilamp',
    templateUrl: './light-profile-wilamp.component.html'
})
export class LightProfileWilampComponent implements OnInit, OnDestroy {
lightProfiles: LightProfileWilamp[];
    currentAccount: any;
    eventSubscriber: Subscription;
    currentSearch: string;

    constructor(
        private lightProfileService: LightProfileWilampService,
        private jhiAlertService: JhiAlertService,
        private eventManager: JhiEventManager,
        private activatedRoute: ActivatedRoute,
        private principal: Principal
    ) {
        this.currentSearch = this.activatedRoute.snapshot && this.activatedRoute.snapshot.params['search'] ?
            this.activatedRoute.snapshot.params['search'] : '';
    }

    loadAll() {
        if (this.currentSearch) {
            this.lightProfileService.search({
                query: this.currentSearch,
                }).subscribe(
                    (res: HttpResponse<LightProfileWilamp[]>) => this.lightProfiles = res.body,
                    (res: HttpErrorResponse) => this.onError(res.message)
                );
            return;
       }
        this.lightProfileService.query().subscribe(
            (res: HttpResponse<LightProfileWilamp[]>) => {
                this.lightProfiles = res.body;
                this.currentSearch = '';
            },
            (res: HttpErrorResponse) => this.onError(res.message)
        );
    }

    search(query) {
        if (!query) {
            return this.clear();
        }
        this.currentSearch = query;
        this.loadAll();
    }

    clear() {
        this.currentSearch = '';
        this.loadAll();
    }
    ngOnInit() {
        this.loadAll();
        this.principal.identity().then((account) => {
            this.currentAccount = account;
        });
        this.registerChangeInLightProfiles();
    }

    ngOnDestroy() {
        this.eventManager.destroy(this.eventSubscriber);
    }

    trackId(index: number, item: LightProfileWilamp) {
        return item.id;
    }
    registerChangeInLightProfiles() {
        this.eventSubscriber = this.eventManager.subscribe('lightProfileListModification', (response) => this.loadAll());
    }

    private onError(error) {
        this.jhiAlertService.error(error.message, null, null);
    }
}
