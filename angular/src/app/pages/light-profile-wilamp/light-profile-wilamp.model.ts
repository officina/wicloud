import {BaseEntity} from '../../_models/base-entity';

export class LightProfileWilamp implements BaseEntity {
    constructor(
        public id?: number,
        public name?: string,
        public description?: string,
        public type?: string,
        public reference?: string,
        public profileCRC?: number,
        public lightProfileId?: number,
        public gatewayId?: number,
        public enabled?: boolean,
        public lightProfileSlots?: BaseEntity[],
    ) {
        this.enabled = false;
    }
}
