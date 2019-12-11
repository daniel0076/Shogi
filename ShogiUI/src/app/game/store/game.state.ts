import { State, Action, StateContext, Selector } from '@ngxs/store';
import { produce, Draft } from 'immer';
import { Game } from './game.actions';

export interface GameStateModel {
  usi: string;
  turn: number;  // 先手、後手
  round: number;
}

@State<GameStateModel>({
  name: 'game'
})

export class GameState{
  constructor() { }

  @Selector()
  static getUSI(state: GameStateModel): string{
    return state.usi;
  }

  @Selector()
  static getTurn(state: GameStateModel): number {
    return state.turn;
  }

  @Selector()
  static getRound(state: GameStateModel): number {
    return state.round;
  }

  @Action(Game.SelectRecord)
  test(ctx: StateContext<GameStateModel>, action: any) {
    console.log(action);
  }

  @Action(Game.UpdateUSI)
  updateUSI(ctx: StateContext<GameStateModel>, action: Game.UpdateUSI) {
    ctx.setState(produce((state: Draft<GameStateModel>) => {
      state.usi = action.usi;
    }));
  }

  @Action(Game.UpdateGameState)
  updateGameState(ctx: StateContext<GameStateModel>, action: any) {
    ctx.setState(produce((state: Draft<GameStateModel>) => {
      console.log(action);
      state.usi = action.content.usi;
      state.turn = action.content.turn;
    }));
  }

  @Action(Game.ResetGame)
  resetGame(ctx: StateContext<GameStateModel>, action: Game.ResetGame) {
    ctx.setState(produce((state: Draft<GameStateModel>) => {
      state.usi = "lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL b - 1";
    }));
  }

  @Action(Game.SetTurn)
  setTurn(ctx: StateContext<GameStateModel>, action: Game.SetTurn) {
    ctx.setState(produce((state: Draft<GameStateModel>) => {
      state.turn = action.turn;
    }));
  }

}
