import { Routes } from '@angular/router';

import { UserRouteAccessService } from '../../shared';
import { LightManagementMeasureWilampComponent } from './light-management-measure-wilamp.component';
import { LightManagementMeasureWilampDetailComponent } from './light-management-measure-wilamp-detail.component';
import { LightManagementMeasureWilampPopupComponent } from './light-management-measure-wilamp-dialog.component';
import {
    LightManagementMeasureWilampDeletePopupComponent,
} from './light-management-measure-wilamp-delete-dialog.component';
import {PagesComponent} from '../pages.component';

export const lightManagementMeasureRoute: Routes = [
    {
        path: '',
        component: PagesComponent,
        children: [
            {
                path: 'light-management-measure-wilamp',
                component: LightManagementMeasureWilampComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.lightManagementMeasure.home.title',
                },
                canActivate: [UserRouteAccessService],
            }, {
                path: 'light-management-measure-wilamp/:id',
                component: LightManagementMeasureWilampDetailComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.lightManagementMeasure.home.title',
                },
                canActivate: [UserRouteAccessService],
            },
        ],
    },
];

export const lightManagementMeasurePopupRoute: Routes = [
    {
        path: 'light-management-measure-wilamp-new',
        component: LightManagementMeasureWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.lightManagementMeasure.home.title',
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup',
    },
    {
        path: 'light-management-measure-wilamp/:id/edit',
        component: LightManagementMeasureWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.lightManagementMeasure.home.title',
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup',
    },
    {
        path: 'light-management-measure-wilamp/:id/delete',
        component: LightManagementMeasureWilampDeletePopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.lightManagementMeasure.home.title',
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup',
    },
];
