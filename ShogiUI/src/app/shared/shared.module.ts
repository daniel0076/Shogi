import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PieceComponent } from './piece/piece.component';
import { NgZorroAntdModule } from 'ng-zorro-antd';


@NgModule({
  declarations: [PieceComponent],
  imports: [
    CommonModule,
    NgZorroAntdModule
  ],
  exports: [
    NgZorroAntdModule,
    PieceComponent
  ]
})
export class SharedModule { }
