import { Routes } from '@angular/router';

import { UserRouteAccessService } from '../../shared';
import { LightProfileSlotWilampComponent } from './light-profile-slot-wilamp.component';
import { LightProfileSlotWilampDetailComponent } from './light-profile-slot-wilamp-detail.component';
import { LightProfileSlotWilampPopupComponent } from './light-profile-slot-wilamp-dialog.component';
import { LightProfileSlotWilampDeletePopupComponent } from './light-profile-slot-wilamp-delete-dialog.component';
import {PagesComponent} from '../pages.component';

export const lightProfileSlotRoute: Routes = [
    {
        path: '',
        component: PagesComponent,
        children: [
            {
                path: 'light-profile-slot-wilamp',
                component: LightProfileSlotWilampComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.lightProfileSlot.home.title'
                },
                canActivate: [UserRouteAccessService]
            }, {
                path: 'light-profile-slot-wilamp/:id',
                component: LightProfileSlotWilampDetailComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.lightProfileSlot.home.title'
                },
                canActivate: [UserRouteAccessService]
            }
        ]
    }
];

export const lightProfileSlotPopupRoute: Routes = [
    {
        path: 'light-profile-slot-wilamp-new',
        component: LightProfileSlotWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.lightProfileSlot.home.title'
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup'
    },
    {
        path: 'light-profile-slot-wilamp/:id/edit',
        component: LightProfileSlotWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.lightProfileSlot.home.title'
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup'
    },
    {
        path: 'light-profile-slot-wilamp/:id/delete',
        component: LightProfileSlotWilampDeletePopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.lightProfileSlot.home.title'
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup'
    }
];
