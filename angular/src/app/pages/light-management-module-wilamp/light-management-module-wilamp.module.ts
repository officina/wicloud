import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { RouterModule } from '@angular/router';

import { WiCloudSharedModule } from '../../shared';
import {
    LightManagementModuleWilampService,
    LightManagementModuleWilampPopupService,
    LightManagementModuleWilampComponent,
    LightManagementModuleWilampDetailComponent,
    LightManagementModuleWilampDialogComponent,
    LightManagementModuleWilampPopupComponent,
    LightManagementModuleWilampDeletePopupComponent,
    LightManagementModuleWilampDeleteDialogComponent,
    lightManagementModuleRoute,
    lightManagementModulePopupRoute,
} from './';

const ENTITY_STATES = [
    ...lightManagementModuleRoute,
    ...lightManagementModulePopupRoute,
];

@NgModule({
    imports: [
        WiCloudSharedModule,
        RouterModule.forChild(ENTITY_STATES)
    ],
    declarations: [
        LightManagementModuleWilampComponent,
        LightManagementModuleWilampDetailComponent,
        LightManagementModuleWilampDialogComponent,
        LightManagementModuleWilampDeleteDialogComponent,
        LightManagementModuleWilampPopupComponent,
        LightManagementModuleWilampDeletePopupComponent,
    ],
    entryComponents: [
        LightManagementModuleWilampComponent,
        LightManagementModuleWilampDialogComponent,
        LightManagementModuleWilampPopupComponent,
        LightManagementModuleWilampDeleteDialogComponent,
        LightManagementModuleWilampDeletePopupComponent,
    ],
    providers: [
        LightManagementModuleWilampService,
        LightManagementModuleWilampPopupService,
    ],
    schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class WilampCloudLightManagementModuleWilampModule {}
