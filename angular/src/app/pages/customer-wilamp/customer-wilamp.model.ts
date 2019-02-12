import {BaseEntity} from '../../_models/base-entity';
import {User} from '../../_models';

export class CustomerWilamp implements BaseEntity {
    constructor(
        public id?: number,
        public companyName?: string,
        public description?: string,
        public contacts?: BaseEntity[],
        public users?: User[],
        public installations?: BaseEntity[],
    ) {
    }
}
