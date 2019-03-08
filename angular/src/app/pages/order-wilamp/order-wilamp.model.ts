import {BaseEntity} from '../../_models/base-entity';

export class OrderWilamp implements BaseEntity {
    constructor(
        public id?: number,
        public name?: string,
        public description?: string,
        public notes?: string,
        public orderDate?: any,
        public preparationDate?: any,
        public totalAmount?: number,
        public nodes?: BaseEntity[],
        public gateways?: BaseEntity[],
        public customerCompanyName?: string,
        public customer?: number,
        public shippings?: BaseEntity[],
    ) {
    }
}
