import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { Observable, Subject } from 'rxjs';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import { JhiDateUtils } from 'ng-jhipster';
import { LightManagementMeasureWilamp } from './light-management-measure-wilamp.model';
import { createRequestOption } from '../../shared';
import {environment} from '../../../environments/environment';

export type EntityResponseType = HttpResponse<LightManagementMeasureWilamp>;

@Injectable()
export class LightManagementMeasureWilampService {

    private resourceUrl =  `${environment.apiUrl}/api/light-management-measure`;
    private resourceSearchUrl =  `${environment.apiUrl}/api/_search/light-management-measure`;

    constructor(private http: HttpClient, private dateUtils: JhiDateUtils) { }

    create(lightManagementMeasure: LightManagementMeasureWilamp): Observable<EntityResponseType> {
        const copy = this.convert(lightManagementMeasure);
        return this.http.post<LightManagementMeasureWilamp>(this.resourceUrl, copy, { observe: 'response' })
            .map((res: EntityResponseType) => this.convertResponse(res));
    }

    update(lightManagementMeasure: LightManagementMeasureWilamp): Observable<EntityResponseType> {
        const copy = this.convert(lightManagementMeasure);
        return this.http.put<LightManagementMeasureWilamp>(this.resourceUrl, copy, { observe: 'response' })
            .map((res: EntityResponseType) => this.convertResponse(res));
    }

    find(id: number): Observable<EntityResponseType> {
        return this.http.get<LightManagementMeasureWilamp>(`${this.resourceUrl}/${id}`, { observe: 'response'})
            .map((res: EntityResponseType) => this.convertResponse(res));
    }

    query(req?: any): Observable<HttpResponse<LightManagementMeasureWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<LightManagementMeasureWilamp[]>(`${this.resourceUrl}/`, { params: options, observe: 'response' })
            .map((res: HttpResponse<LightManagementMeasureWilamp[]>) => this.convertArrayResponse(res));
    }

    getByMacAndMtyAndInterval(macAddress: string, mty: string, startInterval: string, endInterval: string, req?: any): Observable<HttpResponse<LightManagementMeasureWilamp[]>> {
        let options = createRequestOption(req);
          options = options.set('macAddress', macAddress);
          options = options.set('measureType', mty.toString());
          options = options.set('dateFrom', startInterval);
          options = options.set('dateTo', endInterval);

        return this.http.get(`${this.resourceUrl}/ByMac`, { params: options, observe: 'response' })
            .map((res: HttpResponse<LightManagementMeasureWilamp[]>) => this.convertArrayResponse(res));
    }

    getByLightModuleAndMtyAndInterval(lightModuleId: number, mty: number, startInterval: string, endInterval: string, req?: any): Observable<HttpResponse<LightManagementMeasureWilamp[]>> {
        let options = createRequestOption(req);
          options = options.set('lightModuleId', lightModuleId.toString());
          options = options.set('measureType', mty.toString());
          options = options.set('dateFrom', startInterval);
          options = options.set('dateTo', endInterval);

        return this.http.get(`${this.resourceUrl}/ByLightManagementModule`, { params: options, observe: 'response' })
            .map((res: HttpResponse<LightManagementMeasureWilamp[]>) => this.convertArrayResponse(res));
    }

    delete(id: number): Observable<HttpResponse<any>> {
        return this.http.delete<any>(`${this.resourceUrl}/${id}`, { observe: 'response'});
    }

    search(req?: any): Observable<HttpResponse<LightManagementMeasureWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<LightManagementMeasureWilamp[]>(this.resourceSearchUrl, { params: options, observe: 'response' })
            .map((res: HttpResponse<LightManagementMeasureWilamp[]>) => this.convertArrayResponse(res));
    }

    private convertResponse(res: EntityResponseType): EntityResponseType {
        const body: LightManagementMeasureWilamp = this.convertItemFromServer(res.body);
        return res.clone({body});
    }

    private convertArrayResponse(res: HttpResponse<LightManagementMeasureWilamp[]>): HttpResponse<LightManagementMeasureWilamp[]> {
        const jsonResponse: LightManagementMeasureWilamp[] = res.body;
        const body: LightManagementMeasureWilamp[] = [];
        for (let i = 0; i < jsonResponse.length; i++) {
            body.push(this.convertItemFromServer(jsonResponse[i]));
        }
        return res.clone({body});
    }

    /**
     * Convert a returned JSON object to LightManagementMeasureWilamp.
     */
    private convertItemFromServer(lightManagementMeasure: LightManagementMeasureWilamp): LightManagementMeasureWilamp {
        const copy: LightManagementMeasureWilamp = Object.assign({}, lightManagementMeasure);
        copy.measureTimestamp = this.dateUtils
            .convertDateTimeFromServer(lightManagementMeasure.measureTimestamp);
        copy.createdTimestamp = this.dateUtils
            .convertDateTimeFromServer(lightManagementMeasure.createdTimestamp);
        return copy;
    }

    /**
     * Convert a LightManagementMeasureWilamp to a JSON which can be sent to the server.
     */
    private convert(lightManagementMeasure: LightManagementMeasureWilamp): LightManagementMeasureWilamp {
        const copy: LightManagementMeasureWilamp = Object.assign({}, lightManagementMeasure);

        copy.measureTimestamp = this.dateUtils.toDate(lightManagementMeasure.measureTimestamp);

        copy.createdTimestamp = this.dateUtils.toDate(lightManagementMeasure.createdTimestamp);
        return copy;
    }
}
