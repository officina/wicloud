import { Component, OnInit } from '@angular/core';
import {GlobalDatabaseService} from '../../shared/global-database/global-database.service';

@Component({
  selector: '.m-grid__item.m-grid__item--fluid.m-wrapper',
  templateUrl: './nodes-dashboard.component.html',
  styles: []
})
export class NodesDashboardComponent implements OnInit {

  constructor(
      public globalDatabase: GlobalDatabaseService
  ) { }

  ngOnInit() {
  }

}
