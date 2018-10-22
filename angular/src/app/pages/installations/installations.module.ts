import { NgModule } from '@angular/core';
import {InstallationsComponent} from './installations.component';
import {ThemeModule} from '../../@theme/theme.module';
import { DetailComponent } from './detail/detail.component';


const PAGES_COMPONENTS = [
  InstallationsComponent,
  DetailComponent,
];

@NgModule({
  imports: [
    ThemeModule,
  ],
  declarations: [
    ...PAGES_COMPONENTS,
  ],
})
export class InstallationsModule {
}
