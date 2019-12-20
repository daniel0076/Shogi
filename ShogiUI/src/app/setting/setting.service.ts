import { Store } from '@ngxs/store'
import { SendWebSocketMessage } from '@ngxs/websocket-plugin';
import { Injectable } from '@angular/core';

@Injectable({
   providedIn: 'root'    
})

export class SettingService {

    constructor(private store: Store) {}

    update_setting(userSet: any): void {
        const event = new SendWebSocketMessage(
            {
                type: "update_settings",
                  content: userSet
            }
        );
        console.log('QQQQ');
        this.store.dispatch(event);
    }

    get_setting(): void {
        const envent = new SendWebSocketMessage(
            {
                type: "get_settings",
            }
        );
        this.store.dispatch(event);
    }


}
