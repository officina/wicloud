import {Component, Input, OnInit, AfterViewInit, OnChanges} from '@angular/core';
import {NodeWilamp} from '../../pages/node-wilamp';
import { DomSanitizer } from '@angular/platform-browser';
import {GlobalDatabaseService} from '../../shared/global-database/global-database.service';
import {KWtoCO2Factor} from '../../shared/constants/graph.constants';
import { NgbActiveModal, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import {Router} from '@angular/router';
import {Helpers} from '../../shared';

@Component({
  selector: 'node-small-details-widget',
  templateUrl: './node-small-details-widget.component.html',
  styleUrls: ['node-small-details-widget.component.css'],

})
export class NodeSmallDetailsWidgetComponent implements OnInit, AfterViewInit, OnChanges {
    @Input() node: NodeWilamp;
    currentValue = 20;
    sliderValue = 30;

    public driverLabel = '1-10v';
    public lampLabel = 'LED';
    public burningTimeLabel = 'n/a';
    public workingTimeLabel = 'n/a';
    public lastMeasureReceivedLabel = 'n/a';
    public profileLabel = 'n/a';
    public lampConsumptionLabel = 'n/a';
    public zoneLabel = 'n/a';
    public lampNominalPowerLabel = 'n/a';
    public co2Label = 'n/a';
    public nodesNumber = 'n/a';
    public onlineNodes = 'n/a';
    public offlineNodes = 'n/a';
    public alertsLabel = 'n/a';
    public onlineTickets = 'n/a';

    constructor(
      private _DomSanitizationService: DomSanitizer,
      public globalDatabase: GlobalDatabaseService,
      private modalService: NgbModal,
      private _router: Router,
    ) { }

    ngOnInit() {
    }

    ngAfterViewInit() {
        this.updateLabels();
    }

    ngOnChanges() {
        this.updateLabels();
    }

    updateLabels() {
        try {
            if (this.globalDatabase.selectedInstallation.statisticsByNodeIdHMap.size > 0) {
                const nodeStatistics = this.globalDatabase.selectedInstallation.statisticsByNodeIdHMap.get(this.node.id);
                if (nodeStatistics != null) {
                    this.burningTimeLabel = Helpers.prettyDuration(nodeStatistics.burningTime * 60) + '';
                    this.workingTimeLabel = Helpers.prettyDuration(nodeStatistics.nodeLife * 60) + '';
                    this.co2Label = Helpers.round((nodeStatistics.sumEnergyOldLamps - nodeStatistics.sumEnergy) * KWtoCO2Factor) + ' Kg';
                    this.lampConsumptionLabel = Helpers.formatPowerConsumption(nodeStatistics.sumEnergy);
                }
            }
            if (this.node.lightProfileId === 0) {
                this.profileLabel = 'n/d';
            } else {
                if (this.globalDatabase.lightProfiles.has(this.node.lightProfileId)) {
                    const lightProfile = this.globalDatabase.lightProfiles.get(this.node.lightProfileId);
                    this.profileLabel = '' + lightProfile.name;
                } else {
                    this.profileLabel = '' + this.node.lightProfileId;
                }
            }
            if (this.node.nominalPower != null && !isNaN(this.node.nominalPower)) {
                this.lampNominalPowerLabel = this.node.nominalPower + ' W';
            } else { this.lampNominalPowerLabel = 'n/a'; }
            if (this.node.lightZone === 0) {
                this.zoneLabel = 'n/d';
            } else {
                this.zoneLabel = '' + this.node.lightZone;
            }
            if (this.node.nodeType === 10) {
                const gatewayNodes = this.globalDatabase.selectedInstallation.getGatewayNodes(this.node.gatewayId).length;
                this.nodesNumber = gatewayNodes + '';
                this.onlineNodes = '0';
                this.offlineNodes = gatewayNodes + '';
            }
        } catch (e) {
        }
    }

    /* Icons */
    getConnectIcon() {

     // document.querySelector(".svgClass").getSVGDocument().getElementById("svgInternalID").setAttribute("fill", "red")

      return 'data:image/svg+xml;utf-8, \
            \<svg width="38px" height="35px" viewBox="0 0 38 35" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">\n' +
          '    <!-- Generator: Sketch 51.3 (57544) - http://www.bohemiancoding.com/sketch -->\n' +
          '    <g id="Asset" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">\n' +
          '        <g id="Connect" fill="#56B68B">\n' +
          '            <path d="M32.0518308,32.564 C29.8984974,32.564 28.1466,30.8159444 28.1466,28.6673333 C28.1466,26.51775 29.8984974,24.7696944 32.0518308,24.7696944 C34.2051641,24.7696944 35.9570615,26.51775 35.9570615,28.6673333 C35.9570615,30.8159444 34.2051641,32.564 32.0518308,32.564 M5.55511282,20.8555278 C3.40177949,20.8555278 1.64890769,19.1074722 1.64890769,16.9588611 C1.64890769,14.81025 3.40177949,13.0621944 5.55511282,13.0621944 C7.70844615,13.0621944 9.46034359,14.81025 9.46034359,16.9588611 C9.46034359,19.1074722 7.70844615,20.8555278 5.55511282,20.8555278 M32.0518308,1.64538889 C34.2051641,1.64538889 35.9570615,3.39344444 35.9570615,5.54302778 C35.9570615,7.69163889 34.2051641,9.43969444 32.0518308,9.43969444 C29.8984974,9.43969444 28.1466,7.69163889 28.1466,5.54302778 C28.1466,3.39344444 29.8984974,1.64538889 32.0518308,1.64538889 M32.0518308,23.1246944 C30.0748564,23.1246944 28.3366,24.1610833 27.3515231,25.7176111 L10.880959,18.5309444 C11.0290615,18.0321944 11.1099333,17.50525 11.1099333,16.9588611 C11.1099333,16.5067778 11.0543949,16.0683056 10.9511128,15.6483056 L27.3515231,8.49177778 C28.3366,10.0483056 30.0748564,11.0856667 32.0518308,11.0856667 C35.1152154,11.0856667 37.6066513,8.59872222 37.6066513,5.54302778 C37.6066513,2.48636111 35.1152154,0.000388888889 32.0518308,0.000388888889 C28.9884462,0.000388888889 26.4970103,2.48636111 26.4970103,5.54302778 C26.4970103,6.04177778 26.564241,6.52497222 26.688959,6.98483333 L10.3265487,14.1248333 C9.35608718,12.5041389 7.58080513,11.4162222 5.55511282,11.4162222 C2.49172821,11.4162222 0.000292307692,13.9021944 0.000292307692,16.9588611 C0.000292307692,20.0155278 2.49172821,22.5015 5.55511282,22.5015 C7.48336923,22.5015 9.18557436,21.5146944 10.1813692,20.0213611 L26.688959,27.2245556 C26.564241,27.6844167 26.4970103,28.1676111 26.4970103,28.6673333 C26.4970103,31.7230278 28.9884462,34.2099722 32.0518308,34.2099722 C35.1152154,34.2099722 37.6066513,31.7230278 37.6066513,28.6673333 C37.6066513,25.6106667 35.1152154,23.1246944 32.0518308,23.1246944" id="Fill-1"></path>\n' +
          '        </g>\n' +
          '    </g>\n' +
          '</svg>';
    }

    /*Method to listen for onChange event from slider*/
    onSliderChange(selectedValues: number[]) {
        this.currentValue = selectedValues[0];
    }

    openModalGatewayAdmin() {
        this._router.navigate(['../gateway-wilamp', this.node.gatewayId ]);
    }

}
