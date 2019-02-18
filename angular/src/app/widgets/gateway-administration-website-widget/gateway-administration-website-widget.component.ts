import {Component, Input, OnInit, AfterViewInit} from '@angular/core';
import {NodeWilamp} from '../../pages/node-wilamp';
import { DomSanitizer } from '@angular/platform-browser';
import {
    GLOBALDATABASE__INSTALLATION_WEEKLY_STATISTICS_FETCHED,
    INSTALLATION_DASHBOARD__DAILY_STATISTICS_FETCHED,
    INSTALLATION_DASHBOARD__MONTHLY_STATISTICS_FETCHED, INSTALLATION_DASHBOARD__WEEKLY_STATISTICS_FETCHED
} from '../../shared/constants/events.constants';
import {KWtoCO2Factor} from '../../shared/constants/graph.constants';
import {GlobalDatabaseService} from '../../shared/global-database/global-database.service';
import DateTimeFormat = Intl.DateTimeFormat;
import {JhiEventManager} from 'ng-jhipster';
import {Helpers} from '../../shared';
import {Subscription} from 'rxjs/Rx';
import {GatewayWilamp} from '../../pages/gateway-wilamp';

@Component({
  selector: 'gateway-administration-website-widget',
  templateUrl: './gateway-administration-website-widget.component.html',
  styleUrls: ['gateway-administration-website-widget.component.css']

})
export class GatewayAdministrationWebsiteWidgetComponent implements OnInit, AfterViewInit {
    @Input() gateway: GatewayWilamp;

    constructor(
        private _DomSanitizationService: DomSanitizer,
        public globalDatabase: GlobalDatabaseService,
        private eventManager: JhiEventManager
    ) { }

    ngOnInit() {
        console.warn(this.gateway.notes);
    }

    ngAfterViewInit() {
        if (this.gateway != null) {
            if (this.gateway.notes !== null) {
                $('#gateway_content').height('100%').width('100%');
                $('#gateway_content').html('<iframe src="' + this.gateway.notes + '" name="iframe" width="100%" height="100%"></iframe>');
                // $('#gateway_content').html('<object type="text/html" data="' + this.gateway.notes + '"  width="100%" height="100%" style="overflow:auto;"></object>');
            } else {
                $('#gateway_content').height(0).width(0);
            }
        }
    }

}
