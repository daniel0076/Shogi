import { Component, OnInit } from '@angular/core';
import { GameService } from '../game/game.service';
import { Observable } from 'rxjs';
import { Select } from '@ngxs/store';
import { SelectState } from './store/select.state';
import { SelectStateModel } from './store/select.state';
import { Router } from '@angular/router';
import { NzMessageService } from 'ng-zorro-antd/message';
import { Store } from '@ngxs/store';
import { SendWebSocketMessage } from '@ngxs/websocket-plugin';

@Component({
    selector: 'app-select',
    templateUrl: './select.component.html',
    styleUrls: ['./select.component.less']
})

export class SelectComponent implements OnInit {

    @Select(SelectState.getRecordResponse) RecordResponse$: Observable<SelectStateModel>;
    @Select(SelectState.getPuzzleResponse) PuzzleResponse$: Observable<SelectStateModel>;
    recVisible = false;
    puzVisible = false;
    records = [];
    puzzles = [];

    constructor(
        private gameService: GameService,
        private router: Router,
        private message: NzMessageService,
        private store: Store
    ) { }



    ngOnInit(): void {
        this.RecordResponse$.subscribe(this.RecordResponseOvserver);
        this.PuzzleResponse$.subscribe(this.PuzzleResponseOvserver);
    }

    private RecordResponseOvserver = {
        next: RecordResponse => {
            console.log(RecordResponse);
            if (!RecordResponse) {
                console.log('no');
                return;
            }
            if (RecordResponse == []) {
                this.message.create('error', "歷史紀錄為空");
            }
            else {
                this.records = RecordResponse;
                console.log(this.records);
            }
        },
        error: err => console.error('Observer got an error: ' + err),
        complete: () => console.log('Observer got a complete notification'),

    };

    private PuzzleResponseOvserver = {
        next: PuzzleResponse => {
            console.log(PuzzleResponse);
            if (!PuzzleResponse) {
                console.log('no');
                return;
            }
            if (PuzzleResponse == []) {
                this.message.create('error', "Puzzle 紀錄為空");
            }
            else {
                this.puzzles = PuzzleResponse;
            }
        },
        error: err => console.error('Observer got an error: ' + err),
        complete: () => console.log('Observer got a complete notification'),

    };

    showRec() {
        this.recVisible = true;
    }

    showPuz() {
        this.puzVisible = true;
    }

    handleCancel() {
        this.recVisible = false;
        this.puzVisible = false;
        this.gameService.exit();
    }

    startSingleGame() {
        this.gameService.startGame("single");
        this.navigateGame("single");
    }

    startOnlineGame() {
        this.gameService.startGame("online");
        this.navigateGame("online");
    }

    startPuzzleGame() {
        this.showPuz();
        this.gameService.startGame("puzzle");
    }

    startHistoryGame() {
        this.showRec();
        this.gameService.startGame("record");
    }


    navigateGame(gameType: string) {
        this.message.create('success', '準備進行遊戲');
        setTimeout(() => {
            this.router.navigate(['/game', { gameType: gameType }]);
        }, 1000);
    }

    onSelectRecord(record: any): void {
        console.log(record);
        const event = new SendWebSocketMessage(
            {
                type: "move",
                content: {
                    type: "setRecord",
                    content: record.game_id
                }
            }
        );
        this.recVisible = false;
        console.log(this.recVisible);
        this.store.dispatch(event);
        this.navigateGame("history");
    }

    onSelectPuzzle(puzzle: any): void {
        console.log(puzzle);
        const event = new SendWebSocketMessage(
            {
                type: "move",
                content: {
                    type: "setPuzzle",
                    content: puzzle.game_id
                }
            }
        );
        this.store.dispatch(event);
        this.puzVisible = false;
        this.navigateGame("puzzle");
    }

}
