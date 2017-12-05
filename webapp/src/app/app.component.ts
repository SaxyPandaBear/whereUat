import { Component } from '@angular/core';
import { AppService } from './app.service';
import { Observable } from 'rxjs/Observable';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  locations$: Observable<Payload>;
  lat: number = 38.831554;
  lng: number = -77.312089;
  locations: MyLocation[] = [];

  constructor(private service: AppService) {}

  ngOnInit() {
    this.locations$ = this.service.getLocations();
    this.locations$.subscribe(data => {
      this.locations = data.locs;
    });
  }
}

export class Payload {
  locs: MyLocation[];
}

export class MyLocation {
  latitude: number;
  longitude: number;
}
