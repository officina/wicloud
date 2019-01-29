import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { Observable, Subject } from 'rxjs';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import { NodeModulesWilamp } from './node-modules-wilamp.model';
import { createRequestOption } from '../../shared';
import {environment} from '../../../environments/environment';

export type EntityResponseType = HttpResponse<NodeModulesWilamp>;

@Injectable()
export class NodeModulesWilampService {

    private resourceUrl =  `${environment.apiUrl}/api/node-module`;
    private resourceSearchUrl =  `${environment.apiUrl}/api/_search/node-module`;

    constructor(private http: HttpClient) { }

    create(nodeModules: NodeModulesWilamp): Observable<EntityResponseType> {
        const copy = this.convert(nodeModules);
        return this.http.post<NodeModulesWilamp>(this.resourceUrl, copy, { observe: 'response' })
            .map((res: EntityResponseType) => this.convertResponse(res));
    }

    update(nodeModules: NodeModulesWilamp): Observable<EntityResponseType> {
        const copy = this.convert(nodeModules);
        return this.http.put<NodeModulesWilamp>(this.resourceUrl, copy, { observe: 'response' })
            .map((res: EntityResponseType) => this.convertResponse(res));
    }

    find(id: number): Observable<EntityResponseType> {
        return this.http.get<NodeModulesWilamp>(`${this.resourceUrl}/${id}`, { observe: 'response'})
            .map((res: EntityResponseType) => this.convertResponse(res));
    }

    query(req?: any): Observable<HttpResponse<NodeModulesWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<NodeModulesWilamp[]>(`${this.resourceUrl}/`, { params: options, observe: 'response' })
            .map((res: HttpResponse<NodeModulesWilamp[]>) => this.convertArrayResponse(res));
    }

    delete(id: number): Observable<HttpResponse<any>> {
        return this.http.delete<any>(`${this.resourceUrl}/${id}`, { observe: 'response'});
    }

    search(req?: any): Observable<HttpResponse<NodeModulesWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<NodeModulesWilamp[]>(this.resourceSearchUrl, { params: options, observe: 'response' })
            .map((res: HttpResponse<NodeModulesWilamp[]>) => this.convertArrayResponse(res));
    }

    private convertResponse(res: EntityResponseType): EntityResponseType {
        const body: NodeModulesWilamp = this.convertItemFromServer(res.body);
        return res.clone({body});
    }

    private convertArrayResponse(res: HttpResponse<NodeModulesWilamp[]>): HttpResponse<NodeModulesWilamp[]> {
        const jsonResponse: NodeModulesWilamp[] = res.body;
        const body: NodeModulesWilamp[] = [];
        for (let i = 0; i < jsonResponse.length; i++) {
            body.push(this.convertItemFromServer(jsonResponse[i]));
        }
        return res.clone({body});
    }

    /**
     * Convert a returned JSON object to NodeModulesWilamp.
     */
    private convertItemFromServer(nodeModules: NodeModulesWilamp): NodeModulesWilamp {
        const copy: NodeModulesWilamp = Object.assign({}, nodeModules);
        return copy;
    }

    /**
     * Convert a NodeModulesWilamp to a JSON which can be sent to the server.
     */
    private convert(nodeModules: NodeModulesWilamp): NodeModulesWilamp {
        const copy: NodeModulesWilamp = Object.assign({}, nodeModules);
        return copy;
    }
}
