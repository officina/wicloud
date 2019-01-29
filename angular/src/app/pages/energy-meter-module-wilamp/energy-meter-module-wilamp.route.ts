import { Routes } from '@angular/router';

import { UserRouteAccessService } from '../../shared';
import { EnergyMeterModuleWilampComponent } from './energy-meter-module-wilamp.component';
import { EnergyMeterModuleWilampDetailComponent } from './energy-meter-module-wilamp-detail.component';
import { EnergyMeterModuleWilampPopupComponent } from './energy-meter-module-wilamp-dialog.component';
import { EnergyMeterModuleWilampDeletePopupComponent } from './energy-meter-module-wilamp-delete-dialog.component';
import {PagesComponent} from '../pages.component';

export const energyMeterModuleRoute: Routes = [
    {
        path: '',
        component: PagesComponent,
        children: [
            {
                path: 'energy-meter-module-wilamp',
                component: EnergyMeterModuleWilampComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.energyMeterModule.home.title'
                },
                canActivate: [UserRouteAccessService]
            }, {
                path: 'energy-meter-module-wilamp/:id',
                component: EnergyMeterModuleWilampDetailComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.energyMeterModule.home.title'
                },
                canActivate: [UserRouteAccessService]
            }
        ]
    }
];

export const energyMeterModulePopupRoute: Routes = [
    {
        path: 'energy-meter-module-wilamp-new',
        component: EnergyMeterModuleWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.energyMeterModule.home.title'
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup'
    },
    {
        path: 'energy-meter-module-wilamp/:id/edit',
        component: EnergyMeterModuleWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.energyMeterModule.home.title'
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup'
    },
    {
        path: 'energy-meter-module-wilamp/:id/delete',
        component: EnergyMeterModuleWilampDeletePopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.energyMeterModule.home.title'
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup'
    }
];
