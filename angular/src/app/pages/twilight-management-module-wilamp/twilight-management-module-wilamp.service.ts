import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { Observable, Subject } from 'rxjs';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import { JhiDateUtils } from 'ng-jhipster';
import { TwilightManagementModuleWilamp } from './twilight-management-module-wilamp.model';
import { createRequestOption } from '../../shared';
import {environment} from '../../../environments/environment';

export type EntityResponseType = HttpResponse<TwilightManagementModuleWilamp>;

@Injectable()
export class TwilightManagementModuleWilampService {

    private resourceUrl =  `${environment.apiUrl}/api/twilight-management-module`;
    private resourceSearchUrl =  `${environment.apiUrl}/api/_search/twilight-management-module`;

    constructor(private http: HttpClient, private dateUtils: JhiDateUtils) { }

    create(twilightManagementModule: TwilightManagementModuleWilamp): Observable<EntityResponseType> {
        const copy = this.convert(twilightManagementModule);
        return this.http.post<TwilightManagementModuleWilamp>(this.resourceUrl, copy, { observe: 'response' })
            .map((res: EntityResponseType) => this.convertResponse(res));
    }

    update(twilightManagementModule: TwilightManagementModuleWilamp): Observable<EntityResponseType> {
        const copy = this.convert(twilightManagementModule);
        return this.http.put<TwilightManagementModuleWilamp>(this.resourceUrl, copy, { observe: 'response' })
            .map((res: EntityResponseType) => this.convertResponse(res));
    }

    find(id: number): Observable<EntityResponseType> {
        return this.http.get<TwilightManagementModuleWilamp>(`${this.resourceUrl}/${id}`, { observe: 'response'})
            .map((res: EntityResponseType) => this.convertResponse(res));
    }

    query(req?: any): Observable<HttpResponse<TwilightManagementModuleWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<TwilightManagementModuleWilamp[]>(`${this.resourceUrl}/`, { params: options, observe: 'response' })
            .map((res: HttpResponse<TwilightManagementModuleWilamp[]>) => this.convertArrayResponse(res));
    }

    delete(id: number): Observable<HttpResponse<any>> {
        return this.http.delete<any>(`${this.resourceUrl}/${id}`, { observe: 'response'});
    }

    search(req?: any): Observable<HttpResponse<TwilightManagementModuleWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<TwilightManagementModuleWilamp[]>(this.resourceSearchUrl, { params: options, observe: 'response' })
            .map((res: HttpResponse<TwilightManagementModuleWilamp[]>) => this.convertArrayResponse(res));
    }

    private convertResponse(res: EntityResponseType): EntityResponseType {
        const body: TwilightManagementModuleWilamp = this.convertItemFromServer(res.body);
        return res.clone({body});
    }

    private convertArrayResponse(res: HttpResponse<TwilightManagementModuleWilamp[]>): HttpResponse<TwilightManagementModuleWilamp[]> {
        const jsonResponse: TwilightManagementModuleWilamp[] = res.body;
        const body: TwilightManagementModuleWilamp[] = [];
        for (let i = 0; i < jsonResponse.length; i++) {
            body.push(this.convertItemFromServer(jsonResponse[i]));
        }
        return res.clone({body});
    }

    /**
     * Convert a returned JSON object to TwilightManagementModuleWilamp.
     */
    private convertItemFromServer(twilightManagementModule: TwilightManagementModuleWilamp): TwilightManagementModuleWilamp {
        const copy: TwilightManagementModuleWilamp = Object.assign({}, twilightManagementModule);
        copy.createdTimestamp = this.dateUtils
            .convertDateTimeFromServer(twilightManagementModule.createdTimestamp);
        return copy;
    }

    /**
     * Convert a TwilightManagementModuleWilamp to a JSON which can be sent to the server.
     */
    private convert(twilightManagementModule: TwilightManagementModuleWilamp): TwilightManagementModuleWilamp {
        const copy: TwilightManagementModuleWilamp = Object.assign({}, twilightManagementModule);

        copy.createdTimestamp = this.dateUtils.toDate(twilightManagementModule.createdTimestamp);
        return copy;
    }
}
