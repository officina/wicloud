import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { RouterModule } from '@angular/router';

import { WiCloudSharedModule } from '../../shared';
import {
    OrderWilampService,
    OrderWilampPopupService,
    OrderWilampComponent,
    OrderWilampDetailComponent,
    OrderWilampDialogComponent,
    OrderWilampPopupComponent,
    OrderWilampDeletePopupComponent,
    OrderWilampDeleteDialogComponent,
    orderRoute,
    orderPopupRoute,
} from './';

const ENTITY_STATES = [
    ...orderRoute,
    ...orderPopupRoute,
];

@NgModule({
    imports: [
        WiCloudSharedModule,
        RouterModule.forChild(ENTITY_STATES)
    ],
    declarations: [
        OrderWilampComponent,
        OrderWilampDetailComponent,
        OrderWilampDialogComponent,
        OrderWilampDeleteDialogComponent,
        OrderWilampPopupComponent,
        OrderWilampDeletePopupComponent,
    ],
    entryComponents: [
        OrderWilampComponent,
        OrderWilampDialogComponent,
        OrderWilampPopupComponent,
        OrderWilampDeleteDialogComponent,
        OrderWilampDeletePopupComponent,
    ],
    providers: [
        OrderWilampService,
        OrderWilampPopupService,
    ],
    schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class WilampCloudOrderWilampModule {}
