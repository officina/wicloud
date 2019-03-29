import { Routes } from '@angular/router';

import { UserRouteAccessService } from '../../shared';
import { LightManagementModuleWilampComponent } from './light-management-module-wilamp.component';
import { LightManagementModuleWilampDetailComponent } from './light-management-module-wilamp-detail.component';
import { LightManagementModuleWilampPopupComponent } from './light-management-module-wilamp-dialog.component';
import { LightManagementModuleWilampDeletePopupComponent } from './light-management-module-wilamp-delete-dialog.component';
import {PagesComponent} from '../pages.component';

export const lightManagementModuleRoute: Routes = [
    {
        path: '',
        component: PagesComponent,
        children: [
            {
                path: 'light-management-module',
                component: LightManagementModuleWilampComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.lightManagementModule.home.title',
                },
                canActivate: [UserRouteAccessService],
            }, {
                path: 'light-management-module/:id',
                component: LightManagementModuleWilampDetailComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.lightManagementModule.home.title',
                },
                canActivate: [UserRouteAccessService],
            },
        ],
    },
];

export const lightManagementModulePopupRoute: Routes = [
    {
        path: 'light-management-module-new',
        component: LightManagementModuleWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.lightManagementModule.home.title',
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup',
    },
    {
        path: 'light-management-module/:id/edit',
        component: LightManagementModuleWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.lightManagementModule.home.title',
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup',
    },
    {
        path: 'light-management-module/:id/delete',
        component: LightManagementModuleWilampDeletePopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.lightManagementModule.home.title',
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup',
    },
];
