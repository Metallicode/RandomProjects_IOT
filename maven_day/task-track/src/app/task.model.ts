export class Task {

  task_title: string;
  task_id: number;
  task_start: Date;
  emp_id: number;
  task_length: number;

  constructor(title:string, id:number, start_date: Date, empid: number, lenght:number ) {
    this.task_title = title;
    this.task_id = id;
    this.task_start = start_date;
    this.emp_id = empid;
    this.task_length = lenght;
  }      

}
