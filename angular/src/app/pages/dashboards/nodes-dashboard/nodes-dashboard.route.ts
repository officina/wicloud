import { Routes } from '@angular/router';

import { UserRouteAccessService } from '../../../shared';
import {PagesComponent} from '../../pages.component';
import {NodesDashboardComponent} from './nodes-dashboard.component';

export const nodesDashboardRoute: Routes = [
    {
        path: '',
        component: PagesComponent,
        children: [
            {
                path: 'nodes',
                component: NodesDashboardComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'Dashboard'
                },
                canActivate: [UserRouteAccessService]
            }
        ]
    }
];
