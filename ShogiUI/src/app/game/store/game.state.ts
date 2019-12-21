import { State, Action, StateContext, Selector } from '@ngxs/store';
import { produce, Draft } from 'immer';
import { Game } from './game.actions';
import { WebSocketDisconnected, WebSocketConnected } from '@ngxs/websocket-plugin';
import { ConnectWebSocket } from '@ngxs/websocket-plugin';
import { NzMessageService } from 'ng-zorro-antd/message';
import { Store } from '@ngxs/store';

export interface GameStateModel {
  usi: string;
  checkmater: [];
  isCheckmate: boolean;
  isFinish: boolean;
  round: number;
  turn: number;
  territory: string;
  winner: any;
  validMove: object;
  gameType: string;
}

@State<GameStateModel>({
  name: 'game'
})

export class GameState {
  constructor(
    private message: NzMessageService,
    private store: Store
  ) { }

  @Selector()
  static getGameState(state: GameStateModel): GameStateModel {
    return state;
  }

  @Selector()
  static getUSI(state: GameStateModel): string {
    return state.usi;
  }

  @Action(Game.SelectRecord)
  test(ctx: StateContext<GameStateModel>, action: any) {
  }

  @Action(Game.UpdateGameState)
  updateGameState(ctx: StateContext<GameStateModel>, action: any) {
    ctx.setState({ ...(action.content) });
  }

  @Action(Game.ResetGame)
  resetGame(ctx: StateContext<GameStateModel>, action: Game.ResetGame) {
    ctx.setState(produce((state: Draft<GameStateModel>) => {
      state.usi = "";
      state.gameType = undefined;
      state.round = 0;
      state.turn = undefined;
      state.isFinish= false;
    }));
  }

  @Action(Game.SetTurn)
  setTurn(ctx: StateContext<GameStateModel>, action: Game.SetTurn) {
    ctx.setState(produce((state: Draft<GameStateModel>) => {
      state.turn = action.turn;
    }));
  }

  @Action(WebSocketDisconnected)
  WsDisconnected() {
    this.message.create('error', '後端離線...重新連線中');
    this.store.dispatch(new ConnectWebSocket());
  }

  @Action(WebSocketConnected)
  WsConnected() {
    this.message.create('info', '後端連線完成，請登入');
  }
}
