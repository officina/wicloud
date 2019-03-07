import {BaseEntity} from '../../_models/base-entity';
import {EntityIconMarker} from '../../shared/maps/map.models';
import {EntityWithIcon, IconObject} from '../../_models/entity-with-icon';
import {Colors} from '../../shared/constants/graph.constants';

export class LightFixtureWilamp implements EntityWithIcon, BaseEntity {
    private _desiredLightLevel = 0;
    public isSelected = false;
    constructor(
        public id?: number,
        public name?: string,
        public serialNumber?: string,
        public description?: string,
        public deviceType?: number,
        public lampType?: number,
        public lightZone?: number,
        public nominalPower?: number,
        public oldLampPower?: number,
        public logicId?: string,
        public pLCode?: string,
        public userOwner?: string,
        public userType?: string,
        public userAddress?: string,
        public userDistributionBox?: string,
        public userLightpoleMaterial?: string,
        public userLightpoleShape?: string,
        public userLightpoleHeight?: string,
        public userLampType?: string,
        public userLampPower?: string,
        public userLampModel?: string,
        public userLampManufacturer?: string,
        public timeZone?: number,
        public timeZoneCode?: string,
        public latitude?: number,
        public longitude?: number,
        public altitude?: number,
        public nodes?: BaseEntity[],
        public gatewayGatewayHostname?: string,
        public gateway?: number,
        public installationName?: string,
        public installation?: number,
        public lightProfileName?: string,
        public lightProfile?: number,
        public icon?: '/assets/app/media/img/wilamp-icons/0x/pole_icon.png',
    ) {
    }

/*   __   ___ ___ ___  ___  __   __       /     __   ___ ___ ___  ___  __   __
    / _` |__   |   |  |__  |__) /__`     /     /__` |__   |   |  |__  |__) /__`
    \__> |___  |   |  |___ |  \ .__/    /      .__/ |___  |   |  |___ |  \ .__/
 */

    get desiredLightLevel(): number {
        return this._desiredLightLevel;
    }
    set desiredLightLevel(theDesiredLightLevel: number) {
        this._desiredLightLevel = theDesiredLightLevel;
    }

/* JS Stick letters
     __   __              ___  ___     ___            __  ___    __        __
    |__) |__) | \  /  /\   |  |__     |__  |  | |\ | /  `  |  | /  \ |\ | /__`
    |    |  \ |  \/  /~~\  |  |___    |    \__/ | \| \__,  |  | \__/ | \| .__/
*/

    hashNumber(s) {
        let h = 0;
        for (let i = 0; i < s.length; i++) {
            h = Math.imul(31, h) + s.charCodeAt(i) | 0;
        }
        return h;
    }

    decimalColorToHTMLcolor(number) {
        // converts to a integer
        // let intnumber = number - 0;
        if (number != null) {
            const colorIndex = number % Object.keys(Colors).length;
            const colorKey = Object.keys(Colors)[colorIndex];
            const color = Colors[colorKey];
            return color;
            } else { return '#000000'; }
        /* // isolate the colors - really not necessary
        let red, green, blue;

        // needed since toString does not zero fill on left
        const template = '#000000';

        // in the MS Windows world RGB colors
        // are 0xBBGGRR because of the way Intel chips store bytes
        red = (intnumber & 0x0000ff) << 16;
        green = intnumber & 0x00ff00;
        blue = (intnumber & 0xff0000) >>> 16;

        // mask out each color and reverse the order
        intnumber = red | green | blue;

        // toString converts a number to a hexstring
        let HTMLcolor = intnumber.toString(16);

        // template adds # for standard HTML #RRGGBB
        HTMLcolor = template.substring(0, 7 - HTMLcolor.length) + HTMLcolor;

        return HTMLcolor;*/
    }

/*   __        __          __      ___            __  ___    __        __
    |__) |  | |__) |    | /  `    |__  |  | |\ | /  `  |  | /  \ |\ | /__`
    |    \__/ |__) |___ | \__,    |    \__/ | \| \__,  |  | \__/ | \| .__/
*/

