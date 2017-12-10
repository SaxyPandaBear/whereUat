import { Component, OnInit, ViewChild } from '@angular/core';
import { AppService } from '../app.service';
import { IpInfo, IpInfoPayload } from '../models';
import { Observable } from 'rxjs/Observable';
import { MatTableDataSource, MatSort } from '@angular/material';
import { AfterViewInit } from '@angular/core/src/metadata/lifecycle_hooks';

@Component({
  selector: 'app-ips',
  templateUrl: './ips.component.html',
  styleUrls: ['./ips.component.css']
})
export class IpsComponent implements OnInit, AfterViewInit {
  private columns: string[] = ['ip', 'host', 'city', 'country', 'frequency'];
  private dataSource: MatTableDataSource<IpInfo>;
  private ipData$: Observable<IpInfoPayload>;

  @ViewChild(MatSort) sort: MatSort;

  constructor(private service: AppService) { }

  ngOnInit() {
    this.ipData$ = this.service.getIpInfo();
    this.ipData$.subscribe(data => {
      this.dataSource = new MatTableDataSource<IpInfo>(data.ips);
    });
  }

  ngAfterViewInit() {
    this.dataSource.sort = this.sort;
  }

}
