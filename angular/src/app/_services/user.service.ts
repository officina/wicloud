import { Injectable } from '@angular/core';
import {HttpClient, HttpResponse} from '@angular/common/http';

import { User } from '../_models';
import {environment} from '../../environments/environment';
import {NbAuthJWTToken, NbAuthService} from '@nebular/auth';
import { Observable } from 'rxjs';
import { of } from 'rxjs/observable/of';

@Injectable({
  providedIn: 'root',
})
export class UserService {

    private resourceUrl = `${environment.apiUrl}/users`;

    constructor(private authService: NbAuthService, private http: HttpClient) {
        this.authService.onTokenChange()
        .subscribe((token: NbAuthJWTToken) => {

          if (token.isValid()) {
            this.user = token.getPayload(); // receive payload from token and assign it to our `user` variable
          }

        });

    }

    user = {
        name: '',
        given_name: '',
        family_name: '',
        rank: '',
        level: 1,
    };

    getUser(): Observable<any> {
        return of(this.user);
    }

    getAll() {
        return this.http.get<User[]>(`${environment.apiUrl}/users`);
    }

    getById(id: number) {
        return this.http.get(`${environment.apiUrl}/users/` + id);
    }

    register(user: User) {
        return this.http.post(`${environment.apiUrl}/users/register`, user);
    }

    update(user: User) {
        return this.http.put(`${environment.apiUrl}/users/` + user.id, user);
    }

    delete(id: number) {
        return this.http.delete(`${environment.apiUrl}/users/` + id);
    }

    query(req?: any): Observable<HttpResponse<User[]>> {
        const options = null;
        return this.http.get<User[]>(`${this.resourceUrl}/`, { params: options, observe: 'response' });
    }

}
