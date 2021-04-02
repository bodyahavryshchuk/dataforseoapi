import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';

import { ApiService } from '../api.service';
import { Task, TaskData, TaskResult } from '../task';

@Component({
  selector: 'app-task-list',
  templateUrl: './task-list.component.html',
  styleUrls: ['./task-list.component.css']
})
export class TaskListComponent implements OnInit {
  tasks$: Observable<Task[]>;
  taskdata$: Observable<TaskData[]>;
  taskresult$: Observable<TaskResult[]>;
  task_form: FormGroup;

  constructor(private apiService: ApiService, private form_builder: FormBuilder) { }

  ngOnInit() {
    this.getTasks();
    this.getTaskData();

    this.task_form = this.form_builder.group({
      engine: '',
      location: '',
      keyword: '',
    });


    // Set validators for fields.
    this.task_form.controls["engine"].setValidators([Validators.required]);
    this.task_form.controls["location"].setValidators([Validators.required]);
    this.task_form.controls["keyword"].setValidators([Validators.required]);
  }

  public getTasks() {
    this.tasks$ = this.apiService.getTasks();
  }

  public getTaskData() {
    this.taskdata$ = this.apiService.getTaskData();
  }

  public getTaskResult(se: string, pk: string) {
    this.taskresult$ = this.apiService.getTaskResult(se, pk);
  }

  onSubmit() {
    // Create the Task.
    this.apiService.postTask(this.task_form.value)
      .subscribe(
        (response) => {
          console.log(response);
          this.getTasks();
        }
      )
  }

  getResult(se: string, pk: string) {
    this.apiService.getTaskResult(se, pk)
      .subscribe(
        (response) => {
          console.log(response);
          this.getTaskResult(se, pk);
        }
      )
  }

}
