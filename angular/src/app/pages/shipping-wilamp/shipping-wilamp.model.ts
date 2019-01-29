import {BaseEntity} from '../../_models/base-entity';

export class ShippingWilamp implements BaseEntity {
    constructor(
        public id?: number,
        public courier?: string,
        public trackingCode?: string,
        public shippingDate?: string,
        public estimatedArrival?: string,
        public transportDocument?: string,
        public isArrived?: boolean,
        public nodes?: BaseEntity[],
        public gateways?: BaseEntity[],
        public shippingContactContactDescription?: string,
        public shippingContactId?: number,
        public orders?: BaseEntity[],
    ) {
        this.isArrived = false;
    }
}
