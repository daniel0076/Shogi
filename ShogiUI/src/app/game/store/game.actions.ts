
export namespace Game {

    export class UpdateGameState {
        static readonly type = '[Game] Update Game State';
        constructor(public gameState: any|object) { }
    }

    export class ResetGame {
        static readonly type = '[Game] Reset Game';
        constructor() { }
    }

    export class SetTurn{
        static readonly type = '[Game] Reset Game';
        constructor(public turn: number) { }
    }

    export class SelectRecord{
        static readonly type = '[Game] Select Record';
        constructor(public input: any) { }
    }
}
