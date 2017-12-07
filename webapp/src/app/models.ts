export interface GeolocationPayload {
    locs: Geolocation[];
  }
  
export interface Geolocation {
    latitude: number;
    longitude: number;
}

export interface IpInfoPayload {
    ips: IpInfo[];
}

export interface IpInfo {
    ip: string;
    hostname: string;
    city: string;
    country: string;
    latitude: number;
    longitude: number;
    freq: number;
}
