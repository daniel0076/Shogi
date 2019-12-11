import { Component, OnInit } from '@angular/core';
import { Store } from '@ngxs/store';
import { Game } from './store/game.actions';
import { SendWebSocketMessage } from '@ngxs/websocket-plugin';

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

  move() {
    const event = new SendWebSocketMessage({
      type: 'move',
      content: {
        type: 'move',
        content: '9g9f#'
      }
    });
    this.store.dispatch(event);
    console.log("fired");
  }

  move2() {
    const event = new SendWebSocketMessage({
      type: 'move',
      content: {
        type: 'move',
        content: '5c5d'
      }
    });
    this.store.dispatch(event);
    console.log("fired");
  }

  hist() {
    const event = new SendWebSocketMessage({
      type: 'game',
      content: {
        type: 'record',
      }
    });
    this.store.dispatch(event);
    console.log("fired");
  }

}
