import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient, HttpResponse } from '@angular/common/http';

import { JhiDateUtils } from 'ng-jhipster';

import { LightProfileSlotWilamp } from './light-profile-slot-wilamp.model';
import { createRequestOption } from '../../shared';
import {environment} from '../../../environments/environment';

export type EntityResponseType = HttpResponse<LightProfileSlotWilamp>;

@Injectable()
export class LightProfileSlotWilampService {

    private resourceUrl =  `${environment.apiUrl}/api/light-profile-slots`;
    private resourceSearchUrl =  `${environment.apiUrl}/api/_search/light-profile-slots`;

    constructor(private http: HttpClient, private dateUtils: JhiDateUtils) { }

    create(lightProfileSlot: LightProfileSlotWilamp): Observable<EntityResponseType> {
        const copy = this.convert(lightProfileSlot);
        return this.http.post<LightProfileSlotWilamp>(`${this.resourceUrl}/`, copy, { observe: 'response' })
            .map((res: EntityResponseType) => this.convertResponse(res));
    }

    update(lightProfileSlot: LightProfileSlotWilamp): Observable<EntityResponseType> {
        const copy = this.convert(lightProfileSlot);
        return this.http.put<LightProfileSlotWilamp>(`${this.resourceUrl}/`, copy, { observe: 'response' })
            .map((res: EntityResponseType) => this.convertResponse(res));
    }

    find(id: number): Observable<EntityResponseType> {
        return this.http.get<LightProfileSlotWilamp>(`${this.resourceUrl}/${id}`, { observe: 'response'})
            .map((res: EntityResponseType) => this.convertResponse(res));
    }

    getLightProfileSlotsByLightProfile(lightProfileId: number): Observable<EntityResponseType> {
        return this.http.get(`${this.resourceUrl}/byLightProfile/${lightProfileId}`)
            .map((res: EntityResponseType) => this.convertResponse(res));
    }

    query(req?: any): Observable<HttpResponse<LightProfileSlotWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<LightProfileSlotWilamp[]>(`${this.resourceUrl}/`, { params: options, observe: 'response' })
            .map((res: HttpResponse<LightProfileSlotWilamp[]>) => this.convertArrayResponse(res));
    }

    delete(id: number): Observable<HttpResponse<any>> {
        return this.http.delete<any>(`${this.resourceUrl}/${id}`, { observe: 'response'});
    }

    search(req?: any): Observable<HttpResponse<LightProfileSlotWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<LightProfileSlotWilamp[]>(`${this.resourceUrl}/`, { params: options, observe: 'response' })
            .map((res: HttpResponse<LightProfileSlotWilamp[]>) => this.convertArrayResponse(res));
    }

    private convertResponse(res: EntityResponseType): EntityResponseType {
        const body: LightProfileSlotWilamp = this.convertItemFromServer(res.body);
        return res.clone({body});
    }

    private convertArrayResponse(res: HttpResponse<LightProfileSlotWilamp[]>): HttpResponse<LightProfileSlotWilamp[]> {
        const jsonResponse: LightProfileSlotWilamp[] = res.body;
        const body: LightProfileSlotWilamp[] = [];
        for (let i = 0; i < jsonResponse.length; i++) {
            body.push(this.convertItemFromServer(jsonResponse[i]));
        }
        return res.clone({body});
    }

    /**
     * Convert a returned JSON object to LightProfileSlotWilamp.
     */
    private convertItemFromServer(lightProfileSlot: LightProfileSlotWilamp): LightProfileSlotWilamp {
        const copy: LightProfileSlotWilamp = Object.assign({}, lightProfileSlot);
        copy.createdTimestamp = this.dateUtils
            .convertDateTimeFromServer(lightProfileSlot.createdTimestamp);
        return copy;
    }

    /**
     * Convert a LightProfileSlotWilamp to a JSON which can be sent to the server.
     */
    private convert(lightProfileSlot: LightProfileSlotWilamp): LightProfileSlotWilamp {
        const copy: LightProfileSlotWilamp = Object.assign({}, lightProfileSlot);

        copy.createdTimestamp = this.dateUtils.toDate(lightProfileSlot.createdTimestamp);
        return copy;
    }
}
