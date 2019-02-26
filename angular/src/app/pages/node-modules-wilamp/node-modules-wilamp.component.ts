import { Component, OnInit, OnDestroy } from '@angular/core';
import { HttpResponse, HttpErrorResponse } from '@angular/common/http';
import { ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';
import { JhiEventManager, JhiParseLinks, JhiAlertService } from 'ng-jhipster';

import { NodeModulesWilamp } from './node-modules-wilamp.model';
import { NodeModulesWilampService } from './node-modules-wilamp.service';
import { ITEMS_PER_PAGE, Principal } from '../../shared';

@Component({
    selector: '.m-grid__item.m-grid__item--fluid.m-wrapper.m-content',
    templateUrl: './node-modules-wilamp.component.html',
})
export class NodeModulesWilampComponent implements OnInit, OnDestroy {

    nodeModules: NodeModulesWilamp[];
    currentAccount: any;
    eventSubscriber: Subscription;
    itemsPerPage: number;
    links: any;
    page: any;
    predicate: any;
    queryCount: any;
    reverse: any;
    totalItems: number;
    currentSearch: string;

    constructor(
        private nodeModulesService: NodeModulesWilampService,
        private jhiAlertService: JhiAlertService,
        private eventManager: JhiEventManager,
        private parseLinks: JhiParseLinks,
        private activatedRoute: ActivatedRoute,
        private principal: Principal,
    ) {
        this.nodeModules = [];
        this.itemsPerPage = ITEMS_PER_PAGE;
        this.page = 1;
        this.links = {
            last: 0,
        };
        this.predicate = 'id';
        this.reverse = true;
        this.currentSearch = this.activatedRoute.snapshot && this.activatedRoute.snapshot.params['search'] ?
            this.activatedRoute.snapshot.params['search'] : '';
    }

    loadAll() {
        if (this.currentSearch) {
            this.nodeModulesService.search({
                query: this.currentSearch,
                page: this.page,
                size: this.itemsPerPage,
                sort: this.sort(),
            }).subscribe(
                (res: HttpResponse<NodeModulesWilamp[]>) => this.onSuccess(res.body, res.headers),
                (res: HttpErrorResponse) => this.onError(res.message),
            );
            return;
        }
        this.nodeModulesService.query({
            page: this.page,
            size: this.itemsPerPage,
            sort: this.sort(),
        }).subscribe(
            (res: HttpResponse<NodeModulesWilamp[]>) => this.onSuccess(res.body, res.headers),
            (res: HttpErrorResponse) => this.onError(res.message),
        );
    }

    reset() {
        this.page = 1;
        this.nodeModules = [];
        this.loadAll();
    }

    loadPage(page) {
        this.page = page;
        this.loadAll();
    }

    clear() {
        this.nodeModules = [];
        this.links = {
            last: 0,
        };
        this.page = 1;
        this.predicate = 'id';
        this.reverse = true;
        this.currentSearch = '';
        this.loadAll();
    }

    search(query) {
        if (!query) {
            return this.clear();
        }
        this.nodeModules = [];
        this.links = {
            last: 0,
        };
        this.page = 1;
        this.predicate = '_score';
        this.reverse = false;
        this.currentSearch = query;
        this.loadAll();
    }
    ngOnInit() {
        this.loadAll();
        this.principal.identity().then((account) => {
            this.currentAccount = account;
        });
        this.registerChangeInNodeModules();
    }

    ngOnDestroy() {
        this.eventManager.destroy(this.eventSubscriber);
    }

    trackId(index: number, item: NodeModulesWilamp) {
        return item.id;
    }
    registerChangeInNodeModules() {
        this.eventSubscriber = this.eventManager.subscribe('nodeModulesListModification', (response) => this.reset());
    }

    sort() {
        const result = [this.predicate + ',' + (this.reverse ? 'asc' : 'desc')];
        if (this.predicate !== 'id') {
            result.push('id');
        }
        return result;
    }

    private onSuccess(data, headers) {
        this.links = this.parseLinks.parse(headers.get('link'));
        this.totalItems = headers.get('X-Total-Count');
        for (let i = 0; i < data.length; i++) {
            this.nodeModules.push(data[i]);
        }
    }

    private onError(error) {
        this.jhiAlertService.error(error.message, null, null);
    }
}
