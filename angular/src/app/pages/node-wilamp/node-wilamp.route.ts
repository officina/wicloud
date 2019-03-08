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
                path: 'node',
                component: NodeWilampComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.node.home.title',
                },
                canActivate: [UserRouteAccessService],
            }, {
                path: 'node/:id',
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
        path: 'node-new',
        component: NodeWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.node.home.title',
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup',
    },
    {
        path: 'node/:id/edit',
        component: NodeWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.node.home.title',
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup',
    },
    {
        path: 'node/:id/delete',
        component: NodeWilampDeletePopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.node.home.title',
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup',
    },
];
