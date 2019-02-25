import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager } from 'ng-jhipster';

import { NodeModulesWilamp } from './node-modules-wilamp.model';
import { NodeModulesWilampPopupService } from './node-modules-wilamp-popup.service';
import { NodeModulesWilampService } from './node-modules-wilamp.service';

@Component({
    selector: 'jhi-node-modules-wilamp-delete-dialog',
    templateUrl: './node-modules-wilamp-delete-dialog.component.html',
})
export class NodeModulesWilampDeleteDialogComponent {

    nodeModules: NodeModulesWilamp;

    constructor(
        private nodeModulesService: NodeModulesWilampService,
        public activeModal: NgbActiveModal,
        private eventManager: JhiEventManager,
    ) {
    }

    clear() {
        this.activeModal.dismiss('cancel');
    }

    confirmDelete(id: number) {
        this.nodeModulesService.delete(id).subscribe((response) => {
            this.eventManager.broadcast({
                name: 'nodeModulesListModification',
                content: 'Deleted an nodeModules',
            });
            this.activeModal.dismiss(true);
        });
    }
}

@Component({
    selector: 'jhi-node-modules-wilamp-delete-popup',
    template: '',
})
export class NodeModulesWilampDeletePopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private nodeModulesPopupService: NodeModulesWilampPopupService,
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            this.nodeModulesPopupService
                .open(NodeModulesWilampDeleteDialogComponent as Component, params['id']);
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
