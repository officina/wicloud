import { Injectable, Component } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal, NgbModalRef } from '@ng-bootstrap/ng-bootstrap';
import { HttpResponse } from '@angular/common/http';
import { DatePipe } from '@angular/common';
import { MotionManagementModuleWilamp } from './motion-management-module-wilamp.model';
import { MotionManagementModuleWilampService } from './motion-management-module-wilamp.service';

@Injectable()
export class MotionManagementModuleWilampPopupService {
    private ngbModalRef: NgbModalRef;

    constructor(
        private datePipe: DatePipe,
        private modalService: NgbModal,
        private router: Router,
        private motionManagementModuleService: MotionManagementModuleWilampService

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
                this.motionManagementModuleService.find(id)
                    .subscribe((motionManagementModuleResponse: HttpResponse<MotionManagementModuleWilamp>) => {
                        const motionManagementModule: MotionManagementModuleWilamp = motionManagementModuleResponse.body;
                        motionManagementModule.createdTimestamp = this.datePipe
                            .transform(motionManagementModule.createdTimestamp, 'yyyy-MM-ddTHH:mm:ss');
                        this.ngbModalRef = this.motionManagementModuleModalRef(component, motionManagementModule);
                        resolve(this.ngbModalRef);
                    });
            } else {
                // setTimeout used as a workaround for getting ExpressionChangedAfterItHasBeenCheckedError
                setTimeout(() => {
                    this.ngbModalRef = this.motionManagementModuleModalRef(component, new MotionManagementModuleWilamp());
                    resolve(this.ngbModalRef);
                }, 0);
            }
        });
    }

    motionManagementModuleModalRef(component: Component, motionManagementModule: MotionManagementModuleWilamp): NgbModalRef {
        const modalRef = this.modalService.open(component, { size: 'lg', backdrop: 'static'});
        modalRef.componentInstance.motionManagementModule = motionManagementModule;
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
