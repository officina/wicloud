import {Customer} from './customer';
import {Address} from './address';

export class Installation {
    constructor(
        public id?: number,
        public name?: string,
        public description?: string,
        public preparationDate?: any,
        public installationDate?: any,
        public notes?: string,
        public address?: Address,
        public customer?: Customer,
        public customerId?: number,
        public gateways?: any[],

        // TEMP
        public notifications?: any[],
        public overview?: any[],
    ) {
    }



}
