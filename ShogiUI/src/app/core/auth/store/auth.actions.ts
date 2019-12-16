import { LoginResponse, RegisterResponse} from '../auth.interface';

export namespace Auth{

    export class SetLoginResponse{
        static readonly type = '[Auth] Login Response';
        constructor(public loginResponse: LoginResponse) { }
    }

    export class SetRegisterResponse{
        static readonly type = '[Auth] Register Response';
        constructor(public registerResponse: RegisterResponse) { }
    }
}
