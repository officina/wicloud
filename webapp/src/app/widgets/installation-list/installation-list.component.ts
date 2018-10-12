import { Component, OnInit } from '@angular/core';
import {Installation} from "../../_models/installation";
import {InstallationService} from "../../_services/installation.service";

@Component({
  selector: 'app-installation-list',
  templateUrl: './installation-list.component.html',
  styleUrls: ['./installation-list.component.css']
})
export class InstallationListComponent implements OnInit {

  installations:Array<Installation>;

  constructor(private installationservice:InstallationService) { }

  ngOnInit(){

    this.installationservice.getInstallationsForUser().subscribe(installations => {

            console.log("got installations: " + installations.results);
            this.installations = installations.results;
        });
  }



}
