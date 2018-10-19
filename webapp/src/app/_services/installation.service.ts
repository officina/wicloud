import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {map} from "rxjs/operators";

import {Installation} from "../_models/installation";
import {User} from "../_models";

@Injectable({
  providedIn: 'root'
})

export class InstallationService {



  constructor(private http: HttpClient) {


  }


  getInstallationsForUser() {

        console.log("calling installation list service");
        return this.http.get<any>(`${config.apiUrl}/backend/installation/list/`);
    }
}
