
import {map} from 'rxjs/operators';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { JhiDateUtils } from 'ng-jhipster';
import { OrderWilamp } from './order-wilamp.model';
import {environment} from '../../../environments/environment';
import {createRequestOption} from '../../shared/model/request-util';

export type EntityResponseType = HttpResponse<OrderWilamp>;

@Injectable()
export class OrderWilampService {

    private resourceUrl =  `${environment.apiUrl}/api/order`;
    private resourceSearchUrl =  `${environment.apiUrl}/api/_search/order`;

    constructor(private http: HttpClient, private dateUtils: JhiDateUtils) { }

    create(order: OrderWilamp): Observable<EntityResponseType> {
        const copy = this.convert(order);
        return this.http.post<OrderWilamp>(this.resourceUrl, copy, { observe: 'response' }).pipe(
            map((res: EntityResponseType) => this.convertResponse(res)));
    }

    update(order: OrderWilamp): Observable<EntityResponseType> {
        const copy = this.convert(order);
        return this.http.put<OrderWilamp>(this.resourceUrl, copy, { observe: 'response' }).pipe(
            map((res: EntityResponseType) => this.convertResponse(res)));
    }

    find(id: number): Observable<EntityResponseType> {
        return this.http.get<OrderWilamp>(`${this.resourceUrl}/${id}`, { observe: 'response'}).pipe(
            map((res: EntityResponseType) => this.convertResponse(res)));
    }

    query(req?: any): Observable<HttpResponse<OrderWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<OrderWilamp[]>(`${this.resourceUrl}/`, { params: options, observe: 'response' }).pipe(
            map((res: HttpResponse<OrderWilamp[]>) => this.convertArrayResponse(res)));
    }

    delete(id: number): Observable<HttpResponse<any>> {
        return this.http.delete<any>(`${this.resourceUrl}/${id}`, { observe: 'response'});
    }

    search(req?: any): Observable<HttpResponse<OrderWilamp[]>> {
        const options = createRequestOption(req);
        return this.http.get<OrderWilamp[]>(this.resourceSearchUrl, { params: options, observe: 'response' }).pipe(
            map((res: HttpResponse<OrderWilamp[]>) => this.convertArrayResponse(res)));
    }

    private convertResponse(res: EntityResponseType): EntityResponseType {
        const body: OrderWilamp = this.convertItemFromServer(res.body);
        return res.clone({body});
    }

    private convertArrayResponse(res: HttpResponse<OrderWilamp[]>): HttpResponse<OrderWilamp[]> {
        const jsonResponse: OrderWilamp[] = res.body;
        const body: OrderWilamp[] = [];
        for (let i = 0; i < jsonResponse.length; i++) {
            body.push(this.convertItemFromServer(jsonResponse[i]));
        }
        return res.clone({body});
    }

    /**
     * Convert a returned JSON object to OrderWilamp.
     */
    private convertItemFromServer(order: OrderWilamp): OrderWilamp {
        const copy: OrderWilamp = Object.assign({}, order);
        copy.orderDate = this.dateUtils
            .convertDateTimeFromServer(order.orderDate);
        copy.preparationDate = this.dateUtils
            .convertDateTimeFromServer(order.preparationDate);
        return copy;
    }

    /**
     * Convert a OrderWilamp to a JSON which can be sent to the server.
     */
    private convert(order: OrderWilamp): OrderWilamp {
        const copy: OrderWilamp = Object.assign({}, order);

        copy.orderDate = this.dateUtils.toDate(order.orderDate);

        copy.preparationDate = this.dateUtils.toDate(order.preparationDate);
        return copy;
    }
}
