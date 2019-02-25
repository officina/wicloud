import { Injectable, Component } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal, NgbModalRef } from '@ng-bootstrap/ng-bootstrap';
import { HttpResponse } from '@angular/common/http';
import { LightProfileWilamp } from './light-profile-wilamp.model';
import { LightProfileWilampService } from './light-profile-wilamp.service';

@Injectable()
export class LightProfileWilampPopupService {
    private ngbModalRef: NgbModalRef;

    constructor(
        private modalService: NgbModal,
        private router: Router,
        private lightProfileService: LightProfileWilampService,

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
                this.lightProfileService.find(id)
                    .subscribe((lightProfileResponse: HttpResponse<LightProfileWilamp>) => {
                        const lightProfile: LightProfileWilamp = lightProfileResponse.body;
                        this.ngbModalRef = this.lightProfileModalRef(component, lightProfile);
                        resolve(this.ngbModalRef);
                    });
            } else {
                // setTimeout used as a workaround for getting ExpressionChangedAfterItHasBeenCheckedError
                setTimeout(() => {
                    this.ngbModalRef = this.lightProfileModalRef(component, new LightProfileWilamp());
                    resolve(this.ngbModalRef);
                }, 0);
            }
        });
    }

    lightProfileModalRef(component: Component, lightProfile: LightProfileWilamp): NgbModalRef {
        const modalRef = this.modalService.open(component, { size: 'lg', backdrop: 'static'});
        modalRef.componentInstance.lightProfile = lightProfile;
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
