import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { RouterModule } from '@angular/router';

import { WiCloudSharedModule } from '../../shared';
import {
    GatewayWilampService,
    GatewayWilampPopupService,
    GatewayWilampComponent,
    GatewayWilampDetailComponent,
    GatewayWilampDialogComponent,
    GatewayWilampPopupComponent,
    GatewayWilampDeletePopupComponent,
    GatewayWilampDeleteDialogComponent,
    gatewayRoute,
    gatewayPopupRoute,
    GatewayWilampResolvePagingParams,
} from './';

const ENTITY_STATES = [
    ...gatewayRoute,
    ...gatewayPopupRoute,
];

@NgModule({
    imports: [
        WiCloudSharedModule,
        RouterModule.forChild(ENTITY_STATES),
        // WidgetsModule
    ],
    declarations: [
        GatewayWilampComponent,
        GatewayWilampDetailComponent,
        GatewayWilampDialogComponent,
        GatewayWilampDeleteDialogComponent,
        GatewayWilampPopupComponent,
        GatewayWilampDeletePopupComponent,
    ],
    entryComponents: [
        GatewayWilampComponent,
        GatewayWilampDialogComponent,
        GatewayWilampPopupComponent,
        GatewayWilampDeleteDialogComponent,
        GatewayWilampDeletePopupComponent,
    ],
    providers: [
        GatewayWilampService,
        GatewayWilampPopupService,
        GatewayWilampResolvePagingParams,
        // WidgetsModule
    ],
    schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class WilampCloudGatewayWilampModule {}
