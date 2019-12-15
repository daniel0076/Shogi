import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators} from '@angular/forms';
import { AuthService } from './auth.service';

@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.less']
})
export class AuthComponent implements OnInit{
  loginForm: FormGroup;
  regForm: FormGroup;

  submitForm(): void {
    for (const i in this.loginForm.controls) {
      this.loginForm.controls[i].markAsDirty();
      this.loginForm.controls[i].updateValueAndValidity();
    }
  }

  constructor(private fb: FormBuilder, private authService: AuthService) {}

  regVisible = false;

  showReg(): void {
    this.regVisible = true;
  }

  handleLogin(): void {
    this.authService.login(this.loginForm.value);
  }

  handleRegister(): void {
    this.authService.register(this.regForm.value);
    this.regVisible = false;
  }

  handleCancel(): void {
    console.log('Button cancel clicked!');
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
  }
}
