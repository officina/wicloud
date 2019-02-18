import { Routes } from '@angular/router';

import { UserRouteAccessService } from '../../shared';
import { LightProfileWilampComponent } from './light-profile-wilamp.component';
import { LightProfileWilampDetailComponent } from './light-profile-wilamp-detail.component';
import { LightProfileWilampPopupComponent } from './light-profile-wilamp-dialog.component';
import { LightProfileWilampDeletePopupComponent } from './light-profile-wilamp-delete-dialog.component';
import {PagesComponent} from '../pages.component';

export const lightProfileRoute: Routes = [
    {
        path: '',
        component: PagesComponent,
        children: [
            {
                path: 'light-profile-wilamp',
                component: LightProfileWilampComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.lightProfile.home.title'
                },
                canActivate: [UserRouteAccessService]
            }, {
                path: 'light-profile-wilamp/:id',
                component: LightProfileWilampDetailComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.lightProfile.home.title'
                },
                canActivate: [UserRouteAccessService]
            }
        ]
    }
];

export const lightProfilePopupRoute: Routes = [
    {
        path: 'light-profile-wilamp-new',
        component: LightProfileWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.lightProfile.home.title'
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup'
    },
    {
        path: 'light-profile-wilamp/:id/edit',
        component: LightProfileWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.lightProfile.home.title'
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup'
    },
    {
        path: 'light-profile-wilamp/:id/delete',
        component: LightProfileWilampDeletePopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.lightProfile.home.title'
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup'
    }
];
