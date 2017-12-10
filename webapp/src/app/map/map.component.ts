import { Component, OnInit } from '@angular/core';
import { AppService } from '../app.service';
import { Observable } from 'rxjs/Observable';
import { GeolocationPayload, Geolocation } from '../models';

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit {
  locations$: Observable<GeolocationPayload>;
  // lat, lng coordinates point to GMU Fairfax campus
  lat: number = 38.831554;
  lng: number = -77.312089;
  locations: Geolocation[] = [];

  constructor(private service: AppService) {}

  ngOnInit() {
    this.locations$ = this.service.getLocations();
    this.locations$.subscribe(data => {
      this.locations = data.locs;
    });
  }
}
