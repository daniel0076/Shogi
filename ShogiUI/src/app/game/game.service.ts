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

  surrender(userId: number) {
    const event = new SendWebSocketMessage({
      type: 'move',
      content: {
        type: 'surrender',
        content: userId
      }
    });
    console.log("surrender", event);
    this.store.dispatch(event);
  }

  exit() {
    const event = new SendWebSocketMessage({
      type: 'move',
      content: {
        type: 'exit'
      }
    });
    this.store.dispatch(event);
  }

  startHistoryGame(){
    const event = new SendWebSocketMessage({
      type: 'game',
      content: {
        type: 'record',
      }
    });
    this.store.dispatch(event);
  }

  startGame(gameType: string) {
    const event = new SendWebSocketMessage(
      {
        type: "game",
        content: {
          type: gameType
        }
      }
    );
    this.store.dispatch(event);

  }

}
