import { Component, Input } from '@angular/core';
import { LocalDataSource } from 'ng2-smart-table';

import {GlobalDatabaseService} from '../../../shared/global-database/global-database.service';
import {
    GLOBALDATABASE__GATEWAYS_FETCHED,
    GLOBALDATABASE__INSTALLATION_FETCHED, GLOBALDATABASE__INSTALLATION_STATISTICS_BY_NODEID_FETCHED,
    GLOBALDATABASE__INSTALLATION_WEEKLY_STATISTICS_FETCHED, GLOBALDATABASE__INSTALLATION_WEEKLY_STATISTICS_FETCHING,
    GLOBALDATABASE__LIGHT_FIXTURES_FETCHED,
    INSTALLATION__SELECTED_ID_CHANGED,
} from '../../../shared/constants/events.constants';
import {JhiEventManager} from 'ng-jhipster';
import {Subscription} from 'rxjs';

@Component({
  selector: 'ngx-installation-light-fixture-list-card',
  templateUrl: './installation-light-fixture-list.component.html',
})
export class InstallationLightFixtureListComponent {
  private eventSubscriberLightFixturesFetched: Subscription;

  settings = {
    actions: false,
    columns: {
      name: {
        title: 'Name',
        type: 'string',
      },
      serialNumber: {
        title: 'Serial number',
        type: 'string',
      },
      nominalPower: {
        title: 'Nominal Power',
        type: 'string',
      },
      /*userDistributionBox: {
        title: 'Distribution box',
        type: 'string',
      },
      gateway: {
        title: 'DCU',
        type: 'number',
      },
      lightProfile: {
        title: 'Light profile',
        type: 'number',
      },*/
    },
  };

  source: LocalDataSource = new LocalDataSource();

  constructor(
      private globalDatabase: GlobalDatabaseService,
      private eventManager: JhiEventManager,
  ) {
    this.registerChangeInInstallations();
  }

  updateTable(): void {
    const lightFixtures = this.globalDatabase.selectedInstallation.lightFixtures;
    this.source.load(lightFixtures);
  }
  onDeleteConfirm(event): void {
    if (window.confirm('Are you sure you want to delete?')) {
      event.confirm.resolve();
    } else {
      event.confirm.reject();
    }
  }

  registerChangeInInstallations() {
    this.eventSubscriberLightFixturesFetched = this.eventManager.subscribe(
        GLOBALDATABASE__LIGHT_FIXTURES_FETCHED,
        (response) => this.updateTable(),
    );
  }

}

/***
 * in HTML:
<table><tbody><ng2-smart-table [settings]="gridSettings" [source]="source" ></ng2-smart-table</tbody></table>

in CSS:
tbody { height: 120px; overflow-y: auto; }

If you wish to remove the pagination feature as well then all we need to do is remove the "perPage" attribute of the gridSettings of the [settings] i.e.
(<ng2-smart-table [settings]="gridSettings" [source]="source" ></ng2-smart-table>).

in TYPESCRIPT:

gridSettings = { actions:{ //action settings goes here }, pager: { display: false, //set this to false so as to prevent the Page# //perPage: 10, //we need to remove this perPage limiter }, columns: { //columns info goes here } };


 */
