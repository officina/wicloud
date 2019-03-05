import {AfterViewInit, Component, OnDestroy, OnInit} from '@angular/core';
import {InstallationWilampService} from '../../pages/installation-wilamp';
import {NodeWilamp, NodeWilampService} from '../../pages/node-wilamp';
import {GatewayWilampService} from '../../pages/gateway-wilamp';
import {EntityIconMarker, MapLeafletLayers, MapOptions} from '../../shared/maps/map.models';
import {GoogleMapsAPIWrapper, MapsAPILoader} from '@agm/core';
import {Principal} from '../../shared';
import {
    GLOBALDATABASE__LIGHT_FIXTURES_FETCHED,
    INSTALLATION__SELECTED_ID_CHANGED, INSTALLATION__SELECTED_INSTALLATION_CHANGED, MAP_INSTANCE_GETTER__MAP_OBTAINED,
} from '../../shared/constants/events.constants';
import {Subscription} from 'rxjs/Rx';
import {JhiEventManager} from 'ng-jhipster';
import {GlobalDatabaseService} from '../../shared/global-database/global-database.service';
import GMap = google.maps.Map;
import {Helpers} from '../../shared';
import {ScriptLoaderService} from '../../_services/script-loader.service';
import * as L from 'leaflet';

import 'leaflet.markercluster';
import 'leaflet.awesome-markers/dist/leaflet.awesome-markers';
import 'leaflet-canvas-marker';
import 'leaflet.awesome-markers';
import 'leaflet-sidebar-v2';
import {NG2Heatmap} from '../../shared/maps/heatmap-js';
// import '../../../../../../node_modules/leaflet-sidebar-v2/js/leaflet-sidebar.js';

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
  selector: 'full-leaflet-map-widget',
  templateUrl: './full-leaflet-map-widget.component.html',
  styleUrls: ['full-leaflet-map-widget.component.scss'],

})
export class FullLeafletMapWidgetComponent implements OnInit, OnDestroy, AfterViewInit {
    /* SIDEBAR SUPPORT */
    sidebar = L.control.sidebar({
        container: 'sidebar',
        autopan: true,
        closeButton: false,
    });
    userpanel = {
        id:   'user1',
        tab:  '<i class="fa fa-user"></i>',
        // title: 'User Profile',
        pane: 'user ipsum amen',
    };
    // Open Street Map and Open Cycle Map definitions
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
        layer: L.canvasIconLayer(),
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
    mapOptions: MapOptions;
    iconsGroupingOptions = [
        { id: 1, label: 'Ungrouped', value: ''},
        { id: 2, label: 'Gateway', value: 'gateway'},
        { id: 3, label: 'Light profile', value: 'light_profile'},
        { id: 4, label: 'Light zone', value: 'light_zone'},
        { id: 5, label: 'Lamp wattage', value: 'lamp_wattage'},
        { id: 6, label: 'Alerts', value: 'alerts'},
    ];
    alertFilterOptions = [
        { id: 1, label: '> 10', value: 10},
        { id: 2, label: '> 50', value: 50},
        { id: 3, label: '> 100', value: 100},
    ];
    heatmapEntitiesToAnalyze = [
        { id: 1, label: 'Average Power', value: 'power'},
        { id: 2, label: 'Consumption', value: 'consumption'},
        { id: 3, label: 'Burning time', value: 'burning_time'},
        { id: 4, label: 'Node life', value: 'node_life'},
        { id: 5, label: 'Number of alerts', value: 'alerts'},
        { id: 6, label: 'Profile consumption', value: 'profile_consumption'},
        { id: 7, label: 'Lamp wattage', value: 'lamp_wattage'},
    ];
    heatmapTimespanIntervals = [
        { id: 1, label: 'Current day', value: 'current_day'},
        { id: 2, label: 'Last day', value: 'last_day'},
        { id: 3, label: 'Current month', value: 'current_month'},
        { id: 4, label: 'Last month', value: 'last_month'},
        { id: 5, label: 'Current year', value: 'current_year'},
        { id: 6, label: 'Total', value: 'total'},
        { id: 7, label: 'Selected interval', value: 'custom'},
    ];
    public heatmapOptions = {
        enabled: false,
        radiusMultiplier: 1,
        alpha: .5,
        entityToAnalyze: 'power',
        selectedInterval: 'total',
        startOfInterval: null,
        endOfInterval: null,
        pendingChanges: false,
    };
    public mapIconOptions = {
        useSimpleIcon: false,
        groupBy: '',
        filterOptions: '',
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
    LAYER_HEATMAP = {
        id: 'layerheatmap',
        name: 'Heatmap',
        enabled: true,
        layer: new NG2Heatmap.HeatOverlay(
            {
                // radius should be small ONLY if scaleRadius is true (or small radius is intended)
                'radius': 0.0001,
                'maxOpacity': this.heatmapOptions.alpha,
                // scales the radius based on map zoom
                'scaleRadius': false,
                // if set to false the heatmap uses the global maximum for colorization
                // if activated: uses the data maximum within the current map boundaries
                //   (there will always be a red spot with useLocalExtremas true)
                'useLocalExtrema': true,
                // which field name in your data represents the latitude - default "lat"
                latField: 'lat',
                // which field name in your data represents the longitude - default "lng"
                lngField: 'lng',
                // which field name in your data represents the data value - default "value"
                valueField: 'radius',
            },
        ),
    };
    leafletMap: L.Map;
    // Form model object
    model = new MapLeafletLayers(
        [ this.LAYER_OSM, this.LAYER_OCM, this.LAYER_GOOGLE_HYBRID, this.LAYER_GOOGLE_STREET ],
        this.LAYER_GOOGLE_HYBRID.id,
        [  this.lcuCluster, this.lcuClusterCanvasRendering, this.dcuCluster, this.LAYER_HEATMAP ],
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
            HEATMAP: this.LAYER_HEATMAP.layer,
        },
    };
    options = {
        zoom: 10,
        center: L.latLng(46.879966, -121.726909),
    };
    private ciLayer = undefined;
    private eventSubscriber: Subscription;
    private eventSubscriberSelectedIdChanged: Subscription;
    private eventSubscriberWaitForMapInstance: Subscription;
    private googleMapsLoaded = false;
    private googleGeocoder: any;
    public mapInstanceId = 'dashboard_map';
    private mapInstance: GMap;
    private mapInstance2: GMap;
    private heatmaps: Map<number, any>;
    public enableGoogleMap = false;
    public enableLeafletMap = true;
    public min = 1;
    public max = 22;
    public disabledValue = 22;
    public demo = 22;
    public val = 22;
    public selectedNode: NodeWilamp = null;
    constructor(
        private _script: ScriptLoaderService,
        private mapsAPILoader: MapsAPILoader,
        private mapsAPIWrapper: GoogleMapsAPIWrapper,
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
        this.registerFetch();
    }
    ngAfterViewInit() {
        this.nodesFetched();
    }

