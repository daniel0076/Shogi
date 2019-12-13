import { Injectable } from '@angular/core';
import { Store } from '@ngxs/store';
import { Game } from './store/game.actions';
import { SendWebSocketMessage } from '@ngxs/websocket-plugin';

@Injectable({
  providedIn: 'root'
})
export class GameService {

  constructor(private store: Store) { }

  reset() {
    this.store.dispatch(new Game.ResetGame());
    this.store.dispatch(new Game.SetTurn(0));
  }

  turn() {
    this.store.dispatch(new Game.SetTurn(1));
  }

  move() {
    const event = new SendWebSocketMessage({
      type: 'move',
      content: {
        type: 'move',
        content: '9g9f#'
      }
    });
    this.store.dispatch(event);
  }

  hist() {
    const event = new SendWebSocketMessage({
      type: 'game',
      content: {
        type: 'record',
      }
    });
    this.store.dispatch(event);
  }

}
