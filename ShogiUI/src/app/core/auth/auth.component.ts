import { Component, OnInit } from '@angular/core';
import {Router} from "@angular/router"
import { Observable } from 'rxjs';
import { FormBuilder, FormGroup, Validators} from '@angular/forms';
import { AuthService } from './auth.service';
import { Select } from '@ngxs/store';
import { AuthState } from './store/auth.state';
import { AuthStateModel } from './store/auth.state';
import { NzMessageService } from 'ng-zorro-antd/message';
import { LoginResponse, RegisterResponse} from './auth.interface';

@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.less']
})
export class AuthComponent implements OnInit{

  @Select(AuthState.getRegisterResponse) registerResponse$: Observable<RegisterResponse>;
  @Select(AuthState.getLoginResponse) loginResponse$: Observable<LoginResponse>;
  loginForm: FormGroup;
  regForm: FormGroup;
  regVisible = false;


  constructor(
    private fb: FormBuilder,
    private authService: AuthService,
    private message: NzMessageService,
    private router: Router
    ) {}

  submitForm(): void {
    for (const i in this.loginForm.controls) {
      this.loginForm.controls[i].markAsDirty();
      this.loginForm.controls[i].updateValueAndValidity();
    }
  }

  private registerResponseObserver = {
    next: registerResponse => {
      if(!registerResponse) {
        return;
      }

      if(registerResponse.status){
        this.message.create('success', '註冊成功');
        this.regVisible = false;
      } else {
        this.message.create('error', registerResponse.errorMsg);
      }
    },
    error: err => console.error('Observer got an error: ' + err),
    complete: () => console.log('Observer got a complete notification'),
  };

  private loginResponseObserver = {
    next: loginResponse => {
      if(!loginResponse) {
        return;
      }

      if(loginResponse.status){
        this.message.create('success', '登入成功，二秒後自動跳轉');
        setTimeout(() => {
          this.router.navigate(['/select']);
        }, 2000);
      } else {
        this.message.create('error', '帳號密碼錯誤，或使用者不存在或已登入系統');
      }
    },
    error: err => console.error('Observer got an error: ' + err),
    complete: () => console.log('Observer got a complete notification'),
  };

  showReg(): void {
    this.regVisible = true;
  }

  handleLogin(): void {
    this.authService.login(this.loginForm.value);
  }

  handleRegister(): void {
    this.authService.register(this.regForm.value);
  }

  handleCancel(): void {
    this.regVisible = false;
  }

  ngOnInit(): void {
    this.loginForm = this.fb.group({
      userName: [null, [Validators.required]],
      password: [null, [Validators.required]]
    });

    this.regForm = this.fb.group({
      userName: [null, [Validators.required]],
      password: [null, [Validators.required]]
    });

    this.registerResponse$.subscribe(this.registerResponseObserver);
    this.loginResponse$.subscribe(this.loginResponseObserver);
  }
}
