export interface PieceInterface {
    symbol: string;
    selected: boolean;
}
export class Piece implements PieceInterface{
    symbol: string;
    selected: boolean;
    constructor(symbol: string = ''){
        this.symbol = symbol;
        this.selected = false;
    }
  }
