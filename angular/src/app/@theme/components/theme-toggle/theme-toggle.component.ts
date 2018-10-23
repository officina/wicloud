import { Component, OnDestroy, Input } from '@angular/core';
import {NbJSThemeOptions} from '@nebular/theme/services/js-themes/theme.options';
import { NbThemeService } from '@nebular/theme';
import {AnalyticsService} from '../../../@core/utils/analytics.service';

@Component({
  selector: 'ngx-layout-theme-toggle',
  template: `
    <ngx-switcher
      [firstValue]="themes[0].key"
      [secondValue]="themes[1].key"
      [firstValueLabel]="themes[0].title"
      [secondValueLabel]="themes[1].title"
      [value]="currentTheme"
      (valueChange)="onToggleTheme($event)"
      [vertical]="vertical">
    </ngx-switcher>
  `,
})
export class ThemeToggleComponent implements OnDestroy {
  alive = true;
  theme: NbJSThemeOptions;
  currentTheme: string;
  themes = [
    {
      title: 'Cosmic',
      key: 'cosmic',
    },
    {
      title: 'Corporate',
      key: 'corporate',
    },
  ];
  @Input() vertical: boolean = false;

  constructor(private analyticsService: AnalyticsService, private themeService: NbThemeService) {
    this.currentTheme = themeService.currentTheme
  }

  onToggleTheme(themeKey: string) {
    this.themeService.changeTheme(themeKey);
    this.analyticsService.trackEvent('switchTheme');
  }

  ngOnDestroy() {
    this.alive = false;
  }
}
