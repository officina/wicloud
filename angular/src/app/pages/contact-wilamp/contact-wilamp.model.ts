import {BaseEntity} from '../../_models/base-entity';

export class ContactWilamp implements BaseEntity {
    constructor(
        public id?: number,
        public contactDescription?: string,
        public firstName?: string,
        public lastName?: string,
        public phone?: string,
        public mobile?: string,
        public email?: string,
        public addresses?: BaseEntity[],
        public customerCompanyName?: string,
        public customerId?: number,
    ) {
    }
}
