import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { RouterModule } from '@angular/router';

import { WiCloudSharedModule } from '../../shared';
import {
    ContactWilampService,
    ContactWilampPopupService,
    ContactWilampComponent,
    ContactWilampDetailComponent,
    ContactWilampDialogComponent,
    ContactWilampPopupComponent,
    ContactWilampDeletePopupComponent,
    ContactWilampDeleteDialogComponent,
    contactRoute,
    contactPopupRoute,
} from './';

const ENTITY_STATES = [
    ...contactRoute,
    ...contactPopupRoute,
];

@NgModule({
    imports: [
        WiCloudSharedModule,
        RouterModule.forChild(ENTITY_STATES)
    ],
    declarations: [
        ContactWilampComponent,
        ContactWilampDetailComponent,
        ContactWilampDialogComponent,
        ContactWilampDeleteDialogComponent,
        ContactWilampPopupComponent,
        ContactWilampDeletePopupComponent,
    ],
    entryComponents: [
        ContactWilampComponent,
        ContactWilampDialogComponent,
        ContactWilampPopupComponent,
        ContactWilampDeleteDialogComponent,
        ContactWilampDeletePopupComponent,
    ],
    providers: [
        ContactWilampService,
        ContactWilampPopupService,
    ],
    schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class WilampCloudContactWilampModule {}
