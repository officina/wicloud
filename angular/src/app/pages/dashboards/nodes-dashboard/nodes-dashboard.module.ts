import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { RouterModule } from '@angular/router';

import { WiCloudSharedModule } from '../../../shared';
import {NodesDashboardComponent} from './nodes-dashboard.component';
import {nodesDashboardRoute} from './nodes-dashboard.route';
import {NodeSmallWidgetComponent} from '../../../widgets/node-small-widget/node-small-widget.component';
import {WidgetsModule} from '../../../widgets/widgets.module';

const ENTITY_STATES = [
    ...nodesDashboardRoute,
];

@NgModule({
    imports: [
        WiCloudSharedModule,
        RouterModule.forChild(ENTITY_STATES),
        WidgetsModule,
    ],
    declarations: [
        NodesDashboardComponent,
    ],
    entryComponents: [
        NodesDashboardComponent,
    ],
    providers: [
    ],
    schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class NodesDashboardModule {}
