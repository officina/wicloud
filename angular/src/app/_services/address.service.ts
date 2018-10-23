import { Injectable } from '@angular/core';
import {environment} from '../../environments/environment';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class AddressService {

  constructor(private http: HttpClient) { }

  getAddressById(id: number) {
    return this.http.get<any>(`${environment.apiUrl}/wicloud/api/backend/address/retrieve/${id}/`);
  }
}
