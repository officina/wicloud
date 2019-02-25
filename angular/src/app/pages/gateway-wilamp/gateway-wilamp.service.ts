
import {map} from 'rxjs/operators';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { JhiDateUtils } from 'ng-jhipster';

import { GatewayWilamp } from './gateway-wilamp.model';
import {environment} from '../../../environments/environment';
import {createRequestOption} from '../../shared/model/request-util';

export type EntityResponseType = HttpResponse<GatewayWilamp>;

@Injectable()
export class GatewayWilampService {

    private resourceUrl =  `${environment.apiUrl}/api/gateway`;
    private resourceSearchUrl =  `${environment.apiUrl}/api/_search/gateway`;

    constructor(private http: HttpClient, private dateUtils: JhiDateUtils) { }

    create(gateway: GatewayWilamp): Observable<EntityResponseType> {
        const copy = this.convert(gateway);
        return this.http.post<GatewayWilamp>(this.resourceUrl, copy, { observe: 'response' }).pipe(
            map((res: EntityResponseType) => this.convertResponse(res)));
    }

    update(gateway: GatewayWilamp): Observable<EntityResponseType> {
        const copy = this.convert(gateway);
        return this.http.put<GatewayWilamp>(this.resourceUrl, copy, { observe: 'response' }).pipe(
            map((res: EntityResponseType) => this.convertResponse(res)));
    }

    find(id: number): Observable<EntityResponseType> {
        return this.http.get<GatewayWilamp>(`${this.resourceUrl}/${id}`, { observe: 'response'}).pipe(
            map((res: EntityResponseType) => this.convertResponse(res)));
    }

    findByInstallation(installationId: number, req?: any): Observable<HttpResponse<GatewayWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get(`${this.resourceUrl}-by-installation/${installationId}`, { params: options, observe: 'response' }).pipe(
            map((res: HttpResponse<GatewayWilamp[]>) => this.convertArrayResponse(res)));
    }

    query(req?: any): Observable<HttpResponse<GatewayWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<GatewayWilamp[]>(`${this.resourceUrl}/`, { params: options, observe: 'response' }).pipe(
            map((res: HttpResponse<GatewayWilamp[]>) => this.convertArrayResponse(res)));
    }

    delete(id: number): Observable<HttpResponse<any>> {
        return this.http.delete<any>(`${this.resourceUrl}/${id}`, { observe: 'response'});
    }

    search(req?: any): Observable<HttpResponse<GatewayWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<GatewayWilamp[]>(this.resourceSearchUrl, { params: options, observe: 'response' }).pipe(
            map((res: HttpResponse<GatewayWilamp[]>) => this.convertArrayResponse(res)));
    }

    private convertResponse(res: EntityResponseType): EntityResponseType {
        const body: GatewayWilamp = this.convertItemFromServer(res.body);
        return res.clone({body});
    }

    private convertArrayResponse(res: HttpResponse<GatewayWilamp[]>): HttpResponse<GatewayWilamp[]> {
        const jsonResponse: GatewayWilamp[] = res.body;
        const body: GatewayWilamp[] = [];
        for (let i = 0; i < jsonResponse.length; i++) {
            body.push(this.convertItemFromServer(jsonResponse[i]));
        }
        return res.clone({body});
    }

    /**
     * Convert a returned JSON object to GatewayWilamp.
     */
    private convertItemFromServer(gateway: GatewayWilamp): GatewayWilamp {
        const copy: GatewayWilamp = Object.assign({}, gateway);
        copy.creationDate = this.dateUtils
            .convertDateTimeFromServer(gateway.creationDate);
        return copy;
    }

    /**
     * Convert a GatewayWilamp to a JSON which can be sent to the server.
     */
    private convert(gateway: GatewayWilamp): GatewayWilamp {
        const copy: GatewayWilamp = Object.assign({}, gateway);

        copy.creationDate = this.dateUtils.toDate(gateway.creationDate);
        return copy;
    }
}
