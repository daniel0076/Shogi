import { State, Action, StateContext, Selector } from '@ngxs/store';
import { RecordResponse, PuzzleResponse } from '../select.interface';
import { Select } from './select.action';
import { produce, Draft } from 'immer';

export interface SelectStateModel {
   recordResponse: RecordResponse;
   puzzleResponse: PuzzleResponse;
}

@State<SelectStateModel>({
    name: 'select'
})

export class SelectState{
    constructor() {}

    @Selector()
    static getRecordResponse(state: SelectStateModel): RecordResponse{
        console.log(state.recordResponse);
        return state.recordResponse;
    }

    @Selector()
    static getPuzzleResponse(state: SelectStateModel): PuzzleResponse{
        return state.puzzleResponse;
    }

    @Action(Select.SetRecordResponse)
    SetRecordResponse(ctx: StateContext<SelectStateModel>, action: any) {
        ctx.setState(produce((state: Draft<SelectStateModel>) =>{
            state.recordResponse = action.content;
        }));
    }

    @Action(Select.SetPuzzleResponse)
    SetPuzzleResponse(ctx: StateContext<SelectStateModel>, action: any) {
        ctx.setState(produce((state: Draft<SelectStateModel>) =>{
            state.puzzleResponse = action.content;
        }));
    }

}
