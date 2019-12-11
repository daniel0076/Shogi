import { Component, OnInit } from '@angular/core';
import { Store } from '@ngxs/store';
import { ConnectWebSocket } from '@ngxs/websocket-plugin';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.less']
})
export class AppComponent implements OnInit{
  constructor(
    private store: Store
  ) {}

  ngOnInit() {
    //this.store.dispatch(new ConnectWebSocket());
  }
}
