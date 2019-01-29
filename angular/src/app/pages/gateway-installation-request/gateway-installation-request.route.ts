import { Injectable } from '@angular/core';
import { Resolve, ActivatedRouteSnapshot, RouterStateSnapshot, Routes } from '@angular/router';
import { JhiPaginationUtil } from 'ng-jhipster';

import { UserRouteAccessService } from '../../shared';
import { GatewayInstallationRequestComponent } from './gateway-installation-request.component';
import { GatewayInstallationRequestDetailComponent } from './gateway-installation-request-detail.component';
import { GatewayInstallationRequestPopupComponent } from './gateway-installation-request-dialog.component';
import { GatewayInstallationRequestDeletePopupComponent } from './gateway-installation-request-delete-dialog.component';
import {GatewayWilampResolvePagingParams} from '../gateway-wilamp/gateway-wilamp.route';
import {PagesComponent} from '../pages.component';

@Injectable()
export class GatewayInstallationRequestResolvePagingParams implements Resolve<any> {

    constructor(private paginationUtil: JhiPaginationUtil) {}

    resolve(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
        const page = route.queryParams['page'] ? route.queryParams['page'] : '1';
        const sort = route.queryParams['sort'] ? route.queryParams['sort'] : 'id,asc';
        return {
            page: this.paginationUtil.parsePage(page),
            predicate: this.paginationUtil.parsePredicate(sort),
            ascending: this.paginationUtil.parseAscending(sort)
        };
    }
}

export const gatewayInstallationRequestRoute: Routes = [
    {
        path: '',
        component: PagesComponent,
        children: [
            {
                path: 'gateway-installation-request',
                component: GatewayInstallationRequestComponent,
                resolve: {
                    'pagingParams': GatewayInstallationRequestResolvePagingParams
                },
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.gatewayInstallationRequest.home.title'
                },
                canActivate: [UserRouteAccessService]
            }, {
                path: 'gateway-installation-request/:id',
                component: GatewayInstallationRequestDetailComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.gatewayInstallationRequest.home.title'
                },
                canActivate: [UserRouteAccessService]
            }
        ]
    }
];

export const gatewayInstallationRequestPopupRoute: Routes = [
    {
        path: 'gateway-installation-request-new',
        component: GatewayInstallationRequestPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.gatewayInstallationRequest.home.title'
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup'
    },
    {
        path: 'gateway-installation-request/:id/edit',
        component: GatewayInstallationRequestPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.gatewayInstallationRequest.home.title'
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup'
    },
    {
        path: 'gateway-installation-request/:id/delete',
        component: GatewayInstallationRequestDeletePopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.gatewayInstallationRequest.home.title'
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup'
    }
];
