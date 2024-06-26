import { Component, OnInit, OnDestroy } from '@angular/core';
import { HttpResponse, HttpErrorResponse } from '@angular/common/http';
import { ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';
import { JhiEventManager, JhiParseLinks, JhiAlertService } from 'ng-jhipster';

import { NodeWilamp } from './node-wilamp.model';
import { NodeWilampService } from './node-wilamp.service';
import { ITEMS_PER_PAGE, Principal } from '../../shared';
import {TranslateService} from '@ngx-translate/core';

@Component({
    selector: '.m-grid__item.m-grid__item--fluid.m-wrapper.m-content',
    templateUrl: './node-wilamp.component.html',
})
export class NodeWilampComponent implements OnInit, OnDestroy {

    nodes: NodeWilamp[];
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
    tableSettings: any;
    data: any;

    constructor(
        private nodeService: NodeWilampService,
        private jhiAlertService: JhiAlertService,
        private eventManager: JhiEventManager,
        private parseLinks: JhiParseLinks,
        private activatedRoute: ActivatedRoute,
        private principal: Principal,
        private translateService: TranslateService,
    ) {

        this.nodes = [];
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
            this.nodeService.search({
                query: this.currentSearch,
                page: this.page,
                size: this.itemsPerPage,
                sort: this.sort(),
            }).subscribe(
                (res: HttpResponse<NodeWilamp[]>) => this.onSuccess(res.body, res.headers),
                (res: HttpErrorResponse) => this.onError(res.message),
            );
            return;
        }
        this.nodeService.query({
            page: this.page,
            size: this.itemsPerPage,
            sort: this.sort(),
        }).subscribe(
            (res: HttpResponse<NodeWilamp[]>) => this.onSuccess(res.body, res.headers),
            (res: HttpErrorResponse) => this.onError(res.message),
        );
    }

    reset() {
        this.page = 1;
        this.nodes = [];
        this.loadAll();
    }

    loadPage(page) {
        this.page = page;
        this.loadAll();
    }

    clear() {
        this.nodes = [];
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
        this.nodes = [];
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
        this.registerChangeInNodes();
        // questo garantisce di aver caricato il translate json
        this.translateService.get('global.field.id').subscribe((translated: string) => {
            this.tableSettings = {
                pager: {
                    perPage: 20,
                },
                hideSubHeader: true,
                actions: {
                    add: false,
                    edit: true,
                    delete: true,
                },
                edit: {
                    editButtonContent: '<i class="nb-edit"></i>',
                    saveButtonContent: '<i class="nb-checkmark"></i>',
                    cancelButtonContent: '<i class="nb-close"></i>',
                },
                delete: {
                    deleteButtonContent: '<i class="nb-trash"></i>',
                    confirmDelete: true,
                },
                columns: {
                    id: {
                        title: this.translateService.instant('global.field.id'),
                    },
                    name: {
                        title: this.translateService.instant('node.name'),
                    },
                    description: {
                        title: this.translateService.instant('node.description'),
                    },
                    nodeType: {
                        title: this.translateService.instant('node.nodeType'),
                    },
                    mac: {
                        title: this.translateService.instant('node.mac'),
                    },
                },
            };
        });
    }

    ngOnDestroy() {
        this.eventManager.destroy(this.eventSubscriber);
    }

    trackId(index: number, item: NodeWilamp) {
        return item.id;
    }
    registerChangeInNodes() {
        this.eventSubscriber = this.eventManager.subscribe('nodeListModification', (response) => this.reset());
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
            this.nodes.push(data[i]);
        }
        this.data = this.nodes;
    }

    private onError(error) {
        this.jhiAlertService.error(error.message, null, null);
    }
}
