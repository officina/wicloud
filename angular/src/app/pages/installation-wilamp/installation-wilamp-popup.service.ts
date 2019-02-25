import { Injectable, Component } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal, NgbModalRef } from '@ng-bootstrap/ng-bootstrap';
import { HttpResponse } from '@angular/common/http';
import { DatePipe } from '@angular/common';
import { InstallationWilamp } from './installation-wilamp.model';
import { InstallationWilampService } from './installation-wilamp.service';

@Injectable()
export class InstallationWilampPopupService {
    private ngbModalRef: NgbModalRef;

    constructor(
        private datePipe: DatePipe,
        private modalService: NgbModal,
        private router: Router,
        private installationService: InstallationWilampService,

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
                this.installationService.find(id)
                    .subscribe((installationResponse: HttpResponse<InstallationWilamp>) => {
                        const installation: InstallationWilamp = installationResponse.body;
                        installation.preparationDate = this.datePipe
                            .transform(installation.preparationDate, 'yyyy-MM-ddTHH:mm:ss');
                        installation.installationDate = this.datePipe
                            .transform(installation.installationDate, 'yyyy-MM-ddTHH:mm:ss');
                        this.ngbModalRef = this.installationModalRef(component, installation);
                        resolve(this.ngbModalRef);
                    });
            } else {
                // setTimeout used as a workaround for getting ExpressionChangedAfterItHasBeenCheckedError
                setTimeout(() => {
                    this.ngbModalRef = this.installationModalRef(component, new InstallationWilamp());
                    resolve(this.ngbModalRef);
                }, 0);
            }
        });
    }

    installationModalRef(component: Component, installation: InstallationWilamp): NgbModalRef {
        const modalRef = this.modalService.open(component, { size: 'lg', backdrop: 'static'});
        modalRef.componentInstance.installation = installation;
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
