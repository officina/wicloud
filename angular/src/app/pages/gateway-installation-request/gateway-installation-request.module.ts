import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { RouterModule } from '@angular/router';

import {
    GatewayInstallationRequestService,
    GatewayInstallationRequestPopupService,
    GatewayInstallationRequestComponent,
    GatewayInstallationRequestDetailComponent,
    GatewayInstallationRequestDialogComponent,
    GatewayInstallationRequestPopupComponent,
    GatewayInstallationRequestDeletePopupComponent,
    GatewayInstallationRequestDeleteDialogComponent,
    gatewayInstallationRequestRoute,
    gatewayInstallationRequestPopupRoute,
    GatewayInstallationRequestResolvePagingParams,
} from './';

const ENTITY_STATES = [
    ...gatewayInstallationRequestRoute,
    ...gatewayInstallationRequestPopupRoute,
];

@NgModule({
    imports: [
        RouterModule.forChild(ENTITY_STATES)
    ],
    declarations: [
        GatewayInstallationRequestComponent,
        GatewayInstallationRequestDetailComponent,
        GatewayInstallationRequestDialogComponent,
        GatewayInstallationRequestDeleteDialogComponent,
        GatewayInstallationRequestPopupComponent,
        GatewayInstallationRequestDeletePopupComponent,
    ],
    entryComponents: [
        GatewayInstallationRequestComponent,
        GatewayInstallationRequestDialogComponent,
        GatewayInstallationRequestPopupComponent,
        GatewayInstallationRequestDeleteDialogComponent,
        GatewayInstallationRequestDeletePopupComponent,
    ],
    providers: [
        GatewayInstallationRequestService,
        GatewayInstallationRequestPopupService,
        GatewayInstallationRequestResolvePagingParams,
    ],
    schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class WilampCloudGatewayInstallationRequestModule {}
