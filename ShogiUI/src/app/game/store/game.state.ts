import { State, Action, StateContext, Selector } from '@ngxs/store';
import { produce, Draft } from 'immer';
import { Game } from './game.actions';

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
  constructor() { }

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
    }));
  }

  @Action(Game.SetTurn)
  setTurn(ctx: StateContext<GameStateModel>, action: Game.SetTurn) {
    ctx.setState(produce((state: Draft<GameStateModel>) => {
      state.turn = action.turn;
    }));
  }
}
