import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

export interface Log {
  message: string;
  level: string;
  ip: string;
  logged_at: string;
}

@Injectable({
  providedIn: 'root',
})
export class LogApi {
  constructor(private http: HttpClient) { }

  getLogs() {
    return this.http.get<Log[]>('http://localhost:8000/logs')
  }
}
