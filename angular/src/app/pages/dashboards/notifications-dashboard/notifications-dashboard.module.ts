import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { RouterModule } from '@angular/router';
import { LeafletModule } from '@asymmetrik/ngx-leaflet';

import { WiCloudSharedModule } from '../../../shared';

import {AgmCoreModule, GoogleMapsAPIWrapper} from '@agm/core';
import {NotificationsDashboardComponent} from './notifications-dashboard.component';
import {notificationsDashboardRoute} from './notifications-dashboard.route';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faCoffee, faStroopwafel, faCalendar, faPalette } from '@fortawesome/free-solid-svg-icons';
import { faTwitter } from '@fortawesome/free-brands-svg-icons';
import { faArrowAltRight, faLightbulb, faLightbulbOn } from '@fortawesome/pro-light-svg-icons';
// Add an icon to the library for convenient access in other components
// library.add(faCoffee, faStroopwafel, faCalendar, faTwitter, faPalette, faArrowAltRight, faLightbulb, faLightbulbOn);

import { fab } from '@fortawesome/free-brands-svg-icons';
// import { fas } from '@fortawesome/free-solid-svg-icons';
// import { far } from '@fortawesome/free-regular-svg-icons';
// library.add(fas, far);
import { fal } from '@fortawesome/pro-light-svg-icons';
import { far } from '@fortawesome/pro-regular-svg-icons';
import { fas } from '@fortawesome/pro-solid-svg-icons';
library.add(fas, far, fal, fab);

const ENTITY_STATES = [
    ...notificationsDashboardRoute,
];

@NgModule({
    imports: [
        WiCloudSharedModule,
        RouterModule.forChild(ENTITY_STATES),
        LeafletModule,
        FontAwesomeModule,
        AgmCoreModule.forRoot({
            apiKey: 'AIzaSyBV2K_NZJykwOD3gg2WtijUm7zfdPfSOBg',
            libraries: ['places', 'visualization']
        }),
    ],
    declarations: [
        NotificationsDashboardComponent,
    ],
    entryComponents: [
        NotificationsDashboardComponent,
    ],
    providers: [
        GoogleMapsAPIWrapper
    ],
    schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class NotificationsDashboardModule {}
