import { LoginResponse, RegisterResponse} from '../auth.interface';

export namespace Auth{

    export class SetLoginResponse{
        static readonly type = '[Login]';
        constructor(public loginResponse: LoginResponse) { }
    }

    export class SetRegisterResponse{
        static readonly type = '[Register]';
        constructor(public registerResponse: RegisterResponse) { }
    }
}
