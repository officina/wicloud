/**
 * @license
 * Copyright Akveo. All Rights Reserved.
 * Licensed under the MIT License. See License.txt in the project root for license information.
 */
import {APP_BASE_HREF} from '@angular/common';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import {HTTP_INTERCEPTORS, HttpClient, HttpClientModule} from '@angular/common/http';
import { CoreModule } from './@core/core.module';
import {NB_AUTH_TOKEN_INTERCEPTOR_FILTER} from '@nebular/auth';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { ThemeModule } from './@theme/theme.module';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import {NbAuthJWTInterceptor, NbTokenLocalStorage, NbTokenStorage} from '@nebular/auth';
import {AuthGuard} from './_guard/auth-guard.service';
import {TranslateLoader, TranslateModule, TranslateService} from '@ngx-translate/core';
import {TranslateHttpLoader} from '@ngx-translate/http-loader';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { WiCloudSharedModule, UserRouteAccessService } from './shared';




@NgModule({
  declarations: [AppComponent],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    CommonModule,
    FormsModule,
    HttpClientModule,
    AppRoutingModule,
    NgbModule.forRoot(),
    ThemeModule.forRoot(),
    CoreModule.forRoot(),
    WiCloudSharedModule,
    TranslateModule.forRoot({
    loader: {
      provide: TranslateLoader,
      useFactory: HttpLoaderFactory,
      deps: [HttpClient],
    },
    }),
  ],
  bootstrap: [AppComponent],
  providers: [
    UserRouteAccessService,
    AuthGuard,
      { provide: APP_BASE_HREF, useValue: '/' }, TranslateService,
      { provide: NB_AUTH_TOKEN_INTERCEPTOR_FILTER, useValue: (req) =>  false },
      { provide: HTTP_INTERCEPTORS, useClass: NbAuthJWTInterceptor, multi: true}, // quick fix for JWT Token on API calls
      { provide: NbTokenStorage, useClass: NbTokenLocalStorage },
  ],
})
export class AppModule {
}


// AoT requires an exported function for factories
export function HttpLoaderFactory(http: HttpClient) {
    return new TranslateHttpLoader(http, './assets/i18n/', '.json');
}




