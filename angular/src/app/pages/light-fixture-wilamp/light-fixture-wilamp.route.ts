import { Routes } from '@angular/router';

import { UserRouteAccessService } from '../../shared';
import { LightFixtureWilampComponent } from './light-fixture-wilamp.component';
import { LightFixtureWilampDetailComponent } from './light-fixture-wilamp-detail.component';
import { LightFixtureWilampPopupComponent } from './light-fixture-wilamp-dialog.component';
import { LightFixtureWilampDeletePopupComponent } from './light-fixture-wilamp-delete-dialog.component';
import {PagesComponent} from '../pages.component';

export const lightFixtureRoute: Routes = [
    {
        path: '',
        component: PagesComponent,
        children: [
            {
                path: 'light-fixture-wilamp',
                component: LightFixtureWilampComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.lightFixture.home.title'
                },
                canActivate: [UserRouteAccessService]
            }, {
                path: 'light-fixture-wilamp/:id',
                component: LightFixtureWilampDetailComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.lightFixture.home.title'
                },
                canActivate: [UserRouteAccessService]
            }
        ]
    }
];


export const lightFixturePopupRoute: Routes = [
    {
        path: 'light-fixture-wilamp-new',
        component: LightFixtureWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.lightFixture.home.title'
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup'
    },
    {
        path: 'light-fixture-wilamp/:id/edit',
        component: LightFixtureWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.lightFixture.home.title'
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup'
    },
    {
        path: 'light-fixture-wilamp/:id/delete',
        component: LightFixtureWilampDeletePopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.lightFixture.home.title'
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup'
    }
];