    getIconObject(mapIconOptions: {} | undefined): IconObject {
        const resultIcon = new IconObject();
        let color = 'green';
        let filtersActive = false;
        if (mapIconOptions.hasOwnProperty('groupBy')) {
            switch (mapIconOptions['groupBy']) {
                case 'gateway':
                    color = this.decimalColorToHTMLcolor(this.gateway);
                    filtersActive = true;
                    break;
                case 'light_profile':
                    color = this.decimalColorToHTMLcolor(this.lightProfile);
                    filtersActive = true;
                    break;
                case 'light_zone':
                    color = this.decimalColorToHTMLcolor(this.lightZone);
                    filtersActive = true;
                    break;
                case 'lamp_wattage':
                    color = this.decimalColorToHTMLcolor(this.nominalPower);
                    filtersActive = true;
                    break;

                default:
                    filtersActive = false;
                    break;
            }
        }
        switch (this.deviceType) {
            case 10:
                if (!filtersActive) { color = '#0071bc'; }
                resultIcon.iconUrl = '<svg id="Livello_1" data-name="Livello 1" xmlns="http://www.w3.org/2000/svg" width="35" height="38" viewBox="0 0 538.61 584.95"><defs><style>.cls-1{fill:' + color + ';}.cls-2{fill:#fff;}.cls-3{fill:#333;}.cls-4{fill:none;stroke:#333;stroke-miterlimit:10;stroke-width:21px;}</style></defs><title>dcu_icon</title><path class="cls-1" d="M269.74,562.4a9.91,9.91,0,0,1-7.06-2.91l-39.94-39.94H58.25a37.48,37.48,0,0,1-37.44-37.44V60A37.48,37.48,0,0,1,58.25,22.55H480.36A37.49,37.49,0,0,1,517.81,60V482.11a37.49,37.49,0,0,1-37.45,37.44H316.74L276.8,559.49A9.9,9.9,0,0,1,269.74,562.4Z"/><path class="cls-2" d="M480.36,23.05a37,37,0,0,1,36.95,37V482.11a37,37,0,0,1-36.95,36.94H316.53l-.29.3-39.79,39.79a9.52,9.52,0,0,1-13.41,0l-39.8-39.79-.29-.3H58.25a37,37,0,0,1-36.94-36.94V60A37,37,0,0,1,58.25,23.05H480.36m0-1H58.25A38.06,38.06,0,0,0,20.31,60V482.11a38,38,0,0,0,37.94,37.94H222.54l39.79,39.79a10.51,10.51,0,0,0,14.83,0L317,520.05H480.36a38.06,38.06,0,0,0,37.95-37.94V60a38.06,38.06,0,0,0-37.95-37.95Z"/><circle class="cls-2" cx="274.31" cy="261.95" r="213"/><rect class="cls-3" x="265.8" y="195.14" width="17.14" height="37.23"/><polygon class="cls-3" points="254.71 200.9 274.37 166.85 294.03 200.9 254.71 200.9"/><rect class="cls-3" x="265.79" y="290.83" width="17.14" height="37.23"/><polygon class="cls-3" points="294.03 322.3 274.37 356.35 254.71 322.3 294.03 322.3"/><rect class="cls-3" x="301.48" y="253.73" width="37.23" height="17.14"/><polygon class="cls-3" points="332.96 242.64 367.01 262.3 332.96 281.96 332.96 242.64"/><rect class="cls-3" x="205.8" y="253.73" width="37.23" height="17.14"/><polygon class="cls-3" points="211.55 281.96 177.5 262.3 211.55 242.64 211.55 281.96"/><circle class="cls-4" cx="274.31" cy="261.95" r="143"/></svg>';
                resultIcon.iconSize = [35, 38];
                resultIcon.iconAnchor = [18, 38];
                break;
            default:
                if (this.isSelected) { color = 'red'; }
                resultIcon.iconUrl = '<svg id="Livello_1" data-name="Livello 1" xmlns="http://www.w3.org/2000/svg" width="25" height="35" viewBox="0 0 442.22 622"><defs><style>.cls-1{fill:' + color + ';}.cls-2{fill:#fff;}</style></defs><title>light_bulb_on</title><path class="cls-1" d="M221.11,621.19C216,614.76,163.18,547.32,111,467.07,60.57,389.61.5,284.07.5,221.11a220.6,220.6,0,0,1,376.6-156,219.13,219.13,0,0,1,64.62,156c0,63-60.08,168.51-110.47,246C279,547.32,226.17,614.77,221.11,621.19Z"/><path class="cls-2" d="M221.11,1A219.93,219.93,0,0,1,441.22,221.11c0,27.7-11.59,66-34.45,113.72-18.32,38.27-43.87,82.67-75.94,132C279.76,545.3,228.05,611.55,221.11,620.38c-6.94-8.83-58.65-75.08-109.73-153.59-32.06-49.29-57.61-93.69-75.93-132C12.59,287.07,1,248.81,1,221.11A219.93,219.93,0,0,1,221.11,1m0-1C99,0,0,99,0,221.11S221.11,622,221.11,622,442.22,343.23,442.22,221.11,343.23,0,221.11,0Z"/><circle class="cls-2" cx="220.88" cy="221.63" r="183.5"/><path d="M97.94,268.11a3.45,3.45,0,0,0-1.27,4.71h0l3.44,6a3.44,3.44,0,0,0,4.7,1.26h0l42.72-24.66A89.49,89.49,0,0,1,139.8,244ZM128.31,200H83.38a3.44,3.44,0,0,0-3.44,3.44v6.89a3.44,3.44,0,0,0,3.44,3.45h45.87A91.51,91.51,0,0,1,128.31,200ZM97.94,145.7l36.67,21.17a87.37,87.37,0,0,1,6.1-12.39l-35.88-20.72a3.46,3.46,0,0,0-4.71,1.26h0l-3.44,6A3.44,3.44,0,0,0,97.94,145.7Zm239.59,0a3.46,3.46,0,0,0,1.26-4.71h0l-3.45-6a3.44,3.44,0,0,0-4.7-1.26h0l-35.91,20.73a89.55,89.55,0,0,1,6.14,12.37ZM352.08,200H307.3a89.25,89.25,0,0,1-1.25,13.78h46a3.45,3.45,0,0,0,3.45-3.45v-6.89A3.45,3.45,0,0,0,352.08,200Zm-14.55,68.09L295.59,243.9a88.47,88.47,0,0,1-7.81,11.4l42.86,24.75a3.44,3.44,0,0,0,4.7-1.27l3.45-6A3.45,3.45,0,0,0,337.53,268.11ZM217.73,151.79A48.29,48.29,0,0,0,169.5,200a6.89,6.89,0,0,0,13.78,0,34.48,34.48,0,0,1,34.45-34.45,6.89,6.89,0,0,0,0-13.78Zm0-27.56c-44.33,0-75.84,36-75.78,75.89a75.32,75.32,0,0,0,18.75,49.75c11.05,12.6,21.66,33.12,22.58,39.71l0,32.38a6.84,6.84,0,0,0,1.15,3.8L195,341.63a6.89,6.89,0,0,0,5.73,3.07h34a6.87,6.87,0,0,0,5.73-3.07L251,325.76a6.84,6.84,0,0,0,1.15-3.8l0-32.38c1-6.77,11.62-27.21,22.58-39.71a75.74,75.74,0,0,0-57-125.64Zm20.65,195.63L231,330.92H204.44l-7.36-11.06v-2.72h41.3Zm0-16.5H197.07l0-13.78h41.37Zm26-62.57a147,147,0,0,0-21.78,35H192.85a147,147,0,0,0-21.78-35A61.77,61.77,0,0,1,155.75,200c-.08-33.15,26-62,62-62A62,62,0,0,1,264.4,240.79Z"/></svg>';
                resultIcon.iconSize = [25, 35];
                resultIcon.iconAnchor = [13, 35];
                break;
        }
        resultIcon.iconUrl = window.btoa(resultIcon.iconUrl);
        resultIcon.iconUrl = 'data:image/svg+xml;base64,' + resultIcon.iconUrl;
        return resultIcon;
    }

