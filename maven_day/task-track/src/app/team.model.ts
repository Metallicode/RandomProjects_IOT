export class Team {
  team_name: string;
  team_id: number;
  team_index: number;

  constructor(name:string, id:number, index:number) {
    this.team_name = name;
    this.team_id = id;
    this.team_index = index;
  }

}
