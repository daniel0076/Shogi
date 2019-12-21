import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AuthComponent } from './auth/auth.component';
import { SharedModule } from '../shared/shared.module';
import { ReactiveFormsModule } from '@angular/forms';
import { NgxsModule } from '@ngxs/store';
import { NgZorroAntdModule, NZ_I18N, en_US } from 'ng-zorro-antd';


@NgModule({
  declarations: [AuthComponent],
  imports: [
    CommonModule,
    SharedModule,
    ReactiveFormsModule,
    NgZorroAntdModule,
    NgxsModule.forRoot([])
  ],
  exports: [AuthComponent]
})
export class CoreModule { }
