import { Injectable } from "@angular/core";
import { Observable } from "rxjs/Observable";
import {of as observableOf} from 'rxjs/observable/of'; // for mocking responses
import { HttpClient } from "@angular/common/http";
import { GeolocationPayload, Geolocation, IpInfo, IpInfoPayload } from "./models";

@Injectable()
export class AppService {
    private headers: Headers = new Headers({'Content-Type': 'application/json'});
    private url: string = '';

    constructor(private http: HttpClient) {}

    public getLocations(): Observable<GeolocationPayload> {
        return observableOf({locs: this.getStaticLocation()});
        // return this.http.get<GeolocationPayload>('http://localhost:5000/location');
    }

    public getIpInfo(): Observable<IpInfoPayload> {
        return observableOf({ips: this.getStaticIpInfo()});
        // return this.http.get<IpInfoPayload>('http://localhost:5000/ip');
    }

    private getStaticLocation(): Geolocation[] {
        return [
            {latitude: 38.831554, longitude: -77.312089}
        ];
    }

    private getStaticIpInfo(): IpInfo[] {
        return [
            {
                ip:'1.1.1.1',
                hostname:'www.gmu.edu',
                city:'Fairfax',
                country:'US', 
                latitude:38.831554, 
                longitude:-77.312089, 
                freq:1
            }
        ];
    }
}
