import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { Observable, Subject } from 'rxjs';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import { JhiDateUtils } from 'ng-jhipster';

import { GatewayInstallationRequest } from './gateway-installation-request.model';
import {environment} from '../../../environments/environment';
import {createRequestOption} from '../../shared/model/request-util';

export type EntityResponseType = HttpResponse<GatewayInstallationRequest>;

@Injectable()
export class GatewayInstallationRequestService {

    private resourceUrl =  `${environment.apiUrl}/api/gateway-installation-request`;
    private resourceSearchUrl =  `${environment.apiUrl}/api/_search/gateway-installation-request`;

    constructor(private http: HttpClient, private dateUtils: JhiDateUtils) { }

    create(gatewayInstallationRequest: GatewayInstallationRequest): Observable<EntityResponseType> {
        const copy = this.convert(gatewayInstallationRequest);
        return this.http.post<GatewayInstallationRequest>(this.resourceUrl, copy, { observe: 'response' })
            .map((res: EntityResponseType) => this.convertResponse(res));
    }

    update(gatewayInstallationRequest: GatewayInstallationRequest): Observable<EntityResponseType> {
        const copy = this.convert(gatewayInstallationRequest);
        return this.http.put<GatewayInstallationRequest>(this.resourceUrl, copy, { observe: 'response' })
            .map((res: EntityResponseType) => this.convertResponse(res));
    }

    find(id: number): Observable<EntityResponseType> {
        return this.http.get<GatewayInstallationRequest>(`${this.resourceUrl}/${id}`, { observe: 'response'})
            .map((res: EntityResponseType) => this.convertResponse(res));
    }

    query(req?: any): Observable<HttpResponse<GatewayInstallationRequest[]>> {
        const options = createRequestOption(req);
        return this.http.get<GatewayInstallationRequest[]>(`${this.resourceUrl}/`, { params: options, observe: 'response' })
            .map((res: HttpResponse<GatewayInstallationRequest[]>) => this.convertArrayResponse(res));
    }

    delete(id: number): Observable<HttpResponse<any>> {
        return this.http.delete<any>(`${this.resourceUrl}/${id}`, { observe: 'response'});
    }

    search(req?: any): Observable<HttpResponse<GatewayInstallationRequest[]>> {
        const options = createRequestOption(req);
        return this.http.get<GatewayInstallationRequest[]>(this.resourceSearchUrl, { params: options, observe: 'response' })
            .map((res: HttpResponse<GatewayInstallationRequest[]>) => this.convertArrayResponse(res));
    }

    private convertResponse(res: EntityResponseType): EntityResponseType {
        const body: GatewayInstallationRequest = this.convertItemFromServer(res.body);
        return res.clone({body});
    }

    private convertArrayResponse(res: HttpResponse<GatewayInstallationRequest[]>): HttpResponse<GatewayInstallationRequest[]> {
        const jsonResponse: GatewayInstallationRequest[] = res.body;
        const body: GatewayInstallationRequest[] = [];
        for (let i = 0; i < jsonResponse.length; i++) {
            body.push(this.convertItemFromServer(jsonResponse[i]));
        }
        return res.clone({body});
    }

    /**
     * Convert a returned JSON object to GatewayInstallationRequest.
     */
    private convertItemFromServer(gatewayInstallationRequest: GatewayInstallationRequest): GatewayInstallationRequest {
        const copy: GatewayInstallationRequest = Object.assign({}, gatewayInstallationRequest);
        copy.creationDate = this.dateUtils
            .convertDateTimeFromServer(gatewayInstallationRequest.creationDate);
        copy.startInstallationTimestamp = this.dateUtils
            .convertDateTimeFromServer(gatewayInstallationRequest.startInstallationTimestamp);
        copy.endInstallationTimestamp = this.dateUtils
            .convertDateTimeFromServer(gatewayInstallationRequest.endInstallationTimestamp);
        return copy;
    }

    /**
     * Convert a GatewayInstallationRequest to a JSON which can be sent to the server.
     */
    private convert(gatewayInstallationRequest: GatewayInstallationRequest): GatewayInstallationRequest {
        const copy: GatewayInstallationRequest = Object.assign({}, gatewayInstallationRequest);

        copy.creationDate = this.dateUtils.toDate(gatewayInstallationRequest.creationDate);

        copy.startInstallationTimestamp = this.dateUtils.toDate(gatewayInstallationRequest.startInstallationTimestamp);

        copy.endInstallationTimestamp = this.dateUtils.toDate(gatewayInstallationRequest.endInstallationTimestamp);
        return copy;
    }
}
