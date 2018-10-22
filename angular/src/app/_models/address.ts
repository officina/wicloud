export class Address {
  constructor(
    public id?: number,
    public description?: string,
    public full_name?: any,
    public street?: any,
    public notes?: string,
    public house_number?: string,
    public zip_code?: number,
    public city?: string,
    public lat?: number,
    public lng?: any[],
  ) {
  }
}
