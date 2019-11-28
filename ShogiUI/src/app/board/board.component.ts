import { Component, OnInit } from '@angular/core';
import { Piece } from '../shared/piece/piece.interface';

@Component({
  selector: 'app-board',
  templateUrl: './board.component.html',
  styleUrls: ['./board.component.less']
})
export class BoardComponent implements OnInit {
  private board: Piece[][] = [
    [{ 'symbol': 'K', 'color': 'b' }],
    [{ 'symbol': 'R', 'color': 'b' }]
  ]

  constructor() { }

  ngOnInit() {
  }

}
