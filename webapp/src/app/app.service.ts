import { Injectable } from "@angular/core";
import { Observable } from "rxjs/Observable";
import {of as observableOf} from 'rxjs/observable/of'; // for mocking responses
import { HttpClient } from "@angular/common/http";
import { GeolocationPayload, Geolocation, IpInfo, IpInfoPayload } from "./models";

@Injectable()
export class AppService {
    private headers: Headers = new Headers({'Content-Type': 'application/json'});

    constructor(private http: HttpClient) {}

    public getLocations(): Observable<GeolocationPayload> {
        return observableOf({locs: this.getStaticLocation()});
        // return this.http.get<GeolocationPayload>('http://localhost:5000/location');
    }

    public getIpInfo(): Observable<IpInfoPayload> {
        return observableOf({ips: this.getStaticIpInfo()});
        // return this.http.get<IpInfoPayload>('http://localhost:5000/ip');
    }

    /**
     * Placeholder data
     */
    private getStaticLocation(): Geolocation[] {
        return [
            {latitude: 38.831554, longitude: -77.312089},
            {latitude: 39.001234, longitude: -76.567890},
            {latitude: 35.998573, longitude: -80.123456}
        ];
    }

    /**
     * Placeholder data
     */
    private getStaticIpInfo(): IpInfo[] {
        return [
            {
                ip: '1.1.1.1',
                hostname: 'www.gmu.edu',
                city: 'Fairfax',
                country: 'US', 
                latitude: 38.831554, 
                longitude: -77.312089, 
                freq: 1
            },
            {
                ip: '2.2.2.2',
                hostname: 'nsa.gov',
                city: 'Somewhere',
                country: 'Somehow',
                latitude: 35.00,
                longitude: 35.00,
                freq: 250
            }
        ];
    }
}
