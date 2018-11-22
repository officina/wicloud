import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {environment} from '../../environments/environment';

@Injectable({
  providedIn: 'root',
})

export class InstallationService {



  constructor(private http: HttpClient) {


  }


  getInstallationsForUser() {
        return this.http.get<any>(`${environment.apiUrl}/api/installation/`);
    }
}
