import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { RouterModule } from '@angular/router';
import { WiCloudSharedModule } from '../../shared';
import {
    NodeModulesWilampService,
    NodeModulesWilampPopupService,
    NodeModulesWilampComponent,
    NodeModulesWilampDetailComponent,
    NodeModulesWilampDialogComponent,
    NodeModulesWilampPopupComponent,
    NodeModulesWilampDeletePopupComponent,
    NodeModulesWilampDeleteDialogComponent,
    nodeModulesRoute,
    nodeModulesPopupRoute,
} from './';

const ENTITY_STATES = [
    ...nodeModulesRoute,
    ...nodeModulesPopupRoute,
];

@NgModule({
    imports: [
        WiCloudSharedModule,
        RouterModule.forChild(ENTITY_STATES),
    ],
    declarations: [
        NodeModulesWilampComponent,
        NodeModulesWilampDetailComponent,
        NodeModulesWilampDialogComponent,
        NodeModulesWilampDeleteDialogComponent,
        NodeModulesWilampPopupComponent,
        NodeModulesWilampDeletePopupComponent,
    ],
    entryComponents: [
        NodeModulesWilampComponent,
        NodeModulesWilampDialogComponent,
        NodeModulesWilampPopupComponent,
        NodeModulesWilampDeleteDialogComponent,
        NodeModulesWilampDeletePopupComponent,
    ],
    providers: [
        NodeModulesWilampService,
        NodeModulesWilampPopupService,
    ],
    schemas: [CUSTOM_ELEMENTS_SCHEMA],
})
export class WilampCloudNodeModulesWilampModule {}
