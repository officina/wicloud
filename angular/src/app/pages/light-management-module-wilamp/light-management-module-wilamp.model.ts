import {BaseEntity} from '../../_models/base-entity';

export class LightManagementModuleWilamp implements BaseEntity {
    constructor(
        public id?: number,
        public name?: string,
        public description?: string,
        public deviceType?: number,
        public lampType?: number,
        public timerAutoMode?: number,
        public timerHPSProtection?: number,
        public lightZone?: number,
        public lightProfileId?: number,
        public lightProfileCRC?: number,
        public nodeModulesId?: number,
        public lightManagementMeasures?: BaseEntity[],
    ) {
    }
}
