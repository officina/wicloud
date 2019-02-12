import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { RouterModule } from '@angular/router';

import { WiCloudSharedModule } from '../../shared';
import {
    EnergyIntervalService,
    EnergyIntervalPopupService,
    EnergyIntervalComponent,
    EnergyIntervalDetailComponent,
    EnergyIntervalDialogComponent,
    EnergyIntervalPopupComponent,
    EnergyIntervalDeletePopupComponent,
    EnergyIntervalDeleteDialogComponent,
    energyIntervalRoute,
    energyIntervalPopupRoute,
} from './';

const ENTITY_STATES = [
    ...energyIntervalRoute,
    ...energyIntervalPopupRoute,
];

@NgModule({
    imports: [
        WiCloudSharedModule,
        RouterModule.forChild(ENTITY_STATES)
    ],
    declarations: [
        EnergyIntervalComponent,
        EnergyIntervalDetailComponent,
        EnergyIntervalDialogComponent,
        EnergyIntervalDeleteDialogComponent,
        EnergyIntervalPopupComponent,
        EnergyIntervalDeletePopupComponent,
    ],
    entryComponents: [
        EnergyIntervalComponent,
        EnergyIntervalDialogComponent,
        EnergyIntervalPopupComponent,
        EnergyIntervalDeleteDialogComponent,
        EnergyIntervalDeletePopupComponent,
    ],
    providers: [
        EnergyIntervalService,
        EnergyIntervalPopupService,
    ],
    schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class WilampCloudEnergyIntervalModule {}
