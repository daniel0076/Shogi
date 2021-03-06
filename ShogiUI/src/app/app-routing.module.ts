import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { GameComponent } from './game/game.component';
import { AuthComponent } from './core/auth/auth.component';
import { WelcomeComponent } from './welcome/welcome.component';
import { SelectComponent } from './select/select.component';

const routes: Routes = [
  {
    path: 'index',
    component: WelcomeComponent
  },
  {
    path: 'game',
    component: GameComponent
  },
  {
    path: 'select',
    component: SelectComponent 
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
