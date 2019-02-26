import {latLng, tileLayer} from 'leaflet';
import LatLng = google.maps.LatLng;
import { Layer, Marker, MarkerOptions, icon } from 'leaflet';
import {EntityWithIcon} from '../../_models/entity-with-icon';

export class MapOptions {
    constructor(
        public layers?: any,
        public center?: any,
        public bounds?: any,
    ) {
        this.center = latLng(0, 0);
    }
}

export class MapLeafletLayers {
    constructor(
        public baseLayers: {
            id: string,
            name: string,
            enabled: boolean,
            layer: Layer,
        }[],
        public baseLayer: string,
        public overlayLayers: {
            id: string,
            name: string,
            enabled: boolean,
            layer: Layer,
        }[] = [],
    ) { }
}

/**
 * In order to use FontAwesome icons you have to load them in the module of each component and then add them to the module itself.
 */
export class EntityIconMarker<P = any> extends Marker {
    // Properties
    referenceEntity: EntityWithIcon;
    constructor(reference, latlng, options?: MarkerOptions) {
        super(latlng, options);
        this.referenceEntity = reference;
    }
    setReferenceEntity(reference: EntityWithIcon) {
        this.referenceEntity = reference;
    }
    getReferenceEntity() {
        return this.referenceEntity;
    }

    /**
     * This function update the icon of the marker using the mapFilterOptions object.
     * mapFilterOptions makes the fitering and the colouring over properties of the entity possible.
     * In order to make it work the entity (referenceEntity) has to implement the interface EntityWithIcon
     * in particular it has to define a method getIconObject that return an IconObject with all the parameters of the icon to be replaced.
     * @param {{} | undefined} mapFilterOptions
     */
    refreshIcon(mapFilterOptions: {} | undefined) {
        const newIcon = this.referenceEntity.getIconObject(mapFilterOptions);
        this.setIcon(icon({
            iconSize: newIcon.iconSize,
            iconAnchor: newIcon.iconAnchor,
            iconUrl: newIcon.iconUrl,
            shadowUrl: newIcon.shadowUrl,
        }));
    }
}
