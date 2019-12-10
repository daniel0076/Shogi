import { State, Action, StateContext, Selector } from '@ngxs/store';
import { produce, Draft } from 'immer';
import { Game } from './game.actions';

export interface GameStateModel {
  usi: string;
  role: boolean;
}

@State<GameStateModel>({
  name: 'game'
})

export class GameState{
  constructor() { }

  @Selector()
  static getUSI(state: GameStateModel) {
    return state.usi;
  }

  @Action(Game.UpdateUSI)
  updateUSI(ctx: StateContext<GameStateModel>, action: Game.UpdateUSI) {
    ctx.setState(produce((state: Draft<GameStateModel>) => {
      state.usi = action.usi;
    }));
  }

  @Action(Game.UpdateGameState)
  updateGameState(ctx: StateContext<GameStateModel>, action: Game.UpdateGameState) {
    ctx.setState(produce((state: Draft<GameStateModel>) => {
      state.usi = action.gameState.usi;
      state.role = action.gameState.role;
    }));
  }

}
