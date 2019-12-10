import { GameState } from '../game.interface';

export namespace Game {

    export class UpdateGameState {
        static readonly type = '[Game] Update Game State';
        constructor(public gameState: GameState) { }
    }

    export class UpdateUSI {
        static readonly type = '[Game] Update USI';
        constructor(public usi: string) { }
    }

}
