import { NgModule } from '@angular/core';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { NgJhipsterModule } from 'ng-jhipster';
import { InfiniteScrollModule } from 'ngx-infinite-scroll';
import { CookieModule } from 'ngx-cookie';
import {EnergyConsumptionSmallGraphWidgetComponent} from './energy-consumption-small-graph-widget/energy-consumption-small-graph-widget.component';
import {EnergySavingWidgetComponent} from './energy-saving-widget/energy-saving-widget.component';
import {NodeListGridWidgetComponent} from './node-list-grid-widget/node-list-grid-widget.component';
import {NodeSmallWidgetComponent} from './node-small-widget/node-small-widget.component';
import {NodeSmallDetailsWidgetComponent} from './node-small-details-widget/node-small-details-widget.component';
import {FlotGraphComponent} from '../shared/flot/flot.component';
import {NgSparklineDirective} from './_directives/ngSparkline.directive';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import {MatButtonModule, MatCheckboxModule, MatNativeDateModule, MatSliderModule, MatRadioModule, MatSlideToggleModule, MatDatepickerModule} from '@angular/material';
import { NpnSliderModule } from 'npn-slider';
import {FullLeafletMapWidgetComponent} from './full-leaflet-map-widget/full-leaflet-map-widget.component';
import { LeafletModule } from '@asymmetrik/ngx-leaflet';
import {MatFormFieldModule} from '@angular/material/form-field';
import {GatewayAdministrationWidgetComponent} from './gateway-administration-widget/gateway-administration-widget.component';

/* Font awesome */
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faCoffee, faStroopwafel, faCalendar, faBraille, faBrush, faPaintBrush, faPaintRoller } from '@fortawesome/free-solid-svg-icons';
import { faTwitter } from '@fortawesome/free-brands-svg-icons';
import { faArrowAltRight, faLightbulb, faHeading, faLightbulbOn, faInfoCircle, } from '@fortawesome/pro-light-svg-icons';
import { faPalette, faLayerGroup } from '@fortawesome/pro-solid-svg-icons';
import {GatewayAdministrationWebsiteWidgetComponent} from './gateway-administration-website-widget/gateway-administration-website-widget.component';
import {UnwrapTagDirective} from './_directives/unwrap-tag.directive';
import {HrefPreventDefaultDirective} from './_directives/href-prevent-default.directive';
// Add an icon to the library for convenient access in other components
library.add(faCoffee, faStroopwafel, faCalendar, faHeading, faLayerGroup, faInfoCircle, faPalette, faTwitter, faArrowAltRight, faLightbulb, faLightbulbOn, faBraille, faBrush, faPaintBrush, faPaintRoller);
/* Font awesome */

@NgModule({
    imports: [
        NgbModule.forRoot(),
        NgJhipsterModule.forRoot({
            // set below to true to make alerts look like toast
            alertAsToast: false,
            i18nEnabled: true,
            defaultI18nLang: 'en'
        }),
        FontAwesomeModule,
        FormsModule,
        ReactiveFormsModule,
        InfiniteScrollModule,
        CookieModule.forRoot(),
        MatButtonModule,
        MatCheckboxModule,
        MatSliderModule,
        MatSlideToggleModule,
        MatNativeDateModule,
        MatDatepickerModule,
        MatRadioModule,
        NpnSliderModule,
        LeafletModule,
        MatFormFieldModule
    ],
    providers: [

    ],
    declarations: [
        EnergyConsumptionSmallGraphWidgetComponent,
        EnergySavingWidgetComponent,
        NodeListGridWidgetComponent,
        NodeSmallWidgetComponent,
        NodeSmallDetailsWidgetComponent,
        FlotGraphComponent,
        NgSparklineDirective,
        UnwrapTagDirective,
        HrefPreventDefaultDirective,
        FullLeafletMapWidgetComponent,
        /*MapInstanceGetterComponent,*/
        GatewayAdministrationWidgetComponent,
        GatewayAdministrationWebsiteWidgetComponent
    ],
    exports: [
        EnergyConsumptionSmallGraphWidgetComponent,
        EnergySavingWidgetComponent,
        NodeListGridWidgetComponent,
        NodeSmallWidgetComponent,
        NodeSmallDetailsWidgetComponent,
        FullLeafletMapWidgetComponent,
        /*MapInstanceGetterComponent,*/
        GatewayAdministrationWidgetComponent,
        GatewayAdministrationWebsiteWidgetComponent
    ]
})
export class WidgetsModule {}
