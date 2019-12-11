import { Component, OnInit, Input } from '@angular/core';
import { Piece } from './piece.interface';

@Component({
  selector: 'app-piece',
  templateUrl: './piece.component.html',
  styleUrls: ['./piece.component.less']
})
export class PieceComponent implements OnInit {
  @Input() piece: Piece;
  @Input() turn: number;
  private static upwardPieceImage = {
    "K": "sgl01.png",
    "k": "sgl11.png",
    "R": "sgl02.png",
    "+R": "sgl22.png",
    "B": "sgl03.png",
    "+B": "sgl23.png",
    "G": "sgl04.png",
    "S": "sgl05.png",
    "+S": "sgl25.png",
    "N": "sgl06.png",
    "+N": "sgl26.png",
    "L": "sgl07.png",
    "+L": "sgl27.png",
    "P": "sgl08.png",
    "+P": "sgl28.png"
  };

  private static downwardPieceImage = {
    "K": "sgl31.png",
    "k": "sgl41.png",
    "R": "sgl32.png",
    "+R": "sgl52.png",
    "B": "sgl33.png",
    "+B": "sgl53.png",
    "G": "sgl34.png",
    "S": "sgl35.png",
    "+S": "sgl55.png",
    "N": "sgl36.png",
    "+N": "sgl56.png",
    "L": "sgl37.png",
    "+L": "sgl57.png",
    "P": "sgl38.png",
    "+P": "sgl58.png"
  };

  constructor() { }

  ngOnInit() {
  }

  getPieceImg(key: string) {
    console.log("getpiece", key, this.turn);
    if (this.turn === 0) { // first hand, usi in upper case
      if (key === key.toUpperCase()) {
        return PieceComponent.upwardPieceImage[key];
      } else {
        if (key === 'k') {  // K and k are different koma
          return PieceComponent.downwardPieceImage[key];

        } else {  // others are all encoded in upper case
          return PieceComponent.downwardPieceImage[key.toUpperCase()];

        }
      }
    } else if (this.turn === 1) { // second hand, usi in lower case
      if (key === key.toLowerCase()) {
        if (key === 'k') {  // K and k are different koma
          return PieceComponent.upwardPieceImage[key];

        } else {  // others are all encoded in upper case
          return PieceComponent.upwardPieceImage[key.toUpperCase()];

        }
      } else {
        return PieceComponent.downwardPieceImage[key];
      }
    }
  }

}
