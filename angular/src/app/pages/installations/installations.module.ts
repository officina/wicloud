import { NgModule } from '@angular/core';
import {InstallationsComponent} from './installations.component';
import {ThemeModule} from '../../@theme/theme.module';
import { DetailComponent } from './detail/detail.component';
import {NbBadgeModule} from '@nebular/theme';
import { WiCloudSharedModule } from '../../shared/shared.module';


const PAGES_COMPONENTS = [
  InstallationsComponent,
  DetailComponent,
];

@NgModule({
  imports: [
      ThemeModule,
      NbBadgeModule,
      WiCloudSharedModule
  ],
  declarations: [
    ...PAGES_COMPONENTS,
  ],
})
export class InstallationsModule {
}
