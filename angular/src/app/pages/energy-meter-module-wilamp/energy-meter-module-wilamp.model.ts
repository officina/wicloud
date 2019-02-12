import {BaseEntity} from '../../_models/base-entity';

export class EnergyMeterModuleWilamp implements BaseEntity {
    constructor(
        public id?: number,
        public name?: string,
        public description?: string,
        public iacCalibration?: number,
        public vacCalibration?: number,
        public patCalibration?: number,
        public preCalibration?: string,
        public nominalPower?: number,
        public oldLampPower?: number,
        public powerLosses?: number,
        public nodeModulesId?: number,
        public peakMeasures?: BaseEntity[],
    ) {
    }
}
