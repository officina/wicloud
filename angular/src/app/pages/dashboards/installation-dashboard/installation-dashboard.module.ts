import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { RouterModule } from '@angular/router';

import { WiCloudSharedModule } from '../../../shared';

import {installationDashboardRoute} from './installation-dashboard.route';
import {InstallationDashboardComponent} from './installation-dashboard.component';
import {TimeAgoPipe} from 'time-ago-pipe';
import {PanelChartWidgetComponent} from '../../../widgets/panel-chart-widget/panel-chart-widget.component';
import {WidgetsModule} from '../../../widgets/widgets.module';

const ENTITY_STATES = [
    ...installationDashboardRoute,
];

@NgModule({
    imports: [
        WiCloudSharedModule,
        RouterModule.forChild(ENTITY_STATES),
        WidgetsModule,
    ],
    declarations: [
        InstallationDashboardComponent,
        TimeAgoPipe,
        PanelChartWidgetComponent,
    ],
    entryComponents: [
        InstallationDashboardComponent,
    ],
    providers: [
    ],
    schemas: [CUSTOM_ELEMENTS_SCHEMA],
})
export class InstallationDashboardModule {}
