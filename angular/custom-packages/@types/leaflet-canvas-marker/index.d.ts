// Type definitions for Leaflet.markercluster 1.0
// Project: https://github.com/Leaflet/Leaflet.markercluster
// Definitions by: Robert Imig <https://github.com/rimig>
// Definitions: https://github.com/DefinitelyTyped/DefinitelyTyped
// TypeScript Version: 2.3

import * as L from 'leaflet';
declare module 'leaflet' {
    class CanvasIconLayer extends Layer {
        /*
        * Recursively retrieve all child markers of this cluster.
        */
        getAllChildMarkers(): Marker[];

        /*
        * Returns the cluster bounds.
        */
        getBounds(): LatLngBounds;

        addMarkers(markers: Marker[]);

        addMarker(marker: Marker);

        removeMarker(marker: Marker, redraw?: boolean);

        redraw();

        clear();

        addOnClickListener(listener);

        addOnHoverListener(listener);

    }

    /*
    * Create a marker cluster group, optionally given marker cluster group options.
    */
    function canvasIconLayer(options?: any): CanvasIconLayer;
}
