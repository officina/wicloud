import {BaseEntity} from '../../_models/base-entity';

export class GatewayWilamp implements BaseEntity {
    constructor(
        public id?: number,
        public name?: string,
        public description?: string,
        public gatewayUUID?: string,
        public gatewayHostname?: string,
        public gatewayType?: number,
        public notes?: string,
        public creationDate?: any,
        public serialNumber?: string,
        public deviceName?: string,
        public hardwareModel?: string,
        public macAddress?: string,
        public coordinatorMac?: string,
        public fileNameEncryptionInfo?: string,
        public hardwareInformations?: string,
        public readyToReceiveData?: boolean,
        public installationName?: string,
        public installationId?: number,
        public shippingShippingDate?: string,
        public shippingId?: number,
        public nodes?: BaseEntity[],
        public vpnConnections?: BaseEntity[],
        public orderId?: number,
        public gatewayInstallationRequestId?: number,
        public gatewayOnline?: boolean,
    ) {
        this.readyToReceiveData = false;
        this.gatewayOnline = false;
    }
}
