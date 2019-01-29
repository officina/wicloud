import { Routes } from '@angular/router';

import { UserRouteAccessService } from '../../shared';
import { CustomerWilampComponent } from './customer-wilamp.component';
import { CustomerWilampDetailComponent } from './customer-wilamp-detail.component';
import { CustomerWilampPopupComponent } from './customer-wilamp-dialog.component';
import { CustomerWilampDeletePopupComponent } from './customer-wilamp-delete-dialog.component';
import {PagesComponent} from '../pages.component';


export const customerRoute: Routes = [
    {
        path: '',
        component: PagesComponent,
        children: [
            {
                path: 'customer-wilamp',
                component: CustomerWilampComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.customer.home.title'
                },
                canActivate: [UserRouteAccessService]
            }, {
                path: 'customer-wilamp/:id',
                component: CustomerWilampDetailComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.customer.home.title'
                },
                canActivate: [UserRouteAccessService]
            }
        ]
    }
];

export const customerPopupRoute: Routes = [
    {
        path: 'customer-wilamp-new',
        component: CustomerWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.customer.home.title'
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup'
    },
    {
        path: 'customer-wilamp/:id/edit',
        component: CustomerWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.customer.home.title'
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup'
    },
    {
        path: 'customer-wilamp/:id/delete',
        component: CustomerWilampDeletePopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.customer.home.title'
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup'
    }
];
