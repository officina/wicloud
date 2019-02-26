import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { RouterModule } from '@angular/router';

import { WiCloudSharedModule } from '../../shared';
import {
    AddressWilampService,
    AddressWilampPopupService,
    AddressWilampComponent,
    AddressWilampDetailComponent,
    AddressWilampDialogComponent,
    AddressWilampPopupComponent,
    AddressWilampDeletePopupComponent,
    AddressWilampDeleteDialogComponent,
    addressRoute,
    addressPopupRoute,
} from './';

const ENTITY_STATES = [
    ...addressRoute,
    ...addressPopupRoute,
];

@NgModule({
    imports: [
        WiCloudSharedModule,
        RouterModule.forChild(ENTITY_STATES),
    ],
    declarations: [
        AddressWilampComponent,
        AddressWilampDetailComponent,
        AddressWilampDialogComponent,
        AddressWilampDeleteDialogComponent,
        AddressWilampPopupComponent,
        AddressWilampDeletePopupComponent,
    ],
    entryComponents: [
        AddressWilampComponent,
        AddressWilampDialogComponent,
        AddressWilampPopupComponent,
        AddressWilampDeleteDialogComponent,
        AddressWilampDeletePopupComponent,
    ],
    providers: [
        AddressWilampService,
        AddressWilampPopupService,
    ],
    schemas: [CUSTOM_ELEMENTS_SCHEMA],
})
export class WilampCloudAddressWilampModule {}
