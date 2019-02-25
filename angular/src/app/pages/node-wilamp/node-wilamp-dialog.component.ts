import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { JhiEventManager, JhiAlertService } from 'ng-jhipster';
import { NodeWilamp } from './node-wilamp.model';
import { NodeWilampPopupService } from './node-wilamp-popup.service';
import { NodeWilampService } from './node-wilamp.service';
import { NodeModulesWilamp } from '../node-modules-wilamp/node-modules-wilamp.model';
import { NodeModulesWilampService } from '../node-modules-wilamp/node-modules-wilamp.service';
import { GatewayWilamp } from '../gateway-wilamp/gateway-wilamp.model';
import { GatewayWilampService } from '../gateway-wilamp/gateway-wilamp.service';
import { ShippingWilamp } from '../shipping-wilamp/shipping-wilamp.model';
import { ShippingWilampService } from '../shipping-wilamp/shipping-wilamp.service';
import { OrderWilamp } from '../order-wilamp/order-wilamp.model';
import { OrderWilampService } from '../order-wilamp/order-wilamp.service';

@Component({
    selector: 'jhi-node-wilamp-dialog',
    templateUrl: './node-wilamp-dialog.component.html',
})
export class NodeWilampDialogComponent implements OnInit {

    node: NodeWilamp;
    isSaving: boolean;

    modules: NodeModulesWilamp[];

    gateways: GatewayWilamp[];

    shippings: ShippingWilamp[];

    orders: OrderWilamp[];

    constructor(
        public activeModal: NgbActiveModal,
        private jhiAlertService: JhiAlertService,
        private nodeService: NodeWilampService,
        private nodeModulesService: NodeModulesWilampService,
        private gatewayService: GatewayWilampService,
        private shippingService: ShippingWilampService,
        private orderService: OrderWilampService,
        private eventManager: JhiEventManager,
    ) {
    }

    ngOnInit() {
        this.isSaving = false;
        this.nodeModulesService
            .query({filter: 'node(mac)-is-null'})
            .subscribe((res: HttpResponse<NodeModulesWilamp[]>) => {
                if (!this.node.modulesId) {
                    this.modules = res.body;
                } else {
                    this.nodeModulesService
                        .find(this.node.modulesId)
                        .subscribe((subRes: HttpResponse<NodeModulesWilamp>) => {
                            this.modules = [subRes.body].concat(res.body);
                        }, (subRes: HttpErrorResponse) => this.onError(subRes.message));
                }
            }, (res: HttpErrorResponse) => this.onError(res.message));
        this.gatewayService.query()
            .subscribe((res: HttpResponse<GatewayWilamp[]>) => { this.gateways = res.body; }, (res: HttpErrorResponse) => this.onError(res.message));
        this.shippingService.query()
            .subscribe((res: HttpResponse<ShippingWilamp[]>) => { this.shippings = res.body; }, (res: HttpErrorResponse) => this.onError(res.message));
        this.orderService.query()
            .subscribe((res: HttpResponse<OrderWilamp[]>) => { this.orders = res.body; }, (res: HttpErrorResponse) => this.onError(res.message));
    }

    clear() {
        this.activeModal.dismiss('cancel');
    }

    save() {
        this.isSaving = true;
        if (this.node.id !== undefined) {
            this.subscribeToSaveResponse(
                this.nodeService.update(this.node));
        } else {
            this.subscribeToSaveResponse(
                this.nodeService.create(this.node));
        }
    }

    private subscribeToSaveResponse(result: Observable<HttpResponse<NodeWilamp>>) {
        result.subscribe((res: HttpResponse<NodeWilamp>) =>
            this.onSaveSuccess(res.body), (res: HttpErrorResponse) => this.onSaveError());
    }

    private onSaveSuccess(result: NodeWilamp) {
        this.eventManager.broadcast({ name: 'nodeListModification', content: 'OK'});
        this.isSaving = false;
        this.activeModal.dismiss(result);
    }

    private onSaveError() {
        this.isSaving = false;
    }

    private onError(error: any) {
        this.jhiAlertService.error(error.message, null, null);
    }

    trackNodeModulesById(index: number, item: NodeModulesWilamp) {
        return item.id;
    }

    trackGatewayById(index: number, item: GatewayWilamp) {
        return item.id;
    }

    trackShippingById(index: number, item: ShippingWilamp) {
        return item.id;
    }

    trackOrderById(index: number, item: OrderWilamp) {
        return item.id;
    }
}

@Component({
    selector: 'jhi-node-wilamp-popup',
    template: '',
})
export class NodeWilampPopupComponent implements OnInit, OnDestroy {

    routeSub: any;

    constructor(
        private route: ActivatedRoute,
        private nodePopupService: NodeWilampPopupService,
    ) {}

    ngOnInit() {
        this.routeSub = this.route.params.subscribe((params) => {
            if ( params['id'] ) {
                this.nodePopupService
                    .open(NodeWilampDialogComponent as Component, params['id']);
            } else {
                this.nodePopupService
                    .open(NodeWilampDialogComponent as Component);
            }
        });
    }

    ngOnDestroy() {
        this.routeSub.unsubscribe();
    }
}
