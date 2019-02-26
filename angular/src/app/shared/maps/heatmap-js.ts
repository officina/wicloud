import * as L from 'leaflet';
import * as heatmapjsReference from 'heatmap.js';
/**
 * author: Rafał Piekarski
 * email: noopek@gmail.com
 * this was made only cuz of need
 * for personal usage feel free to email
 * me with some improvements
 *
 * remember to npm/yarn heatmap.js and leaflet !
 * gl bois!
 */

declare var window: {
    h337: {
        create: Function,
        register: Function,
    },
};

export const CSS_TRANSFORM = (() => {
    const div = document.createElement('div');
    const props = [
        'transform',
        'WebkitTransform',
        'MozTransform',
        'OTransform',
        'msTransform',
    ];
    for (let i = 0; i < props.length; i++) {
        const prop = props[i];
        if (div.style[prop] !== undefined) {
            return prop;
        }
    }
    return props[0];
})();

export namespace NG2Heatmap {
    export interface HTMLElementEx extends HTMLElement {
        _leaflet_pos?: L.Point;
    }

    export interface HeatData {
        latlng: L.LatLng;
        radius: any;
    }

    export interface HeatPoint {
        x: Number;
        y: Number;
        radius?: Number;
    }

    export interface HeatOverlay {

        addTo(map: L.Map | L.LayerGroup): this;

        onAdd(map: L.Map): this;

        onRemove(map: L.Map): this;

        setData(data: Array<HeatData>): any;
    }

    export class HeatOverlay extends L.Layer implements HeatOverlay {
        private heatData: Array<HeatData>;
        private el: HTMLElement;
        private min: Number;
        private max: Number;
        private cfg: any;
        private map: L.Map;
        private x: Number;
        private y: Number;
        private heatmap;
        private heatmapjsReference;

        constructor(config: {}) {
            super();
            this.cfg = config;
            this.el = L.DomUtil.create('div', 'leaflet-zoom-hide');
            this.heatData = [];
            this.min = 0;
            this.max = 1;
            this.cfg.container = this.el;
            this.heatmapjsReference = heatmapjsReference;
        }

        public configure(cfg: {}) {
            this.heatmap.configure(cfg);
        }

        public onAdd(map: L.Map) {
            const size = map.getSize();

            this.map = map;

            this.x = size.x;
            this.y = size.y;

            this.el.style.width = `${size.x}px`;
            this.el.style.height = `${size.y}px`;
            this.el.style.position = 'absolute';

            this.map.getPanes().overlayPane.appendChild(this.el);
            if (!this.heatmap) {
                this.heatmap = this.heatmapjsReference.create(this.cfg);
            }

            map.on('moveend', this.reset, this);
            this.draw();
            return this;
        }

        public addTo(map: L.Map) {
            map.addLayer(this);
            return this;
        }

        public onRemove(map: L.Map) {
            map.getPanes().overlayPane.removeChild(this.el);
            map.off('moveend', this.reset, this);
            return this;
        }

        private draw() {
            if (!this.map) { return; }

            const mapPane: HTMLElementEx = this.map.getPanes().mapPane;
            const point = mapPane._leaflet_pos;

            this.el.style[CSS_TRANSFORM] = `translate(${-Math.round(point.x)}px, ${-Math.round(point.y)}px)`;

            this.update();
        }

        private update() {
            const bounds: L.LatLngBounds = this.map.getBounds();
            const generatedData = {max: this.max, min: this.min, data: []};
            const zoom = this.map.getZoom();
            const scale = Math.pow(2, zoom);

            if (this.heatData.length === 0) {
                if (this.heatmap) {
                    this.heatmap.setData(generatedData);
                }
                return;
            }

            const latLngPoints = [];
            const radiusMultiplier: any = this.cfg.scaleRadius ? scale : 1;
            let localMax = 0;
            let localMin = 0;
            const valueField = this.cfg.valueField;
            let len = this.heatData.length;

            while (len--) {
                const entry = this.heatData[len];
                const value = entry[valueField];
                const latlng = entry.latlng;

                if (!bounds.contains(latlng)) {
                    continue;
                }

                localMax = Math.max(value, localMax);
                localMin = Math.min(value, localMin);

                const point: L.Point = this.map.latLngToContainerPoint(latlng);
                const latlngPoint: HeatPoint = {x: Math.round(point.x), y: Math.round(point.y)};
                latlngPoint[valueField] = value;

                let radius;

                if (entry.radius) {
                    radius = entry.radius * radiusMultiplier;
                } else {
                    radius = (this.cfg.radius || 2) * radiusMultiplier;
                }

                // console.log(radius, this.cfg.radius, radiusMultiplier);

                latlngPoint.radius = radius;
                latLngPoints.push(latlngPoint);
            }

            if (this.cfg.useLocalExtrema) {
                generatedData.max = localMax;
                generatedData.min = localMin;
            }

            generatedData.data = latLngPoints;

            this.heatmap.setData(generatedData);
        }

        setData(data: Array<HeatData>) {

            let len = data.length;
            const d = [];

            while (len--) {
                d.push(data[len]);
            }

            this.heatData = d;

            this.draw();
        }

        private reset() {
            const size = this.map.getSize();
            if (this.x !== size.x || this.y !== size.y) {
                this.x = size.x;
                this.y = size.y;

                this.el.style.width = this.x + 'px';
                this.el.style.height = this.y + 'px';

                this.heatmap._renderer.setDimensions(this.x, this.y);
            }
            this.draw();
        }
    }

}
