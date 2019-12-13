import { Component, OnInit } from '@angular/core';
import { Store } from '@ngxs/store';
import { GameService } from './game.service';
import { Game } from './store/game.actions';

@Component({
  selector: 'app-game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.less']
})
export class GameComponent implements OnInit {

  constructor(private gameService: GameService) { }

  ngOnInit() {
  }

  reset() {
    this.gameService.reset();
  }

  turn() {
    this.gameService.turn();
  }

  move() {
  }

  hist() {
  }

}
