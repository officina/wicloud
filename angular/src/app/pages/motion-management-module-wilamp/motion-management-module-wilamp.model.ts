import {BaseEntity} from '../../_models/base-entity';

export class MotionManagementModuleWilamp implements BaseEntity {
    constructor(
        public id?: number,
        public name?: string,
        public description?: string,
        public motionMode?: number,
        public motionType?: number,
        public motionGroup?: number,
        public delayAfter?: number,
        public retriggerTime?: number,
        public triggerDelay?: number,
        public mi0?: number,
        public mi1?: number,
        public mi2?: number,
        public mi3?: number,
        public fadeIn?: number,
        public fadeOut?: number,
        public createdTimestamp?: any,
        public adcInChannel?: number,
        public duration?: number,
        public nodeModulesId?: number,
        public motionEvents?: BaseEntity[],
    ) {
    }
}
