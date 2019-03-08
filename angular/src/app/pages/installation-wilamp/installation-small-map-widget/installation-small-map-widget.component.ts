import {AfterViewInit, Component, OnDestroy, OnInit} from '@angular/core';
import {
    GLOBALDATABASE__LIGHT_FIXTURES_FETCHED,
    INSTALLATION__SELECTED_ID_CHANGED, INSTALLATION__SELECTED_INSTALLATION_CHANGED, MAP_INSTANCE_GETTER__MAP_OBTAINED,
} from '../../../shared/constants/events.constants';
import {EntityIconMarker, MapLeafletLayers} from '../../../shared/maps/map.models';
import {NodeWilamp, NodeWilampService} from '../../node-wilamp';
import {InstallationWilampService} from '../installation-wilamp.service';
import {GatewayWilampService} from '../../gateway-wilamp';
import {Subscription} from 'rxjs/Rx';
import {JhiEventManager} from 'ng-jhipster';
import {GlobalDatabaseService} from '../../../shared/global-database/global-database.service';
import GMap = google.maps.Map;
import {Helpers, Principal} from '../../../shared';
import * as L from 'leaflet';
import 'leaflet.markercluster';
import 'leaflet.awesome-markers/dist/leaflet.awesome-markers';
// import 'leaflet-canvas-marker';
import 'leaflet.awesome-markers';
import {DomSanitizer} from '@angular/platform-browser';
import {icon} from 'leaflet';

declare let HeatmapOverlay: any;

/**
 * This component make extensive use of the following plugins for leaflet
 * ° leaflet: https://github.com/Asymmetrik/Leaflet
 * ° ngx-leaflet: https://github.com/Asymmetrik/ngx-leaflet
 * ° leaflet-d3: https://github.com/Asymmetrik/leaflet-d3
 * ° ngx-leaflet-d3: https://github.com/Asymmetrik/ngx-leaflet-d3
 * ° leaflet-markercluster: https://github.com/Leaflet/Leaflet.markercluster
 * ° ngx-leaflet-markercluster: https://github.com/Asymmetrik/ngx-leaflet-markercluster
 * ° ngx-leaflet-draw: https://github.com/Asymmetrik/ngx-leaflet-draw
 *
 *
 * ° http://labs.easyblog.it/maps/leaflet-panel-layers/ (custom buttons with layers)
 * ° https://github.com/ismyrnow/leaflet-groupedlayercontrol
 * ° https://github.com/elrobis/L.Control.ZoomBar
 * ° http://brunob.github.io/leaflet.fullscreen/
 * ° https://github.com/yigityuce/Leaflet.Control.Custom (menu figo)
 * ° https://github.com/aratcliffe/Leaflet.contextmenu
 * ° https://github.com/Turbo87/sidebar-v2 ( side bar )
 * ° https://github.com/eJuke/Leaflet.Canvas-Markers ( Importante: canvas rendering per speedup dei marker )
 * ° http://cyrilcherian.github.io/Leaflet-Fullcanvas/demo/Canvas-With-Points.html
 *
 */
