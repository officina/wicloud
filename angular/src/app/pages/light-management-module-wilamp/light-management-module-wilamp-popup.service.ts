import { Injectable, Component } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal, NgbModalRef } from '@ng-bootstrap/ng-bootstrap';
import { HttpResponse } from '@angular/common/http';
import { LightManagementModuleWilamp } from './light-management-module-wilamp.model';
import { LightManagementModuleWilampService } from './light-management-module-wilamp.service';

@Injectable()
export class LightManagementModuleWilampPopupService {
    private ngbModalRef: NgbModalRef;

    constructor(
        private modalService: NgbModal,
        private router: Router,
        private lightManagementModuleService: LightManagementModuleWilampService

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
                this.lightManagementModuleService.find(id)
                    .subscribe((lightManagementModuleResponse: HttpResponse<LightManagementModuleWilamp>) => {
                        const lightManagementModule: LightManagementModuleWilamp = lightManagementModuleResponse.body;
                        this.ngbModalRef = this.lightManagementModuleModalRef(component, lightManagementModule);
                        resolve(this.ngbModalRef);
                    });
            } else {
                // setTimeout used as a workaround for getting ExpressionChangedAfterItHasBeenCheckedError
                setTimeout(() => {
                    this.ngbModalRef = this.lightManagementModuleModalRef(component, new LightManagementModuleWilamp());
                    resolve(this.ngbModalRef);
                }, 0);
            }
        });
    }

    lightManagementModuleModalRef(component: Component, lightManagementModule: LightManagementModuleWilamp): NgbModalRef {
        const modalRef = this.modalService.open(component, { size: 'lg', backdrop: 'static'});
        modalRef.componentInstance.lightManagementModule = lightManagementModule;
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
