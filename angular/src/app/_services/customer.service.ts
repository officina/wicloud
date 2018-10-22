import { Injectable } from '@angular/core';
import {environment} from '../../environments/environment';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class CustomerService {

  constructor(private http: HttpClient) { }

  getCustomerById(id: number) {

    return this.http.get<any>(`${environment.apiUrl}/wicloud/api/backend/customer/retrieve/${id}/`);
  }
}
