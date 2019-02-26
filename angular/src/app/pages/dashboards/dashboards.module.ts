import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import {InstallationDashboardModule} from './installation-dashboard/installation-dashboard.module';
import { MapDashboardComponent } from './map-dashboard/map-dashboard.component';
import { NotificationsDashboardComponent } from './notifications-dashboard/notifications-dashboard.component';
import { NodesDashboardComponent } from './nodes-dashboard/nodes-dashboard.component';
import {MapDashboardModule} from './map-dashboard/map-dashboard.module';
import {NodesDashboardModule} from './nodes-dashboard/nodes-dashboard.module';
import {NotificationsDashboardModule} from './notifications-dashboard/notifications-dashboard.module';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import {WidgetsModule} from '../../widgets/widgets.module';

@NgModule({
    imports: [
        InstallationDashboardModule,
        /*MapDashboardModule,
        NodesDashboardModule,
        NotificationsDashboardModule,*/
        WidgetsModule,
        /* jhipster-needle-add-entity-module - JHipster will add entity modules here */
    ],
    declarations: [
    ],
    entryComponents: [],
    providers: [
        WidgetsModule,
    ],
    schemas: [CUSTOM_ELEMENTS_SCHEMA],
})
export class DashboardsModule {}
