import { Injectable, Component } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal, NgbModalRef } from '@ng-bootstrap/ng-bootstrap';
import { HttpResponse } from '@angular/common/http';
import { DatePipe } from '@angular/common';
import { GatewayWilamp } from './gateway-wilamp.model';
import { GatewayWilampService } from './gateway-wilamp.service';

@Injectable()
export class GatewayWilampPopupService {
    private ngbModalRef: NgbModalRef;

    constructor(
        private datePipe: DatePipe,
        private modalService: NgbModal,
        private router: Router,
        private gatewayService: GatewayWilampService,

    ) {
        this.ngbModalRef = null;
    }

    open(component: Component, id?: number | any): Promise<NgbModalRef> {
        return new Promise<NgbModalRef>((resolve, reject) => {
            const isOpen = this.ngbModalRef !== null;
            if (isOpen) {
                resolve(this.ngbModalRef);
            }

            if (id) {
                this.gatewayService.find(id)
                    .subscribe((gatewayResponse: HttpResponse<GatewayWilamp>) => {
                        const gateway: GatewayWilamp = gatewayResponse.body;
                        gateway.creationDate = this.datePipe
                            .transform(gateway.creationDate, 'yyyy-MM-ddTHH:mm:ss');
                        this.ngbModalRef = this.gatewayModalRef(component, gateway);
                        resolve(this.ngbModalRef);
                    });
            } else {
                // setTimeout used as a workaround for getting ExpressionChangedAfterItHasBeenCheckedError
                setTimeout(() => {
                    this.ngbModalRef = this.gatewayModalRef(component, new GatewayWilamp());
                    resolve(this.ngbModalRef);
                }, 0);
            }
        });
    }

    gatewayModalRef(component: Component, gateway: GatewayWilamp): NgbModalRef {
        const modalRef = this.modalService.open(component, { size: 'lg', backdrop: 'static'});
        modalRef.componentInstance.gateway = gateway;
        modalRef.result.then((result) => {
            this.router.navigate([{ outlets: { popup: null }}], { replaceUrl: true, queryParamsHandling: 'merge' });
            this.ngbModalRef = null;
        }, (reason) => {
            this.router.navigate([{ outlets: { popup: null }}], { replaceUrl: true, queryParamsHandling: 'merge' });
            this.ngbModalRef = null;
        });
        return modalRef;
    }
}
