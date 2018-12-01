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
  lumiere(numero: number): void {
    this.http.get(environment.url + '/lumiere/allume/' +numero).subscribe();
}

}
