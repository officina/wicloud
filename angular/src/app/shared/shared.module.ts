import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { DatePipe } from '@angular/common';
import {WilampCloudSharedCommonModule} from './shared-common.module';
import {WilampCloudSharedLibsModule} from './shared-libs.module';
import {Principal} from './auth/principal.service';

@NgModule({
    imports: [
        WilampCloudSharedLibsModule,
        WilampCloudSharedCommonModule,
    ],
    providers: [
        DatePipe,
        Principal
    ],
    exports: [
        WilampCloudSharedCommonModule,
        DatePipe
    ],
    schemas: [CUSTOM_ELEMENTS_SCHEMA]

})
export class WiCloudSharedModule {}
