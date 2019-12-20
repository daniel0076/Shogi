import { Component, OnInit } from '@angular/core';
import { GameService } from './game.service';
import { ActivatedRoute } from '@angular/router';
import { Observable } from 'rxjs';
import { Select } from '@ngxs/store';
import { AuthState } from '../core/auth/store/auth.state';
import { LoginResponse } from '../core/auth/auth.interface';

@Component({
  selector: 'app-game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.less']
})
export class GameComponent implements OnInit {
  @Select(AuthState.getLoginResponse) loginState$: Observable<LoginResponse>;
  constructor(private gameService: GameService, private route: ActivatedRoute) { }
  private gameType: string;
  private userId: number;

  private loginStateObserver = {
    next: loginState => {this.userId = loginState.userId},
    error: err => console.error('Observer got an error: ' + err),
    complete: () => console.log('Observer got a complete notification'),
  };

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.gameType = params.get("gameType")
    })

    this.loginState$.subscribe(this.loginStateObserver);
  }

  surrender(){
    this.gameService.surrender(this.userId);
  }

  exitSingle(){
    this.gameService.exitSingle();
  }

}
