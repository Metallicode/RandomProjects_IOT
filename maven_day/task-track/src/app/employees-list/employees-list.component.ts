import { Component, OnInit } from '@angular/core';
import { Employee } from '../employee.model';
import { App_Manager } from '../app-manager.service';

@Component({
  selector: 'app-employees-list',
  templateUrl: './employees-list.component.html',
  styleUrls: ['./employees-list.component.css']
})
export class EmployeesListComponent implements OnInit {

  employees: Employee[];

  constructor(private appManager: App_Manager) { }

  ngOnInit() {
    this.employees = this.appManager.get_current_view();
  }


}
