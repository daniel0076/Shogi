import { Component, OnInit } from '@angular/core';
import { Piece } from '../shared/piece/piece.interface';
import { GameState } from '../game/store/game.state';
import { Observable } from 'rxjs';
import { Select } from '@ngxs/store';

@Component({
  selector: 'app-board',
  templateUrl: './board.component.html',
  styleUrls: ['./board.component.less']
})
export class BoardComponent implements OnInit {
  @Select(GameState.getUSI) usi$: Observable<string[]>;
  @Select(GameState.getTurn) turn$: Observable<number>;
  private usi: string;
  private myTurn: number;
  private board: Piece[][] = [];
  private usiObserver = {
    next: usi => { this.usi = usi; this.parseUSI(usi); },
    error: err => console.error('Observer got an error: ' + err),
    complete: () => console.log('Observer got a complete notification'),
  };
  private turnObserver = {
    next: turn => { this.myTurn = turn; this.parseUSI(this.usi) },
    error: err => console.error('Observer got an error: ' + err),
    complete: () => console.log('Observer got a complete notification'),
  };


  constructor() { }

  ngOnInit() {
    this.usi$.subscribe(this.usiObserver);
    this.turn$.subscribe(this.turnObserver);
  }

  parseUSI(usi: string){
    if (!usi) {
      return;
    }
    let usi_tokens: string[] = usi.split(' ');
    let board_state: string = usi_tokens[0];
    let rows: string[] = board_state.split('/')

    this.board = [];
    for(let row of rows){
      this.board.push(this.parsePieces(row));
    }

    if (this.myTurn === 1) {
      this.board = this.board.reverse();
      for (let row of this.board) {
        row = row.reverse();
      }
    }
  }

  parsePieces(row: string): Piece[] {
    let pieces: Piece[] = [];
    let token: string;
    let i= 0;
    while (i < row.length) {
      let piece: Piece = { 'symbol': '' };
      token = row[i];
      if (!isNaN(Number(token))) { // isdigit
        piece.symbol = "";
        for (let i = 0; i < Number(token); i++) {
          pieces.push(piece);
        }
      } else if (token === '+') {
        i += 1;
        token += row[i];
        piece.symbol = token;
        pieces.push(piece);
      } else {
        piece.symbol = token;
        pieces.push(piece);
      }
      i++;
    }

    return pieces;
  }

}
