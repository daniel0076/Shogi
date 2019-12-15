import { Component, OnInit } from '@angular/core';
import { GameService } from './game.service';

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

  startGame(gameType){
    this.gameService.startGame(gameType);
  }
}
