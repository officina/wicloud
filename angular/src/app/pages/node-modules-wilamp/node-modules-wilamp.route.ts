import { Routes } from '@angular/router';

import { UserRouteAccessService } from '../../shared';
import { NodeModulesWilampComponent } from './node-modules-wilamp.component';
import { NodeModulesWilampDetailComponent } from './node-modules-wilamp-detail.component';
import { NodeModulesWilampPopupComponent } from './node-modules-wilamp-dialog.component';
import { NodeModulesWilampDeletePopupComponent } from './node-modules-wilamp-delete-dialog.component';
import {PagesComponent} from '../pages.component';

export const nodeModulesRoute: Routes = [
    {
        path: '',
        component: PagesComponent,
        children: [
            {
                path: 'node-modules',
                component: NodeModulesWilampComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.nodeModules.home.title',
                },
                canActivate: [UserRouteAccessService],
            }, {
                path: 'node-modules/:id',
                component: NodeModulesWilampDetailComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.nodeModules.home.title',
                },
                canActivate: [UserRouteAccessService],
            },
        ],
    },
];

export const nodeModulesPopupRoute: Routes = [
    {
        path: 'node-modules-new',
        component: NodeModulesWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.nodeModules.home.title',
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup',
    },
    {
        path: 'node-modules/:id/edit',
        component: NodeModulesWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.nodeModules.home.title',
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup',
    },
    {
        path: 'node-modules/:id/delete',
        component: NodeModulesWilampDeletePopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.nodeModules.home.title',
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup',
    },
];
