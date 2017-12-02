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
    let value: MyLocation[];
    this.service.getLocations().subscribe(result => value = result);
    return value;
  }
}

export class MyLocation {
  latitude: number;
  longitude: number;
}
