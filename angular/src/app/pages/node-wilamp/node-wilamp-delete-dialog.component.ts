import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager } from 'ng-jhipster';

import { NodeWilamp } from './node-wilamp.model';
import { NodeWilampPopupService } from './node-wilamp-popup.service';
import { NodeWilampService } from './node-wilamp.service';

@Component({
    selector: 'jhi-node-wilamp-delete-dialog',
    templateUrl: './node-wilamp-delete-dialog.component.html'
})
export class NodeWilampDeleteDialogComponent {

    node: NodeWilamp;

    constructor(
        private nodeService: NodeWilampService,
        public activeModal: NgbActiveModal,
        private eventManager: JhiEventManager
    ) {
    }

    clear() {
        this.activeModal.dismiss('cancel');
    }

    confirmDelete(id: number) {
        this.nodeService.delete(id).subscribe((response) => {
            this.eventManager.broadcast({
                name: 'nodeListModification',
                content: 'Deleted an node'
            });
            this.activeModal.dismiss(true);
        });
    }
}

@Component({
    selector: 'jhi-node-wilamp-delete-popup',
    template: ''
})
export class NodeWilampDeletePopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private nodePopupService: NodeWilampPopupService
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            this.nodePopupService
                .open(NodeWilampDeleteDialogComponent as Component, params['id']);
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
