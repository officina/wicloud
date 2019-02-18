import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { RouterModule } from '@angular/router';

import { WiCloudSharedModule } from '../../shared';
import {
    LightProfileWilampService,
    LightProfileWilampPopupService,
    LightProfileWilampComponent,
    LightProfileWilampDetailComponent,
    LightProfileWilampDialogComponent,
    LightProfileWilampPopupComponent,
    LightProfileWilampDeletePopupComponent,
    LightProfileWilampDeleteDialogComponent,
    lightProfileRoute,
    lightProfilePopupRoute,
} from './';

const ENTITY_STATES = [
    ...lightProfileRoute,
    ...lightProfilePopupRoute,
];

@NgModule({
    imports: [
        WiCloudSharedModule,
        RouterModule.forChild(ENTITY_STATES)
    ],
    declarations: [
        LightProfileWilampComponent,
        LightProfileWilampDetailComponent,
        LightProfileWilampDialogComponent,
        LightProfileWilampDeleteDialogComponent,
        LightProfileWilampPopupComponent,
        LightProfileWilampDeletePopupComponent,
    ],
    entryComponents: [
        LightProfileWilampComponent,
        LightProfileWilampDialogComponent,
        LightProfileWilampPopupComponent,
        LightProfileWilampDeleteDialogComponent,
        LightProfileWilampDeletePopupComponent,
    ],
    providers: [
        LightProfileWilampService,
        LightProfileWilampPopupService,
    ],
    schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class WilampCloudLightProfileWilampModule {}
