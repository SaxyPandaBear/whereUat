import { Injectable } from "@angular/core";
import { Observable } from "rxjs/Observable";
import {of as observableOf} from 'rxjs/observable/of'; // for mocking responses
import { HttpClient } from "@angular/common/http";
import { GeolocationPayload } from "./models";

@Injectable()
export class AppService {
    private headers: Headers = new Headers({'Content-Type': 'application/json'});
    private url: string = '';

    constructor(private http: HttpClient) {}

    getLocations(): Observable<GeolocationPayload> {
        return this.http.get<GeolocationPayload>('http://localhost:5000/location');
    }
}
