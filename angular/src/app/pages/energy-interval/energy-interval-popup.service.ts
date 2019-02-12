import { Injectable, Component } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal, NgbModalRef } from '@ng-bootstrap/ng-bootstrap';
import { HttpResponse } from '@angular/common/http';
import { DatePipe } from '@angular/common';
import { EnergyInterval } from './energy-interval.model';
import { EnergyIntervalService } from './energy-interval.service';

@Injectable()
export class EnergyIntervalPopupService {
    private ngbModalRef: NgbModalRef;

    constructor(
        private datePipe: DatePipe,
        private modalService: NgbModal,
        private router: Router,
        private energyIntervalService: EnergyIntervalService

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
                this.energyIntervalService.find(id)
                    .subscribe((energyIntervalResponse: HttpResponse<EnergyInterval>) => {
                        const energyInterval: EnergyInterval = energyIntervalResponse.body;
                        energyInterval.startInterval = this.datePipe
                            .transform(energyInterval.startInterval, 'yyyy-MM-ddTHH:mm:ss');
                        energyInterval.endInterval = this.datePipe
                            .transform(energyInterval.endInterval, 'yyyy-MM-ddTHH:mm:ss');
                        energyInterval.startIntervalMeasureTimestamp = this.datePipe
                            .transform(energyInterval.startIntervalMeasureTimestamp, 'yyyy-MM-ddTHH:mm:ss');
                        energyInterval.endIntervalMeasureTimestamp = this.datePipe
                            .transform(energyInterval.endIntervalMeasureTimestamp, 'yyyy-MM-ddTHH:mm:ss');
                        this.ngbModalRef = this.energyIntervalModalRef(component, energyInterval);
                        resolve(this.ngbModalRef);
                    });
            } else {
                // setTimeout used as a workaround for getting ExpressionChangedAfterItHasBeenCheckedError
                setTimeout(() => {
                    this.ngbModalRef = this.energyIntervalModalRef(component, new EnergyInterval());
                    resolve(this.ngbModalRef);
                }, 0);
            }
        });
    }

    energyIntervalModalRef(component: Component, energyInterval: EnergyInterval): NgbModalRef {
        const modalRef = this.modalService.open(component, { size: 'lg', backdrop: 'static'});
        modalRef.componentInstance.energyInterval = energyInterval;
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
