import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { BoardComponent } from './board/board.component';
import { AuthComponent } from './core/auth/auth.component';
import { WelcomeComponent } from './welcome/welcome.component';

const routes: Routes = [
  {
    path: 'index',
    component: WelcomeComponent
  },
  {
    path: 'board',
    component: BoardComponent
  },
  {
    path: '',
    redirectTo: '/index',
    pathMatch: 'full'
  }

];

@NgModule({
  imports: [RouterModule.forRoot(routes, { useHash: true })],
  exports: [RouterModule]
})
export class AppRoutingModule { }
