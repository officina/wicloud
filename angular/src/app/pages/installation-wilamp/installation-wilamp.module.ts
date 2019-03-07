import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { RouterModule } from '@angular/router';

import { WiCloudSharedModule } from '../../shared';
import {
    InstallationWilampService,
    InstallationWilampPopupService,
    InstallationWilampComponent,
    InstallationWilampDetailComponent,
    InstallationWilampDialogComponent,
    InstallationWilampPopupComponent,
    InstallationWilampDeletePopupComponent,
    InstallationWilampDeleteDialogComponent,
    installationRoute,
    installationPopupRoute,
} from './';
import {InstallationWilampWidgetComponent} from './installation-wilamp-widget/installation-wilamp-widget.component';
import {InstallationWilampListComponent} from './installation-wilamp-list.component';
import {ThemeModule} from '../../@theme/theme.module';
import {LeafletMapWidgetComponent} from './leaflet-map-widget/leaflet-map-widget.component';
import {LeafletModule} from '@asymmetrik/ngx-leaflet';
import {InstallationWilampDashboardComponent} from './installation-detail-component/installation-wilamp-dashboard.component';
import {InstallationStatusCardComponent} from './installation-status-card/installation-status-card.component';
import {WidgetsModule} from '../../widgets/widgets.module';
import {InstallationLightFixtureListComponent} from './installation-light-fixture-list-widget/installation-light-fixture-list.component';
import {Ng2SmartTableModule} from 'ng2-smart-table';
import {HTTP_INTERCEPTORS} from '@angular/common/http';
import {NbAuthJWTInterceptor} from '@nebular/auth';  // TODO: AT wait for bug https://github.com/akveo/ng2-smart-table/issues/892"
import {InstallationSmallMapWidgetComponent} from './installation-small-map-widget/installation-small-map-widget.component';

const ENTITY_STATES = [
    ...installationRoute,
    ...installationPopupRoute,
];

@NgModule({
    imports: [
        Ng2SmartTableModule,
        ThemeModule,
        LeafletModule,
        WiCloudSharedModule,
        RouterModule.forChild(ENTITY_STATES),
        WidgetsModule,
    ],
    declarations: [
        InstallationWilampComponent,
        InstallationWilampListComponent,
        InstallationWilampDetailComponent,
        InstallationWilampDialogComponent,
        InstallationWilampDeleteDialogComponent,
        InstallationWilampPopupComponent,
        InstallationWilampDeletePopupComponent,
        InstallationWilampWidgetComponent,
        InstallationWilampDashboardComponent,
        LeafletMapWidgetComponent,
        InstallationStatusCardComponent,
        InstallationLightFixtureListComponent,
        InstallationSmallMapWidgetComponent,
    ],
    entryComponents: [
        InstallationWilampComponent,
        InstallationWilampDialogComponent,
        InstallationWilampPopupComponent,
        InstallationWilampDeleteDialogComponent,
        InstallationWilampDeletePopupComponent,
    ],
    providers: [
        InstallationWilampService,
        InstallationWilampPopupService,
        { provide: HTTP_INTERCEPTORS, useClass: NbAuthJWTInterceptor, multi: true}, // TODO: AT è una porcata ma c'è un bug con gli interceptors importando NG2SmartTable

    ],
    schemas: [CUSTOM_ELEMENTS_SCHEMA],
})
export class WilampCloudInstallationWilampModule {}
