import { NgModule } from '@angular/core';

import { ThemeModule } from '../../@theme/theme.module';
import { UiFeaturesRoutingModule } from './ui-features-routing.module';
import { UiFeaturesComponent } from './ui-features.component';
import { GridComponent } from './grid/grid.component';
import { IconsComponent } from './icons/icons.component';
import { TypographyComponent } from './typography/typography.component';
import { SearchComponent } from './search-fields/search-fields.component';

/*
import { library } from '@fortawesome/fontawesome-svg-core';
import { faCoffee } from '@fortawesome/free-solid-svg-icons';
import {FontAwesomeModule} from '@fortawesome/angular-fontawesome';

// Add an icon to the library for convenient access in other components
// library.add(faCoffee);

import { fab } from '@fortawesome/free-brands-svg-icons';
// import { fas } from '@fortawesome/free-solid-svg-icons';
// import { far } from '@fortawesome/free-regular-svg-icons';
// library.add(fas, far);
import { fal } from '@fortawesome/pro-light-svg-icons';
import { far } from '@fortawesome/pro-regular-svg-icons';
import { fas } from '@fortawesome/pro-solid-svg-icons';
library.add(fas, far, fal, fab);
*/


const components = [
  UiFeaturesComponent,
  GridComponent,
  IconsComponent,
  TypographyComponent,
  SearchComponent,
];

@NgModule({
  imports: [
    ThemeModule,
    UiFeaturesRoutingModule,
    // FontAwesomeModule,
  ],
  declarations: [
    ...components,
  ],
})
export class UiFeaturesModule { }
