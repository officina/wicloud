import { Routes } from '@angular/router';

import { UserRouteAccessService } from '../../shared';
import { EnergyIntervalComponent } from './energy-interval.component';
import { EnergyIntervalDetailComponent } from './energy-interval-detail.component';
import { EnergyIntervalPopupComponent } from './energy-interval-dialog.component';
import { EnergyIntervalDeletePopupComponent } from './energy-interval-delete-dialog.component';
import {PagesComponent} from '../pages.component';

export const energyIntervalRoute: Routes = [
    {

        path: '',
        component: PagesComponent,
        children: [
            {
                path: 'energy-interval',
                component: EnergyIntervalComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.energyInterval.home.title',
                },
                canActivate: [UserRouteAccessService],
            }, {
                path: 'energy-interval/:id',
                component: EnergyIntervalDetailComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.energyInterval.home.title',
                },
                canActivate: [UserRouteAccessService],
            },
        ],
    },
];

export const energyIntervalPopupRoute: Routes = [
    {
        path: 'energy-interval-new',
        component: EnergyIntervalPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.energyInterval.home.title',
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup',
    },
    {
        path: 'energy-interval/:id/edit',
        component: EnergyIntervalPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.energyInterval.home.title',
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup',
    },
    {
        path: 'energy-interval/:id/delete',
        component: EnergyIntervalDeletePopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.energyInterval.home.title',
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup',
    },
];
