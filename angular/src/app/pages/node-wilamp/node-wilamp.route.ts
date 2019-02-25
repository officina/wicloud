import { Routes } from '@angular/router';

import { UserRouteAccessService } from '../../shared';
import { NodeWilampComponent } from './node-wilamp.component';
import { NodeWilampDetailComponent } from './node-wilamp-detail.component';
import { NodeWilampPopupComponent } from './node-wilamp-dialog.component';
import { NodeWilampDeletePopupComponent } from './node-wilamp-delete-dialog.component';
import {PagesComponent} from '../pages.component';

export const nodeRoute: Routes = [
    {
        path: '',
        component: PagesComponent,
        children: [
            {
                path: 'node-wilamp',
                component: NodeWilampComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.node.home.title',
                },
                canActivate: [UserRouteAccessService],
            }, {
                path: 'node-wilamp/:id',
                component: NodeWilampDetailComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.node.home.title',
                },
                canActivate: [UserRouteAccessService],
            },
        ],
    },
];

export const nodePopupRoute: Routes = [
    {
        path: 'node-wilamp-new',
        component: NodeWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.node.home.title',
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup',
    },
    {
        path: 'node-wilamp/:id/edit',
        component: NodeWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.node.home.title',
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup',
    },
    {
        path: 'node-wilamp/:id/delete',
        component: NodeWilampDeletePopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.node.home.title',
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup',
    },
];
