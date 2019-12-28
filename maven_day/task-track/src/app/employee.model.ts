export class Employee {

  First_name: string;
  Last_name: string;
  Emp_id: number;
  Team_id: number;

  constructor(fname: string, lname: string, empid: number, Team_id:number) {
    this.First_name = fname;
    this.Last_name = lname;
    this.Emp_id = empid;
    this.Team_id = Team_id;
  }

}
