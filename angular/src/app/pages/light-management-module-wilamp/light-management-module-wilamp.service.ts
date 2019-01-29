import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { Observable, Subject } from 'rxjs';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import { LightManagementModuleWilamp } from './light-management-module-wilamp.model';
import { createRequestOption } from '../../shared';
import {environment} from '../../../environments/environment';

export type EntityResponseType = HttpResponse<LightManagementModuleWilamp>;

@Injectable()
export class LightManagementModuleWilampService {

    private resourceUrl =  `${environment.apiUrl}/api/light-management-module`;
    private resourceSearchUrl =  `${environment.apiUrl}/api/_search/light-management-module`;

    constructor(private http: HttpClient) { }

    create(lightManagementModule: LightManagementModuleWilamp): Observable<EntityResponseType> {
        const copy = this.convert(lightManagementModule);
        return this.http.post<LightManagementModuleWilamp>(this.resourceUrl, copy, { observe: 'response' })
            .map((res: EntityResponseType) => this.convertResponse(res));
    }

    update(lightManagementModule: LightManagementModuleWilamp): Observable<EntityResponseType> {
        const copy = this.convert(lightManagementModule);
        return this.http.put<LightManagementModuleWilamp>(this.resourceUrl, copy, { observe: 'response' })
            .map((res: EntityResponseType) => this.convertResponse(res));
    }

    find(id: number): Observable<EntityResponseType> {
        return this.http.get<LightManagementModuleWilamp>(`${this.resourceUrl}/${id}`, { observe: 'response'})
            .map((res: EntityResponseType) => this.convertResponse(res));
    }

    query(req?: any): Observable<HttpResponse<LightManagementModuleWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<LightManagementModuleWilamp[]>(`${this.resourceUrl}/`, { params: options, observe: 'response' })
            .map((res: HttpResponse<LightManagementModuleWilamp[]>) => this.convertArrayResponse(res));
    }

    delete(id: number): Observable<HttpResponse<any>> {
        return this.http.delete<any>(`${this.resourceUrl}/${id}`, { observe: 'response'});
    }

    search(req?: any): Observable<HttpResponse<LightManagementModuleWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<LightManagementModuleWilamp[]>(this.resourceSearchUrl, { params: options, observe: 'response' })
            .map((res: HttpResponse<LightManagementModuleWilamp[]>) => this.convertArrayResponse(res));
    }

    private convertResponse(res: EntityResponseType): EntityResponseType {
        const body: LightManagementModuleWilamp = this.convertItemFromServer(res.body);
        return res.clone({body});
    }

    private convertArrayResponse(res: HttpResponse<LightManagementModuleWilamp[]>): HttpResponse<LightManagementModuleWilamp[]> {
        const jsonResponse: LightManagementModuleWilamp[] = res.body;
        const body: LightManagementModuleWilamp[] = [];
        for (let i = 0; i < jsonResponse.length; i++) {
            body.push(this.convertItemFromServer(jsonResponse[i]));
        }
        return res.clone({body});
    }

    /**
     * Convert a returned JSON object to LightManagementModuleWilamp.
     */
    private convertItemFromServer(lightManagementModule: LightManagementModuleWilamp): LightManagementModuleWilamp {
        const copy: LightManagementModuleWilamp = Object.assign({}, lightManagementModule);
        return copy;
    }

    /**
     * Convert a LightManagementModuleWilamp to a JSON which can be sent to the server.
     */
    private convert(lightManagementModule: LightManagementModuleWilamp): LightManagementModuleWilamp {
        const copy: LightManagementModuleWilamp = Object.assign({}, lightManagementModule);
        return copy;
    }
}
