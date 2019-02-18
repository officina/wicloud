import { Routes } from '@angular/router';

import { UserRouteAccessService } from '../../shared';
import {PagesComponent} from '../../pages/pages.component';
import {NotificationsDashboardComponent} from './notifications-dashboard.component';

export const notificationsDashboardRoute: Routes = [
    {
        path: '',
        component: PagesComponent,
        children: [
            {
                path: 'notifications',
                component: NotificationsDashboardComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'Dashboard'
                },
                canActivate: [UserRouteAccessService]
            }
        ]
    }
];
