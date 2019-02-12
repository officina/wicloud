
import {map} from 'rxjs/operators';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { ContactWilamp } from './contact-wilamp.model';
import { createRequestOption } from '../../shared';
import {environment} from '../../../environments/environment';

export type EntityResponseType = HttpResponse<ContactWilamp>;

@Injectable()
export class ContactWilampService {

    private resourceUrl =  `${environment.apiUrl}/api/contact`;
    private resourceSearchUrl =  `${environment.apiUrl}/api/_search/contact`;

    constructor(private http: HttpClient) { }

    create(contact: ContactWilamp): Observable<EntityResponseType> {
        const copy = this.convert(contact);
        return this.http.post<ContactWilamp>(this.resourceUrl, copy, { observe: 'response' }).pipe(
            map((res: EntityResponseType) => this.convertResponse(res)));
    }

    update(contact: ContactWilamp): Observable<EntityResponseType> {
        const copy = this.convert(contact);
        return this.http.put<ContactWilamp>(this.resourceUrl, copy, { observe: 'response' }).pipe(
            map((res: EntityResponseType) => this.convertResponse(res)));
    }

    find(id: number): Observable<EntityResponseType> {
        return this.http.get<ContactWilamp>(`${this.resourceUrl}/${id}`, { observe: 'response'}).pipe(
            map((res: EntityResponseType) => this.convertResponse(res)));
    }

    query(req?: any): Observable<HttpResponse<ContactWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<ContactWilamp[]>(`${this.resourceUrl}/`, { params: options, observe: 'response' }).pipe(
            map((res: HttpResponse<ContactWilamp[]>) => this.convertArrayResponse(res)));
    }

    delete(id: number): Observable<HttpResponse<any>> {
        return this.http.delete<any>(`${this.resourceUrl}/${id}`, { observe: 'response'});
    }

    search(req?: any): Observable<HttpResponse<ContactWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<ContactWilamp[]>(this.resourceSearchUrl, { params: options, observe: 'response' }).pipe(
            map((res: HttpResponse<ContactWilamp[]>) => this.convertArrayResponse(res)));
    }

    private convertResponse(res: EntityResponseType): EntityResponseType {
        const body: ContactWilamp = this.convertItemFromServer(res.body);
        return res.clone({body});
    }

    private convertArrayResponse(res: HttpResponse<ContactWilamp[]>): HttpResponse<ContactWilamp[]> {
        const jsonResponse: ContactWilamp[] = res.body;
        const body: ContactWilamp[] = [];
        for (let i = 0; i < jsonResponse.length; i++) {
            body.push(this.convertItemFromServer(jsonResponse[i]));
        }
        return res.clone({body});
    }

    /**
     * Convert a returned JSON object to ContactWilamp.
     */
    private convertItemFromServer(contact: ContactWilamp): ContactWilamp {
        const copy: ContactWilamp = Object.assign({}, contact);
        return copy;
    }

    /**
     * Convert a ContactWilamp to a JSON which can be sent to the server.
     */
    private convert(contact: ContactWilamp): ContactWilamp {
        const copy: ContactWilamp = Object.assign({}, contact);
        return copy;
    }
}
