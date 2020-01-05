import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { Team } from '../team.model';
import { App_Manager } from '../app-manager.service';


@Component({
  selector: 'app-team-filter',
  templateUrl: './team-filter.component.html',
  styleUrls: ['./team-filter.component.css']
})
export class TeamFilterComponent implements OnInit {

  teams: Team[];
  @Output() teams_filter_changed = new EventEmitter<{ team_id: number, action: boolean }>();


  constructor(private appManager: App_Manager) { }

  ngOnInit() {
    this.teams = this.appManager.all_teams;
  }

  checkbox_changed(e: Event) {
    console.log((<HTMLInputElement>e.target).checked);
    console.log((<HTMLInputElement>e.target).value);

    this.teams_filter_changed.emit({ team_id: +(<HTMLInputElement>e.target).value, action: (<HTMLInputElement>e.target).checked});

  }


}
