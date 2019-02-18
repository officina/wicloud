import {BaseEntity} from '../../_models/base-entity';

export class LightFixtureWilamp implements BaseEntity {
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
        public gatewayId?: number,
        public installationName?: string,
        public installationId?: number,
        public lightProfileName?: string,
        public lightProfileId?: number,
    ) {
    }
}