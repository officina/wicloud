import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { RouterModule } from '@angular/router';

import { WiCloudSharedModule } from '../../shared';
import {
    LightProfileSlotWilampService,
    LightProfileSlotWilampPopupService,
    LightProfileSlotWilampComponent,
    LightProfileSlotWilampDetailComponent,
    LightProfileSlotWilampDialogComponent,
    LightProfileSlotWilampPopupComponent,
    LightProfileSlotWilampDeletePopupComponent,
    LightProfileSlotWilampDeleteDialogComponent,
    lightProfileSlotRoute,
    lightProfileSlotPopupRoute,
} from './';

const ENTITY_STATES = [
    ...lightProfileSlotRoute,
    ...lightProfileSlotPopupRoute,
];

@NgModule({
    imports: [
        WiCloudSharedModule,
        RouterModule.forChild(ENTITY_STATES)
    ],
    declarations: [
        LightProfileSlotWilampComponent,
        LightProfileSlotWilampDetailComponent,
        LightProfileSlotWilampDialogComponent,
        LightProfileSlotWilampDeleteDialogComponent,
        LightProfileSlotWilampPopupComponent,
        LightProfileSlotWilampDeletePopupComponent,
    ],
    entryComponents: [
        LightProfileSlotWilampComponent,
        LightProfileSlotWilampDialogComponent,
        LightProfileSlotWilampPopupComponent,
        LightProfileSlotWilampDeleteDialogComponent,
        LightProfileSlotWilampDeletePopupComponent,
    ],
    providers: [
        LightProfileSlotWilampService,
        LightProfileSlotWilampPopupService,
    ],
    schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class WilampCloudLightProfileSlotWilampModule {}
