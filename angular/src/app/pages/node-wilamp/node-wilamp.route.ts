import { Routes } from '@angular/router';

import { UserRouteAccessService } from '../../shared';
import { NodeWilampComponent } from './node-wilamp.component';
import { NodeWilampDetailComponent } from './node-wilamp-detail.component';
import {NodeWilampDialogComponent, NodeWilampPopupComponent} from './node-wilamp-dialog.component';
import { NodeWilampDeletePopupComponent } from './node-wilamp-delete-dialog.component';
import {PagesComponent} from '../pages.component';

export const nodeRoute: Routes = [
    {
        path: 'node',
        component: PagesComponent,
        children: [
            {
                path: '',
                component: NodeWilampComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.node.home.title',
                },
                canActivate: [UserRouteAccessService],
            }, {
                path: 'add',
                component: NodeWilampDialogComponent,
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
        component: NodeWilampDialogComponent,
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
