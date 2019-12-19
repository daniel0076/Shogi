import { Component, OnInit, HostBinding, Input } from '@angular/core';
import { NzModalService } from 'ng-zorro-antd/modal';
import { NzMessageService } from 'ng-zorro-antd/message';
import { Piece } from '../shared/piece/piece.interface';
import { GameState, GameStateModel } from '../game/store/game.state';
import { Observable } from 'rxjs';
import { Select } from '@ngxs/store';
import { BoardService } from './board.service';
import { PieceState } from './board.interface';

import { trigger, state, style, animate, transition } from '@angular/animations';

@Component({
  selector: 'app-board',

//
	animations: [
		trigger('select', [
			state('unselected', style({
				opacity: 0.3
	  	})),
			state('selected', style({
				opacity: 1
			})),
			transition('unselected => selected, selected => unselected', [
			animate('0.5s')
			]),
		]),
	],	
//

  templateUrl: './board.component.html',
  styleUrls: ['./board.component.less']
})
export class BoardComponent implements OnInit {
  @Input() gameType: string;
  @Select(GameState.getGameState) gameState$: Observable<GameStateModel>;
  private turn: number
  private board: Piece[][] = [];
  private pieceState: PieceState = { selected: false, usi_position: "" };
  private validMove: Object = {};
  private secondPlayerHandPieces: Piece[] = [];
  private firstPlayerHandPieces: Piece[] = [];
  private territory: string[][] = [];

  private gameStateObserver = {
    next: gameState => { this.parseGameState(gameState); },
    error: err => console.error('Observer got an error: ' + err),
    complete: () => console.log('Observer got a complete notification'),
  };

  constructor(
    private boardService: BoardService,
    private modalService: NzModalService,
    private message: NzMessageService,
  ) { }

  ngOnInit() {
    this.gameState$.subscribe(this.gameStateObserver);
  }

  cellClicked(rowIndex: number, colIndex: number) {
	
		let table = <HTMLTableElement>document.getElementById('theTablee');
		console.log(table);
		//var theCell = <HTMLTableCellElement>table.rows[rowIndex].cells[colIndex];
		//theCell.style.setProperty( "background-color", "#FF0000" );
		//theCell.style.color = "#FF0000";
		//theCell.bgColor = 'black';


    // check valid move

    if (!this.pieceState.selected) {  // select source
      let pieceUSI = this.usi_encode(rowIndex, colIndex, this.turn);  // piece position in USI

      if (!this.validMove[pieceUSI]) {  // can't move this piece
        this.message.create('error', '那不是你的棋!');
        return;
      }

      this.pieceState.selected = true;
      this.pieceState.usi_position = pieceUSI;
    }
    else if (this.pieceState.selected) {  // select destination

      let sourceUSI = this.pieceState.usi_position;
      let destinationUSI = this.usi_encode(rowIndex, colIndex, this.turn);

      if (destinationUSI == sourceUSI) { // cancel select
        this.pieceState.selected = false;
        this.pieceState.usi_position = "";
        return
      }
      // check valid move
      for (let validPos of this.validMove[sourceUSI]) {
        let found: boolean = false;
        if (validPos.includes(destinationUSI)) {
          found = true;
          break;
        }
        this.message.create('error', '無法走到那');
        return;

      }

      let usi_move = sourceUSI + destinationUSI;
      // send
      this.boardService.movePiece(usi_move);
      //reset state
      this.pieceState.selected = false;
      this.pieceState.usi_position = "";
    }
  }

	highlightCell(event){
		console.log(event);
		if(this.pieceState.selected)
			event.toElement.style.backgroundColor = "#FF0000";
		else
			event.toElement.style.backgroundColor = "#000000";
	}

  handPieceClicked(piece: Piece) {
    // check valid move
    let pieceUSI = piece.symbol + "*";
    if (!this.pieceState.selected) {  // select source
      if (!this.validMove[pieceUSI]) {  // can't move this piece
        this.message.create('error', '不合規則');
        return;
      }
      this.pieceState.selected = true;
      this.pieceState.usi_position = pieceUSI;
    }
    else if (this.pieceState.selected) {  // select destination
      if (pieceUSI === this.pieceState.usi_position) {  // reset
        this.pieceState.selected = false;
        this.pieceState.usi_position = "";
      }
      return;
    }
  }

  parseGameState(gameState: GameStateModel) {
    console.log(gameState);
    if (gameState.turn != undefined && this.turn === undefined) {
      this.showModal('棋局開始', '');
    } else if (gameState.turn != this.turn) {
      this.showModal('玩家交換', '起手無回');
    }

    setTimeout(() => {
      if (this.gameType === 'single') {
        this.turn = 0;
      } else {
        this.turn = gameState.turn;
      }
      this.validMove = gameState.validMove;
      this.parseUSI(gameState.usi);
      this.parseTerritory(gameState.territory);
    }, 1000);
  }

  parseUSI(usi: string) {
    if (!usi) {
      return;
    }
    let usi_tokens: string[] = usi.split(' ');
    let board_state: string = usi_tokens[0];
    let handPieces: string = usi_tokens[2];
    this.parseHandPiece(handPieces);

    let rows: string[] = board_state.split('/')
    this.board = [];
    for (let row of rows) {
      this.board.push(this.parsePieces(row));
    }

    if (this.gameType != 'single') {
      // turn the side of board
      if (this.turn === 1) {
        this.board = this.board.reverse();
        for (let row of this.board) {
          row = row.reverse();
        }
      }
    }
  }

  parseHandPiece(usi: string) {
    this.firstPlayerHandPieces = []
    this.secondPlayerHandPieces = [];
    if (usi === '-') {
      return;
    }

    for (let token of usi) {
      let piece: Piece = { symbol: token };
      if (piece.symbol === piece.symbol.toLowerCase()) {
        this.secondPlayerHandPieces.push(piece);
      } else if (piece.symbol === piece.symbol.toUpperCase()) {
        this.firstPlayerHandPieces.push(piece);
      }
    }
  }
  parseTerritory(territory: string) {
    this.territory = [];
    let rows: string[] = territory.split('/');
    for (let row of rows) {
      let tmp_row = [];
      for (let token of row) {
        switch (token) {
          case 'W':
            tmp_row.push('white-side');
            break;
          case 'B':
            tmp_row.push('black-side');
            break;
          case 'G':
            tmp_row.push('neutral-side');
            break;

          default:
            break;
        }
      }
      this.territory.push(tmp_row);
    }
  }

  usi_encode(rowIndex: number, colIndex: number, turn: number): string {
    let reversed = turn ? true : false;
    let usi_position: string = "";
    if (!reversed) { // first hand
      let rowNote: string[] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'];
      usi_position = (9 - colIndex).toString() + rowNote[rowIndex];
    } else if (reversed) { // second hand
      let rowNote: string[] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'].reverse();
      usi_position = (colIndex + 1).toString() + rowNote[rowIndex];
    }
    return usi_position;
  }


  parsePieces(row: string): Piece[] {
    let pieces: Piece[] = [];
    let token: string;
    let i = 0;
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
