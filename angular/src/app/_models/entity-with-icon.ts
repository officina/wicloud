export interface EntityWithIcon {
    getIconUrl(mapFilterOptions: {} | undefined): string;
    getIconObject(mapFilterOptions: {} | undefined): IconObject;
}

export class IconObject {
    constructor(
        public iconUrl?: string,
        public iconSize?: [number, number],
        public iconAnchor?: [number, number],
        public shadowUrl?: string,
    ) {
    }
}