import {BaseEntity} from '../../_models/base-entity';

export class EnergyInterval implements BaseEntity {
    constructor(
        public id?: number,
        public mac?: string,
        public lightManagementModuleId?: number,
        public installationId?: number,
        public startInterval?: any,
        public endInterval?: any,
        public startIntervalMeasureTimestamp?: any,
        public endIntervalMeasureTimestamp?: any,
        public dimLevel?: number,
        public adc0Level?: number,
        public adc1Level?: number,
        public activePower?: number,
        public reactivePower?: number,
        public startIntervalActiveEnergyCounterValue?: number,
        public endIntervalActiveEnergyCounterValue?: number,
        public activeEnergy?: number,
        public startIntervalReactiveEnergyCounterValue?: number,
        public endIntervalReactiveEnergyCounterValue?: number,
        public reactiveEnergy?: number,
        public activeEnergyMty0?: number,
        public activeEnergyMty1?: number,
        public activeEnergyMty2?: number,
        public activeEnergyMty3?: number,
        public activeEnergyWithoutDim?: number,
        public activeEnergyWithoutControl?: number,
        public activeEnergyOldLamps?: number,
        public burningTime?: number,
        public nodeLife?: number,
    ) {
    }
}
