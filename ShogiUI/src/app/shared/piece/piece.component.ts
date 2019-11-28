import { Component, OnInit, Input } from '@angular/core';
import { Piece } from './piece.interface';

@Component({
  selector: 'app-piece',
  templateUrl: './piece.component.html',
  styleUrls: ['./piece.component.less']
})
export class PieceComponent implements OnInit {
  @Input() piece: Piece;
  private static pieceImg = {
    "K": "sgl01.png",
    "R": "sgl02.png"
    /* TODO */
  };

  constructor() { }

  ngOnInit() {
    console.log(this.piece.symbol);
  }

  getPieceImg(key: string){
    return PieceComponent.pieceImg[key];
  }

}
