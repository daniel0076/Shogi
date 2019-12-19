import { RecordResponse, PuzzleResponse} from '../select.interface';

export namespace Select{
    export class SetRecordResponse{
        static readonly type = '[Game] Select Record';
        constructor(public recordResponse: RecordResponse) {}
    }

    export class SetPuzzleResponse{
        static readonly type = '[Game] Select Puzzle';
        constructor(public puzzleResponse: PuzzleResponse) {}
    }
}
