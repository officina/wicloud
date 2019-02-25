import { Injectable, Component } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal, NgbModalRef } from '@ng-bootstrap/ng-bootstrap';
import { HttpResponse } from '@angular/common/http';
import { DatePipe } from '@angular/common';
import { LightManagementMeasureWilamp } from './light-management-measure-wilamp.model';
import { LightManagementMeasureWilampService } from './light-management-measure-wilamp.service';

@Injectable()
export class LightManagementMeasureWilampPopupService {
    private ngbModalRef: NgbModalRef;

    constructor(
        private datePipe: DatePipe,
        private modalService: NgbModal,
        private router: Router,
        private lightManagementMeasureService: LightManagementMeasureWilampService,

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
                this.lightManagementMeasureService.find(id)
                    .subscribe((lightManagementMeasureResponse: HttpResponse<LightManagementMeasureWilamp>) => {
                        const lightManagementMeasure: LightManagementMeasureWilamp = lightManagementMeasureResponse.body;
                        lightManagementMeasure.measureTimestamp = this.datePipe
                            .transform(lightManagementMeasure.measureTimestamp, 'yyyy-MM-ddTHH:mm:ss');
                        lightManagementMeasure.createdTimestamp = this.datePipe
                            .transform(lightManagementMeasure.createdTimestamp, 'yyyy-MM-ddTHH:mm:ss');
                        this.ngbModalRef = this.lightManagementMeasureModalRef(component, lightManagementMeasure);
                        resolve(this.ngbModalRef);
                    });
            } else {
                // setTimeout used as a workaround for getting ExpressionChangedAfterItHasBeenCheckedError
                setTimeout(() => {
                    this.ngbModalRef = this.lightManagementMeasureModalRef(component, new LightManagementMeasureWilamp());
                    resolve(this.ngbModalRef);
                }, 0);
            }
        });
    }

    lightManagementMeasureModalRef(component: Component, lightManagementMeasure: LightManagementMeasureWilamp): NgbModalRef {
        const modalRef = this.modalService.open(component, { size: 'lg', backdrop: 'static'});
        modalRef.componentInstance.lightManagementMeasure = lightManagementMeasure;
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
