import {Component, Input, OnInit} from '@angular/core';
import {Installation} from '../../../_models/installation';

@Component({
  selector: 'ngx-installation-detail',
  templateUrl: './detail.component.html',
  styleUrls: ['./detail.component.scss'],
})
export class DetailComponent implements OnInit {
  @Input() installation: Installation;
  constructor() { }

  ngOnInit() {
  }

}
