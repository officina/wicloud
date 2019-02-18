import {BaseEntity} from '../../_models/base-entity';

export class LightProfileSlotWilamp implements BaseEntity {
    constructor(
        public id?: number,
        public name?: string,
        public description?: string,
        public don?: number,
        public dof?: number,
        public ton?: string,
        public tof?: string,
        public eas?: boolean,
        public ecr?: boolean,
        public emo?: boolean,
        public edw?: number,
        public enabled?: boolean,
        public lightProfileIndex?: number,
        public pw0?: number,
        public pw1?: number,
        public pw2?: number,
        public pw3?: number,
        public fadeIn?: number,
        public fadeOut?: number,
        public slot?: number,
        public createdTimestamp?: any,
        public motionDuration?: number,
        public motionDelay?: number,
        public mi0?: number,
        public mi1?: number,
        public mi2?: number,
        public mi3?: number,
        public motionFadeIn?: number,
        public motionFadeOut?: number,
        public lightProfileName?: string,
        public lightProfileId?: number,
    ) {
        this.eas = false;
        this.ecr = false;
        this.emo = false;
        this.enabled = false;
    }
}
