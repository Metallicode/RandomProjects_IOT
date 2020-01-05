import { Component, OnInit } from '@angular/core';
import { App_Manager } from 'src/app/app-manager.service';
import { Employee } from 'src/app/employee.model';

@Component({
  selector: 'app-employee-schedule',
  templateUrl: './employee-schedule.component.html',
  styleUrls: ['./employee-schedule.component.css']
})
export class EmployeeScheduleComponent implements OnInit {

  employees: Employee[]; 

  constructor(private appManager: App_Manager) { }

  ngOnInit() {

    this.employees = this.appManager.current_view;
  }

}
