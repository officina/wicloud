import {Component, Input, OnInit} from '@angular/core';

import * as L from 'leaflet';
import 'style-loader!leaflet/dist/leaflet.css';
import {Installation} from "../../../_models/installation";

@Component({
  selector: 'ngx-leaflet-map-widget',
  styleUrls: ['./leaflet-map-widget.component.scss'],
  template: `
      <div leaflet [leafletOptions]="options"
      (leafletMapReady)="onMapReady($event)"
      ></div>
  `,
})
export class LeafletMapWidgetComponent implements OnInit {
  @Input() latitude: number;
  @Input() longitude: number;
  private map: any;

  options = {
    layers: [
      L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 18, attribution: '...' }),
    ],
    zoom: 5,
    center: L.latLng({ lat: 38.991709, lng: -76.886109 }),
  };

  onMapReady(map: any) {
    this.map = map;
        if (this.latitude) {
          this.map.panTo(L.latLng({ lat: this.latitude, lng: this.longitude }));
    }

  }

  ngOnInit() {
    if (this.latitude && this.map) {
          this.map.panTo(L.latLng({ lat: this.latitude, lng: this.longitude }));
    }
  }

}
