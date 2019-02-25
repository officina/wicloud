import { NgModule } from '@angular/core';
import {InstallationsComponent} from './installations.component';
import {ThemeModule} from '../../@theme/theme.module';
import { DetailComponent } from './detail/detail.component';
import {NbBadgeModule} from '@nebular/theme';
import {TranslateModule} from '@ngx-translate/core';
import { LeafletModule } from '@asymmetrik/ngx-leaflet';


const PAGES_COMPONENTS = [
  InstallationsComponent,
  DetailComponent,
];

@NgModule({
  imports: [
      ThemeModule,
      NbBadgeModule,
      LeafletModule,
      TranslateModule.forChild(),
  ],
  declarations: [
    ...PAGES_COMPONENTS,
  ],
})
export class InstallationsModule {
}
