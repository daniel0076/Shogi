import { BrowserModule } from '@angular/platform-browser';
//import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { NgxsModule } from '@ngxs/store';
import { NgxsWebsocketPluginModule } from '@ngxs/websocket-plugin';
import { WelcomeComponent } from './welcome/welcome.component';
import { BoardComponent } from './board/board.component';
import { NgZorroAntdModule, NZ_I18N, en_US } from 'ng-zorro-antd';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { registerLocaleData } from '@angular/common';
import en from '@angular/common/locales/en';

import { CoreModule } from './core/core.module';
import { SharedModule } from './shared/shared.module';
import { GameComponent } from './game/game.component';

import { GameState } from './game/store/game.state';
import { AuthState } from './core/auth/store/auth.state';

registerLocaleData(en);

@NgModule({
  declarations: [
    AppComponent,
    BoardComponent,
    WelcomeComponent,
    GameComponent
  ],
  imports: [
    CoreModule,
    SharedModule,
    BrowserModule,
		AppRoutingModule,
    NgxsModule.forRoot([
      GameState,
      AuthState
    ]),
    NgxsWebsocketPluginModule.forRoot({
      url: 'ws://127.0.0.1:8000/ws/'
    }),
    NgZorroAntdModule,
    FormsModule,
    HttpClientModule,
    BrowserAnimationsModule
  ],
  providers: [{ provide: NZ_I18N, useValue: en_US }],
  bootstrap: [AppComponent]
})
export class AppModule { }
