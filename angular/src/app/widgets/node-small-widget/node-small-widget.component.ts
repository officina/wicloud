import {Component, Input, OnInit} from '@angular/core';
import {NodeWilamp} from '../../pages/node-wilamp';

@Component({
  selector: 'jhi-node-small-widget',
  templateUrl: './node-small-widget.component.html',
  styles: [],
})
export class NodeSmallWidgetComponent implements OnInit {
  @Input() node: NodeWilamp;

  constructor() { }

  ngOnInit() {
  }

}
