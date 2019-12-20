import { SettingResponse }   from '../setting.interface';

export namespace Setting{

    export class SetSettingResponse{
        static readonly type = '[Settings]';
        constructor(public settingResponse: SettingResponse){} 
    }

}
