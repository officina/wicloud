import { Component, Input, OnInit } from '@angular/core';

import { NbMenuService, NbSidebarService } from '@nebular/theme';
import { UserData } from '../../../@core/data/users';
import { AnalyticsService } from '../../../@core/utils';
import { LayoutService } from '../../../@core/utils';
import {NbAuthJWTToken, NbAuthService, NbTokenService} from '@nebular/auth';
import { Router } from '@angular/router';

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
              private userService: UserData,
              private analyticsService: AnalyticsService,
              private layoutService: LayoutService,
              private authService: NbAuthService,
              private router: Router,
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
    });

    this.userService.getUsers()
      .subscribe((users: any) => this.user = users.nick);
  }

  onItemSelection( title ) {

    if ( title === 'Log out' ) {
      this.router.navigate(['/auth/logout']);
      // Do something on Log out

      /*this.authService.logout('email').subscribe(( result ) => {
        this.tokenService.clear();

      })*/

    } else if ( title === 'Profile' ) {
      // Do something on Profile

    }
  }

  toggleSidebar(): boolean {
    this.sidebarService.toggle(true, 'menu-sidebar');
    this.layoutService.changeLayoutSize();

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
