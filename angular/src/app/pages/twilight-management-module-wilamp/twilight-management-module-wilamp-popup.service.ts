import { Injectable, Component } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal, NgbModalRef } from '@ng-bootstrap/ng-bootstrap';
import { HttpResponse } from '@angular/common/http';
import { DatePipe } from '@angular/common';
import { TwilightManagementModuleWilamp } from './twilight-management-module-wilamp.model';
import { TwilightManagementModuleWilampService } from './twilight-management-module-wilamp.service';

@Injectable()
export class TwilightManagementModuleWilampPopupService {
    private ngbModalRef: NgbModalRef;

    constructor(
        private datePipe: DatePipe,
        private modalService: NgbModal,
        private router: Router,
        private twilightManagementModuleService: TwilightManagementModuleWilampService,

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
                this.twilightManagementModuleService.find(id)
                    .subscribe((twilightManagementModuleResponse: HttpResponse<TwilightManagementModuleWilamp>) => {
                        const twilightManagementModule: TwilightManagementModuleWilamp = twilightManagementModuleResponse.body;
                        twilightManagementModule.createdTimestamp = this.datePipe
                            .transform(twilightManagementModule.createdTimestamp, 'yyyy-MM-ddTHH:mm:ss');
                        this.ngbModalRef = this.twilightManagementModuleModalRef(component, twilightManagementModule);
                        resolve(this.ngbModalRef);
                    });
            } else {
                // setTimeout used as a workaround for getting ExpressionChangedAfterItHasBeenCheckedError
                setTimeout(() => {
                    this.ngbModalRef = this.twilightManagementModuleModalRef(component, new TwilightManagementModuleWilamp());
                    resolve(this.ngbModalRef);
                }, 0);
            }
        });
    }

    twilightManagementModuleModalRef(component: Component, twilightManagementModule: TwilightManagementModuleWilamp): NgbModalRef {
        const modalRef = this.modalService.open(component, { size: 'lg', backdrop: 'static'});
        modalRef.componentInstance.twilightManagementModule = twilightManagementModule;
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
