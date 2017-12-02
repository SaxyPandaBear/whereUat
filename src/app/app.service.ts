import { Injectable } from "@angular/core";
import { MyLocation } from "./app.component";
import { Observable } from "rxjs/Observable";
import {of as observableOf} from 'rxjs/observable/of';
import { HttpClient } from "selenium-webdriver/http";

@Injectable()
export class AppService {
    private headers: Headers = new Headers({'Content-Type': 'application/json'});
    private url: string = '';

    constructor(private http: HttpClient) {}

    getLocations(): Observable<MyLocation[]> {
        return observableOf([
            {latitude: 38.832229, longitude: -77.475889}, 
            {latitude: 38.831554, longitude: -77.312089}, 
            {latitude: 51.678418, longitude: 7.809007}
          ]);
    }
}