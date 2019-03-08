import { Routes } from '@angular/router';

import { UserRouteAccessService } from '../../shared';
import { InstallationWilampComponent } from './installation-wilamp.component';
import { InstallationWilampDetailComponent } from './installation-wilamp-detail.component';
import { InstallationWilampPopupComponent } from './installation-wilamp-dialog.component';
import { InstallationWilampDeletePopupComponent } from './installation-wilamp-delete-dialog.component';
import {PagesComponent} from '../pages.component';
import {InstallationWilampDashboardComponent} from './installation-detail-component/installation-wilamp-dashboard.component';

export const installationRoute: Routes = [
    {
        path: '',
        component: PagesComponent,
        children: [
            {
                path: 'installation',
                component: InstallationWilampComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.installation.home.title',
                },
                canActivate: [UserRouteAccessService],
            }, {
                path: 'installation/:id',
                component: InstallationWilampDashboardComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.installation.home.title',
                },
                canActivate: [UserRouteAccessService],
            },
        ],
    },
];

export const installationPopupRoute: Routes = [
    {
        path: 'installation-wilamp-new',
        component: InstallationWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.installation.home.title',
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup',
    },
    {
        path: 'installation-wilamp/:id/edit',
        component: InstallationWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.installation.home.title',
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup',
    },
    {
        path: 'installation-wilamp/:id/delete',
        component: InstallationWilampDeletePopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.installation.home.title',
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup',
    },
];
