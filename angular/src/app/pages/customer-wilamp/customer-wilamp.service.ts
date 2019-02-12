
import {map} from 'rxjs/operators';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { CustomerWilamp } from './customer-wilamp.model';
import { createRequestOption } from '../../shared';
import {environment} from '../../../environments/environment';

export type EntityResponseType = HttpResponse<CustomerWilamp>;

@Injectable()
export class CustomerWilampService {

    private resourceUrl =  `${environment.apiUrl}/api/customer`;
    private resourceSearchUrl =  `${environment.apiUrl}/api/_search/customer`;

    constructor(private http: HttpClient) { }

    create(customer: CustomerWilamp): Observable<EntityResponseType> {
        const copy = this.convert(customer);
        return this.http.post<CustomerWilamp>(this.resourceUrl, copy, { observe: 'response' }).pipe(
            map((res: EntityResponseType) => this.convertResponse(res)));
    }

    update(customer: CustomerWilamp): Observable<EntityResponseType> {
        const copy = this.convert(customer);
        return this.http.put<CustomerWilamp>(this.resourceUrl, copy, { observe: 'response' }).pipe(
            map((res: EntityResponseType) => this.convertResponse(res)));
    }

    find(id: number): Observable<EntityResponseType> {
        return this.http.get<CustomerWilamp>(`${this.resourceUrl}/${id}`, { observe: 'response'}).pipe(
            map((res: EntityResponseType) => this.convertResponse(res)));
    }

    query(req?: any): Observable<HttpResponse<CustomerWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<CustomerWilamp[]>(`${this.resourceUrl}/`, { params: options, observe: 'response' }).pipe(
            map((res: HttpResponse<CustomerWilamp[]>) => this.convertArrayResponse(res)));
    }

    delete(id: number): Observable<HttpResponse<any>> {
        return this.http.delete<any>(`${this.resourceUrl}/${id}`, { observe: 'response'});
    }

    search(req?: any): Observable<HttpResponse<CustomerWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<CustomerWilamp[]>(this.resourceSearchUrl, { params: options, observe: 'response' }).pipe(
            map((res: HttpResponse<CustomerWilamp[]>) => this.convertArrayResponse(res)));
    }

    private convertResponse(res: EntityResponseType): EntityResponseType {
        const body: CustomerWilamp = this.convertItemFromServer(res.body);
        return res.clone({body});
    }

    private convertArrayResponse(res: HttpResponse<CustomerWilamp[]>): HttpResponse<CustomerWilamp[]> {
        const jsonResponse: CustomerWilamp[] = res.body;
        const body: CustomerWilamp[] = [];
        for (let i = 0; i < jsonResponse.length; i++) {
            body.push(this.convertItemFromServer(jsonResponse[i]));
        }
        return res.clone({body});
    }

    /**
     * Convert a returned JSON object to CustomerWilamp.
     */
    private convertItemFromServer(customer: CustomerWilamp): CustomerWilamp {
        const copy: CustomerWilamp = Object.assign({}, customer);
        return copy;
    }

    /**
     * Convert a CustomerWilamp to a JSON which can be sent to the server.
     */
    private convert(customer: CustomerWilamp): CustomerWilamp {
        const copy: CustomerWilamp = Object.assign({}, customer);
        return copy;
    }
}
