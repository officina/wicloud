import { Component, OnInit } from '@angular/core';
import {GlobalDatabaseService} from '../../../shared/global-database/global-database.service';

/**
 * https://www.jqwidgets.com/angular/angular-grid/index.htm?gclid=CjwKCAiA2fjjBRAjEiwAuewS_Qk4-DOb3aLxtQCddSDLXNZgvTWBoJihMBblgZQp5Hv9iLZgox6LIhoC3l8QAvD_BwE
 *
 */
@Component({
  selector: 'ngx-nodes-dashboard',
  templateUrl: './nodes-dashboard.component.html',
  styles: [],
})
export class NodesDashboardComponent implements OnInit {

  constructor(
      public globalDatabase: GlobalDatabaseService,
  ) { }

  ngOnInit() {
  }

}
