import {BaseEntity} from '../../_models/base-entity';

export class NodeModulesWilamp implements BaseEntity {
    constructor(
        public id?: number,
        public name?: string,
        public lightManagementName?: string,
        public lightManagementId?: number,
        public energyMeterName?: string,
        public energyMeterId?: number,
        public twilightManagementName?: string,
        public twilightManagementId?: number,
        public motionManagementName?: string,
        public motionManagementId?: number,
        public nodeId?: number,
    ) {
    }
}
