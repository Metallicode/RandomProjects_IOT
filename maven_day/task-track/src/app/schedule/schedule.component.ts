import { Component, OnInit } from '@angular/core';
import { App_Manager } from '../app-manager.service';
import { Employee } from '../employee.model';

@Component({
  selector: 'app-schedule',
  templateUrl: './schedule.component.html',
  styleUrls: ['./schedule.component.css']
})
export class ScheduleComponent implements OnInit {

  current_emp_view: Employee[];
  schedule_timeframe: number;
  schedule_dates: Date[];

  constructor(private appManager: App_Manager) { }

  ngOnInit() {

    this.current_emp_view = this.appManager.current_view;
    this.schedule_timeframe = this.appManager.time_frame;

  }

  get_dates(start_date: Date = new Date()): Date[]  {

    var weekend_days_counter = 0;
    this.schedule_dates = [];

    for (var i = 0; i < this.schedule_timeframe; i++) {
      var date = new Date(start_date);
      var calculated_date = new Date(date.setDate(date.getDate()+i));

      if (!(calculated_date.getDay() === 6 || calculated_date.getDay() === 0)) {
        this.schedule_dates.push(calculated_date);
      } else {
        weekend_days_counter++;
      }
   
    }
    if (weekend_days_counter > 0) {

      for (var i = 0; i < weekend_days_counter; i++) {
        var date = new Date(start_date);
        var calculated_date = new Date(date.setDate(date.getDate() + this.schedule_timeframe + weekend_days_counter + i));
        this.schedule_dates.push(calculated_date);
      }
    }
    return this.schedule_dates;
  }

}
