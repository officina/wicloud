/**
 * @license
 * Copyright Akveo. All Rights Reserved.
 * Licensed under the MIT License. See License.txt in the project root for license information.
 */
import { APP_BASE_HREF } from '@angular/common';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import {HTTP_INTERCEPTORS, HttpClient, HttpClientModule} from '@angular/common/http';
import { CoreModule } from './@core/core.module';
import {NB_AUTH_TOKEN_INTERCEPTOR_FILTER} from '@nebular/auth';

import {AppComponent, LogoutComponent} from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { ThemeModule } from './@theme/theme.module';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import {NbAuthJWTInterceptor, NbTokenLocalStorage, NbTokenStorage} from '@nebular/auth';
import {AuthGuard} from './_guard/auth-guard.service';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { UserRouteAccessService } from './shared';
import {AmChartsModule} from '@amcharts/amcharts3-angular';
import { ScriptLoaderService } from './_services/script-loader.service';
import {LeafletModule} from '@asymmetrik/ngx-leaflet';


@NgModule({
  declarations: [
      AppComponent,
      LogoutComponent,
  ],
  imports: [
      AmChartsModule,
      BrowserModule,
      BrowserAnimationsModule,
      CommonModule,
      FormsModule,
      HttpClientModule,
      AppRoutingModule,
      NgbModule.forRoot(),
      ThemeModule.forRoot(),
      CoreModule.forRoot(),
      LeafletModule.forRoot(),
      WiCloudSharedModule,
  ],
  bootstrap: [AppComponent],
  providers: [
      ScriptLoaderService,
      UserRouteAccessService,
      AuthGuard,
        { provide: APP_BASE_HREF, useValue: '/' }, TranslateService,
        { provide: NB_AUTH_TOKEN_INTERCEPTOR_FILTER, useValue: authTokenInterceptorFilter },
        // quick fix for JWT Token on API calls
        // TODO:AT controlla, può provocare ricorsioni
        { provide: HTTP_INTERCEPTORS, useClass: NbAuthJWTInterceptor, multi: true},
        { provide: NbTokenStorage, useClass: NbTokenLocalStorage },
  ],
})
export class AppModule {
}

export function authTokenInterceptorFilter(req) {
    try {
        if (req.url.includes('api-token'))
            return true;
        return false;
    } catch (ex) {
        return false;
    }
}

