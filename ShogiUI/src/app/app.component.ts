import { Component, OnInit, HostBinding } from '@angular/core';
import { Store } from '@ngxs/store';
import { ConnectWebSocket } from '@ngxs/websocket-plugin';

//import { Component, HostBinding } from '@angular/core';
import { trigger, state, style, animate, transition } from '@angular/animations';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.less'],
  animations: [
	// animation triggers go here
  ]
})
export class AppComponent implements OnInit{
  constructor(
    private store: Store
  ) {}

  ngOnInit() {
    this.store.dispatch(new ConnectWebSocket());
  }
}