@Component({
  selector: 'ngx-instsallation-small-map-widget',
  templateUrl: './installation-small-map-widget.component.html',
  styleUrls: ['installation-small-map-widget.component.scss'],

})
export class InstallationSmallMapWidgetComponent implements OnInit, OnDestroy, AfterViewInit {
    /* Marker cluster */
    lcuClusterGroup: L.MarkerClusterGroup = L.markerClusterGroup({
        spiderfyOnMaxZoom: true,
        showCoverageOnHover: false,
        zoomToBoundsOnClick: true,
        removeOutsideVisibleBounds: true,
        disableClusteringAtZoom: 14,
    });
    lcuCluster = {
        id: 'lcuCluster',
        name: 'LCU',
        enabled: true,
        layer: this.lcuClusterGroup,
    };
    lcuClusterCanvasRendering = {
        id: 'lcuClusterCR',
        name: 'LCU - CR',
        enabled: true,
        layer: undefined//L.canvasIconLayer(),
    };
    dcuClusterGroup: L.MarkerClusterGroup = L.markerClusterGroup({
        spiderfyOnMaxZoom: true,
        showCoverageOnHover: true,
        zoomToBoundsOnClick: true,
        removeOutsideVisibleBounds: true,
        disableClusteringAtZoom: 14,
    });
    dcuCluster = {
        id: 'dcuCluster',
        name: 'DCU',
        enabled: true,
        layer: this.dcuClusterGroup,
    };
    LAYER_OCM = {
        id: 'opencyclemap',
        name: 'Open Cycle Map',
        enabled: false,
        layer: L.tileLayer('http://{s}.tile.opencyclemap.org/cycle/{z}/{x}/{y}.png', {
            maxZoom: 20,
            attribution: 'Open Cycle Map',
        }),
    };
    LAYER_OSM = {
        id: 'openstreetmap',
        name: 'Open Street Map',
        enabled: false,
        layer: L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 20,
            attribution: 'Open Street Map',
        }),
    };
    LAYER_GOOGLE_HYBRID = {
        id: 'googlehybrid',
        name: 'Google Hybrid Map',
        enabled: true,
        layer: L.tileLayer('http://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}', {
            maxZoom: 20,
            subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
        }),
    };
    LAYER_GOOGLE_STREET = {
        id: 'googlestreet',
        name: 'Google Streets Map',
        enabled: false,
        layer: L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', {
            maxZoom: 20,
            subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
        }),
    };
    leafletMap: L.Map;
    // Form model object
    model = new MapLeafletLayers(
        [ this.LAYER_OSM, this.LAYER_OCM, this.LAYER_GOOGLE_HYBRID, this.LAYER_GOOGLE_STREET ],
        this.LAYER_GOOGLE_HYBRID.id,
        [  this.lcuCluster, this.lcuClusterCanvasRendering, this.dcuCluster ],
    );
    // Values to bind to Leaflet Directive
    layers: L.Layer[];
    layersControl = {
        baseLayers: {
            'Open Street Map': this.LAYER_OSM.layer,
            'Open Cycle Map': this.LAYER_OCM.layer,
            'Google Hybrid Map': this.LAYER_GOOGLE_HYBRID.layer,
            'Google Streets Map': this.LAYER_GOOGLE_STREET.layer,
        },
        overlays: {
            LCU: this.lcuCluster.layer,
            LCU_CR: this.lcuClusterCanvasRendering.layer,
            DCU: this.dcuCluster.layer,
        },
    };
    options = {
        zoom: 10,
        center: L.latLng(46.879966, -121.726909),
    };
    private eventSubscriber: Subscription;
    private eventSubscriberSelectedIdChanged: Subscription;
    public enableLeafletMap = true;
    public min = 1;
    public max = 22;
    public disabledValue = 22;
    public demo = 22;
    public val = 22;
    public selectedNode: NodeWilamp = null;
    public mapIconOptions = {
        useSimpleIcon: false,
        groupBy: '',
        filterOptions: '',
    };
    private canvasMarkersInitialized: boolean;
    constructor(
        private sanitizer: DomSanitizer,
        private installationService: InstallationWilampService,
        private nodeService: NodeWilampService,
        private gatewayService: GatewayWilampService,
        private eventManager: JhiEventManager,
        private principal: Principal,
        public globalDatabase: GlobalDatabaseService,

    ) {
        this.apply();
    }

    ngOnInit() {
        this.canvasMarkersInitialized = false;
        this.registerFetch();
    }
    ngAfterViewInit() {
        this.nodesFetched();
    }

    nodesFetched() {
        if (this.enableLeafletMap) {
            if (this.globalDatabase.selectedInstallation && this.globalDatabase.selectedInstallation.lightFixtures.length > 0) {
                if (this.canvasMarkersInitialized) {
                    this.updateMarkerCanvasIcons();
                    this.leafletMap.fitBounds(this.lcuClusterCanvasRendering.layer.getBounds());
                } else {
                    this.updateMarkers();
                    this.leafletMap.fitBounds(this.lcuClusterCanvasRendering.layer.getBounds());
                }
            }
        }
    }

    ngOnDestroy() {
        this.eventManager.destroy(this.eventSubscriber);
        this.eventManager.destroy(this.eventSubscriberSelectedIdChanged);
    }

    registerFetch() {
        this.eventSubscriber = this.eventManager.subscribe(
            GLOBALDATABASE__LIGHT_FIXTURES_FETCHED,
            (response) => {
                this.nodesFetched();
            },
        );
        this.eventSubscriberSelectedIdChanged = this.eventManager.subscribe(
            INSTALLATION__SELECTED_INSTALLATION_CHANGED,
            (response) => {
                try {
                    if (this.enableLeafletMap) {
                        this.updateMarkerCanvasIcons();
                        this.leafletMap.fitBounds(this.lcuClusterCanvasRendering.layer.getBounds());
                    }
                } catch (Exception) {
                    console.warn(Exception);
                }
            },
        );
    }

    iconFilterChanged() {
        if (this.enableLeafletMap) { this.updateMarkerIcons(); }
    }

    /* __    _____ _____ _____ __    _____ _____    _____ _____ _____ _____ _____ _____ _____
      |  |  |   __|  _  |   __|  |  |   __|_   _|  |   __|  |  |  _  |  _  |     | __  |_   _|
      |  |__|   __|     |   __|  |__|   __| | |    |__   |  |  |   __|   __|  |  |    -| | |
      |_____|_____|__|__|__|  |_____|_____| |_|    |_____|_____|__|  |__|  |_____|__|__| |_| */

    apply() {
        // Get the active base layer
        const baseLayer = this.model.baseLayers.find((l: any) => (l.id === this.model.baseLayer));
        // Get all the active overlay layers
        const newLayers = this.model.overlayLayers
            .filter((l: any) => l.enabled)
            .map((l: any) => l.layer);
        newLayers.unshift(baseLayer.layer);
        this.layers = newLayers;
        return false;
    }

    onLMapReady(map: L.Map) {
        // Do stuff with map
        this.leafletMap = map;
        // this.lcuClusterCanvasRendering.layer.addOnClickListener(this.markerClickAction.bind(this));
        const reference = this;
        setTimeout((function() { this.leafletMap.invalidateSize(); }).bind(this), 400);
    }

    updateMarkers() {
        if (this.enableLeafletMap && this.globalDatabase.selectedInstallation != null) {
            let count = 0;
            this.globalDatabase.selectedInstallation.lightFixtures.forEach((node) => {
                if (node.latitude !== 0 && node.longitude !== 0 && node.latitude != null && node.longitude != null) {
                    const newMarker = new EntityIconMarker(node, [node.latitude, node.longitude]);
                    newMarker.refreshIcon(this.mapIconOptions); // TODO: AT FIX SVG PROBLEM
                    /*const iconBase64 = node.getIconObject(this.mapIconOptions);
                    newMarker.setIcon(icon({
                        iconSize: iconBase64.iconSize,
                        iconAnchor: iconBase64.iconAnchor,
                        iconUrl: this.sanitizer.bypassSecurityTrustResourceUrl(iconBase64.iconUrl).toString(),
                        shadowUrl: iconBase64.shadowUrl,
                    }));*/

                    count++;
                    if (node.deviceType === 10) {
                        /* const redMarker = L.AwesomeMarkers.icon({
                            icon: 'coffee',
                            markerColor: 'red'
                        });*/
                        this.lcuClusterCanvasRendering.layer.addMarker(newMarker);
                        // this.dcuClusterGroup.addLayer(newMarker);
                    } else {
                        this.lcuClusterCanvasRendering.layer.addMarker(newMarker);
                        // this.lcuClusterGroup.addLayer(newMarker);
                    }
                }
                this.canvasMarkersInitialized = true;
            });
            // console.warn('Total count: ' + count);
        }
    }

    updateMarkerCanvasIcons() {
        try {
            const markers = this.lcuClusterCanvasRendering.layer.getAllChildMarkers();
            markers.forEach((marker: any) => {
                // marker.data.refreshIcon(this.mapIconOptions);
                this.lcuClusterCanvasRendering.layer.removeMarker(marker, false);
            });
        } catch (Exception) {
            console.warn(Exception);
        }
        this.updateMarkers();
        this.lcuClusterCanvasRendering.layer.redraw();
    }

    selectNodes(nodes: NodeWilamp[]) {
        this.dcuClusterGroup.clearLayers();
        this.lcuClusterGroup.clearLayers();
        nodes.forEach((node) => {
            if (node.latitude !== 0 && node.longitude !== 0) {
                node.isSelected = true;
                const newMarker = new EntityIconMarker(node, [node.latitude, node.longitude]);
                newMarker.refreshIcon(this.mapIconOptions);
                if (node.nodeType === 10) {
                    /* const redMarker = L.AwesomeMarkers.icon({
                        icon: 'coffee',
                        markerColor: 'red'
                    });*/
                    // this.lcuClusterCanvasRendering.layer.addMarker(newMarker);
                    this.dcuClusterGroup.addLayer(newMarker);
                } else {
                    // this.lcuClusterCanvasRendering.layer.addMarker(newMarker);
                    this.lcuClusterGroup.addLayer(newMarker);
                }
            }
        });
    }

    updateMarkerIcons() {
        this.updateMarkerCanvasIcons();
        /*this.lcuClusterGroup.getLayers().forEach((marker: EntityIconMarker) => {
            marker.refreshIcon(this.mapIconOptions);
        });
        this.dcuClusterGroup.getLayers().forEach((marker: EntityIconMarker) => {
            marker.refreshIcon(this.mapIconOptions);
        });*/
    }

    markerClickAction(event, markers) {
    }

    /**
     * Not used, was used to test the draw image for a bug in the render of SVG with xml that led to the use of SVG + Base64
     */
    overWriteLeaflet() {
        (<any>this.lcuClusterCanvasRendering.layer)._drawMarker = function (marker, pointPos) {

            const self = this;

            if (!this._imageLookup) this._imageLookup = {};
            if (!pointPos) {

                pointPos = self._map.latLngToContainerPoint(marker.getLatLng());
            }

            const iconUrl = marker.options.icon.options.iconUrl;

            if (marker.canvas_img) {

                self._drawImage(marker, pointPos);
            } else {

                if (self._imageLookup[iconUrl]) {

                    marker.canvas_img = self._imageLookup[iconUrl][0];

                    if (self._imageLookup[iconUrl][1] === false) {

                        self._imageLookup[iconUrl][2].push([marker, pointPos]);
                    } else {

                        self._drawImage(marker, pointPos);
                    }
                } else {

                    const i = new Image();
                    // i.innerHTML = iconUrl; // data:image/svg+xml;utf-8,
                    // i.src = 'data:image/gif;base64,R0lGODlhCwALAIAAAAAA3pn/ZiH5BAEAAAEALAAAAAALAAsAAAIUhA+hkcuO4lmNVindo7qyrIXiGBYAOw==';
                    // let iconB64 = window.btoa(iconUrl);
                    // iconB64 = 'data:image/svg+xml;base64,' + iconB64;
                    // const iconXML = 'data:image/svg+xml;charset=utf-8,' + iconUrl;
                    i.src = iconUrl;
                    marker.canvas_img = i;

                    // Image,isLoaded,marker\pointPos ref
                    self._imageLookup[iconUrl] = [i, false, [[marker, pointPos]]];
                    const placeHolderDiv = document.getElementById('placeholder');
                    i.onload = function(image) {

                        self._imageLookup[iconUrl][1] = true;
                        self._imageLookup[iconUrl][2].forEach(function (e) {
                            self._drawImage(e[0], e[1]);
                        });
                    };

                    i.onerror = function(error) {
                        console.warn(error);
                        self._imageLookup[iconUrl][1] = true;
                        self._imageLookup[iconUrl][2].forEach(function (e) {
                            self._drawImage(e[0], e[1]);
                        });
                    }
                }
            }
        }
    }

}
