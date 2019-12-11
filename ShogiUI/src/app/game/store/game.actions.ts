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

    export class ResetGame {
        static readonly type = '[Game] Reset Game';
        constructor() { }
    }

    export class SetTurn{
        static readonly type = '[Game] Reset Game';
        constructor(public turn: number) { }
    }

}
