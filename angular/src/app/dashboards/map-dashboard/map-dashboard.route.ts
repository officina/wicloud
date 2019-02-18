import { Routes } from '@angular/router';

import { UserRouteAccessService } from '../../shared';
import {PagesComponent} from '../../pages/pages.component';
import {MapDashboardComponent} from './map-dashboard.component';

export const mapDashboardRoute: Routes = [
    {
        path: '',
        component: PagesComponent,
        children: [
            {
                path: 'map',
                component: MapDashboardComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'Dashboard'
                },
                canActivate: [UserRouteAccessService]
            }
        ]
    }
];
