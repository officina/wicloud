/* import * as $ from 'jquery';*/
/// <reference types="@types/googlemaps" />

export class MapHelpers {

    static generateBounds(markers): any {
        if (markers && markers.length > 0) {
            const bounds = new google.maps.LatLngBounds();

            markers.forEach((marker: any) => {
                if (marker.latitude > 0 && marker.longitude  > 0) {
                    bounds.extend(new google.maps.LatLng(marker.latitude, marker.longitude));
                }
            });

            // check if there is only one marker
            if (bounds.getNorthEast().equals(bounds.getSouthWest())) {
                const extendPoint = new google.maps.LatLng(bounds.getNorthEast().lat() + 0.01, bounds.getNorthEast().lng() + 0.01);
                bounds.extend(extendPoint);
            }
            return bounds;
            /*return {
                northeast: {
                    latitude: bounds.getNorthEast().lat(),
                    longitude: bounds.getNorthEast().lng()
                },
                southwest: {
                    latitude: bounds.getSouthWest().lat(),
                    longitude: bounds.getSouthWest().lng()
                }
            }*/
        }
        // return empty object when no bundle selected
        return {};
    }
}
