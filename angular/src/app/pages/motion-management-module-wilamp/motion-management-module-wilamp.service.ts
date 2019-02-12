import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { Observable, Subject } from 'rxjs';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import { JhiDateUtils } from 'ng-jhipster';
import { MotionManagementModuleWilamp } from './motion-management-module-wilamp.model';
import { createRequestOption } from '../../shared';
import {environment} from '../../../environments/environment';

export type EntityResponseType = HttpResponse<MotionManagementModuleWilamp>;

@Injectable()
export class MotionManagementModuleWilampService {

    private resourceUrl =  `${environment.apiUrl}/api/motion-management-module`;
    private resourceSearchUrl =  `${environment.apiUrl}/api/_search/motion-management-module`;

    constructor(private http: HttpClient, private dateUtils: JhiDateUtils) { }

    create(motionManagementModule: MotionManagementModuleWilamp): Observable<EntityResponseType> {
        const copy = this.convert(motionManagementModule);
        return this.http.post<MotionManagementModuleWilamp>(this.resourceUrl, copy, { observe: 'response' })
            .map((res: EntityResponseType) => this.convertResponse(res));
    }

    update(motionManagementModule: MotionManagementModuleWilamp): Observable<EntityResponseType> {
        const copy = this.convert(motionManagementModule);
        return this.http.put<MotionManagementModuleWilamp>(this.resourceUrl, copy, { observe: 'response' })
            .map((res: EntityResponseType) => this.convertResponse(res));
    }

    find(id: number): Observable<EntityResponseType> {
        return this.http.get<MotionManagementModuleWilamp>(`${this.resourceUrl}/${id}`, { observe: 'response'})
            .map((res: EntityResponseType) => this.convertResponse(res));
    }

    query(req?: any): Observable<HttpResponse<MotionManagementModuleWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<MotionManagementModuleWilamp[]>(`${this.resourceUrl}/`, { params: options, observe: 'response' })
            .map((res: HttpResponse<MotionManagementModuleWilamp[]>) => this.convertArrayResponse(res));
    }

    delete(id: number): Observable<HttpResponse<any>> {
        return this.http.delete<any>(`${this.resourceUrl}/${id}`, { observe: 'response'});
    }

    search(req?: any): Observable<HttpResponse<MotionManagementModuleWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<MotionManagementModuleWilamp[]>(this.resourceSearchUrl, { params: options, observe: 'response' })
            .map((res: HttpResponse<MotionManagementModuleWilamp[]>) => this.convertArrayResponse(res));
    }

    private convertResponse(res: EntityResponseType): EntityResponseType {
        const body: MotionManagementModuleWilamp = this.convertItemFromServer(res.body);
        return res.clone({body});
    }

    private convertArrayResponse(res: HttpResponse<MotionManagementModuleWilamp[]>): HttpResponse<MotionManagementModuleWilamp[]> {
        const jsonResponse: MotionManagementModuleWilamp[] = res.body;
        const body: MotionManagementModuleWilamp[] = [];
        for (let i = 0; i < jsonResponse.length; i++) {
            body.push(this.convertItemFromServer(jsonResponse[i]));
        }
        return res.clone({body});
    }

    /**
     * Convert a returned JSON object to MotionManagementModuleWilamp.
     */
    private convertItemFromServer(motionManagementModule: MotionManagementModuleWilamp): MotionManagementModuleWilamp {
        const copy: MotionManagementModuleWilamp = Object.assign({}, motionManagementModule);
        copy.createdTimestamp = this.dateUtils
            .convertDateTimeFromServer(motionManagementModule.createdTimestamp);
        return copy;
    }

    /**
     * Convert a MotionManagementModuleWilamp to a JSON which can be sent to the server.
     */
    private convert(motionManagementModule: MotionManagementModuleWilamp): MotionManagementModuleWilamp {
        const copy: MotionManagementModuleWilamp = Object.assign({}, motionManagementModule);

        copy.createdTimestamp = this.dateUtils.toDate(motionManagementModule.createdTimestamp);
        return copy;
    }
}
