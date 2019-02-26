import {Component} from '@angular/core';
import {HttpClient} from '@angular/common/http';
@Component({
    selector: 'gateway-administration-component',
    template: '<div [innerHTML]="fetchedHtml"></div>',
})
export class GatewayAdministrationWidgetComponent {

    public fetchedHtml = '';

    constructor(
        private http: HttpClient,
    ) {
        const headers = new Headers();
        headers.append('x-forwarded-host', 'foo');
        http.get('http://10.8.10.34', {headers: null}).subscribe((response) => {
        this.fetchedHtml = response.toString();
        });
    }
}
