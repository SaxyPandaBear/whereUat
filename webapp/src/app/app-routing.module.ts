import { NgModule } from '@angular/core'
import { RouterModule, Routes } from '@angular/router'
import { MapComponent } from './map/map.component';
import { IpsComponent } from './ips/ips.component';

const appRoutes: Routes = [
    { path: 'map', component:  MapComponent},
    { path: '',   redirectTo: 'map', pathMatch: 'full' },
    { path: 'ips', component: IpsComponent },
    { path: '**', redirectTo: 'map' }
  ];

@NgModule({
    imports: [
      RouterModule.forRoot(
        appRoutes
        // appRoutes,
        // { enableTracing: true } // <-- debugging purposes only
      )
    ],
    exports: [
      RouterModule
    ]
  })
  export class AppRoutingModule {}