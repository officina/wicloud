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
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { UserRouteAccessService } from './shared';
import {AmChartsModule} from '@amcharts/amcharts3-angular';
import { ScriptLoaderService } from './_services/script-loader.service';
import {GlobalDatabaseService} from './shared/global-database/global-database.service';


@NgModule({
  declarations: [AppComponent],
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
  ],
  bootstrap: [AppComponent],
  providers: [
      GlobalDatabaseService,
      ScriptLoaderService,
      UserRouteAccessService,
      AuthGuard,
        { provide: APP_BASE_HREF, useValue: '/' },
        { provide: NB_AUTH_TOKEN_INTERCEPTOR_FILTER, useValue: (req) =>  false },
        { provide: HTTP_INTERCEPTORS, useClass: NbAuthJWTInterceptor, multi: true}, // quick fix for JWT Token on API calls //TODO:AT controlla, può provocare ricorsioni
        { provide: NbTokenStorage, useClass: NbTokenLocalStorage },
  ],
})
export class AppModule {
}


