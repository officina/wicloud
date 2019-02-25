
import {map} from 'rxjs/operators';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import {Http, Response, URLSearchParams} from '@angular/http';
import { HttpClient, HttpResponse } from '@angular/common/http';

import { JhiDateUtils } from 'ng-jhipster';

import {
    InstallationRuntimeParameters,
    EnergyStatistics,
    EnergyStatisticsByResourceId,
} from './installation-wilamp.model';
import DateTimeFormat = Intl.DateTimeFormat;
import { InstallationWilamp } from './installation-wilamp.model';
import {environment} from '../../../environments/environment';
import {createRequestOption} from '../../shared/model/request-util';

export type EntityResponseType = HttpResponse<InstallationWilamp>;

@Injectable()
export class InstallationWilampService {

    private resourceUrl =  `${environment.apiUrl}/api/installation`;
    private resourceSearchUrl =  `${environment.apiUrl}/api/_search/installation`;

    constructor(private http: HttpClient, private dateUtils: JhiDateUtils) { }

    create(installation: InstallationWilamp): Observable<EntityResponseType> {
        const copy = this.convert(installation);
        return this.http.post<InstallationWilamp>(this.resourceUrl, copy, { observe: 'response' }).pipe(
            map((res: EntityResponseType) => this.convertResponse(res)));
    }

    update(installation: InstallationWilamp): Observable<EntityResponseType> {
        const copy = this.convert(installation);
        return this.http.put<InstallationWilamp>(this.resourceUrl, copy, { observe: 'response' }).pipe(
            map((res: EntityResponseType) => this.convertResponse(res)));
    }

    find(id: number): Observable<EntityResponseType> {
        return this.http.get<InstallationWilamp>(`${this.resourceUrl}/${id}`, { observe: 'response'}).pipe(
            map((res: EntityResponseType) => this.convertResponse(res)));
    }

    getRuntimeParameters(id: number, startInterval: Date, endInterval: Date): Observable<InstallationRuntimeParameters> {
        let options = createRequestOption();
          options = options.set('startInterval', startInterval.toISOString());
          options = options.set('endInterval', endInterval.toISOString());

        return this.http.get(`${this.resourceUrl}/runtimeParameters/${id}`, { params: options, observe: 'response' }).pipe(map((res: HttpResponse<InstallationRuntimeParameters>) => {
            const copy: InstallationRuntimeParameters = Object.assign({}, res.body);
            return copy;
        }));
    }

    getWeeklyEnergyStatistics(id: number, measureType?: number, startInterval?: Date, endInterval?: Date, currentAnalyzedDate?: Date): Observable<EnergyStatistics> {
        let options = createRequestOption();
        if (startInterval != null) {   options = options.set('startInterval', startInterval.toISOString()); }
        if (endInterval != null) {   options = options.set('endInterval', endInterval.toISOString()); }
        if (measureType != null) {   options = options.set('measureType', measureType.toString()); }
        if (currentAnalyzedDate != null) {   options = options.set('currentAnalyzedDate', currentAnalyzedDate.toISOString()); }
        return this.http.get(`${this.resourceUrl}/weeklyEnergyStatistics/${id}`, { params: options, observe: 'response' }).pipe(map((res: HttpResponse<EnergyStatistics>) => {
            const copy: EnergyStatistics = Object.assign({}, res.body);
            try {
                copy.globalEnergyConsumption.lastIntervalTimestamp = this.dateUtils.toDate(copy.globalEnergyConsumption.lastIntervalTimestamp);
            } catch (e) {
                console.warn(e);
            }
            return copy;
        }));
    }

    getStatisticsByLightManagementModule(id: number, measureType?: number, startInterval?: Date, endInterval?: Date): Observable<EnergyStatistics> {
        let options = createRequestOption();
        if (startInterval != null) {   options = options.set('startInterval', startInterval.toISOString()); }
        if (endInterval != null) {   options = options.set('endInterval', endInterval.toISOString()); }
        if (measureType != null) {   options = options.set('measureType', measureType.toString()); }

        return this.http.get(`${this.resourceUrl}/energyStatisticsByLightModule/${id}`, { params: options, observe: 'response' }).pipe(map((res: HttpResponse<EnergyStatistics>) => {
            const copy: EnergyStatistics = Object.assign({}, res.body);
            return copy;
        }));
    }

