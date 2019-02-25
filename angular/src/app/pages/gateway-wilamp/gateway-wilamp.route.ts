import { Injectable } from '@angular/core';
import { Resolve, ActivatedRouteSnapshot, RouterStateSnapshot, Routes } from '@angular/router';
import { JhiPaginationUtil } from 'ng-jhipster';

import { UserRouteAccessService } from '../../shared';
import { GatewayWilampComponent } from './gateway-wilamp.component';
import { GatewayWilampDetailComponent } from './gateway-wilamp-detail.component';
import { GatewayWilampPopupComponent } from './gateway-wilamp-dialog.component';
import { GatewayWilampDeletePopupComponent } from './gateway-wilamp-delete-dialog.component';
import {PagesComponent} from '../pages.component';

@Injectable()
export class GatewayWilampResolvePagingParams implements Resolve<any> {

    constructor(private paginationUtil: JhiPaginationUtil) {}

    resolve(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
        const page = route.queryParams['page'] ? route.queryParams['page'] : '1';
        const sort = route.queryParams['sort'] ? route.queryParams['sort'] : 'id,asc';
        return {
            page: this.paginationUtil.parsePage(page),
            predicate: this.paginationUtil.parsePredicate(sort),
            ascending: this.paginationUtil.parseAscending(sort),
      };
    }
}

export const gatewayRoute: Routes = [
    {
        path: '',
        component: PagesComponent,
        children: [
            {
                path: 'gateway-wilamp',
                component: GatewayWilampComponent,
                resolve: {
                    'pagingParams': GatewayWilampResolvePagingParams,
                },
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.gateway.home.title',
                },
                canActivate: [UserRouteAccessService],
            }, {
                path: 'gateway-wilamp/:id',
                component: GatewayWilampDetailComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.gateway.home.title',
                },
                canActivate: [UserRouteAccessService],
            },
        ],
    },
];

export const gatewayPopupRoute: Routes = [
    {
        path: 'gateway-wilamp-new',
        component: GatewayWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.gateway.home.title',
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup',
    },
    {
        path: 'gateway-wilamp/:id/edit',
        component: GatewayWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.gateway.home.title',
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup',
    },
    {
        path: 'gateway-wilamp/:id/delete',
        component: GatewayWilampDeletePopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.gateway.home.title',
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup',
    },
];
