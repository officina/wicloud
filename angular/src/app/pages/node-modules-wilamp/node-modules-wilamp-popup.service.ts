import { Injectable, Component } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal, NgbModalRef } from '@ng-bootstrap/ng-bootstrap';
import { HttpResponse } from '@angular/common/http';
import { NodeModulesWilamp } from './node-modules-wilamp.model';
import { NodeModulesWilampService } from './node-modules-wilamp.service';

@Injectable()
export class NodeModulesWilampPopupService {
    private ngbModalRef: NgbModalRef;

    constructor(
        private modalService: NgbModal,
        private router: Router,
        private nodeModulesService: NodeModulesWilampService

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
                this.nodeModulesService.find(id)
                    .subscribe((nodeModulesResponse: HttpResponse<NodeModulesWilamp>) => {
                        const nodeModules: NodeModulesWilamp = nodeModulesResponse.body;
                        this.ngbModalRef = this.nodeModulesModalRef(component, nodeModules);
                        resolve(this.ngbModalRef);
                    });
            } else {
                // setTimeout used as a workaround for getting ExpressionChangedAfterItHasBeenCheckedError
                setTimeout(() => {
                    this.ngbModalRef = this.nodeModulesModalRef(component, new NodeModulesWilamp());
                    resolve(this.ngbModalRef);
                }, 0);
            }
        });
    }

    nodeModulesModalRef(component: Component, nodeModules: NodeModulesWilamp): NgbModalRef {
        const modalRef = this.modalService.open(component, { size: 'lg', backdrop: 'static'});
        modalRef.componentInstance.nodeModules = nodeModules;
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
