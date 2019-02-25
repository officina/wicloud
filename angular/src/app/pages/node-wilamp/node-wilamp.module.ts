import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { RouterModule } from '@angular/router';

import { WiCloudSharedModule } from '../../shared';
import {
    NodeWilampService,
    NodeWilampPopupService,
    NodeWilampComponent,
    NodeWilampDetailComponent,
    NodeWilampDialogComponent,
    NodeWilampPopupComponent,
    NodeWilampDeletePopupComponent,
    NodeWilampDeleteDialogComponent,
    nodeRoute,
    nodePopupRoute,
} from './';

const ENTITY_STATES = [
    ...nodeRoute,
    ...nodePopupRoute,
];

@NgModule({
    imports: [
        WiCloudSharedModule,
        RouterModule.forChild(ENTITY_STATES),
    ],
    declarations: [
        NodeWilampComponent,
        NodeWilampDetailComponent,
        NodeWilampDialogComponent,
        NodeWilampDeleteDialogComponent,
        NodeWilampPopupComponent,
        NodeWilampDeletePopupComponent,
    ],
    entryComponents: [
        NodeWilampComponent,
        NodeWilampDialogComponent,
        NodeWilampPopupComponent,
        NodeWilampDeleteDialogComponent,
        NodeWilampDeletePopupComponent,
    ],
    providers: [
        NodeWilampService,
        NodeWilampPopupService,
    ],
    schemas: [CUSTOM_ELEMENTS_SCHEMA],
})
export class WilampCloudNodeWilampModule {}
