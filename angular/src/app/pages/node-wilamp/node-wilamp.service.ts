
import {map} from 'rxjs/operators';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient, HttpResponse } from '@angular/common/http';

import { NodeWilamp } from './node-wilamp.model';
import {environment} from '../../../environments/environment';
import {createRequestOption} from '../../shared/model/request-util';

export type EntityResponseType = HttpResponse<NodeWilamp>;

@Injectable({
  providedIn: 'root',
})
export class NodeWilampService {

    private resourceUrl =  `${environment.apiUrl}/api/node`;
    private resourceSearchUrl =  `${environment.apiUrl}/api/_search/node`;

    constructor(private http: HttpClient) { }

    create(node: NodeWilamp): Observable<EntityResponseType> {
        const copy = this.convert(node);
        return this.http.post<NodeWilamp>(this.resourceUrl, copy, { observe: 'response' }).pipe(
            map((res: EntityResponseType) => this.convertResponse(res)));
    }

    update(node: NodeWilamp): Observable<EntityResponseType> {
        const copy = this.convert(node);
        return this.http.put<NodeWilamp>(this.resourceUrl, copy, { observe: 'response' }).pipe(
            map((res: EntityResponseType) => this.convertResponse(res)));
    }

    find(id: number): Observable<EntityResponseType> {
        return this.http.get<NodeWilamp>(`${this.resourceUrl}/${id}`, { observe: 'response'}).pipe(
            map((res: EntityResponseType) => this.convertResponse(res)));
    }

    findByInstallation(installationId: number, req?: any): Observable<HttpResponse<NodeWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get(`${this.resourceUrl}-by-installation/${installationId}`, { params: options, observe: 'response' }).pipe(
            map((res: HttpResponse<NodeWilamp[]>)  => this.convertArrayResponse(res)));
    }

    query(req?: any): Observable<HttpResponse<NodeWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<NodeWilamp[]>(`${this.resourceUrl}/`, { params: options, observe: 'response' }).pipe(
            map((res: HttpResponse<NodeWilamp[]>) => this.convertArrayResponse(res)));
    }

    delete(id: number): Observable<HttpResponse<any>> {
        return this.http.delete<any>(`${this.resourceUrl}/${id}`, { observe: 'response'});
    }

    search(req?: any): Observable<HttpResponse<NodeWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<NodeWilamp[]>(this.resourceSearchUrl, { params: options, observe: 'response' }).pipe(
            map((res: HttpResponse<NodeWilamp[]>) => this.convertArrayResponse(res)));
    }

    private convertResponse(res: EntityResponseType): EntityResponseType {
        const body: NodeWilamp = this.convertItemFromServer(res.body);
        return res.clone({body});
    }

    private convertArrayResponse(res: HttpResponse<NodeWilamp[]>): HttpResponse<NodeWilamp[]> {
        const jsonResponse: NodeWilamp[] = res.body;
        const body: NodeWilamp[] = [];
        for (let i = 0; i < jsonResponse.length; i++) {
            body.push(this.convertItemFromServer(jsonResponse[i]));
        }
        return res.clone({body});
    }

    /**
     * Convert a returned JSON object to NodeWilamp.
     */
    private convertItemFromServer(node: NodeWilamp): NodeWilamp {
        const nodeW = new NodeWilamp();
        const copy = Object.assign(nodeW, node);
        // const copy: NodeWilamp = Object.assign({}, node);
        return copy;
    }

    /**
     * Convert a NodeWilamp to a JSON which can be sent to the server.
     */
    private convert(node: NodeWilamp): NodeWilamp {
        const copy: NodeWilamp = Object.assign({}, node);
        return copy;
    }
}
