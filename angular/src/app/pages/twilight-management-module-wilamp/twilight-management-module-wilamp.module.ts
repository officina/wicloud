import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { RouterModule } from '@angular/router';

import { WiCloudSharedModule } from '../../shared';
import {
    TwilightManagementModuleWilampService,
    TwilightManagementModuleWilampPopupService,
    TwilightManagementModuleWilampComponent,
    TwilightManagementModuleWilampDetailComponent,
    TwilightManagementModuleWilampDialogComponent,
    TwilightManagementModuleWilampPopupComponent,
    TwilightManagementModuleWilampDeletePopupComponent,
    TwilightManagementModuleWilampDeleteDialogComponent,
    twilightManagementModuleRoute,
    twilightManagementModulePopupRoute,
} from './';

const ENTITY_STATES = [
    ...twilightManagementModuleRoute,
    ...twilightManagementModulePopupRoute,
];

@NgModule({
    imports: [
        WiCloudSharedModule,
        RouterModule.forChild(ENTITY_STATES),
    ],
    declarations: [
        TwilightManagementModuleWilampComponent,
        TwilightManagementModuleWilampDetailComponent,
        TwilightManagementModuleWilampDialogComponent,
        TwilightManagementModuleWilampDeleteDialogComponent,
        TwilightManagementModuleWilampPopupComponent,
        TwilightManagementModuleWilampDeletePopupComponent,
    ],
    entryComponents: [
        TwilightManagementModuleWilampComponent,
        TwilightManagementModuleWilampDialogComponent,
        TwilightManagementModuleWilampPopupComponent,
        TwilightManagementModuleWilampDeleteDialogComponent,
        TwilightManagementModuleWilampDeletePopupComponent,
    ],
    providers: [
        TwilightManagementModuleWilampService,
        TwilightManagementModuleWilampPopupService,
    ],
    schemas: [CUSTOM_ELEMENTS_SCHEMA],
})
export class WilampCloudTwilightManagementModuleWilampModule {}
