import {AfterViewInit, Component, Input, OnDestroy, OnInit} from '@angular/core';
import { LocalDataSource } from 'ng2-smart-table';
import {JhiEventManager} from 'ng-jhipster';
import {Subscription} from 'rxjs';
import {GlobalDatabaseService} from '../../shared/global-database/global-database.service';
import {
    GLOBALDATABASE__LIGHT_FIXTURES_FETCHED,
    INSTALLATION__SELECTED_INSTALLATION_CHANGED,
} from '../../shared/constants/events.constants';

@Component({
  selector: 'ngx-light-fixture-list',
  templateUrl: './light-fixture-list.component.html',
    styleUrls: [ './light-fixture-list.component.scss'],
})
export class LightFixtureListComponent implements AfterViewInit, OnDestroy {
  private eventSubscriberLightFixturesFetched: Subscription;
  private eventSubscriberInstallationChanged: Subscription;

  settings = {
    actions: false,
    pager: {
      display: false, // set this to false so as to prevent the Page# //
      // perPage: 10, //we need to remove this perPage limiter
    },
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
      userDistributionBox: {
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
      },
    },
  };

  source: LocalDataSource = new LocalDataSource();

  constructor(
      private globalDatabase: GlobalDatabaseService,
      private eventManager: JhiEventManager,
  ) {
  }

  ngAfterViewInit(): void {
    this.registerChangeInInstallations();
    this.updateTable();
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
    this.eventSubscriberInstallationChanged = this.eventManager.subscribe(
        INSTALLATION__SELECTED_INSTALLATION_CHANGED,
        (response) => this.updateTable(),
    )
  }

  ngOnDestroy() {
    this.eventManager.destroy(this.eventSubscriberLightFixturesFetched);
    this.eventManager.destroy(this.eventSubscriberInstallationChanged);
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
