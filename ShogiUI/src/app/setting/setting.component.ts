import { Component, OnInit, DoCheck } from '@angular/core';
import { Store } from '@ngxs/store';
import { SettingState } from './store/setting.state';
import { SettingStateModel } from './store/setting.state';
import { SettingService } from './setting.service';
import { Observable } from 'rxjs';
import { Settingform } from './setting.interface';
import { NzMessageService } from 'ng-zorro-antd/message';
import { Select } from '@ngxs/store';

@Component({
    selector: 'app-setting',
    templateUrl: './setting.component.html',
    styleUrls: ['./setting.component.less']
})


export class SettingComponent implements OnInit {

    @Select(SettingState.getSettingResponse) settingResponse$: Observable<SettingStateModel>; 
    settingVisible = false;
    private user_setting: Settingform = {show_terr: true};
    show_territory = "On"; 

    constructor(
        private settingService: SettingService,
        private message: NzMessageService
    ){
    }

    ngOnInit(): void {
        this.settingResponse$.subscribe(this.settingResponseObserver);
    }

    

    SubmitSetting(){
        this.settingService.update_setting(this.user_setting);
        this.message.create('success', '正在儲存設定..');
        this.settingVisible = false;
    }

    Setting(){
        this.settingVisible = true; 
    }
    
    private settingResponseObserver = {
        next: settingResponse => {
            if(!settingResponse){
                return ;
            }
            console.log(settingResponse);
            if(settingResponse.show_terr != null){
                this.user_setting.show_terr = settingResponse.show_terr;
                if(this.user_setting.show_terr){
                   this.show_territory = "On";
                }else{
                   this.show_territory = "Off";
                }
                console.log(settingResponse);
            }
        },
        error: err => console.error('Observer got an error: ' + err), 
        complete: () => console.log('Observer got a complete notification')

    };


    handleCancel(){
        this.settingVisible = false;
    }

    handleSet(){
        this.user_setting.show_terr = !this.user_setting.show_terr; 
        if(this.user_setting.show_terr){
            this.show_territory = "On";
        }else{
            this.show_territory = "Off";
        }
    }


}
