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
import {InstallationWilampWidgetComponent} from './widget/installation-wilamp-widget.component';
import {InstallationWilampListComponent} from './installation-wilamp-list.component';
import {ThemeModule} from "../../@theme/theme.module";
import {LeafletMapWidgetComponent} from "./leaflet-map-widget/leaflet-map-widget.component";
import {LeafletModule} from '@asymmetrik/ngx-leaflet';
import {InstallationWilampDashboardComponent} from "./dashboard/installation-wilamp-dashboard.component";

const ENTITY_STATES = [
    ...installationRoute,
    ...installationPopupRoute,
];

@NgModule({
    imports: [
        ThemeModule,
        LeafletModule,
        WiCloudSharedModule,
        RouterModule.forChild(ENTITY_STATES),
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
        LeafletMapWidgetComponent
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
    ],
    schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class WilampCloudInstallationWilampModule {}
