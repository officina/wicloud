import { NgModule } from '@angular/core';

import { PagesComponent } from './pages.component';
import { DashboardModule } from './dashboard/dashboard.module';
import { PagesRoutingModule } from './pages-routing.module';
import { ThemeModule } from '../@theme/theme.module';
import { MiscellaneousModule } from './miscellaneous/miscellaneous.module';
import {InstallationsModule} from './installations/installations.module';


import { WilampCloudAddressWilampModule } from './address-wilamp/address-wilamp.module';
import { WilampCloudContactWilampModule } from './contact-wilamp/contact-wilamp.module';
import { WilampCloudCustomerWilampModule } from './customer-wilamp/customer-wilamp.module';
import { WilampCloudEnergyMeterModuleWilampModule } from './energy-meter-module-wilamp/energy-meter-module-wilamp.module';
import { WilampCloudGatewayWilampModule } from './gateway-wilamp/gateway-wilamp.module';
import { WilampCloudGatewayInstallationRequestModule } from './gateway-installation-request/gateway-installation-request.module';
import { WilampCloudInstallationWilampModule } from './installation-wilamp/installation-wilamp.module';
import { WilampCloudLightManagementMeasureWilampModule } from './light-management-measure-wilamp/light-management-measure-wilamp.module';
import { WilampCloudLightManagementModuleWilampModule } from './light-management-module-wilamp/light-management-module-wilamp.module';
import { WilampCloudMotionManagementModuleWilampModule } from './motion-management-module-wilamp/motion-management-module-wilamp.module';
import { WilampCloudNodeWilampModule } from './node-wilamp/node-wilamp.module';
import { WilampCloudNodeModulesWilampModule } from './node-modules-wilamp/node-modules-wilamp.module';
import { WilampCloudOrderWilampModule } from './order-wilamp/order-wilamp.module';
import { WilampCloudShippingWilampModule } from './shipping-wilamp/shipping-wilamp.module';
import { WilampCloudTwilightManagementModuleWilampModule } from './twilight-management-module-wilamp/twilight-management-module-wilamp.module';
import { WilampCloudEnergyIntervalModule } from './energy-interval/energy-interval.module';
import {WiCloudHomeModule} from './home';
import {WilampCloudLightProfileWilampModule} from './light-profile-wilamp/light-profile-wilamp.module';
import {WilampCloudLightProfileSlotWilampModule} from './light-profile-slot-wilamp/light-profile-slot-wilamp.module';
import {InstallationDashboardModule} from './dashboards/installation-dashboard/installation-dashboard.module';
import {GlobalDatabaseService} from '../shared/global-database/global-database.service';


const PAGES_COMPONENTS = [
  PagesComponent,
];

@NgModule({
    imports: [
        InstallationDashboardModule,
        PagesRoutingModule,
        WiCloudHomeModule,
        ThemeModule,
        DashboardModule,
        InstallationsModule,
        MiscellaneousModule,
        WilampCloudAddressWilampModule,
        WilampCloudContactWilampModule,
        WilampCloudCustomerWilampModule,
        WilampCloudEnergyMeterModuleWilampModule,
        WilampCloudGatewayWilampModule,
        WilampCloudGatewayInstallationRequestModule,
        WilampCloudInstallationWilampModule,
        WilampCloudLightManagementMeasureWilampModule,
        WilampCloudLightManagementModuleWilampModule,
        WilampCloudMotionManagementModuleWilampModule,
        WilampCloudNodeWilampModule,
        WilampCloudNodeModulesWilampModule,
        WilampCloudOrderWilampModule,
        WilampCloudShippingWilampModule,
        WilampCloudTwilightManagementModuleWilampModule,
        WilampCloudEnergyIntervalModule,
        WilampCloudLightProfileWilampModule,
        WilampCloudLightProfileSlotWilampModule,
    ],
    declarations: [
        ...PAGES_COMPONENTS,
    ],
    providers: [
              GlobalDatabaseService,
    ]
})
export class PagesModule {
}
