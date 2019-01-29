import { Routes } from '@angular/router';

import { UserRouteAccessService } from '../../shared';
import { OrderWilampComponent } from './order-wilamp.component';
import { OrderWilampDetailComponent } from './order-wilamp-detail.component';
import { OrderWilampPopupComponent } from './order-wilamp-dialog.component';
import { OrderWilampDeletePopupComponent } from './order-wilamp-delete-dialog.component';
import {PagesComponent} from '../pages.component';

export const orderRoute: Routes = [
    {
        path: '',
        component: PagesComponent,
        children: [
            {
                path: 'order-wilamp',
                component: OrderWilampComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.order.home.title'
                },
                canActivate: [UserRouteAccessService]
            }, {
                path: 'order-wilamp/:id',
                component: OrderWilampDetailComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.order.home.title'
                },
                canActivate: [UserRouteAccessService]
            }
        ]
    }
];

export const orderPopupRoute: Routes = [
    {
        path: 'order-wilamp-new',
        component: OrderWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.order.home.title'
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup'
    },
    {
        path: 'order-wilamp/:id/edit',
        component: OrderWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.order.home.title'
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup'
    },
    {
        path: 'order-wilamp/:id/delete',
        component: OrderWilampDeletePopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.order.home.title'
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup'
    }
];
