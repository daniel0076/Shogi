import { Component, OnInit, HostBinding, Input } from '@angular/core';
import { NzModalService } from 'ng-zorro-antd/modal';
import { NzMessageService } from 'ng-zorro-antd/message';
import { Piece } from '../shared/piece/piece.interface';
import { GameState, GameStateModel } from '../game/store/game.state';
import { GameService } from '../game/game.service';
import { Observable, Subscription } from 'rxjs';
import { Select } from '@ngxs/store';
import { BoardService } from './board.service';
import { PieceState } from './board.interface';
import { Router } from "@angular/router"
import { SettingState, SettingStateModel } from '../setting/store/setting.state';
import { SettingResponse } from '../setting/setting.interface';

import { trigger, state, style, animate, transition } from '@angular/animations';

@Component({
  selector: 'app-board',
  templateUrl: './board.component.html',
  styleUrls: ['./board.component.less']
})
export class BoardComponent implements OnInit {
  @Select(GameState.getGameState) gameState$: Observable<GameStateModel>;
  @Select(SettingState.getSettingResponse) settingState$: Observable<SettingResponse>;
  private gameStateSubscription: Subscription = null;
  private settingStateSubscription: Subscription = null;
  private gameType: string = null;
  private turn: number
  private board: Piece[][] = [];
  private pieceState: PieceState = { selected: false, usi_position: "" };
  private validMove: Object = {};
  private secondPlayerHandPieces: Piece[] = [];
  private firstPlayerHandPieces: Piece[] = [];
  private territory: string[][] = [];
	private checkmater: string[][] = [];
  private validCell: string[][] = [];
  private ori_territory: string = "";
	private ori_checkmater: string = "";
  terrVisible = true;
  constructor(
    private boardService: BoardService,
    private modalService: NzModalService,
    private message: NzMessageService,
    private router: Router,
    private gameService: GameService,
  ) { }

  ngOnInit() {
    if (!this.gameStateSubscription) {
      console.log("Subscribe");
      this.gameStateSubscription = this.gameState$.subscribe(this.gameStateObserver);
    }
    if (!this.settingStateSubscription) {
      console.log("Subscribe");
      this.settingStateSubscription = this.settingState$.subscribe(this.settingResponseObserver);
    }
  }
  ngOnDestroy() {

    this.gameStateSubscription.unsubscribe();
    this.settingStateSubscription.unsubscribe();
  }

  private gameStateObserver = {
    next: gameState => { this.parseGameState(gameState); },
    error: err => console.error('Observer got an error: ' + err),
    complete: () => console.log('Observer got a complete notification'),
  };

   private settingResponseObserver = {
        next: settingResponse => {
            if(!settingResponse){
                return ;
            }
            console.log(settingResponse);
            if(settingResponse.show_terr != null){
                this.terrVisible = settingResponse.show_terr;
            }
        },
        error: err => console.error('Observer got an error: ' + err),
        complete: () => console.log('Observer got a complete notification')

    };


