import { Component, OnInit } from '@angular/core';
import { Store } from '@ngxs/store';
import { Game } from './store/game.actions';

@Component({
  selector: 'app-game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.less']
})
export class GameComponent implements OnInit {

  constructor(private store: Store) { }

  ngOnInit() {
  }

  reset() {
    this.store.dispatch(new Game.ResetGame());
    this.store.dispatch(new Game.SetTurn(0));
  }

  turn() {
    this.store.dispatch(new Game.SetTurn(1));
  }

}
