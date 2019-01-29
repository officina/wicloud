import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { Observable, Subject } from 'rxjs';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import { EnergyMeterModuleWilamp } from './energy-meter-module-wilamp.model';
import { createRequestOption } from '../../shared';
import {environment} from '../../../environments/environment';

export type EntityResponseType = HttpResponse<EnergyMeterModuleWilamp>;

@Injectable()
export class EnergyMeterModuleWilampService {

    private resourceUrl =  `${environment.apiUrl}/api/energy-meter-module`;
    private resourceSearchUrl =  `${environment.apiUrl}/api/_search/energy-meter-module`;

    constructor(private http: HttpClient) { }

    create(energyMeterModule: EnergyMeterModuleWilamp): Observable<EntityResponseType> {
        const copy = this.convert(energyMeterModule);
        return this.http.post<EnergyMeterModuleWilamp>(this.resourceUrl, copy, { observe: 'response' })
            .map((res: EntityResponseType) => this.convertResponse(res));
    }

    update(energyMeterModule: EnergyMeterModuleWilamp): Observable<EntityResponseType> {
        const copy = this.convert(energyMeterModule);
        return this.http.put<EnergyMeterModuleWilamp>(this.resourceUrl, copy, { observe: 'response' })
            .map((res: EntityResponseType) => this.convertResponse(res));
    }

    find(id: number): Observable<EntityResponseType> {
        return this.http.get<EnergyMeterModuleWilamp>(`${this.resourceUrl}/${id}`, { observe: 'response'})
            .map((res: EntityResponseType) => this.convertResponse(res));
    }

    query(req?: any): Observable<HttpResponse<EnergyMeterModuleWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<EnergyMeterModuleWilamp[]>(`${this.resourceUrl}/`, { params: options, observe: 'response' })
            .map((res: HttpResponse<EnergyMeterModuleWilamp[]>) => this.convertArrayResponse(res));
    }

    delete(id: number): Observable<HttpResponse<any>> {
        return this.http.delete<any>(`${this.resourceUrl}/${id}`, { observe: 'response'});
    }

    search(req?: any): Observable<HttpResponse<EnergyMeterModuleWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<EnergyMeterModuleWilamp[]>(this.resourceSearchUrl, { params: options, observe: 'response' })
            .map((res: HttpResponse<EnergyMeterModuleWilamp[]>) => this.convertArrayResponse(res));
    }

    private convertResponse(res: EntityResponseType): EntityResponseType {
        const body: EnergyMeterModuleWilamp = this.convertItemFromServer(res.body);
        return res.clone({body});
    }

    private convertArrayResponse(res: HttpResponse<EnergyMeterModuleWilamp[]>): HttpResponse<EnergyMeterModuleWilamp[]> {
        const jsonResponse: EnergyMeterModuleWilamp[] = res.body;
        const body: EnergyMeterModuleWilamp[] = [];
        for (let i = 0; i < jsonResponse.length; i++) {
            body.push(this.convertItemFromServer(jsonResponse[i]));
        }
        return res.clone({body});
    }

    /**
     * Convert a returned JSON object to EnergyMeterModuleWilamp.
     */
    private convertItemFromServer(energyMeterModule: EnergyMeterModuleWilamp): EnergyMeterModuleWilamp {
        const copy: EnergyMeterModuleWilamp = Object.assign({}, energyMeterModule);
        return copy;
    }

    /**
     * Convert a EnergyMeterModuleWilamp to a JSON which can be sent to the server.
     */
    private convert(energyMeterModule: EnergyMeterModuleWilamp): EnergyMeterModuleWilamp {
        const copy: EnergyMeterModuleWilamp = Object.assign({}, energyMeterModule);
        return copy;
    }
}