  cellClicked(rowIndex: number, colIndex: number) {

    let original_territory: string[][] = this.territory;

    // check valid move

    if (!this.pieceState.selected) {  // select source
      let pieceUSI = this.usi_encode(rowIndex, colIndex, this.turn);  // piece position in USI

      if (!this.validMove[pieceUSI]) {  // can't move this piece
        this.message.create('error', '你不能動這顆棋!');
        return;
      }


      this.validCell = [];
      for (let i = 0; i < 9; ++i) {
        let tmp_row = [];
        for (let j = 0; j < 9; ++j) {
          tmp_row.push('N');
        }
        this.validCell.push(tmp_row);
      }

      let x: string = "";
      let valid_pos: number[] = [];
      for (x of this.validMove[pieceUSI]) {
        //console.log(x);
        valid_pos = this.usi_decode(x, this.turn);

        this.validCell[valid_pos[0]][valid_pos[1]] = 'V';

        //		console.log(valid_pos[0]);
        //	console.log(valid_pos[1]);

        //console.log(this.validCell);
      }

      for (let i = 0; i < 9; ++i) {
        for (let j = 0; j < 9; ++j) {
          if (this.validCell[i][j] == 'V') {
            if(	this.territory[i][j] == "checkmating_first" ||
								this.territory[i][j] == "checkmating_second"	) this.territory[i][j] = 'valid-checkmating';
						else this.territory[i][j] = 'valid';
          }
        }
      }
      //console.log(this.territory);



      this.pieceState.selected = true;
      this.pieceState.usi_position = pieceUSI;
      this.selectPiece(rowIndex, colIndex, true);
    }
    else if (this.pieceState.selected) {  // select destination

      let sourceUSI = this.pieceState.usi_position;
      let destinationUSI = this.usi_encode(rowIndex, colIndex, this.turn);

      if (destinationUSI == sourceUSI) { // cancel select
        this.pieceState.selected = false;
        this.pieceState.usi_position = "";
        this.selectPiece(rowIndex, colIndex, false);
        //this.territory = original_territory;
        this.parseTerritory(this.ori_territory, this.turn);
		//console.log("ter="+this.territory);
				this.parseCheckmater(this.ori_checkmater, this.turn)
		//console.log("che="+this.checkmater);
        return
      }
      // check valid move
      let found: boolean = false;
      let validPos: string = "";
      for (validPos of this.validMove[sourceUSI]) {
        if (validPos.includes(destinationUSI)) {
          found = true;
          break;
        }
      }
      if (!found) {
        this.message.create('error', '無法走到那');
        return;
      }

      let usi_move = sourceUSI + destinationUSI;

      // check promotion
      if (validPos.includes('+')) {  // can promote
        let timer: any = undefined;

        const modal = this.modalService.confirm({
          nzTitle: "昇變",
          nzContent: "是否要昇變?",
          //nzOnOk: () => {this.promoteResponse = true},
          nzOnOk: () => {
            usi_move += "+";
            this.boardService.movePiece(usi_move);
            clearTimeout(timer);
            modal.destroy()
          },
          nzOnCancel: () => {
            this.boardService.movePiece(usi_move);
            clearTimeout(timer);
            modal.destroy()
          }
        });

        timer = setTimeout(() => {
          // no promote on default timeout
          this.boardService.movePiece(usi_move);
          modal.destroy()
        }, 100000);
      }
      else if (validPos.includes('*')) {  // must promote
        usi_move += "+";
        this.boardService.movePiece(usi_move);
      } else {
        this.boardService.movePiece(usi_move);
      }

      //reset state
      this.pieceState.selected = false;
      this.pieceState.usi_position = "";
    }
  }


  handPieceClicked(piece: Piece) {

    let original_territory: string[][] = this.territory;

    // check valid move

    let pieceUSI = piece.symbol + "*";
    if (!this.pieceState.selected) {  // select source
      if (!this.validMove[pieceUSI]) {  // can't move this piece
        this.message.create('error', '不合規則');
        return;
      }

      this.validCell = [];
      for (let i = 0; i < 9; ++i) {
        let tmpRow = [];
        for (let j = 0; j < 9; ++j) {
          tmpRow.push('N');
        }
        this.validCell.push(tmpRow);
      }

      let validPosUSI: string = "";
      let validPosNum: number[] = [];
      for (validPosUSI of this.validMove[pieceUSI]) {
        //console.log(validPosUSI);
        validPosNum = this.usi_decode(validPosUSI, this.turn);

        this.validCell[validPosNum[0]][validPosNum[1]] = 'V';

        //console.log(this.validCell);
      }

      for (let i = 0; i < 9; ++i) {
        for (let j = 0; j < 9; ++j) {
          if (this.validCell[i][j] == 'V') {
            this.territory[i][j] = 'valid';
          }
        }
      }


      this.pieceState.selected = true;
      this.pieceState.usi_position = pieceUSI;
      piece.selected = true;
    }
    else if (this.pieceState.selected) {  // select destination
      if (pieceUSI === this.pieceState.usi_position) {  // reset
        this.pieceState.selected = false;
        this.pieceState.usi_position = "";
        this.parseTerritory(this.ori_territory, this.turn);
				this.parseCheckmater(this.ori_checkmater, this.turn)
        piece.selected = false;
      }
      return;
    }
  }

  selectPiece(rowIndex: number, colIndex: number, selected: boolean) {
    this.board[rowIndex][colIndex].selected = selected;
  }

  parseGameState(gameState: GameStateModel) {
    console.log(gameState);
    this.gameType = gameState.gameType;
    setTimeout(() => {
      if (this.gameType === 'online') {
        this.turn = gameState.turn;
      } else {
        this.turn = 0;
      }
      this.parseFinish(gameState.isFinish, gameState.winner, gameState.round);
      this.validMove = gameState.validMove;
      this.parseUSI(gameState.usi);
      this.ori_territory = gameState.territory;
			this.ori_checkmater = gameState.checkmater.toString();
			//console.log(gameState.checkmater);
      this.parseTerritory(gameState.territory, this.turn);
			this.parseCheckmater(gameState.checkmater.toString(), this.turn)
		}, 200);
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

    if (this.gameType === 'online') {
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

    let i = 0;
    let token: string = "";
    while (i < usi.length) {
      token = usi[i];
      if (!isNaN(Number(token))) { // isdigit
        let count: number = Number(token);
        i++;
        token = usi[i];
        if (token === token.toLowerCase()) {
          for (let i = 0; i < count; i++) {
            this.secondPlayerHandPieces.push(new Piece(token));
          }
        } else if (token === token.toUpperCase()) {
          for (let i = 0; i < count; i++) {
            this.firstPlayerHandPieces.push(new Piece(token));
          }
        }

      } else if (isNaN(Number(token))) {
        if (token === token.toLowerCase()) {
          this.secondPlayerHandPieces.push(new Piece(token));
        } else if (token === token.toUpperCase()) {
          this.firstPlayerHandPieces.push(new Piece(token));
        }
      }

      i++;
    }
  }
  parseTerritory(territory: string, turn: number) {
    this.territory = [];
    if (turn == 1) territory = territory.split('').reverse().join('');
    let rows: string[] = territory.split('/');
    for (let row of rows) {
      let tmp_row = [];
      for (let token of row) {
      if(!this.terrVisible){
        token = 'Q';
      }
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
            tmp_row.push('default');
            break;
        }
      }
      this.territory.push(tmp_row);
    }
  }

