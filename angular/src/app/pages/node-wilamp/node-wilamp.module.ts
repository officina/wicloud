import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { RouterModule } from '@angular/router';
import { ThemeModule } from '../../@theme/theme.module';
import {Ng2SmartTableModule} from 'ng2-smart-table';
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
        ThemeModule,
        Ng2SmartTableModule,
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
