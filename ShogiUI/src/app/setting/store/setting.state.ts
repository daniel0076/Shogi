import { State, Action, StateContext, Selector } from '@ngxs/store';
import { SettingResponse } from '../setting.interface';
import { Setting } from './setting.action';
import { produce, Draft } from 'immer';

export interface SettingStateModel {
    settingResponse: SettingResponse;
}

@State<SettingStateModel>({
    name: 'setting'
})


export class SettingState{
    constructor() {}

    @Selector()
    static getSettingResponse(state: SettingStateModel): SettingResponse{
        return state.settingResponse;
    }

    @Action(Setting.SetSettingResponse)
    SetSettingResponse(ctx: StateContext<SettingStateModel>, action: any){
        ctx.setState(produce((state: Draft<SettingStateModel>) => {
            state.settingResponse = action.content;
        }));
    }

}
