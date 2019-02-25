import { Route } from '@angular/router';

import { HomeComponent } from './home.component';
import {PagesComponent} from '../pages.component';

export const HOME_ROUTE: Route = {
    path: '',
    component: PagesComponent,
    children: [
        {
            path: 'home',
            component: HomeComponent,
            data: {
                authorities: [],
                pageTitle: 'home.title',
            },
        },
    ],
};
