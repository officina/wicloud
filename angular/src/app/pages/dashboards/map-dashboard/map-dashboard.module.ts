import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { RouterModule } from '@angular/router';

import { WiCloudSharedModule } from '../../../shared';

import {mapDashboardRoute} from './map-dashboard.route';
import {MapDashboardComponent} from './map-dashboard.component';
import {WidgetsModule} from '../../../widgets/widgets.module';

const ENTITY_STATES = [
    ...mapDashboardRoute,
];

@NgModule({
    imports: [
        WiCloudSharedModule,
        RouterModule.forChild(ENTITY_STATES),
        WidgetsModule,
    ],
    declarations: [
        MapDashboardComponent,
    ],
    entryComponents: [
        MapDashboardComponent,
    ],
    schemas: [CUSTOM_ELEMENTS_SCHEMA],
})
export class MapDashboardModule {}
