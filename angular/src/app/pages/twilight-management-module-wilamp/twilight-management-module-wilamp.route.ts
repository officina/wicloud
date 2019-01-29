import { Routes } from '@angular/router';

import { UserRouteAccessService } from '../../shared';
import { TwilightManagementModuleWilampComponent } from './twilight-management-module-wilamp.component';
import { TwilightManagementModuleWilampDetailComponent } from './twilight-management-module-wilamp-detail.component';
import { TwilightManagementModuleWilampPopupComponent } from './twilight-management-module-wilamp-dialog.component';
import {
    TwilightManagementModuleWilampDeletePopupComponent
} from './twilight-management-module-wilamp-delete-dialog.component';
import {PagesComponent} from '../pages.component';

export const twilightManagementModuleRoute: Routes = [
    {
        path: '',
        component: PagesComponent,
        children: [
            {
                path: 'twilight-management-module-wilamp',
                component: TwilightManagementModuleWilampComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.twilightManagementModule.home.title'
                },
                canActivate: [UserRouteAccessService]
            }, {
                path: 'twilight-management-module-wilamp/:id',
                component: TwilightManagementModuleWilampDetailComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.twilightManagementModule.home.title'
                },
                canActivate: [UserRouteAccessService]
            }
        ]
    }
];

export const twilightManagementModulePopupRoute: Routes = [
    {
        path: 'twilight-management-module-wilamp-new',
        component: TwilightManagementModuleWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.twilightManagementModule.home.title'
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup'
    },
    {
        path: 'twilight-management-module-wilamp/:id/edit',
        component: TwilightManagementModuleWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.twilightManagementModule.home.title'
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup'
    },
    {
        path: 'twilight-management-module-wilamp/:id/delete',
        component: TwilightManagementModuleWilampDeletePopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.twilightManagementModule.home.title'
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup'
    }
];
