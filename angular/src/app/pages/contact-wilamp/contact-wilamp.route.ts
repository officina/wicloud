import { Routes } from '@angular/router';

import { UserRouteAccessService } from '../../shared';
import { ContactWilampComponent } from './contact-wilamp.component';
import { ContactWilampDetailComponent } from './contact-wilamp-detail.component';
import { ContactWilampPopupComponent } from './contact-wilamp-dialog.component';
import { ContactWilampDeletePopupComponent } from './contact-wilamp-delete-dialog.component';
import {PagesComponent} from '../pages.component';

export const contactRoute: Routes = [
    {
        path: '',
        component: PagesComponent,
        children: [
            {
                path: 'contact-wilamp',
                component: ContactWilampComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.contact.home.title'
                },
                canActivate: [UserRouteAccessService]
            }, {
                path: 'contact-wilamp/:id',
                component: ContactWilampDetailComponent,
                data: {
                    authorities: ['ROLE_USER'],
                    pageTitle: 'wilampCloudApp.contact.home.title'
                },
                canActivate: [UserRouteAccessService]
            }
        ]
    }
];

export const contactPopupRoute: Routes = [
    {
        path: 'contact-wilamp-new',
        component: ContactWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.contact.home.title'
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup'
    },
    {
        path: 'contact-wilamp/:id/edit',
        component: ContactWilampPopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.contact.home.title'
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup'
    },
    {
        path: 'contact-wilamp/:id/delete',
        component: ContactWilampDeletePopupComponent,
        data: {
            authorities: ['ROLE_USER'],
            pageTitle: 'wilampCloudApp.contact.home.title'
        },
        canActivate: [UserRouteAccessService],
        outlet: 'popup'
    }
];
