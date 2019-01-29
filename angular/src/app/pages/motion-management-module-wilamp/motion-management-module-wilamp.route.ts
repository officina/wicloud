import { Routes } from '@angular/router';

import { UserRouteAccessService } from '../../shared';
import { MotionManagementModuleWilampComponent } from './motion-management-module-wilamp.component';
import { MotionManagementModuleWilampDetailComponent } from './motion-management-module-wilamp-detail.component';
import { MotionManagementModuleWilampPopupComponent } from './motion-management-module-wilamp-dialog.component';
import {
    MotionManagementModuleWilampDeletePopupComponent
} from './motion-management-module-wilamp-delete-dialog.component';
import {PagesComponent} from '../pages.component';

export const motionManagementModuleRoute: Routes = [
    {
        path: '',
        component: PagesComponent,
        children: [
            {
                path: 'motion-management-module-wilamp',
                component: MotionManagementModuleWilampComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.motionManagementModule.home.title'
                },
                canActivate: [UserRouteAccessService]
            }, {
                path: 'motion-management-module-wilamp/:id',
                component: MotionManagementModuleWilampDetailComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.motionManagementModule.home.title'
                },
                canActivate: [UserRouteAccessService]
            }
        ]
    }
];

export const motionManagementModulePopupRoute: Routes = [
    {
        path: 'motion-management-module-wilamp-new',
        component: MotionManagementModuleWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.motionManagementModule.home.title'
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup'
    },
    {
        path: 'motion-management-module-wilamp/:id/edit',
        component: MotionManagementModuleWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.motionManagementModule.home.title'
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup'
    },
    {
        path: 'motion-management-module-wilamp/:id/delete',
        component: MotionManagementModuleWilampDeletePopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.motionManagementModule.home.title'
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup'
    }
];
