import { Component } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {environment} from '../environments/environment';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'iot-front';

  constructor( private http: HttpClient){

  };


  test(): void {
    this.http.get(environment.url + '/').subscribe();
  }
  lumiereAllume(numero: number): void {
    this.http.get(environment.url + '/lumiere/allume/' + numero, {responseType: 'text'}).subscribe(console.log);
  }
  lumiereEteint(numero: number): void {
    this.http.get(environment.url + '/lumiere/eteint/' + numero, {responseType: 'text'}).subscribe(console.log);
  }
  voletOn(numero: number): void {
    this.http.get(environment.url + '/volet/ouvre/' + numero, {responseType: 'text'}).subscribe(console.log);
  }
  voletOff(numero: number): void {
    this.http.get(environment.url + '/volet/ferme/' + numero, {responseType: 'text'}).subscribe(console.log);
  }

}