    getStatisticsByNodeId(id: number, measureType?: number, startInterval?: Date, endInterval?: Date, currentDate?: Date): Observable<HttpResponse<EnergyStatisticsByResourceId[]>> {
        let options = createRequestOption();
        if (startInterval != null) {   options = options.set('startInterval', startInterval.toISOString()); }
        if (endInterval != null) {   options = options.set('endInterval', endInterval.toISOString()); }
        if (endInterval != null) {   options = options.set('currentDate', currentDate.toISOString()); }
        if (measureType != null) {   options = options.set('measureType', measureType.toString()); }

        return this.http.get(`${this.resourceUrl}/energyStatisticsByNodeId/${id}`, { params: options, observe: 'response' }).pipe(map((res: HttpResponse<EnergyStatisticsByResourceId[]>)  => {
            const jsonResponse: EnergyStatisticsByResourceId[] = res.body;
            const body: EnergyStatisticsByResourceId[] = [];
            for (let i = 0; i < jsonResponse.length; i++) {
                body.push(this.convertItemFromServer(jsonResponse[i]));
            }
            return res.clone({body});
        }));
    }

    getDimAndPowerAtTimestampByNodeId(id: number, timestamp?: Date): Observable<HttpResponse<EnergyStatisticsByResourceId[]>> {
        let options = createRequestOption();
        if (timestamp != null)  {   options = options.set('timestamp', timestamp.toISOString()); }
        return this.http.get(`${this.resourceUrl}/dimAndPowerAtTimestamp/${id}`, { params: options, observe: 'response' }).pipe(map((res: HttpResponse<EnergyStatisticsByResourceId[]>)  => this.convertArrayResponse(res)));
    }

    query(req?: any): Observable<HttpResponse<InstallationWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<InstallationWilamp[]>(`${this.resourceUrl}/`, { params: options, observe: 'response' }).pipe(
            map((res: HttpResponse<InstallationWilamp[]>) => this.convertArrayResponse(res)));
    }

    delete(id: number): Observable<HttpResponse<any>> {
        return this.http.delete<any>(`${this.resourceUrl}/${id}`, { observe: 'response'});
    }

    search(req?: any): Observable<HttpResponse<InstallationWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<InstallationWilamp[]>(this.resourceSearchUrl, { params: options, observe: 'response' }).pipe(
            map((res: HttpResponse<InstallationWilamp[]>) => this.convertArrayResponse(res)));
    }

    private convertResponse(res: EntityResponseType): EntityResponseType {
        const body: InstallationWilamp = this.convertItemFromServer(res.body);
        return res.clone({body});
    }

    private convertArrayResponse(res: HttpResponse<InstallationWilamp[]>): HttpResponse<InstallationWilamp[]> {
        const jsonResponse: InstallationWilamp[] = res.body;
        const body: InstallationWilamp[] = [];
        for (let i = 0; i < jsonResponse.length; i++) {
            body.push(this.convertItemFromServer(jsonResponse[i]));
        }
        return res.clone({body});
    }

    /**
     * Convert a returned JSON object to InstallationWilamp.
     */
    private convertEnergyStatisticsItemFromServer(json: any): EnergyStatisticsByResourceId {
        const entity: EnergyStatisticsByResourceId = Object.assign(new EnergyStatisticsByResourceId(), json);
        entity.lastMeasureTimestamp = this.dateUtils
            .convertDateTimeFromServer(json.lastMeasureTimestamp);
        return entity;
    }

    /**
     * Convert a returned JSON object to InstallationWilamp.
     */
    private convertItemFromServer(installation: InstallationWilamp): InstallationWilamp {
        const copy: InstallationWilamp = Object.assign({}, installation);
        copy.preparationDate = this.dateUtils
            .convertDateTimeFromServer(installation.preparationDate);
        copy.installationDate = this.dateUtils
            .convertDateTimeFromServer(installation.installationDate);
        return copy;
    }

    /**
     * Convert a InstallationWilamp to a JSON which can be sent to the server.
     */
    private convert(installation: InstallationWilamp): InstallationWilamp {
        const copy: InstallationWilamp = Object.assign({}, installation);

        copy.preparationDate = this.dateUtils.toDate(installation.preparationDate);

        copy.installationDate = this.dateUtils.toDate(installation.installationDate);
        return copy;
    }
}
