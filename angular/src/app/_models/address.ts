export class Address {
  constructor(
    public id?: number,
    public description?: string,
    public fullName?: any,
    public street?: any,
    public notes?: string,
    public country?: string,
    public houseNumber?: string,
    public zipCode?: number,
    public city?: string,
    public lat?: number,
    public lng?: any[],
  ) {
  }
}
