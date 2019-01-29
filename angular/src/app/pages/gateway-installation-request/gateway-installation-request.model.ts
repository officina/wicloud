import {BaseEntity} from '../../_models/base-entity';

export class GatewayInstallationRequest implements BaseEntity {
    constructor(
        public id?: number,
        public macAddress?: string,
        public gatewayUUID?: string,
        public gatewayIP?: string,
        public gatewayType?: string,
        public fwVersion?: string,
        public creationDate?: any,
        public deviceName?: string,
        public hardwareModel?: string,
        public hardwareInformations?: string,
        public readyToInstall?: boolean,
        public startInstallationTimestamp?: any,
        public endInstallationTimestamp?: any,
        public currentInstallationStep?: string,
        public errorMessage?: string,
        public errorDetected?: boolean,
        public installationConcluded?: boolean,
        public gatewayGatewayHostname?: string,
        public gatewayId?: number,
    ) {
        this.readyToInstall = false;
        this.errorDetected = false;
        this.installationConcluded = false;
    }
}
