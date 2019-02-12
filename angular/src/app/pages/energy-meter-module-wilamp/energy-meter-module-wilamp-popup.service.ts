import { Injectable, Component } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal, NgbModalRef } from '@ng-bootstrap/ng-bootstrap';
import { HttpResponse } from '@angular/common/http';
import { EnergyMeterModuleWilamp } from './energy-meter-module-wilamp.model';
import { EnergyMeterModuleWilampService } from './energy-meter-module-wilamp.service';

@Injectable()
export class EnergyMeterModuleWilampPopupService {
    private ngbModalRef: NgbModalRef;

    constructor(
        private modalService: NgbModal,
        private router: Router,
        private energyMeterModuleService: EnergyMeterModuleWilampService

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
                this.energyMeterModuleService.find(id)
                    .subscribe((energyMeterModuleResponse: HttpResponse<EnergyMeterModuleWilamp>) => {
                        const energyMeterModule: EnergyMeterModuleWilamp = energyMeterModuleResponse.body;
                        this.ngbModalRef = this.energyMeterModuleModalRef(component, energyMeterModule);
                        resolve(this.ngbModalRef);
                    });
            } else {
                // setTimeout used as a workaround for getting ExpressionChangedAfterItHasBeenCheckedError
                setTimeout(() => {
                    this.ngbModalRef = this.energyMeterModuleModalRef(component, new EnergyMeterModuleWilamp());
                    resolve(this.ngbModalRef);
                }, 0);
            }
        });
    }

    energyMeterModuleModalRef(component: Component, energyMeterModule: EnergyMeterModuleWilamp): NgbModalRef {
        const modalRef = this.modalService.open(component, { size: 'lg', backdrop: 'static'});
        modalRef.componentInstance.energyMeterModule = energyMeterModule;
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
