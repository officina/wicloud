import {BaseEntity} from '../../_models/base-entity';

export class TwilightManagementModuleWilamp implements BaseEntity {
    constructor(
        public id?: number,
        public name?: string,
        public description?: string,
        public twMode?: number,
        public twType?: number,
        public twGroup?: number,
        public validPeriod?: number,
        public thsSunsetOn?: number,
        public thsSunsetOff?: number,
        public thsSunriseOn?: number,
        public thsSunriseOff?: number,
        public persistencePeriod?: number,
        public delayOffset?: number,
        public voltagemV?: number,
        public luxMeasured?: number,
        public samplingPeriod?: number,
        public numberAverageMeasures?: number,
        public adcInChannel?: number,
        public programmingStatus?: number,
        public createdTimestamp?: any,
        public nodeModulesId?: number,
        public twilightMeasures?: BaseEntity[],
    ) {
    }
}
