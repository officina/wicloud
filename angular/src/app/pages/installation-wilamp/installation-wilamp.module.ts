import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { RouterModule } from '@angular/router';
import { NbButtonModule } from '@nebular/theme';
import { WiCloudSharedModule } from '../../shared';
import { Ng2SmartTableModule } from 'ng2-smart-table';

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


const ENTITY_STATES = [
    ...installationRoute,
    ...installationPopupRoute,
];

@NgModule({
    imports: [
        WiCloudSharedModule,
        RouterModule.forChild(ENTITY_STATES),
        NbButtonModule,
        Ng2SmartTableModule
    ],
    declarations: [
        InstallationWilampComponent,
        InstallationWilampDetailComponent,
        InstallationWilampDialogComponent,
        InstallationWilampDeleteDialogComponent,
        InstallationWilampPopupComponent,
        InstallationWilampDeletePopupComponent,
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
