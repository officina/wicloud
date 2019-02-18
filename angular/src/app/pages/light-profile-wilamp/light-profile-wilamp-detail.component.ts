import {Component, OnInit, OnDestroy, AfterViewInit, AfterContentInit, AfterViewChecked} from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse } from '@angular/common/http';
import { Subscription } from 'rxjs';
import { JhiEventManager } from 'ng-jhipster';

import { LightProfileWilamp } from './light-profile-wilamp.model';
import { LightProfileWilampService } from './light-profile-wilamp.service';
import {ScriptLoaderService} from '../../_services/script-loader.service';
import {LightProfileSlotWilampService} from '../light-profile-slot-wilamp/light-profile-slot-wilamp.service';
import {MapHelpers} from '../../shared/maps/map.helpers';
declare let lightProfileViewer: any;

@Component({
    selector: 'jhi-light-profile-wilamp-detail',
    templateUrl: './light-profile-wilamp-detail.component.html',
    styleUrls: [
        'lightProfileViewer.css'
    ]
})
export class LightProfileWilampDetailComponent implements OnInit, OnDestroy, AfterViewInit {

    lightProfile: LightProfileWilamp;
    private subscription: Subscription;
    private eventSubscriber: Subscription;
    private lPP: any;

    constructor(
        private _script: ScriptLoaderService,
        private eventManager: JhiEventManager,
        private lightProfileService: LightProfileWilampService,
        private lightProfileSlotService: LightProfileSlotWilampService,
        private route: ActivatedRoute
    ) {
    }

    ngOnInit() {
        this.subscription = this.route.params.subscribe((params) => {
            this.load(params['id']);
        });
        this.registerChangeInLightProfiles();
    }

    load(id) {
        this.lightProfileService.find(id)
            .subscribe((lightProfileResponse: HttpResponse<LightProfileWilamp>) => {
                this.lightProfile = lightProfileResponse.body;
            });
    }

    reloadLightProfileSlots(id, reference, callback) {
        this.lightProfileSlotService.getLightProfileSlotsByLightProfile(id).subscribe((response) => {
            this.lightProfile = response.body;
            callback(response.body, reference);
            // this.startLightProfileViewer();
        });
    }

    replaceLightProfileSlots(id, slots, reference, callback) {
        this.lightProfileService.replaceLightProfileSlots(id, slots).subscribe(() => {
            callback();
        });
    }

    previousState() {
        window.history.back();
    }

    ngOnDestroy() {
        this.subscription.unsubscribe();
        this.eventManager.destroy(this.eventSubscriber);
    }

    registerChangeInLightProfiles() {
        this.eventSubscriber = this.eventManager.subscribe(
            'lightProfileListModification',
            (response) => this.load(this.lightProfile.id)
        );
    }

    startLightProfileViewer() {

        this.lPP = new lightProfileViewer($);
        this.lPP.LightProfileController = this;
        this.lPP.lightProfileId = this.lightProfile.id;
        if (parent != null) { this.lPP.homePage = (<any>parent).homePage; }
        this.lPP._unreadTMTime = 1;
        /*Handle resize*/
        window.addEventListener('resize', this.setLayoutSizes, false);
        this.lPP.init();
    }

    setLayoutSizes() {
        if (this.lPP.dhxLayout) {
            this.lPP.dhxLayout.setAutoSize('a;b', 'a;b');
            this.lPP.dhxLayout.setSizes();
        }
    }

    waitForDiv(reference) {
        const lpViewer = document.getElementById('lpViewer');
        if (lpViewer != null) {
            reference.startLightProfileViewer();
        } else {
            setTimeout(reference.waitForDiv.bind(null, reference), 250);
        }

    }

    ngAfterViewInit() {
        this._script.load('body',
            'assets/app/js/libs/common.js',
            'assets/app/js/libs/dhtmlxsuite/dhtmlx.js',
            'assets/app/js/libs/dhtmlxgantt/dhtmlxgantt_pro.js',
            'assets/app/js/libs/lightProfileViewer/lightProfileViewer.js')
            .then((result) => {
                console.warn('DHTMLX loaded');
                this.waitForDiv(this);
            });
    }
}
