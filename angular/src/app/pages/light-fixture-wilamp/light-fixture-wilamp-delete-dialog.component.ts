import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager } from 'ng-jhipster';

import { LightFixtureWilamp } from './light-fixture-wilamp.model';
import { LightFixtureWilampPopupService } from './light-fixture-wilamp-popup.service';
import { LightFixtureWilampService } from './light-fixture-wilamp.service';

@Component({
    selector: 'jhi-light-fixture-wilamp-delete-dialog',
    templateUrl: './light-fixture-wilamp-delete-dialog.component.html'
})
export class LightFixtureWilampDeleteDialogComponent {

    lightFixture: LightFixtureWilamp;

    constructor(
        private lightFixtureService: LightFixtureWilampService,
        public activeModal: NgbActiveModal,
        private eventManager: JhiEventManager
    ) {
    }

    clear() {
        this.activeModal.dismiss('cancel');
    }

    confirmDelete(id: number) {
        this.lightFixtureService.delete(id).subscribe((response) => {
            this.eventManager.broadcast({
                name: 'lightFixtureListModification',
                content: 'Deleted an lightFixture'
            });
            this.activeModal.dismiss(true);
        });
    }
}

@Component({
    selector: 'jhi-light-fixture-wilamp-delete-popup',
    template: ''
})
export class LightFixtureWilampDeletePopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private lightFixturePopupService: LightFixtureWilampPopupService
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            this.lightFixturePopupService
                .open(LightFixtureWilampDeleteDialogComponent as Component, params['id']);
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
