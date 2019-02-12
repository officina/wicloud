import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { RouterModule } from '@angular/router';

import { WiCloudSharedModule } from '../../shared';
import {
    ShippingWilampService,
    ShippingWilampPopupService,
    ShippingWilampComponent,
    ShippingWilampDetailComponent,
    ShippingWilampDialogComponent,
    ShippingWilampPopupComponent,
    ShippingWilampDeletePopupComponent,
    ShippingWilampDeleteDialogComponent,
    shippingRoute,
    shippingPopupRoute,
} from './';

const ENTITY_STATES = [
    ...shippingRoute,
    ...shippingPopupRoute,
];

@NgModule({
    imports: [
        WiCloudSharedModule,
        RouterModule.forChild(ENTITY_STATES)
    ],
    declarations: [
        ShippingWilampComponent,
        ShippingWilampDetailComponent,
        ShippingWilampDialogComponent,
        ShippingWilampDeleteDialogComponent,
        ShippingWilampPopupComponent,
        ShippingWilampDeletePopupComponent,
    ],
    entryComponents: [
        ShippingWilampComponent,
        ShippingWilampDialogComponent,
        ShippingWilampPopupComponent,
        ShippingWilampDeleteDialogComponent,
        ShippingWilampDeletePopupComponent,
    ],
    providers: [
        ShippingWilampService,
        ShippingWilampPopupService,
    ],
    schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class WilampCloudShippingWilampModule {}
