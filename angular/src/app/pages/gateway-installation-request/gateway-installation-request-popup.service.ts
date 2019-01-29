import { Injectable, Component } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal, NgbModalRef } from '@ng-bootstrap/ng-bootstrap';
import { HttpResponse } from '@angular/common/http';
import { DatePipe } from '@angular/common';
import { GatewayInstallationRequest } from './gateway-installation-request.model';
import { GatewayInstallationRequestService } from './gateway-installation-request.service';

@Injectable()
export class GatewayInstallationRequestPopupService {
    private ngbModalRef: NgbModalRef;

    constructor(
        private datePipe: DatePipe,
        private modalService: NgbModal,
        private router: Router,
        private gatewayInstallationRequestService: GatewayInstallationRequestService

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
                this.gatewayInstallationRequestService.find(id)
                    .subscribe((gatewayInstallationRequestResponse: HttpResponse<GatewayInstallationRequest>) => {
                        const gatewayInstallationRequest: GatewayInstallationRequest = gatewayInstallationRequestResponse.body;
                        gatewayInstallationRequest.creationDate = this.datePipe
                            .transform(gatewayInstallationRequest.creationDate, 'yyyy-MM-ddTHH:mm:ss');
                        gatewayInstallationRequest.startInstallationTimestamp = this.datePipe
                            .transform(gatewayInstallationRequest.startInstallationTimestamp, 'yyyy-MM-ddTHH:mm:ss');
                        gatewayInstallationRequest.endInstallationTimestamp = this.datePipe
                            .transform(gatewayInstallationRequest.endInstallationTimestamp, 'yyyy-MM-ddTHH:mm:ss');
                        this.ngbModalRef = this.gatewayInstallationRequestModalRef(component, gatewayInstallationRequest);
                        resolve(this.ngbModalRef);
                    });
            } else {
                // setTimeout used as a workaround for getting ExpressionChangedAfterItHasBeenCheckedError
                setTimeout(() => {
                    this.ngbModalRef = this.gatewayInstallationRequestModalRef(component, new GatewayInstallationRequest());
                    resolve(this.ngbModalRef);
                }, 0);
            }
        });
    }

    gatewayInstallationRequestModalRef(component: Component, gatewayInstallationRequest: GatewayInstallationRequest): NgbModalRef {
        const modalRef = this.modalService.open(component, { size: 'lg', backdrop: 'static'});
        modalRef.componentInstance.gatewayInstallationRequest = gatewayInstallationRequest;
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
