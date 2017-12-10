import { BrowserModule } from '@angular/platform-browser';
import { NgModule, ApplicationRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { AppComponent } from './app.component';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';

import { AgmCoreModule } from '@agm/core';
import { AppService } from './app.service';
import {HttpClientModule} from '@angular/common/http';
import { MapComponent } from './map/map.component';

import { MatToolbarModule, MatButtonModule, MatTableModule, MatPaginatorModule, MatSortModule } from '@angular/material'
import { AppRoutingModule } from './app-routing.module';
import { AboutComponent } from './about/about.component';
import { IpsComponent } from './ips/ips.component';

@NgModule({
  imports: [
    AppRoutingModule,
    BrowserModule,
    BrowserAnimationsModule,
    CommonModule,
    FormsModule,
    HttpClientModule,
    AgmCoreModule.forRoot({
      apiKey: 'AIzaSyD62ElwFqHAUNCbdvTU0sHVKUifpVHKwWE'
    }),
    // Angular Material imports
    MatToolbarModule,
    MatButtonModule,
    MatTableModule,
    MatPaginatorModule,
    MatSortModule
  ],
  providers: [ AppService ],
  declarations: [ AppComponent, MapComponent, AboutComponent, IpsComponent ],
  bootstrap: [ AppComponent ]
})
export class AppModule {}
