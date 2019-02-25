/**
 * @license
 * Copyright Akveo. All Rights Reserved.
 * Licensed under the MIT License. See License.txt in the project root for license information.
 */
import {Component, Inject, OnInit} from '@angular/core';
import { AnalyticsService } from './@core/utils/analytics.service';
import {TranslateService} from '@ngx-translate/core';
import {NB_AUTH_OPTIONS, NbAuthService, NbLogoutComponent, NbTokenService} from '@nebular/auth';
import {Router} from '@angular/router';

@Component({
  selector: 'ngx-app',
  template: '<router-outlet></router-outlet>',
})
export class AppComponent implements OnInit {

  constructor(private analytics: AnalyticsService, private translate: TranslateService) {

    // init language
    this.translate.addLangs(['en', 'it']);
    this.translate.setDefaultLang('it');
    this.translate.use('it'); // Fallback
  }

  ngOnInit() {
    this.analytics.trackPageViews();
  }
}

export class LogoutComponent extends NbLogoutComponent implements OnInit {
  constructor(
    protected service: NbAuthService,
    @Inject(NB_AUTH_OPTIONS) protected options = {},
    protected router: Router,
    protected tokenService: NbTokenService
  ) {
    super(service, options, router);
  }

  ngOnInit() {
    super.ngOnInit();
  }

  logout(strategy: string): void {
    super.logout(strategy);
    this.tokenService.clear();
  }
}
