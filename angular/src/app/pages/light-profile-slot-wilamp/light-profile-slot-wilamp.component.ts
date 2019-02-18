import { Component, OnInit, OnDestroy } from '@angular/core';
import { HttpResponse, HttpErrorResponse } from '@angular/common/http';
import { ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';
import { JhiEventManager, JhiAlertService } from 'ng-jhipster';

import { LightProfileSlotWilamp } from './light-profile-slot-wilamp.model';
import { LightProfileSlotWilampService } from './light-profile-slot-wilamp.service';
import { Principal } from '../../shared';

@Component({
    selector: 'jhi-light-profile-slot-wilamp',
    templateUrl: './light-profile-slot-wilamp.component.html'
})
export class LightProfileSlotWilampComponent implements OnInit, OnDestroy {
lightProfileSlots: LightProfileSlotWilamp[];
    currentAccount: any;
    eventSubscriber: Subscription;
    currentSearch: string;

    constructor(
        private lightProfileSlotService: LightProfileSlotWilampService,
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
            this.lightProfileSlotService.search({
                query: this.currentSearch,
                }).subscribe(
                    (res: HttpResponse<LightProfileSlotWilamp[]>) => this.lightProfileSlots = res.body,
                    (res: HttpErrorResponse) => this.onError(res.message)
                );
            return;
       }
        this.lightProfileSlotService.query().subscribe(
            (res: HttpResponse<LightProfileSlotWilamp[]>) => {
                this.lightProfileSlots = res.body;
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
        this.registerChangeInLightProfileSlots();
    }

    ngOnDestroy() {
        this.eventManager.destroy(this.eventSubscriber);
    }

    trackId(index: number, item: LightProfileSlotWilamp) {
        return item.id;
    }
    registerChangeInLightProfileSlots() {
        this.eventSubscriber = this.eventManager.subscribe('lightProfileSlotListModification', (response) => this.loadAll());
    }

    private onError(error) {
        this.jhiAlertService.error(error.message, null, null);
    }
}
