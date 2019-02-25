import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { RouterModule } from '@angular/router';
import {WiCloudSharedModule} from '../../shared';

import {
    LightFixtureWilampService,
    LightFixtureWilampPopupService,
    LightFixtureWilampComponent,
    LightFixtureWilampDetailComponent,
    LightFixtureWilampDialogComponent,
    LightFixtureWilampPopupComponent,
    LightFixtureWilampDeletePopupComponent,
    LightFixtureWilampDeleteDialogComponent,
    lightFixtureRoute,
    lightFixturePopupRoute,
} from './';

const ENTITY_STATES = [
    ...lightFixtureRoute,
    ...lightFixturePopupRoute,
];

@NgModule({
    imports: [
        WiCloudSharedModule,
        RouterModule.forChild(ENTITY_STATES),
    ],
    declarations: [
        LightFixtureWilampComponent,
        LightFixtureWilampDetailComponent,
        LightFixtureWilampDialogComponent,
        LightFixtureWilampDeleteDialogComponent,
        LightFixtureWilampPopupComponent,
        LightFixtureWilampDeletePopupComponent,
    ],
    entryComponents: [
        LightFixtureWilampComponent,
        LightFixtureWilampDialogComponent,
        LightFixtureWilampPopupComponent,
        LightFixtureWilampDeleteDialogComponent,
        LightFixtureWilampDeletePopupComponent,
    ],
    providers: [
        LightFixtureWilampService,
        LightFixtureWilampPopupService,
    ],
    schemas: [CUSTOM_ELEMENTS_SCHEMA],
})
export class WilampCloudLightFixtureWilampModule {}
