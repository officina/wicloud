
import {map} from 'rxjs/operators';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { ShippingWilamp } from './shipping-wilamp.model';
import {createRequestOption} from '../../shared/model/request-util';
import {environment} from '../../../environments/environment';

export type EntityResponseType = HttpResponse<ShippingWilamp>;

@Injectable()
export class ShippingWilampService {

    private resourceUrl =  `${environment.apiUrl}/api/shipping`;
    private resourceSearchUrl =  `${environment.apiUrl}/api/_search/shipping`;

    constructor(private http: HttpClient) { }

    create(shipping: ShippingWilamp): Observable<EntityResponseType> {
        const copy = this.convert(shipping);
        return this.http.post<ShippingWilamp>(this.resourceUrl, copy, { observe: 'response' }).pipe(
            map((res: EntityResponseType) => this.convertResponse(res)));
    }

    update(shipping: ShippingWilamp): Observable<EntityResponseType> {
        const copy = this.convert(shipping);
        return this.http.put<ShippingWilamp>(this.resourceUrl, copy, { observe: 'response' }).pipe(
            map((res: EntityResponseType) => this.convertResponse(res)));
    }

    find(id: number): Observable<EntityResponseType> {
        return this.http.get<ShippingWilamp>(`${this.resourceUrl}/${id}`, { observe: 'response'}).pipe(
            map((res: EntityResponseType) => this.convertResponse(res)));
    }

    query(req?: any): Observable<HttpResponse<ShippingWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<ShippingWilamp[]>(`${this.resourceUrl}/`, { params: options, observe: 'response' }).pipe(
            map((res: HttpResponse<ShippingWilamp[]>) => this.convertArrayResponse(res)));
    }

    delete(id: number): Observable<HttpResponse<any>> {
        return this.http.delete<any>(`${this.resourceUrl}/${id}`, { observe: 'response'});
    }

    search(req?: any): Observable<HttpResponse<ShippingWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<ShippingWilamp[]>(this.resourceSearchUrl, { params: options, observe: 'response' }).pipe(
            map((res: HttpResponse<ShippingWilamp[]>) => this.convertArrayResponse(res)));
    }

    private convertResponse(res: EntityResponseType): EntityResponseType {
        const body: ShippingWilamp = this.convertItemFromServer(res.body);
        return res.clone({body});
    }

    private convertArrayResponse(res: HttpResponse<ShippingWilamp[]>): HttpResponse<ShippingWilamp[]> {
        const jsonResponse: ShippingWilamp[] = res.body;
        const body: ShippingWilamp[] = [];
        for (let i = 0; i < jsonResponse.length; i++) {
            body.push(this.convertItemFromServer(jsonResponse[i]));
        }
        return res.clone({body});
    }

    /**
     * Convert a returned JSON object to ShippingWilamp.
     */
    private convertItemFromServer(shipping: ShippingWilamp): ShippingWilamp {
        const copy: ShippingWilamp = Object.assign({}, shipping);
        return copy;
    }

    /**
     * Convert a ShippingWilamp to a JSON which can be sent to the server.
     */
    private convert(shipping: ShippingWilamp): ShippingWilamp {
        const copy: ShippingWilamp = Object.assign({}, shipping);
        return copy;
    }
}
