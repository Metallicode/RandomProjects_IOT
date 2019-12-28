import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { Api_Layer } from './api-layer.service';
import { App_Manager } from './app-manager.service';

import { AppComponent } from './app.component';
import { TeamFilterComponent } from './team-filter/team-filter.component';
import { EmployeesListComponent } from './employees-list/employees-list.component';
import { ScheduleComponent } from './schedule/schedule.component';
import { EmployeeScheduleComponent } from './schedule/employee-schedule/employee-schedule.component';

@NgModule({
  declarations: [
    AppComponent,
    TeamFilterComponent,
    EmployeesListComponent,
    ScheduleComponent,
    EmployeeScheduleComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [Api_Layer, App_Manager],
  bootstrap: [AppComponent]
})
export class AppModule { }
