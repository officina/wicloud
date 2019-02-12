import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { RouterModule } from '@angular/router';

import { WiCloudSharedModule } from '../../shared';
import {
    EnergyMeterModuleWilampService,
    EnergyMeterModuleWilampPopupService,
    EnergyMeterModuleWilampComponent,
    EnergyMeterModuleWilampDetailComponent,
    EnergyMeterModuleWilampDialogComponent,
    EnergyMeterModuleWilampPopupComponent,
    EnergyMeterModuleWilampDeletePopupComponent,
    EnergyMeterModuleWilampDeleteDialogComponent,
    energyMeterModuleRoute,
    energyMeterModulePopupRoute,
} from './';

const ENTITY_STATES = [
    ...energyMeterModuleRoute,
    ...energyMeterModulePopupRoute,
];

@NgModule({
    imports: [
        WiCloudSharedModule,
        RouterModule.forChild(ENTITY_STATES)
    ],
    declarations: [
        EnergyMeterModuleWilampComponent,
        EnergyMeterModuleWilampDetailComponent,
        EnergyMeterModuleWilampDialogComponent,
        EnergyMeterModuleWilampDeleteDialogComponent,
        EnergyMeterModuleWilampPopupComponent,
        EnergyMeterModuleWilampDeletePopupComponent,
    ],
    entryComponents: [
        EnergyMeterModuleWilampComponent,
        EnergyMeterModuleWilampDialogComponent,
        EnergyMeterModuleWilampPopupComponent,
        EnergyMeterModuleWilampDeleteDialogComponent,
        EnergyMeterModuleWilampDeletePopupComponent,
    ],
    providers: [
        EnergyMeterModuleWilampService,
        EnergyMeterModuleWilampPopupService,
    ],
    schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class WilampCloudEnergyMeterModuleWilampModule {}
