import { Component } from '@angular/core';
import { Log, LogApi } from '../log-api';
import { MatTableDataSource, MatTableModule } from '@angular/material/table';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatSortModule } from '@angular/material/sort';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-log-table',
    imports: [
    CommonModule,
    MatTableModule,
    MatPaginatorModule,
    MatSortModule,
  ],
  standalone: true,
  templateUrl: './log-table.html',
  styleUrl: './log-table.css',
})
export class LogTable {

  dataSource = new MatTableDataSource<Log>();
  displayedColumns: string[] = ['logged_at', 'ip', 'message', 'level'];

  constructor(private logApi:LogApi) {}

  ngOnInit() {
    this.logApi.getLogs().subscribe(logs => 
      this.dataSource.data = logs
    )
  }

}
