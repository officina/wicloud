import {AfterViewInit, Component, Input, OnDestroy, OnInit} from '@angular/core';
import {GoogleMapsAPIWrapper, MapsAPILoader} from '@agm/core';
import {GoogleMap} from '@agm/core/services/google-maps-types';
import {GLOBALDATABASE__GATEWAYS_FETCHED, MAP_INSTANCE_GETTER__MAP_OBTAINED} from '../constants/events.constants';
import {JhiEventManager} from 'ng-jhipster';

declare var google: any;

/***
 * This component allows to extract an instance of the @agm map, in order to make it works you should
 * insert the selector inside an @agm map like the example following
 *   <agm-map>
 *      <extract_map_instance mapId="targetMapInstance"></extract_map_instance>
 *   </agm-map>
 * The map instance will be extracted and will be collected in the Global Database or sent by event.
 */
@Component({
  selector: 'extract_map_instance',
  template: `<button [class]="className">Okay</button>`
})
export class MapInstanceGetterComponent implements OnInit, AfterViewInit {
    @Input() mapId = '';
    private googleMapsLoaded = false;
    private googleGeocoder: any;
    private mapInstance: GoogleMap;
    public className: any;
    constructor(
        private mapsAPILoader: MapsAPILoader,
        private mapsAPIWrapper: GoogleMapsAPIWrapper,
        private eventManager: JhiEventManager
    ) {
    }

    ngOnInit() {
        console.log('Map instance: ' + this.mapId);
    }

    ngAfterViewInit() {
        console.log('afer');
        this.mapsAPIWrapper.getNativeMap().then((m) => {
            console.log('native map', m);
            this.mapInstance = m;
            this.googleMapsLoaded = true;
            this.eventManager.broadcast({
                name: MAP_INSTANCE_GETTER__MAP_OBTAINED,
                content: {
                    mapId: this.mapId,
                    mapInstance: this.mapInstance
                }
            });
        }, (err) => {
            console.log('error', err);
        });

        this.mapsAPILoader.load().then(() => {
            this.googleGeocoder = new google.maps.Geocoder();
        });
    }

}
