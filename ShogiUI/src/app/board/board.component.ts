import { Component, OnInit } from '@angular/core';
import { Piece } from '../shared/piece/piece.interface';

@Component({
  selector: 'app-board',
  templateUrl: './board.component.html',
  styleUrls: ['./board.component.less']
})
export class BoardComponent implements OnInit {
  private board: Piece[][] = [
    [{ 'symbol': 'K', 'color': 'b' }],
    [{ 'symbol': 'R', 'color': 'b' }],
  ]

  constructor() { }

  ngOnInit() {
  }

  parseUSI(usi: string){
    let usi_tokens: string[] = usi.split(' ');
    let board_state: string = usi[0];

    let rows: string[] = board_state.split('/')
    for(let row of rows){
      this.parsePieces(row);
    }

  }
  parsePieces(row: string) {
    let pieces: string[];
    let i= 0
    let token: string;
    while (i < row.length) {
      token = pieces[i];
      if (!isNaN(Number(token))) { // isdigit
        for (let i = 0; i < Number(token); i++) {
          pieces.push(null);
        }
      } else if (token === '+') {
        i += 1;
        token += pieces[i];
        pieces.push(token);
      } else {
        pieces.push(token);
      }
      i++;
    }

  }

}
