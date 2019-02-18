import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse, HttpErrorResponse } from '@angular/common/http';

import { Observable } from 'rxjs/Observable';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager } from 'ng-jhipster';

import { LightProfileWilamp } from './light-profile-wilamp.model';
import { LightProfileWilampPopupService } from './light-profile-wilamp-popup.service';
import { LightProfileWilampService } from './light-profile-wilamp.service';

@Component({
    selector: 'jhi-light-profile-wilamp-dialog',
    templateUrl: './light-profile-wilamp-dialog.component.html'
})
export class LightProfileWilampDialogComponent implements OnInit {

    lightProfile: LightProfileWilamp;
    isSaving: boolean;

    constructor(
        public activeModal: NgbActiveModal,
        private lightProfileService: LightProfileWilampService,
        private eventManager: JhiEventManager
    ) {
    }

    ngOnInit() {
        this.isSaving = false;
    }

    clear() {
        this.activeModal.dismiss('cancel');
    }

    save() {
        this.isSaving = true;
        if (this.lightProfile.id !== undefined) {
            this.subscribeToSaveResponse(
                this.lightProfileService.update(this.lightProfile));
        } else {
            this.subscribeToSaveResponse(
                this.lightProfileService.create(this.lightProfile));
        }
    }

    private subscribeToSaveResponse(result: Observable<HttpResponse<LightProfileWilamp>>) {
        result.subscribe((res: HttpResponse<LightProfileWilamp>) =>
            this.onSaveSuccess(res.body), (res: HttpErrorResponse) => this.onSaveError());
    }

    private onSaveSuccess(result: LightProfileWilamp) {
        this.eventManager.broadcast({ name: 'lightProfileListModification', content: 'OK'});
        this.isSaving = false;
        this.activeModal.dismiss(result);
    }

    private onSaveError() {
        this.isSaving = false;
    }
}

@Component({
    selector: 'jhi-light-profile-wilamp-popup',
    template: ''
})
export class LightProfileWilampPopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private lightProfilePopupService: LightProfileWilampPopupService
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            if ( params['id'] ) {
                this.lightProfilePopupService
                    .open(LightProfileWilampDialogComponent as Component, params['id']);
            } else {
                this.lightProfilePopupService
                    .open(LightProfileWilampDialogComponent as Component);
            }
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
