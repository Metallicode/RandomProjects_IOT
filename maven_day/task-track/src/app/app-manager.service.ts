import { Employee } from './employee.model';
import { Task } from './task.model';
import { Team } from './team.model';
import { Api_Layer } from './api-layer.service';
import { OnInit, Injectable } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class App_Manager {

  all_employees: Employee[];
  all_tasks: Task[];
  all_teams: Team[];

  current_view: Employee[];
  time_frame: number;


  constructor(private api_layer: Api_Layer) {
    console.log("App_Manager started");

    this.time_frame =5;

    this.all_employees = this.api_layer.get_employees();
    this.all_tasks = this.api_layer.get_tasks();
    this.all_teams = this.api_layer.get_teams();

    this.current_view = [...this.all_employees];

    console.log("manager constructor");
    console.log(this.all_employees);

    this.current_view.sort((a, b) => a.Team_id - b.Team_id);
  }

  get_current_view() {

    return this.current_view;
  }

  get_all_teams() {

    return this.all_teams;
  }

  set_emp_list(data: { team_id: number, action: boolean }) {

    var employeesarr= [];

    for (var i = 0; i < this.all_employees.length; i++) {
      if (this.all_employees[i].Team_id === data.team_id) {
        employeesarr.push(this.all_employees[i]);
      }
    }

    if (data.action === true) {
      this.add_emp_to_view(employeesarr);
    } else {
      this.remove_emp_from_view(employeesarr);
    }

  }


  add_emp_to_view(employees: Employee[]) {
    for (var i = 0; i < employees.length; i++) {
      this.current_view.push(employees[i]);
    }

    this.current_view.sort((a, b) => a.Team_id - b.Team_id);

  }

  remove_emp_from_view(employees: Employee[]) {
    console.log("removing from emp arry");
    for (var i = 0; i < this.current_view.length; i++) {
      for (var j = 0; j < employees.length; j++) {
        if (employees[j].Emp_id === this.current_view[i].Emp_id) {
          this.current_view.splice(this.current_view.indexOf(this.current_view[i]), 1);
        }
      }
    }


    this.current_view.sort((a, b) => a.Team_id - b.Team_id);

  }

}
