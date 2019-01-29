import {BaseEntity} from '../../_models/base-entity';

export class AddressWilamp implements BaseEntity {
    constructor(
        public id?: number,
        public addressDescription?: string,
        public fullName?: string,
        public street?: string,
        public houseNumber?: string,
        public zipCode?: string,
        public city?: string,
        public country?: string,
        public lat?: string,
        public lng?: string,
        public timezoneCode?: string,
        public contacts?: BaseEntity[],
    ) {
    }
}
