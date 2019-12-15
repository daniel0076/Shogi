import { Injectable } from '@angular/core';
import { Store } from '@ngxs/store';
import { SendWebSocketMessage } from '@ngxs/websocket-plugin';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private store: Store) { }

  register(userInfo): void {
    const event = new SendWebSocketMessage(
      {
        type: "register",
        content: {
          username: userInfo.userName,
          password: userInfo.password
        }
      }
    );
    this.store.dispatch(event);
  }

  login(userInfo): void {
    const event = new SendWebSocketMessage(
      {
        type: "login",
        content: {
          username: userInfo.userName,
          password: userInfo.password
        }
      }
    );
    this.store.dispatch(event);
  }
}
