import { Routes } from '@angular/router';

import { UserRouteAccessService } from '../../shared';
import { ShippingWilampComponent } from './shipping-wilamp.component';
import { ShippingWilampDetailComponent } from './shipping-wilamp-detail.component';
import { ShippingWilampPopupComponent } from './shipping-wilamp-dialog.component';
import { ShippingWilampDeletePopupComponent } from './shipping-wilamp-delete-dialog.component';
import {PagesComponent} from '../pages.component';

export const shippingRoute: Routes = [
    {
        path: '',
        component: PagesComponent,
        children: [
            {
                path: 'shipping',
                component: ShippingWilampComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.shipping.home.title',
                },
                canActivate: [UserRouteAccessService],
            }, {
                path: 'shipping/:id',
                component: ShippingWilampDetailComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.shipping.home.title',
                },
                canActivate: [UserRouteAccessService],
            },
        ],
    },
];

export const shippingPopupRoute: Routes = [
    {
        path: 'shipping-new',
        component: ShippingWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.shipping.home.title',
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup',
    },
    {
        path: 'shipping/:id/edit',
        component: ShippingWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.shipping.home.title',
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup',
    },
    {
        path: 'shipping/:id/delete',
        component: ShippingWilampDeletePopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.shipping.home.title',
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup',
    },
];