    nodesFetched() {
        if (this.enableLeafletMap) {
            this.updateMarkerCanvasIcons();
            this.leafletMap.fitBounds(this.lcuClusterCanvasRendering.layer.getBounds());
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

    heatmapOptionsChanged() {
        this.heatmapOptions.pendingChanges = true;
    }

    heatmapApplyChanges() {
        if (this.enableLeafletMap) { this.updateHeatmap(); }
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
        this.sidebar.addTo(this.leafletMap);
        this.lcuClusterCanvasRendering.layer.addOnClickListener(this.markerClickAction.bind(this));
        // this.ciLayer = L.canvasIconLayer({}).addTo(this.leafletMap);
        const reference = this;
        // $('#leaflet_full_div').height('100%').width('99%');
        // this.leafletMap.invalidateSize();
        // $('#leaflet_full_div').height('100%').width('100%');
        setTimeout((function() { this.leafletMap.invalidateSize(); }).bind(this), 400);
        // (<any>window).leaflet = this.leafletMap;
        /*this.sidebar
        // add a button pointing to a link
            .addPanel({
                id:   'home',
                tab:  '<i class="fa fa-arrow-left"></i>'
            })
            // add a button with click listener
            .addPanel({
                id:   'info',
                tab:  '<i class="fa fa-info"></i>',
                button(e) { alert('info tab clicked'); }
            })
            // add a panel that is disabled
            .addPanel({
                id:   'mail',
                tab:  '<i class="fa fa-envelope"></i>',
                title: 'Messages',
                pane: '<p>Lorem ipsum dolor amet</p>',
                disabled: true,
            })
            // add a panel at the bottom
            .addPanel({
                id:   'settings',
                tab:  '<i class="fa fa-gear"></i>',
                title: 'Settings',
                pane: '<p><button onclick="functionTest();">enable mails panel</button><button onclick="sidebar.disablePanel(\'mail\')">disable mails panel</button></p><p><button onclick="reference.addSidebarPanel()">add user</button></b>',
                position: 'bottom'
            });*/
        // open the settings panel
        // .open('settings');
    }

    addSidebarPanel() {
        const num = Number.parseInt(this.userpanel.id.slice(4), 10);
        this.userpanel.id = 'user' + (num + 1); // increment number by 1
        this.sidebar.addPanel(this.userpanel);
    }

    updateMarkers() {
        if (this.enableLeafletMap && this.globalDatabase.selectedInstallation != null) {
            let count = 0;
            this.globalDatabase.selectedInstallation.lightFixtures.forEach((node) => {
                if (node.latitude !== 0 && node.longitude !== 0 && node.latitude != null && node.longitude != null) {
                    const newMarker = new EntityIconMarker(node, [node.latitude, node.longitude]);
                    newMarker.refreshIcon(this.mapIconOptions);
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
        /* open a panel */
        const nodes = [];
        markers.forEach((marker) => {
            nodes.push(marker.data.referenceEntity);
        });
        this.selectedNode = markers[0].data.referenceEntity;
        // this.selectNodes(nodes);
        this.selectNodes([ markers[0].data.referenceEntity ]);
        this.sidebar.open('nodeinfo');
    }

    updateHeatmap() {
        const result = [];
        this.LAYER_HEATMAP.layer.setData(result);
        if (this.heatmapOptions.enabled) {
            let maximumValue = 20;
            this.LAYER_HEATMAP.layer.configure({'maxOpacity': this.heatmapOptions.alpha});
            this.globalDatabase.selectedInstallation.lightFixtures.forEach((function(node) {
                let radiusValue = Helpers.getRandomInt(1, 50) * this.heatmapOptions.radiusMultiplier;
                if (node.latitude !== 0 && node.longitude !== 0) {
                    switch (this.heatmapOptions.entityToAnalyze) {
                        case 'power':
                            if (this.globalDatabase.selectedInstallation.statisticsByNodeIdHMap.size > 0) {
                                const nodeStatistics = this.globalDatabase.selectedInstallation.statisticsByNodeIdHMap.get(node.id);
                                if (nodeStatistics != null) {
                                    radiusValue = nodeStatistics.sumEnergy != null ? nodeStatistics.sumEnergy / 10 * this.heatmapOptions.radiusMultiplier : 1 * this.heatmapOptions.radiusMultiplier;
                                    if (nodeStatistics.sumEnergy / 10 > maximumValue) {
                                        maximumValue = nodeStatistics.sumEnergy / 10;
                                    }
                                } else { radiusValue = 1.0 * this.heatmapOptions.radiusMultiplier; }
                            }
                            if (node.nodeType === 10) { radiusValue = 1.0 * this.heatmapOptions.radiusMultiplier; }
                            break;
                        case 'consumption':
                            break;
                        case 'burning_time':
                            if (this.globalDatabase.selectedInstallation.statisticsByNodeIdHMap.size > 0) {
                                const nodeStatistics = this.globalDatabase.selectedInstallation.statisticsByNodeIdHMap.get(node.id);
                                if (nodeStatistics != null) {
                                    radiusValue = nodeStatistics.burningTime  != null ? nodeStatistics.burningTime / 60.0 / 24.0 * this.heatmapOptions.radiusMultiplier : 1 * this.heatmapOptions.radiusMultiplier;
                                    if (nodeStatistics.burningTime / 60.0 / 24.0 > maximumValue) {
                                        maximumValue = nodeStatistics.burningTime / 60.0 / 24.0;
                                    }
                                } else { radiusValue = 1.0 * this.heatmapOptions.radiusMultiplier; }
                            }
                            if (node.nodeType === 10) { radiusValue = 1.0 * this.heatmapOptions.radiusMultiplier; }
                            break;
                        case 'node_life':
                            break;
                        case 'alerts':
                            break;
                        case 'profile_consumption':
                            break;
                        case 'lamp_wattage':
                            if (node.nominalPower > maximumValue) {
                                maximumValue = node.nominalPower / 10.0 * this.heatmapOptions.radiusMultiplier;
                            }
                            radiusValue = node.nominalPower / 10.0 * this.heatmapOptions.radiusMultiplier;
                            break;
                        default:
                            break;
                    }
                    const heatmapPoint = {
                            latlng: new L.LatLng(node.latitude, node.longitude),
                            radius: radiusValue,
                    };
                    maximumValue = 50;
                    result.push(heatmapPoint);
                }
            }).bind(this));
            this.LAYER_HEATMAP.layer.setData(result);
            this.heatmapOptions.pendingChanges = false;
            return result;
        }
    }
}
