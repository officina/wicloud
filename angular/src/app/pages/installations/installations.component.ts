import { Component, OnInit } from '@angular/core';
import {Installation} from '../../_models/installation';
import {InstallationService} from '../../_services';

@Component({
  selector: 'ngx-installations',
  templateUrl: './installations.component.html',
  styleUrls: ['./installations.component.scss'],
})
export class InstallationsComponent implements OnInit {
  installations: Installation[];
  constructor(
    private installationService: InstallationService,
  ) {}

  ngOnInit() {
    this.installationService.getInstallationsForUser().subscribe(installations => {

        this.installations = <Installation[]> installations.results;
    })
  }
}
