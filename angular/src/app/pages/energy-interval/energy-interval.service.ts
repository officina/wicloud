
import {map} from 'rxjs/operators';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { JhiDateUtils } from 'ng-jhipster';

import { EnergyInterval } from './energy-interval.model';
import { createRequestOption } from '../../shared';
import {environment} from '../../../environments/environment';

export type EntityResponseType = HttpResponse<EnergyInterval>;

@Injectable()
export class EnergyIntervalService {

    private resourceUrl =  `${environment.apiUrl}/api/energy-interval`;
    private resourceSearchUrl =  `${environment.apiUrl}/api/_search/energy-interval`;

    constructor(private http: HttpClient, private dateUtils: JhiDateUtils) { }

    create(energyInterval: EnergyInterval): Observable<EntityResponseType> {
        const copy = this.convert(energyInterval);
        return this.http.post<EnergyInterval>(this.resourceUrl, copy, { observe: 'response' }).pipe(
            map((res: EntityResponseType) => this.convertResponse(res)));
    }

    update(energyInterval: EnergyInterval): Observable<EntityResponseType> {
        const copy = this.convert(energyInterval);
        return this.http.put<EnergyInterval>(this.resourceUrl, copy, { observe: 'response' }).pipe(
            map((res: EntityResponseType) => this.convertResponse(res)));
    }

    find(id: number): Observable<EntityResponseType> {
        return this.http.get<EnergyInterval>(`${this.resourceUrl}/${id}`, { observe: 'response'}).pipe(
            map((res: EntityResponseType) => this.convertResponse(res)));
    }

    query(req?: any): Observable<HttpResponse<EnergyInterval[]>> {
        const options = createRequestOption(req);
        return this.http.get<EnergyInterval[]>(`${this.resourceUrl}/`, { params: options, observe: 'response' }).pipe(
            map((res: HttpResponse<EnergyInterval[]>) => this.convertArrayResponse(res)));
    }

    getByMacAndMtyAndInterval(macAddress: string, mty: string, startInterval: string, endInterval: string, req?: any): Observable<EntityResponseType> {
        let options = createRequestOption(req);
          options = options.set('macAddress', macAddress);
          options = options.set('measureType', mty.toString());
          options = options.set('dateFrom', startInterval);
          options = options.set('dateTo', endInterval);

        return this.http.get(`${this.resourceUrl}/ByMac`, { params: options, observe: 'response' }).pipe(
            map((res: EntityResponseType) => this.convertResponse(res)));
    }

    getByLightModuleAndInterval(lightModuleId: number, startInterval: string, endInterval: string, req?: any): Observable<HttpResponse<EnergyInterval[]>> {
        let options = createRequestOption(req);
          options = options.set('lightModuleId', lightModuleId.toString());
          options = options.set('dateFrom', startInterval);
          options = options.set('dateTo', endInterval);

        return this.http.get(`${this.resourceUrl}/ByLightManagementModule`, { params: options, observe: 'response' }).pipe(
            map((res: HttpResponse<EnergyInterval[]>) => this.convertArrayResponse(res)));
    }
    delete(id: number): Observable<HttpResponse<any>> {
        return this.http.delete<any>(`${this.resourceUrl}/${id}`, { observe: 'response'});
    }

    search(req?: any): Observable<HttpResponse<EnergyInterval[]>> {
        const options = createRequestOption(req);
        return this.http.get<EnergyInterval[]>(this.resourceSearchUrl, { params: options, observe: 'response' }).pipe(
            map((res: HttpResponse<EnergyInterval[]>) => this.convertArrayResponse(res)));
    }

    private convertResponse(res: EntityResponseType): EntityResponseType {
        const body: EnergyInterval = this.convertItemFromServer(res.body);
        return res.clone({body});
    }

    private convertArrayResponse(res: HttpResponse<EnergyInterval[]>): HttpResponse<EnergyInterval[]> {
        const jsonResponse: EnergyInterval[] = res.body;
        const body: EnergyInterval[] = [];
        for (let i = 0; i < jsonResponse.length; i++) {
            body.push(this.convertItemFromServer(jsonResponse[i]));
        }
        return res.clone({body});
    }

    /**
     * Convert a returned JSON object to EnergyInterval.
     */
    private convertItemFromServer(energyInterval: EnergyInterval): EnergyInterval {
        const copy: EnergyInterval = Object.assign({}, energyInterval);
        copy.startInterval = this.dateUtils
            .convertDateTimeFromServer(energyInterval.startInterval);
        copy.endInterval = this.dateUtils
            .convertDateTimeFromServer(energyInterval.endInterval);
        copy.startIntervalMeasureTimestamp = this.dateUtils
            .convertDateTimeFromServer(energyInterval.startIntervalMeasureTimestamp);
        copy.endIntervalMeasureTimestamp = this.dateUtils
            .convertDateTimeFromServer(energyInterval.endIntervalMeasureTimestamp);
        return copy;
    }

    /**
     * Convert a EnergyInterval to a JSON which can be sent to the server.
     */
    private convert(energyInterval: EnergyInterval): EnergyInterval {
        const copy: EnergyInterval = Object.assign({}, energyInterval);

        copy.startInterval = this.dateUtils.toDate(energyInterval.startInterval);

        copy.endInterval = this.dateUtils.toDate(energyInterval.endInterval);

        copy.startIntervalMeasureTimestamp = this.dateUtils.toDate(energyInterval.startIntervalMeasureTimestamp);

        copy.endIntervalMeasureTimestamp = this.dateUtils.toDate(energyInterval.endIntervalMeasureTimestamp);
        return copy;
    }
}
