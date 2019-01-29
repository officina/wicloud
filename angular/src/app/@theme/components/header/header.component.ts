import { Component, Input, OnInit } from '@angular/core';

import { NbMenuService, NbSidebarService } from '@nebular/theme';

import { AnalyticsService } from '../../../@core/utils/analytics.service';
import {NbAuthJWTToken, NbAuthService, NbTokenService} from '@nebular/auth';


@Component({
  selector: 'ngx-header',
  styleUrls: ['./header.component.scss'],
  templateUrl: './header.component.html',

})
export class HeaderComponent implements OnInit {


  @Input() position = 'normal';

  user: any;

  userMenu = [{ title: 'Profile' }, { title: 'Log out'}];

  constructor(private sidebarService: NbSidebarService,
              private menuService: NbMenuService,
              // private userService: UserService,
              private analyticsService: AnalyticsService,
              private authService: NbAuthService,
              protected tokenService: NbTokenService,

              ) {

    this.authService.onTokenChange()
      .subscribe((token: NbAuthJWTToken) => {
        if (token.isValid()) {
            this.user = token.getPayload(); // here we receive a payload from the token and assigne it to our `user` variable
        }
      });
  }

  ngOnInit() {

    this.menuService.onItemClick().subscribe(( event ) => {
      this.onItemSelection(event.item.title);
    })
  }

  onItemSelection( title ) {

    if ( title === 'Log out' ) {
      // Do something on Log out
      this.authService.logout('email').subscribe(( result ) => {
        this.tokenService.clear()

      })

    } else if ( title === 'Profile' ) {
      // Do something on Profile

    }
  }

  toggleSidebar(): boolean {
    this.sidebarService.toggle(true, 'menu-sidebar');
    return false;
  }

  toggleSettings(): boolean {
    this.sidebarService.toggle(false, 'settings-sidebar');
    return false;
  }

  goToHome() {
    this.menuService.navigateHome();
  }

  startSearch() {
    this.analyticsService.trackEvent('startSearch');
  }

}
