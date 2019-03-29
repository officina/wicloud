import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { DatePipe } from '@angular/common';
import {WilampCloudSharedCommonModule} from './shared-common.module';
import {WilampCloudSharedLibsModule} from './shared-libs.module';
import {Principal} from './auth/principal.service';
import {HttpClient} from '@angular/common/http';
import {TranslateLoader, TranslateModule, TranslateService} from '@ngx-translate/core';
import {TranslateHttpLoader} from '@ngx-translate/http-loader';

@NgModule({
    imports: [
        WilampCloudSharedLibsModule,
        WilampCloudSharedCommonModule,
        TranslateModule.forRoot({
            loader: {
                provide: TranslateLoader,
                useFactory: (createTranslateLoader),
                deps: [HttpClient],
            },
        }),
    ],
    providers: [
        DatePipe,
        Principal,
    ],
    exports: [
        WilampCloudSharedCommonModule,
        DatePipe,
        TranslateModule,
    ],
    schemas: [CUSTOM_ELEMENTS_SCHEMA],

})
export class WiCloudSharedModule {
    constructor(private translate: TranslateService) {
        this.translate.addLangs(['en', 'it']);
        this.translate.setDefaultLang('it');
        this.translate.use('it'); // Fallback
    }
}

export function createTranslateLoader(http: HttpClient) {
    return new TranslateHttpLoader(http, './assets/i18n/', '.json');
}
