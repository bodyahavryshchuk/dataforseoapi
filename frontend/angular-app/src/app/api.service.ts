import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

import { Task, TaskData, TaskResult } from './task';
import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  API_URL = environment.apiUrl;

  constructor(private http: HttpClient) { }

  public getTasks(): Observable<Task[]> {
    return this.http.get<Task[]>(`${this.API_URL}/task-list/`,
            {});
  }
  public getTaskData(): Observable<TaskData[]> {
    return this.http.get<TaskData[]>(`${this.API_URL}/task/data/`,
            {});
  }

  // Create a Task.
  public postTask(new_task: Task) {
    return this.http.post(`${this.API_URL}/task/`,new_task,
            {
            });
  }


  public getTaskResult(se: string, pk: string): Observable<TaskResult[]> {
      return this.http.get<TaskResult[]>(`${this.API_URL}/task/result/${se}/${pk}/`,
              {
              });
    }
}
