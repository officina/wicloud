import { Injectable, Component } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal, NgbModalRef } from '@ng-bootstrap/ng-bootstrap';
import { HttpResponse } from '@angular/common/http';
import { LightFixtureWilamp } from './light-fixture-wilamp.model';
import { LightFixtureWilampService } from './light-fixture-wilamp.service';

@Injectable()
export class LightFixtureWilampPopupService {
    private ngbModalRef: NgbModalRef;

    constructor(
        private modalService: NgbModal,
        private router: Router,
        private lightFixtureService: LightFixtureWilampService,

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
                this.lightFixtureService.find(id)
                    .subscribe((lightFixtureResponse: HttpResponse<LightFixtureWilamp>) => {
                        const lightFixture: LightFixtureWilamp = lightFixtureResponse.body;
                        this.ngbModalRef = this.lightFixtureModalRef(component, lightFixture);
                        resolve(this.ngbModalRef);
                    });
            } else {
                // setTimeout used as a workaround for getting ExpressionChangedAfterItHasBeenCheckedError
                setTimeout(() => {
                    this.ngbModalRef = this.lightFixtureModalRef(component, new LightFixtureWilamp());
                    resolve(this.ngbModalRef);
                }, 0);
            }
        });
    }

    lightFixtureModalRef(component: Component, lightFixture: LightFixtureWilamp): NgbModalRef {
        const modalRef = this.modalService.open(component, { size: 'lg', backdrop: 'static'});
        modalRef.componentInstance.lightFixture = lightFixture;
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
