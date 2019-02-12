
import {map} from 'rxjs/operators';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { AddressWilamp } from './address-wilamp.model';
import { createRequestOption } from '../../shared';
import {environment} from '../../../environments/environment';

export type EntityResponseType = HttpResponse<AddressWilamp>;

@Injectable()
export class AddressWilampService {

    private resourceUrl =  `${environment.apiUrl}/api/address`;
    private resourceSearchUrl =  `${environment.apiUrl}/api/_search/address`;

    constructor(private http: HttpClient) { }

    create(address: AddressWilamp): Observable<EntityResponseType> {
        const copy = this.convert(address);
        return this.http.post<AddressWilamp>(this.resourceUrl, copy, { observe: 'response' }).pipe(
            map((res: EntityResponseType) => this.convertResponse(res)));
    }

    update(address: AddressWilamp): Observable<EntityResponseType> {
        const copy = this.convert(address);
        return this.http.put<AddressWilamp>(this.resourceUrl, copy, { observe: 'response' }).pipe(
            map((res: EntityResponseType) => this.convertResponse(res)));
    }

    find(id: number): Observable<EntityResponseType> {
        return this.http.get<AddressWilamp>(`${this.resourceUrl}/${id}`, { observe: 'response'}).pipe(
            map((res: EntityResponseType) => this.convertResponse(res)));
    }

    query(req?: any): Observable<HttpResponse<AddressWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<AddressWilamp[]>(`${this.resourceUrl}/`, { params: options, observe: 'response' }).pipe(
            map((res: HttpResponse<AddressWilamp[]>) => this.convertArrayResponse(res)));
    }

    delete(id: number): Observable<HttpResponse<any>> {
        return this.http.delete<any>(`${this.resourceUrl}/${id}`, { observe: 'response'});
    }

    search(req?: any): Observable<HttpResponse<AddressWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<AddressWilamp[]>(this.resourceSearchUrl, { params: options, observe: 'response' }).pipe(
            map((res: HttpResponse<AddressWilamp[]>) => this.convertArrayResponse(res)));
    }

    private convertResponse(res: EntityResponseType): EntityResponseType {
        const body: AddressWilamp = this.convertItemFromServer(res.body);
        return res.clone({body});
    }

    private convertArrayResponse(res: HttpResponse<AddressWilamp[]>): HttpResponse<AddressWilamp[]> {
        const jsonResponse: AddressWilamp[] = res.body;
        const body: AddressWilamp[] = [];
        for (let i = 0; i < jsonResponse.length; i++) {
            body.push(this.convertItemFromServer(jsonResponse[i]));
        }
        return res.clone({body});
    }

    /**
     * Convert a returned JSON object to AddressWilamp.
     */
    private convertItemFromServer(address: AddressWilamp): AddressWilamp {
        const copy: AddressWilamp = Object.assign({}, address);
        return copy;
    }

    /**
     * Convert a AddressWilamp to a JSON which can be sent to the server.
     */
    private convert(address: AddressWilamp): AddressWilamp {
        const copy: AddressWilamp = Object.assign({}, address);
        return copy;
    }
}
