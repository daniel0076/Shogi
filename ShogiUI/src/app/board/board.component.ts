import { Component, OnInit } from '@angular/core';
import { NzModalService } from 'ng-zorro-antd/modal';
import { Piece } from '../shared/piece/piece.interface';
import { GameState, GameStateModel } from '../game/store/game.state';
import { Observable } from 'rxjs';
import { Select } from '@ngxs/store';
import { BoardService } from './board.service';
import { PieceState } from './board.interface';

@Component({
  selector: 'app-board',
  templateUrl: './board.component.html',
  styleUrls: ['./board.component.less']
})
export class BoardComponent implements OnInit {
  @Select(GameState.getGameState) gameState$: Observable<GameStateModel>;
  private turn: number
  private board: Piece[][] = [];
  private pieceState: PieceState = { selected: false, usi_position: "" };

  private gameStateObserver = {
    next: gameState => { this.parseGameState(gameState); },
    error: err => console.error('Observer got an error: ' + err),
    complete: () => console.log('Observer got a complete notification'),
  };

constructor(private boardService: BoardService, private modalService: NzModalService) { }

  ngOnInit() {
    this.gameState$.subscribe(this.gameStateObserver);
  }

  cellClicked(rowIndex: number, colIndex: number) {
    if(this.pieceState.selected){
      // check valid move
      let usi_move = this.pieceState.usi_position;
      usi_move += this.usi_encode(rowIndex, colIndex);
      // send
      this.boardService.movePiece(usi_move);
      //reset state
      this.pieceState.selected = false;
      this.pieceState.usi_position = "";
    } else {
      this.pieceState.selected = true;
      this.pieceState.usi_position = this.usi_encode(rowIndex, colIndex);
    }
  }

  parseGameState(gameState: GameStateModel) {
    if(this.turn === undefined){
      this.showModal('棋局開始', '');
    } else {
      this.showModal('玩家交換', '起手無回');
    }
    this.turn = gameState.turn;
    this.parseUSI(gameState.usi);
  }

  parseUSI(usi: string){
    console.log(usi);
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

    if (this.turn === 1) {  // for opposite player
      this.board = this.board.reverse();
      for (let row of this.board) {
        row = row.reverse();
      }
    }
  }

  usi_encode(rowIndex: number, colIndex: number): string {
    let usi_position: string = "";
    if (this.turn === 0) { // first hand
      let rowNote: string[] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'];
      usi_position = (9 - colIndex).toString() + rowNote[rowIndex];
    } else if (this.turn === 1) { // second hand
      let rowNote: string[] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'].reverse();
      usi_position = (colIndex + 1).toString() + rowNote[rowIndex];
    }
    return usi_position;
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

  showModal(title: string, content: string): void {
    const modal = this.modalService.create({
      nzTitle: title,
      nzFooter: null,
      nzContent: content
    });

    setTimeout(() => modal.destroy(), 1000);
  }

}
