import { Component } from '@angular/core';
import { App_Manager } from "./app-manager.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'task-track';

  constructor(private app_manager: App_Manager) {}

  teams_changed(data: any) {

    this.app_manager.set_emp_list(data);

  }



}
