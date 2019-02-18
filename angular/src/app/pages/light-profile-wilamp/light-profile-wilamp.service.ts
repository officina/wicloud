import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';

import { LightProfileWilamp } from './light-profile-wilamp.model';
import { createRequestOption } from '../../shared';
export type EntityResponseType = HttpResponse<LightProfileWilamp>;
import {LightProfileSlotWilamp} from '../light-profile-slot-wilamp';
import {environment} from '../../../environments/environment';

@Injectable()
export class LightProfileWilampService {

    private resourceUrl =  `${environment.apiUrl}/api/light-profiles`;
    private resourceSearchUrl =  `${environment.apiUrl}/api/_search/light-profiles`;

    constructor(private http: HttpClient) { }

    create(lightProfile: LightProfileWilamp): Observable<EntityResponseType> {
        const copy = this.convert(lightProfile);
        return this.http.post<LightProfileWilamp>(`${this.resourceUrl}/`, copy, { observe: 'response' })
            .map((res: EntityResponseType) => this.convertResponse(res));
    }

    update(lightProfile: LightProfileWilamp): Observable<EntityResponseType> {
        const copy = this.convert(lightProfile);
        return this.http.put<LightProfileWilamp>(this.resourceUrl, copy, { observe: 'response' })
            .map((res: EntityResponseType) => this.convertResponse(res));
    }

    find(id: number): Observable<EntityResponseType> {
        return this.http.get<LightProfileWilamp>(`${this.resourceUrl}/${id}/`, { observe: 'response'})
            .map((res: EntityResponseType) => this.convertResponse(res));
    }

    query(req?: any): Observable<HttpResponse<LightProfileWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<LightProfileWilamp[]>(`${this.resourceUrl}/`, { params: options, observe: 'response' })
            .map((res: HttpResponse<LightProfileWilamp[]>) => this.convertArrayResponse(res));
    }

    delete(id: number): Observable<HttpResponse<any>> {
        return this.http.delete<any>(`${this.resourceUrl}/${id}/`, { observe: 'response'});
    }

    search(req?: any): Observable<HttpResponse<LightProfileWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<LightProfileWilamp[]>(`${this.resourceUrl}/`, { params: options, observe: 'response' })
            .map((res: HttpResponse<LightProfileWilamp[]>) => this.convertArrayResponse(res));
    }

    private convertResponse(res: EntityResponseType): EntityResponseType {
        const body: LightProfileWilamp = this.convertItemFromServer(res.body);
        return res.clone({body});
    }

    private convertArrayResponse(res: HttpResponse<LightProfileWilamp[]>): HttpResponse<LightProfileWilamp[]> {
        const jsonResponse: LightProfileWilamp[] = res.body;
        const body: LightProfileWilamp[] = [];
        for (let i = 0; i < jsonResponse.length; i++) {
            body.push(this.convertItemFromServer(jsonResponse[i]));
        }
        return res.clone({body});
    }

    replaceLightProfileSlots(lightProfileId, slots: LightProfileSlotWilamp[]): Observable<HttpResponse<LightProfileWilamp>> {
        return this.http.post(`${this.resourceUrl}/replaceSlots/?lightProfileId=${lightProfileId}/`, slots, { observe: 'response' }).map((res: EntityResponseType) => this.convertResponse(res));
    }

    /**
     * Convert a returned JSON object to LightProfileWilamp.
     */
    private convertItemFromServer(lightProfile: LightProfileWilamp): LightProfileWilamp {
        const copy: LightProfileWilamp = Object.assign({}, lightProfile);
        return copy;
    }

    /**
     * Convert a LightProfileWilamp to a JSON which can be sent to the server.
     */
    private convert(lightProfile: LightProfileWilamp): LightProfileWilamp {
        const copy: LightProfileWilamp = Object.assign({}, lightProfile);
        return copy;
    }
}
