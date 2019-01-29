import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { RouterModule } from '@angular/router';

import { WiCloudSharedModule } from '../../shared';
import {
    CustomerWilampService,
    CustomerWilampPopupService,
    CustomerWilampComponent,
    CustomerWilampDetailComponent,
    CustomerWilampDialogComponent,
    CustomerWilampPopupComponent,
    CustomerWilampDeletePopupComponent,
    CustomerWilampDeleteDialogComponent,
    customerRoute,
    customerPopupRoute,
} from './';

const ENTITY_STATES = [
    ...customerRoute,
    ...customerPopupRoute,
];

@NgModule({
    imports: [
        WiCloudSharedModule,
        RouterModule.forChild(ENTITY_STATES),
    ],
    declarations: [
        CustomerWilampComponent,
        CustomerWilampDetailComponent,
        CustomerWilampDialogComponent,
        CustomerWilampDeleteDialogComponent,
        CustomerWilampPopupComponent,
        CustomerWilampDeletePopupComponent,
    ],
    entryComponents: [
        CustomerWilampComponent,
        CustomerWilampDialogComponent,
        CustomerWilampPopupComponent,
        CustomerWilampDeleteDialogComponent,
        CustomerWilampDeletePopupComponent,
    ],
    providers: [
        CustomerWilampService,
        CustomerWilampPopupService,
    ],
    schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class WilampCloudCustomerWilampModule {}
