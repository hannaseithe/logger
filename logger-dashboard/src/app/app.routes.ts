import { Routes } from '@angular/router';
import { LogTable } from './log-table/log-table';

export const routes: Routes = [
  { path: 'logs', component: LogTable },
  { path: '', redirectTo: '/logs', pathMatch: 'full' }
];
