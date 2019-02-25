import {Component, Input, OnInit} from '@angular/core';
import {Installation} from '../../../_models/installation';

@Component({
  selector: 'ngx-installation-wilamp-widget',
  templateUrl: './installation-wilamp-widget.component.html',
  styleUrls: ['./installation-wilamp-widget.component.scss'],
})
export class InstallationWilampWidgetComponent implements OnInit {
  @Input() installation: Installation;
  constructor() {
  }

  ngOnInit() {
  }


}
