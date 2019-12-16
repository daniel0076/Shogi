import { State, Action, StateContext, Selector } from '@ngxs/store';
import { produce, Draft } from 'immer';
import { LoginResponse, RegisterResponse} from '../auth.interface';
import { Auth } from './auth.actions';

export interface AuthStateModel {
  loginResponse: LoginResponse;
  registerResponse: RegisterResponse;
}

@State<AuthStateModel>({
  name: 'auth'
})

export class AuthState{
  constructor() { }

  @Selector()
  static getLoginResponse(state: AuthStateModel): LoginResponse{
    return state.loginResponse;
  }

  @Selector()
  static getRegisterResponse(state: AuthStateModel): RegisterResponse{
    return state.registerResponse;
  }



  @Action(Auth.SetLoginResponse)
  setLoginResponse(ctx: StateContext<AuthStateModel>, action: any) {
    console.log(action);
    ctx.setState(produce((state: Draft<AuthStateModel>) => {
      state.loginResponse = action.content;
    }));
  }

  @Action(Auth.SetRegisterResponse)
  setRegisterResponse(ctx: StateContext<AuthStateModel>, action: any) {
    console.log(action);
    ctx.setState(produce((state: Draft<AuthStateModel>) => {
      state.registerResponse = action.content;
    }));
  }


}
