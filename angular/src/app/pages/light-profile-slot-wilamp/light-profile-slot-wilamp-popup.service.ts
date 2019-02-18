import { Injectable, Component } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal, NgbModalRef } from '@ng-bootstrap/ng-bootstrap';
import { HttpResponse } from '@angular/common/http';
import { DatePipe } from '@angular/common';
import { LightProfileSlotWilamp } from './light-profile-slot-wilamp.model';
import { LightProfileSlotWilampService } from './light-profile-slot-wilamp.service';

@Injectable()
export class LightProfileSlotWilampPopupService {
    private ngbModalRef: NgbModalRef;

    constructor(
        private datePipe: DatePipe,
        private modalService: NgbModal,
        private router: Router,
        private lightProfileSlotService: LightProfileSlotWilampService

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
                this.lightProfileSlotService.find(id)
                    .subscribe((lightProfileSlotResponse: HttpResponse<LightProfileSlotWilamp>) => {
                        const lightProfileSlot: LightProfileSlotWilamp = lightProfileSlotResponse.body;
                        lightProfileSlot.createdTimestamp = this.datePipe
                            .transform(lightProfileSlot.createdTimestamp, 'yyyy-MM-ddTHH:mm:ss');
                        this.ngbModalRef = this.lightProfileSlotModalRef(component, lightProfileSlot);
                        resolve(this.ngbModalRef);
                    });
            } else {
                // setTimeout used as a workaround for getting ExpressionChangedAfterItHasBeenCheckedError
                setTimeout(() => {
                    this.ngbModalRef = this.lightProfileSlotModalRef(component, new LightProfileSlotWilamp());
                    resolve(this.ngbModalRef);
                }, 0);
            }
        });
    }

    lightProfileSlotModalRef(component: Component, lightProfileSlot: LightProfileSlotWilamp): NgbModalRef {
        const modalRef = this.modalService.open(component, { size: 'lg', backdrop: 'static'});
        modalRef.componentInstance.lightProfileSlot = lightProfileSlot;
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
