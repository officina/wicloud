import { Routes } from '@angular/router';

import { UserRouteAccessService } from '../../shared';
import { AddressWilampComponent } from './address-wilamp.component';
import { AddressWilampDetailComponent } from './address-wilamp-detail.component';
import { AddressWilampPopupComponent } from './address-wilamp-dialog.component';
import { AddressWilampDeletePopupComponent } from './address-wilamp-delete-dialog.component';
import {PagesComponent} from '../pages.component';

export const addressRoute: Routes = [
    {
        path: '',
        component: PagesComponent,
        children: [
            {
                path: 'address',
                component: AddressWilampComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.address.home.title',
                },
                canActivate: [UserRouteAccessService],
            }, {
                path: 'address/:id',
                component: AddressWilampDetailComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.address.home.title',
                },
                canActivate: [UserRouteAccessService],
            },
        ],
    },

];

export const addressPopupRoute: Routes = [
    {
        path: 'address-new',
        component: AddressWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.address.home.title',
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup',
    },
    {
        path: 'address/:id/edit',
        component: AddressWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.address.home.title',
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup',
    },
    {
        path: 'address/:id/delete',
        component: AddressWilampDeletePopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.address.home.title',
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup',
    },
];
