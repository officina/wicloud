import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { RouterModule } from '@angular/router';

import { WiCloudSharedModule } from '../../shared';
import {
    LightManagementMeasureWilampService,
    LightManagementMeasureWilampPopupService,
    LightManagementMeasureWilampComponent,
    LightManagementMeasureWilampDetailComponent,
    LightManagementMeasureWilampDialogComponent,
    LightManagementMeasureWilampPopupComponent,
    LightManagementMeasureWilampDeletePopupComponent,
    LightManagementMeasureWilampDeleteDialogComponent,
    lightManagementMeasureRoute,
    lightManagementMeasurePopupRoute,
} from './';

const ENTITY_STATES = [
    ...lightManagementMeasureRoute,
    ...lightManagementMeasurePopupRoute,
];

@NgModule({
    imports: [
        WiCloudSharedModule,
        RouterModule.forChild(ENTITY_STATES),
    ],
    declarations: [
        LightManagementMeasureWilampComponent,
        LightManagementMeasureWilampDetailComponent,
        LightManagementMeasureWilampDialogComponent,
        LightManagementMeasureWilampDeleteDialogComponent,
        LightManagementMeasureWilampPopupComponent,
        LightManagementMeasureWilampDeletePopupComponent,
    ],
    entryComponents: [
        LightManagementMeasureWilampComponent,
        LightManagementMeasureWilampDialogComponent,
        LightManagementMeasureWilampPopupComponent,
        LightManagementMeasureWilampDeleteDialogComponent,
        LightManagementMeasureWilampDeletePopupComponent,
    ],
    providers: [
        LightManagementMeasureWilampService,
        LightManagementMeasureWilampPopupService,
    ],
    schemas: [CUSTOM_ELEMENTS_SCHEMA],
})
export class WilampCloudLightManagementMeasureWilampModule {}