    getIconUrl(mapIconOptions: {} | undefined): string {
        if (this.icon === undefined) {
            let color = 'green';
            let filtersActive = false;
            if (mapIconOptions.hasOwnProperty('groupBy')) {
                switch (mapIconOptions['groupBy']) {
                    case 'gateway':
                        color = this.decimalColorToHTMLcolor(this.gateway);
                        filtersActive = true;
                        break;
                    case 'light_profile':
                        color = this.decimalColorToHTMLcolor(this.lightProfile);
                        filtersActive = true;
                        break;
                    case 'light_zone':
                        color = this.decimalColorToHTMLcolor(this.lightZone);
                        filtersActive = true;
                        break;
                    case 'lamp_wattage':
                        color = this.decimalColorToHTMLcolor(this.nominalPower);
                        filtersActive = true;
                        break;
                    default:
                        filtersActive = false;
                        break;
                }
            }
            let svgIcon = '<svg id="Livello_1" data-name="Livello 1" xmlns="http://www.w3.org/2000/svg" width="25" height="35" viewBox="0 0 442.22 622"><defs><style>.cls-1{fill:' + color + ';}.cls-2{fill:#fff;}</style></defs><title>light_bulb_on</title><path class="cls-1" d="M221.11,621.19C216,614.76,163.18,547.32,111,467.07,60.57,389.61.5,284.07.5,221.11a220.6,220.6,0,0,1,376.6-156,219.13,219.13,0,0,1,64.62,156c0,63-60.08,168.51-110.47,246C279,547.32,226.17,614.77,221.11,621.19Z"/><path class="cls-2" d="M221.11,1A219.93,219.93,0,0,1,441.22,221.11c0,27.7-11.59,66-34.45,113.72-18.32,38.27-43.87,82.67-75.94,132C279.76,545.3,228.05,611.55,221.11,620.38c-6.94-8.83-58.65-75.08-109.73-153.59-32.06-49.29-57.61-93.69-75.93-132C12.59,287.07,1,248.81,1,221.11A219.93,219.93,0,0,1,221.11,1m0-1C99,0,0,99,0,221.11S221.11,622,221.11,622,442.22,343.23,442.22,221.11,343.23,0,221.11,0Z"/><circle class="cls-2" cx="220.88" cy="221.63" r="183.5"/><path d="M97.94,268.11a3.45,3.45,0,0,0-1.27,4.71h0l3.44,6a3.44,3.44,0,0,0,4.7,1.26h0l42.72-24.66A89.49,89.49,0,0,1,139.8,244ZM128.31,200H83.38a3.44,3.44,0,0,0-3.44,3.44v6.89a3.44,3.44,0,0,0,3.44,3.45h45.87A91.51,91.51,0,0,1,128.31,200ZM97.94,145.7l36.67,21.17a87.37,87.37,0,0,1,6.1-12.39l-35.88-20.72a3.46,3.46,0,0,0-4.71,1.26h0l-3.44,6A3.44,3.44,0,0,0,97.94,145.7Zm239.59,0a3.46,3.46,0,0,0,1.26-4.71h0l-3.45-6a3.44,3.44,0,0,0-4.7-1.26h0l-35.91,20.73a89.55,89.55,0,0,1,6.14,12.37ZM352.08,200H307.3a89.25,89.25,0,0,1-1.25,13.78h46a3.45,3.45,0,0,0,3.45-3.45v-6.89A3.45,3.45,0,0,0,352.08,200Zm-14.55,68.09L295.59,243.9a88.47,88.47,0,0,1-7.81,11.4l42.86,24.75a3.44,3.44,0,0,0,4.7-1.27l3.45-6A3.45,3.45,0,0,0,337.53,268.11ZM217.73,151.79A48.29,48.29,0,0,0,169.5,200a6.89,6.89,0,0,0,13.78,0,34.48,34.48,0,0,1,34.45-34.45,6.89,6.89,0,0,0,0-13.78Zm0-27.56c-44.33,0-75.84,36-75.78,75.89a75.32,75.32,0,0,0,18.75,49.75c11.05,12.6,21.66,33.12,22.58,39.71l0,32.38a6.84,6.84,0,0,0,1.15,3.8L195,341.63a6.89,6.89,0,0,0,5.73,3.07h34a6.87,6.87,0,0,0,5.73-3.07L251,325.76a6.84,6.84,0,0,0,1.15-3.8l0-32.38c1-6.77,11.62-27.21,22.58-39.71a75.74,75.74,0,0,0-57-125.64Zm20.65,195.63L231,330.92H204.44l-7.36-11.06v-2.72h41.3Zm0-16.5H197.07l0-13.78h41.37Zm26-62.57a147,147,0,0,0-21.78,35H192.85a147,147,0,0,0-21.78-35A61.77,61.77,0,0,1,155.75,200c-.08-33.15,26-62,62-62A62,62,0,0,1,264.4,240.79Z"/></svg>';
            switch (this.deviceType) {
                case 10:
                    if (!filtersActive) {
                        color = '#0071bc';
                    }
                    svgIcon = '<svg id="Livello_1" data-name="Livello 1" xmlns="http://www.w3.org/2000/svg" width="35" height="38" viewBox="0 0 538.61 584.95"><defs><style>.cls-1{fill:' + color + ';}.cls-2{fill:#fff;}.cls-3{fill:#333;}.cls-4{fill:none;stroke:#333;stroke-miterlimit:10;stroke-width:21px;}</style></defs><title>dcu_icon</title><path class="cls-1" d="M269.74,562.4a9.91,9.91,0,0,1-7.06-2.91l-39.94-39.94H58.25a37.48,37.48,0,0,1-37.44-37.44V60A37.48,37.48,0,0,1,58.25,22.55H480.36A37.49,37.49,0,0,1,517.81,60V482.11a37.49,37.49,0,0,1-37.45,37.44H316.74L276.8,559.49A9.9,9.9,0,0,1,269.74,562.4Z"/><path class="cls-2" d="M480.36,23.05a37,37,0,0,1,36.95,37V482.11a37,37,0,0,1-36.95,36.94H316.53l-.29.3-39.79,39.79a9.52,9.52,0,0,1-13.41,0l-39.8-39.79-.29-.3H58.25a37,37,0,0,1-36.94-36.94V60A37,37,0,0,1,58.25,23.05H480.36m0-1H58.25A38.06,38.06,0,0,0,20.31,60V482.11a38,38,0,0,0,37.94,37.94H222.54l39.79,39.79a10.51,10.51,0,0,0,14.83,0L317,520.05H480.36a38.06,38.06,0,0,0,37.95-37.94V60a38.06,38.06,0,0,0-37.95-37.95Z"/><circle class="cls-2" cx="274.31" cy="261.95" r="213"/><rect class="cls-3" x="265.8" y="195.14" width="17.14" height="37.23"/><polygon class="cls-3" points="254.71 200.9 274.37 166.85 294.03 200.9 254.71 200.9"/><rect class="cls-3" x="265.79" y="290.83" width="17.14" height="37.23"/><polygon class="cls-3" points="294.03 322.3 274.37 356.35 254.71 322.3 294.03 322.3"/><rect class="cls-3" x="301.48" y="253.73" width="37.23" height="17.14"/><polygon class="cls-3" points="332.96 242.64 367.01 262.3 332.96 281.96 332.96 242.64"/><rect class="cls-3" x="205.8" y="253.73" width="37.23" height="17.14"/><polygon class="cls-3" points="211.55 281.96 177.5 262.3 211.55 242.64 211.55 281.96"/><circle class="cls-4" cx="274.31" cy="261.95" r="143"/></svg>';
                    break;
                default:
                    if (this.isSelected) {
                        color = 'red';
                    }
                    // return 'data:image/svg+xml;utf-8, \
                    svgIcon = '<svg id="Livello_1" data-name="Livello 1" xmlns="http://www.w3.org/2000/svg" width="25" height="35" viewBox="0 0 442.22 622"><defs><style>.cls-1{fill:' + color + ';}.cls-2{fill:#fff;}</style></defs><title>light_bulb_on</title><path class="cls-1" d="M221.11,621.19C216,614.76,163.18,547.32,111,467.07,60.57,389.61.5,284.07.5,221.11a220.6,220.6,0,0,1,376.6-156,219.13,219.13,0,0,1,64.62,156c0,63-60.08,168.51-110.47,246C279,547.32,226.17,614.77,221.11,621.19Z"/><path class="cls-2" d="M221.11,1A219.93,219.93,0,0,1,441.22,221.11c0,27.7-11.59,66-34.45,113.72-18.32,38.27-43.87,82.67-75.94,132C279.76,545.3,228.05,611.55,221.11,620.38c-6.94-8.83-58.65-75.08-109.73-153.59-32.06-49.29-57.61-93.69-75.93-132C12.59,287.07,1,248.81,1,221.11A219.93,219.93,0,0,1,221.11,1m0-1C99,0,0,99,0,221.11S221.11,622,221.11,622,442.22,343.23,442.22,221.11,343.23,0,221.11,0Z"/><circle class="cls-2" cx="220.88" cy="221.63" r="183.5"/><path d="M97.94,268.11a3.45,3.45,0,0,0-1.27,4.71h0l3.44,6a3.44,3.44,0,0,0,4.7,1.26h0l42.72-24.66A89.49,89.49,0,0,1,139.8,244ZM128.31,200H83.38a3.44,3.44,0,0,0-3.44,3.44v6.89a3.44,3.44,0,0,0,3.44,3.45h45.87A91.51,91.51,0,0,1,128.31,200ZM97.94,145.7l36.67,21.17a87.37,87.37,0,0,1,6.1-12.39l-35.88-20.72a3.46,3.46,0,0,0-4.71,1.26h0l-3.44,6A3.44,3.44,0,0,0,97.94,145.7Zm239.59,0a3.46,3.46,0,0,0,1.26-4.71h0l-3.45-6a3.44,3.44,0,0,0-4.7-1.26h0l-35.91,20.73a89.55,89.55,0,0,1,6.14,12.37ZM352.08,200H307.3a89.25,89.25,0,0,1-1.25,13.78h46a3.45,3.45,0,0,0,3.45-3.45v-6.89A3.45,3.45,0,0,0,352.08,200Zm-14.55,68.09L295.59,243.9a88.47,88.47,0,0,1-7.81,11.4l42.86,24.75a3.44,3.44,0,0,0,4.7-1.27l3.45-6A3.45,3.45,0,0,0,337.53,268.11ZM217.73,151.79A48.29,48.29,0,0,0,169.5,200a6.89,6.89,0,0,0,13.78,0,34.48,34.48,0,0,1,34.45-34.45,6.89,6.89,0,0,0,0-13.78Zm0-27.56c-44.33,0-75.84,36-75.78,75.89a75.32,75.32,0,0,0,18.75,49.75c11.05,12.6,21.66,33.12,22.58,39.71l0,32.38a6.84,6.84,0,0,0,1.15,3.8L195,341.63a6.89,6.89,0,0,0,5.73,3.07h34a6.87,6.87,0,0,0,5.73-3.07L251,325.76a6.84,6.84,0,0,0,1.15-3.8l0-32.38c1-6.77,11.62-27.21,22.58-39.71a75.74,75.74,0,0,0-57-125.64Zm20.65,195.63L231,330.92H204.44l-7.36-11.06v-2.72h41.3Zm0-16.5H197.07l0-13.78h41.37Zm26-62.57a147,147,0,0,0-21.78,35H192.85a147,147,0,0,0-21.78-35A61.77,61.77,0,0,1,155.75,200c-.08-33.15,26-62,62-62A62,62,0,0,1,264.4,240.79Z"/></svg>';
            }
            svgIcon = window.btoa(svgIcon);
            return 'data:image/svg+xml;base64,' + svgIcon;
        }
        return this.icon;
    }
}
