import { Injectable } from '@angular/core';
import { Store } from '@ngxs/store';
import { SendWebSocketMessage } from '@ngxs/websocket-plugin';

@Injectable({
  providedIn: 'root'
})
export class BoardService {

  constructor(private store: Store) { }

  movePiece(usi_move: string) {
    console.log(usi_move)
    const event = new SendWebSocketMessage({
      type: 'move',
      content: {
        type: 'move',
        content: usi_move
      }
    });
    this.store.dispatch(event);
  }
}