	parseCheckmater(checkmater: string, turn: number){
		//console.log("State.checkmater="+checkmater);
		this.checkmater = [];
		if(turn == 1) checkmater = checkmater.split('').reverse().join('');
		let rows: string[] = checkmater.split('/');
		for(let i = 0; i < 9; ++i) {
			let tmpRow = [];
			for(let j = 0; j < 9; ++j){
				switch (rows[i][j]){
					case 'T':
						//tmpRow.push(this.territory[i][j]);
						if(this.territory[i][j] == "black-side")	tmpRow.push('checkmating_first');
						else																			tmpRow.push('checkmating_second');
						//tmpRow.push('checkmating');
						break;					
					case 'F':
						tmpRow.push(this.territory[i][j]);
						break;
				}
			}
			//console.log("tmpRow="+tmpRow);
			this.checkmater.push(tmpRow);
		}
		//console.log("checkmater="+this.checkmater);
		
		//what did i just see
			this.territory = this.checkmater;
		//
	}

  parseFinish(isFinish: boolean, winner: number, round: number) {
    if (isFinish) {
      if(winner != -1){
        if(this.gameType == "online" ){
            if (winner == this.turn) {
              this.winnerModal();
            } else {
              this.loserModal();
            }
        }else{
        if(winner && round % 2 === this.turn){
          this.winnerModal();
        } else {
          this.loserModal();
        }}
      }
      else{
         this.Force_Exit();
      }
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

  usi_decode(usi_pos: string, turn: number): number[] {
    let reversed = turn ? true : false;
    //console.log("turn: " + turn);
    //console.log("reversed: " + reversed);
    let row: number = 0;
    let col: number = 0;
    let ref: string = "a";
    //console.log(usi_pos[0]);
    //console.log(usi_pos[1]);
    if (!reversed) {	// first hand
      col = 9 - Number(usi_pos[0]);
      row = usi_pos.charCodeAt(1) - ref.charCodeAt(0);
    } else if (reversed) {
      col = Number(usi_pos[0]) - 1;
      row = 8 - (usi_pos.charCodeAt(1) - ref.charCodeAt(0));
    }

    let ret: number[] = [];
    ret.push(row);
    ret.push(col);
    return ret;
  }

  parsePieces(row: string): Piece[] {
    let pieces: Piece[] = [];
    let token: string;
    let i = 0;
    while (i < row.length) {
      let piece: Piece = new Piece()
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

  Exit() {
    let modal = this.modalService.confirm({
      nzTitle: '是否確認結束？',
      nzOnOk: () => {
        this.gameService.resetGame();
        modal.destroy();
        setTimeout(() => {
          this.router.navigate(['/select']);
        }, 100);
        this.gameService.exit();
      },
      nzOnCancel: () => {
        modal.destroy();
      }
    });
  }

  Force_Exit(){
    this.message.create('success', '遊戲結束!');
    this.gameService.resetGame();
    setTimeout(() => {
      this.router.navigate(['/select']);
    }, 100);
    this.gameService.exit();
  }

  showModal(title: string, content: string): void {
    const modal = this.modalService.create({
      nzTitle: title,
      nzFooter: null,
      nzContent: content
    });

    setTimeout(() => modal.destroy(), 1000);
  }

  winnerModal() {
    let modal = this.modalService.success({
      nzTitle: '棋局結束',
      nzContent: '恭喜你贏了!',
      nzOnOk: () => {
        modal.destroy();
        setTimeout(() => {
          this.router.navigate(['/select']);
        }, 100);
      }
    });
  }

  loserModal() {
    let modal = this.modalService.success({
      nzTitle: '棋局結束',
      nzContent: '敗北QQ',
      nzOnOk: () => {
        modal.destroy();
        setTimeout(() => {
          this.router.navigate(['/select']);
        }, 100);
      }
    });
  }


}
