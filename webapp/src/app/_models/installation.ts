export class Installation {
    constructor(
        public id?: number,
        public name?: string,
        public description?: string,
        public preparationDate?: any,
        public installationDate?: any,
        public notes?: string,
        public addressAddressDescription?: string,
        public addressId?: number,
        public customerCompanyName?: string,
        public customerId?: number,
        public gateways?: any[],
    ) {
    }
}
