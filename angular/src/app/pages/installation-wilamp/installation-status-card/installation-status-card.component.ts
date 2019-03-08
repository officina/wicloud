import { Component, Input } from '@angular/core';

@Component({
  selector: 'ngx-installation-status-card',
  styleUrls: ['./installation-status-card.component.scss'],
  template: `
    <nb-card (click)="on = !on" [ngClass]="{'off': !on}">
      <div class="icon-container">
        <div class="icon {{ type }}">
          <ng-content></ng-content>
        </div>
      </div>

      <div class="details">
        <div class="details-head">
        <div class="title">{{ headTitle }}</div>
        <div class="status">{{ headValue }}</div>
        </div>
        <hr class="horizontal-line" />
        <div class="values">
          <div class="param1">
            <div class="title">{{ param1Title }}</div>
            <div class="status">{{ param1Value }}</div>
          </div>
          <div class="param2" *ngIf="param2Title">
            <div class="title">{{ param2Title }}</div>
            <div class="status">{{ param2Value }}</div>
          </div>
        </div>
      </div>
    </nb-card>
  `,
})
export class InstallationStatusCardComponent {

  @Input() headTitle: string;
  @Input() headValue: string;
  @Input() param1Title: string;
  @Input() param1Value: string;
  @Input() param2Title: string;
  @Input() param2Value: string;
  @Input() type: string;
  @Input() on = true;
}
