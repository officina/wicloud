import { Routes } from '@angular/router';

import { UserRouteAccessService } from '../../../shared';
import {InstallationDashboardComponent} from './installation-dashboard.component';
import {PagesComponent} from '../../pages.component';

export const installationDashboardRoute: Routes = [
    {
        path: '',
        component: PagesComponent,
        children: [
            {
                path: 'global-reports',
                component: InstallationDashboardComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'Dashboard'
                },
                canActivate: [UserRouteAccessService]
            }
        ]
    }
];
