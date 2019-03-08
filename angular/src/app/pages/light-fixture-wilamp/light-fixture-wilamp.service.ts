import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';

import { LightFixtureWilamp } from './light-fixture-wilamp.model';
import { createRequestOption } from '../../shared';
import {environment} from '../../../environments/environment';
import {GatewayWilamp} from '../gateway-wilamp';
import {map} from 'rxjs/operators';
import {NodeWilamp} from '../node-wilamp';

export type EntityResponseType = HttpResponse<LightFixtureWilamp>;

@Injectable()
export class LightFixtureWilampService {

    private resourceUrl =  `${environment.apiUrl}/api/light-fixture`;
    private resourceSearchUrl =  `${environment.apiUrl}/api/_search/light-fixture`;

    constructor(private http: HttpClient) { }

    create(lightFixture: LightFixtureWilamp): Observable<EntityResponseType> {
        const copy = this.convert(lightFixture);
        return this.http.post<LightFixtureWilamp>(`${this.resourceUrl}/`, copy, { observe: 'response' })
            .map((res: EntityResponseType) => this.convertResponse(res));
    }

    update(lightFixture: LightFixtureWilamp): Observable<EntityResponseType> {
        const copy = this.convert(lightFixture);
        return this.http.put<LightFixtureWilamp>(`${this.resourceUrl}/`, copy, { observe: 'response' })
            .map((res: EntityResponseType) => this.convertResponse(res));
    }

    find(id: number): Observable<EntityResponseType> {
        return this.http.get<LightFixtureWilamp>(`${this.resourceUrl}/${id}/`, { observe: 'response'})
            .map((res: EntityResponseType) => this.convertResponse(res));
    }

    findByInstallation(id: number, req?: any): Observable<HttpResponse<LightFixtureWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<LightFixtureWilamp[]>(`${this.resourceUrl}-by-installation/${id}/`, { params: options, observe: 'response'})
            .map((res: HttpResponse<LightFixtureWilamp[]>) => this.convertArrayResponse(res));
    }

    query(req?: any): Observable<HttpResponse<LightFixtureWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<LightFixtureWilamp[]>(`${this.resourceUrl}/`, { params: options, observe: 'response' })
            .map((res: HttpResponse<LightFixtureWilamp[]>) => this.convertArrayResponse(res));
    }

    delete(id: number): Observable<HttpResponse<any>> {
        return this.http.delete<any>(`${this.resourceUrl}/${id}/`, { observe: 'response'});
    }

    search(req?: any): Observable<HttpResponse<LightFixtureWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<LightFixtureWilamp[]>(`${this.resourceSearchUrl}/`, { params: options, observe: 'response' })
            .map((res: HttpResponse<LightFixtureWilamp[]>) => this.convertArrayResponse(res));
    }

    private convertResponse(res: EntityResponseType): EntityResponseType {
        const body: LightFixtureWilamp = this.convertItemFromServer(res.body);
        return res.clone({body});
    }

    private convertArrayResponse(res: HttpResponse<LightFixtureWilamp[]>): HttpResponse<LightFixtureWilamp[]> {
        const jsonResponse: LightFixtureWilamp[] = res.body;
        const body: LightFixtureWilamp[] = [];
        for (let i = 0; i < jsonResponse.length; i++) {
            body.push(this.convertItemFromServer(jsonResponse[i]));
        }
        return res.clone({body});
    }

    /**
     * Convert a returned JSON object to LightFixtureWilamp.
     */
    private convertItemFromServer(lightFixture: LightFixtureWilamp): LightFixtureWilamp {
        const lightFixtureW = new LightFixtureWilamp();
        const copy = Object.assign(lightFixtureW, lightFixture);
        return copy;
    }

    /**
     * Convert a LightFixtureWilamp to a JSON which can be sent to the server.
     */
    private convert(lightFixture: LightFixtureWilamp): LightFixtureWilamp {
        const copy: LightFixtureWilamp = Object.assign({}, lightFixture);
        return copy;
    }
}
