import { Component } from '@angular/core';
import { AppService } from './app.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  locations: MyLocation[] = [];  // holds list of location data
  lat: number = 38.831554;
  lng: number = -77.312089;

  constructor(private service: AppService) {}

  ngOnInit() {
    this.locations = this.getLocations();
    console.log(this.locations)
  }

  getLocations(): MyLocation[] {
    // return [
    //   {latitude: 38.832229, longitude: -77.475889}, 
    //   {latitude: 38.831554, longitude: -77.312089}, 
    //   {latitude: 51.678418, longitude: 7.809007}
    // ];
    let value: MyLocation[];
    this.service.getLocations().subscribe(result => value = result);
    return value;
  }
}

export class MyLocation {
  latitude: number;
  longitude: number;
}
