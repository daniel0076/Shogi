from Shogi_app.Consts import * 

class Piece():
    def __init__(self, symbol, color, location):
        self.symbol = symbol
        self.color = color
        self.location = location

    def __str__(self):
        return PIECE_SYMBOLS[self.symbol] + ' ' +  str(self.location)

    def sign_side(self):
        # black to be -1 white to be 1
        if self.color == 0:
            return -1
        return 1 

    def is_promote(self):
        return self.symbol >= PRO_P  

    def promote(self):
        if PIECE_PROMOTE[self.symbol] != NONE:
            self.symbol = PIECE_PROMOTE[self.symbol]
            return True
        return False

    def get_front_symbol(self):
        return PIECE_SYMBOLS[PROMOTED_PIECE[self.symbol]]

    def get_symbol(self):
        if self.color == b:
            return PIECE_SYMBOLS[self.symbol].upper()
        return PIECE_SYMBOLS[self.symbol]
