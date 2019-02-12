import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { RouterModule } from '@angular/router';

import { WiCloudSharedModule } from '../../shared';
import {
    MotionManagementModuleWilampService,
    MotionManagementModuleWilampPopupService,
    MotionManagementModuleWilampComponent,
    MotionManagementModuleWilampDetailComponent,
    MotionManagementModuleWilampDialogComponent,
    MotionManagementModuleWilampPopupComponent,
    MotionManagementModuleWilampDeletePopupComponent,
    MotionManagementModuleWilampDeleteDialogComponent,
    motionManagementModuleRoute,
    motionManagementModulePopupRoute,
} from './';

const ENTITY_STATES = [
    ...motionManagementModuleRoute,
    ...motionManagementModulePopupRoute,
];

@NgModule({
    imports: [
        WiCloudSharedModule,
        RouterModule.forChild(ENTITY_STATES)
    ],
    declarations: [
        MotionManagementModuleWilampComponent,
        MotionManagementModuleWilampDetailComponent,
        MotionManagementModuleWilampDialogComponent,
        MotionManagementModuleWilampDeleteDialogComponent,
        MotionManagementModuleWilampPopupComponent,
        MotionManagementModuleWilampDeletePopupComponent,
    ],
    entryComponents: [
        MotionManagementModuleWilampComponent,
        MotionManagementModuleWilampDialogComponent,
        MotionManagementModuleWilampPopupComponent,
        MotionManagementModuleWilampDeleteDialogComponent,
        MotionManagementModuleWilampDeletePopupComponent,
    ],
    providers: [
        MotionManagementModuleWilampService,
        MotionManagementModuleWilampPopupService,
    ],
    schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class WilampCloudMotionManagementModuleWilampModule {}
