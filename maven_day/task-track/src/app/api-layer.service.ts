import { Employee } from './employee.model';
import { Team } from './team.model';
import { Task } from './task.model';
import { OnInit, Injectable } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class Api_Layer {


  mock_tasks = {
    tasks: []
  };

  mock_work_data = {
    employees: [],
    teams: []
  };

  constructor() {

    console.log("Api_Layer started");
    this.create_mock_data();
  }

  create_mock_data() {

    //create mock emp...
    for (var i = 0; i < 10; i++) {
      this.mock_work_data.employees.push(new Employee(
        "f_name " + i,
        "l_name " + i,
      i,i%6));
    }

    //create mock teams...
    for (var i = 0; i < 6; i++) {
      this.mock_work_data.teams.push(new Team("temName "+i,i,i));
    }

    //create mock tasks...

    this.mock_tasks.tasks.push(new Task("task_title01", 1, new Date(), 1, 0));
    this.mock_tasks.tasks.push(new Task("task_title02", 2, new Date(), 2, 1));
    this.mock_tasks.tasks.push(new Task("task_title03", 3, new Date(), 3, 2));

  }


  get_tasks() {
    return this.mock_tasks.tasks;
  }

  get_employees() {



    return this.mock_work_data.employees;
  }

  get_teams() {
    return this.mock_work_data.teams;
  }

}
