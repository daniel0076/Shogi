from Shogi_app.Piece import Piece
from Shogi_app.Consts import *
import json

'''
The upper piece is for black, lower is for white 
white is on the top of the board, black is at the botton
'''

class Board():
    def __init__(self, usi= DEFAULT_USI):
        board, side, hand_pieces, move_count = self.parse_usi(usi)
        self.board = self.init_boardstate(board)
        self.hands = self.init_hand(hand_pieces)
        self.move_count = move_count
        self.side = side
        self.is_checkmate = False
        self.checkmater = []
        self.possible = [None, None]
        self.possible = self.cal_possible_moves()
        self.cal_checkmate()
        self.winer = None
        self.check_win()

    def init_board(self, usi): 
        self.init_board_nowin(usi)
        self.check_win()

    def init_board_nowin(self, usi):
        board, side, hand_pieces, move_count = self.parse_usi(usi)
        self.board = self.init_boardstate(board)
        self.hands = self.init_hand(hand_pieces)
        self.move_count = move_count
        self.side = side
        self.is_checkmate = False
        self.possible = [None, None]
        self.possible = self.cal_possible_moves() # the possible move of the black
        self.cal_checkmate()


    def parse_piece(self, pieces):
        piece = []
        i = 0
        while(i < len(pieces)):
            token = pieces[i]
            if(token.isdigit()):
                token = int(token)
            elif(token == '+'):
                i += 1
                token += pieces[i]
            piece.append(token)
            i += 1
        return piece

    def parse_usi(self, usi): 
        usi = usi.split(' ')
        board_state = usi[0]
        side = eval(usi[1])
        if(usi[2] == '-'):
            hand_pieces = usi[2]
        else:
            hand_pieces = self.parse_piece(usi[2]) 
        move_count = int(usi[3])
        rows = board_state.split('/')
        assert(len(rows) == 9) 
        for i in range(9):
            rows[i] = self.parse_piece(rows[i])
            
        return rows, side, hand_pieces, move_count 
   
    def init_hand(self, hand_s):
        hands = {}
        if hand_s != '-':
            i = 0
            while i < len(hand_s):
                sym = hand_s[i]
                num = 1
                if(type(sym) == int):
                    num = sym
                    i += 1
                    sym = hand_s[i]
                hands[sym] = num
                i += 1
        return hands 
                
    def init_boardstate(self, board_s):
        board = []
        for i in range(9):
            j , row  = 0, []
            for token in board_s[i]:
                if(type(token) == int):
                    row.extend([None] * token)
                    j += token
                else:
                    color = b
                    if(token.islower()):
                        token = token.upper() 
                        color = w
                    #if(token ==) 
                    # TODO
                    row.append(Piece(eval(token.replace('+', 'PRO_')), color, (i, j)))
                    j += 1
            board.append(row)
        return board

    def output_usi(self):
        board = [''] * 9
        for i in range(9):
            con = 0
            for j in range(9): 
                if(self.board[i][j] == None):
                    if(j == 8 or self.board[i][j+1] != None):
                        board[i] += str(con+1)
                        con = 0
                    else:
                        con += 1
                else:
                    board[i] += self.board[i][j].get_symbol()
        board = '/'.join(board)

        side = COLORS_OUT[self.side]
        hand = ''
        if(len(self.hands) == 0):
            hand = '-'
        else:
            for key in self.hands:
                value = self.hands[key]
                if value == 1:
                    hand += key
                elif value > 1:
                    hand += str(value) + key

        return '{} {} {} {}'.format(board, side, hand, self.move_count)
   


    def cal_checkmate(self):
        sym = 'K'
        if self.side:
            sym = 'k'
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != None and self.board[i][j].get_symbol() == sym:
                    loc = (i, j)
                    break
        assert(loc != None)
        self.is_checkmate = False
        self.checkmater = []
        for move in self.possible[1^self.side]:
            if self.possible[1^self.side][move] != None and loc in self.possible[1^self.side][move]:
                self.is_checkmate = True
                self.checkmater.append(self.loc2usi(move))


        
    def simulate_move(self, lc, move):
        usi = self.output_usi()
        if type(lc[0]) == int:
            move_com = self.loc2usi(lc) + self.loc2usi(move) 
        else:
            move_com = lc + move
        assert(len(move_com) == 4 or len(move_com) == 5)
        if(move_com[1] == '*'):
            loc = self.get_loc(move_com[2:4])
            piece = self.put_piece(move_com[0], loc)
            self.board[loc[0]][loc[1]] = piece
        else:
            lc1, lc2 = self.get_loc(move_com[:2]) , self.get_loc(move_com[2:4])
            if(self.board[lc2[0]][lc2[1]] != None):
                self.take_piece(lc2, self.side)
            self.board[lc2[0]][lc2[1]] = self.board[lc1[0]][lc1[1]]  
            self.board[lc1[0]][lc1[1]] = None
            if(len(move_com) == 5):
               self.do_promote(lc2) 
        self.possible = self.cal_possible_moves()
        self.cal_checkmate()
        check = self.is_checkmate
        self.init_board_nowin(usi)
        return check

    def have_promote(self, lc1, lc2, side):
        pc = self.board[lc1[0]][lc1[1]]
        if pc.is_promote():
            return -1
        line = 4 + 2 * side 
        dis = self.side * (lc2[0] - line)
        if dis > 0:
            if pc.get_symbol() == 'p' or pc.get_symbol() == 'l':
                if dis > 1:
                    return 1
            elif pc.get_symbol() == 'n':
                if dis > 0:
                    return 1
            return 0
        return -1

    def legal_moves(self):
        # TODO the checkmate
        moves = {}
        side = 1
        if(self.side):
            side = -1
        for lc in self.possible[self.side]:
            if self.possible[self.side][lc]:
                if type(lc[0]) == int:
                    tmp = []
                    for pos in self.possible[self.side][lc]:
                        ans = self.loc2usi(pos)
                        if self.have_promote(lc, pos, side) == 1:
                            ans += '*'
                        elif self.have_promote(lc, pos, side) == 0:
                            ans += '+'
                        else:
                            ans += '#'
                        tmp.append(ans)
                    moves[self.loc2usi(lc)] = tmp
                else:
                    moves[lc] = self.possible[self.side][lc]
        return moves



    def get_possible(self, loc, side):
        pc = self.board[loc[0]][loc[1]]
        rule = Rule(self.board)
        rules = { 
                'p': rule.pawn_rule,
                'n': rule.night_rule,
                'l': rule.lance_rule,
                'b': rule.bishop_rule,
                'r': rule.rook_rule,
                'g': rule.gold_rule,
                's': rule.silver_rule,
                'k': rule.king_rule,
                '+p': rule.gold_rule,
                '+n': rule.gold_rule,
                '+l': rule.gold_rule,
                '+b': rule.prom_bishop_rule,
                '+r': rule.prom_rook_rule,
                '+s': rule.gold_rule
        }
        method = rules.get(pc.get_symbol().lower())
        if method: 
            return method(loc, side)
    
    def drop_piece(self, sy, side):
        sym =  sy.lower()
        pos = []
        if sym == 'p':
            for i in range(9):
                flag = True
                for j in range(9):
                    if self.board[j][i] != None and self.board[j][i].get_symbol() == sy:  
                        flag = False 
                if flag:
                    for j in range(4-side*4, 4+side*2, side):
                        if self.board[j][i] == None:
                            pos.append(self.loc2usi((j, i)) + '#')

        else:
            dis = 4
            if sym == 'l':
               dis = 2  
            elif sym == 'n':
               dis = 3 
            for i in range(4-side*4, 4+side*dis, side):
                for j in range(9):
                    if self.board[i][j] == None:
                        pos.append(self.loc2usi((i, j)) + '#')
             
        return pos

    def cal_possible_moves(self):
        possible = []
        for side in range(2):
            moves = {}
            sign_side = 1
            if(side == 0):
                sign_side = -1
            for i in range(9):
                for j in range(9):
                    if self.board[i][j] != None and self.board[i][j].color == side: 
                        moves[(i, j)] = self.get_possible((i,j), sign_side)
            for piece in self.hands:
                if (piece.islower() and side) or (piece.isupper() and not side):
                    if self.hands[piece] == 0:
                        moves[piece+'*']= self.valid_move(piece+'*')
            possible.append(moves) 
                
        return possible

    def valid_move(self, loc):
        moves = []
        if loc[1] == '*':
            if loc[0].islower():
                side = 1
            else:
                side = -1
            moves = self.drop_piece(loc[0], side)
        else:
            lc = self.get_loc(loc)
            side = -1 + 2 * self.board[lc[0]][lc[1]].color # if self.side == 1, side = 1 elif self.side == 0, side = -1
            positions = self.get_possible(lc, side)
            if positions:
                for pos in positions:
                    ans = self.loc2usi(pos)
                    if self.have_promote(lc, pos, side) == 1:
                        ans += '*'
                    elif self.have_promote(lc, pos, side) == 0:
                        ans += '+'
                    else:
                        ans += '#'
                    moves.append(ans)
        return moves 

    def get_loc(self, lc):
        return (ord(lc[1])- ord('a'), 9-int(lc[0]))  

    def loc2usi(self, lc):
        return str(9-lc[1])+chr(ord('a')+lc[0])

    def do_promote(self, loc):
        piece = self.board[loc[0]][loc[1]]
        assert piece.promote() == True
        return True 
   
    def take_piece(self, lc, side):
        taken = self.board[lc[0]][lc[1]] 
        sym =  taken.get_front_symbol()
        if side == b:
            sym = sym.upper()
        if sym in self.hands:
            self.hands[sym] += 1
        else:
            self.hands[sym] = 1
        return 
   
    def put_piece(self, sym, loc):
        if self.side == b:
            piece = Piece(eval(sym.upper()), self.side, loc)
        else:
            sym = sym.lower()
            piece = Piece(eval(sym.upper()), self.side, loc)
        assert(self.hands[sym])
        self.hands[sym] -= 1
        if(self.hands[sym] == 0):
            del self.hands[sym]

        return piece 


    def do_move(self, move):
        assert(len(move) == 4 or len(move) == 5)
        if(move[1] == '*'):
            loc = self.get_loc(move[2:4])
            piece = self.put_piece(move[0], loc)
            self.board[loc[0]][loc[1]] = piece
        else:
            lc1, lc2 = self.get_loc(move[:2]) , self.get_loc(move[2:4])
            if(self.board[lc2[0]][lc2[1]] != None):
                self.take_piece(lc2, self.side)
            self.board[lc2[0]][lc2[1]] = self.board[lc1[0]][lc1[1]]  
            self.board[lc1[0]][lc1[1]] = None
            if(len(move) == 5):
               self.do_promote(lc2) 
        self.side ^= 1 
        self.move_count += 1
        self.possible = self.cal_possible_moves()
        self.cal_checkmate()
        self.check_win()

        return self.output_usi() 

    def check_win(self):
        if self.is_checkmate:
            self.is_win = True
            tmp_pos = {}
            for lc in self.possible[self.side]:
                tmp = []
                for move in self.possible[self.side][lc]:
                    if not self.simulate_move(lc, move):
                        tmp.append(move)
                        self.is_win = False
                if tmp != []:
                    tmp_pos[lc] = tmp
            self.possible[self.side] = tmp_pos
            if self.is_win:
                self.winer = self.side ^ 1

    def __str__(self):
        output = ''
        for i in range(9):
            for j in range(9):
                pc = self.board[i][j]
                if pc == None:
                    output += ' .'
                else:
                    if pc.is_promote():
                        output += pc.get_symbol()
                    else:
                        output += (' ' + pc.get_symbol())
            output += '\n'
        return output

class Rule():
    def __init__(self, board):
        self.board = board
            
    def is_sameside(self, loc1, loc2):
        if self.board[loc1[0]][loc1[1]].color == self.board[loc2[0]][loc2[1]].color:
            return True
        return False 

    def valid_place(self, start, loc):
        if (loc[0] < 0 or loc[0] >= 9 or loc[1] < 0 or loc[1] >= 9):
            return False
        if self.board[loc[0]][loc[1]] != None and self.is_sameside(start, loc):
            return False
        return True
     
    def valid_places(self, start, locs):
        ans = []
        for loc in locs:
            if self.valid_place(start, loc):
                ans.append(loc)
        return ans
    def pawn_rule(self, loc, side): 
        locs = []
        locs.append((loc[0]+side, loc[1]))
        locs = self.valid_places(loc, locs)
        return locs

    def night_rule(self, loc, side):
        locs = []
        locs.append((loc[0]+side * 2, loc[1]+1))
        locs.append((loc[0]+side * 2, loc[1]-1))
        locs = self.valid_places(loc, locs)
        return locs

    def lance_rule(self, loc, side):
        locs = []
        di = (side, 0)
        pos = tuple(map(sum, zip(loc, di)))
        while self.valid_place(loc, pos):
            locs.append(pos) 
            if(self.board[pos[0]][pos[1]] != None):
                break
            pos = tuple(map(sum, zip(pos, di)))
        return locs

    def bishop_rule(self, loc, side):
        locs = []
        dirs = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
        for di in dirs:
            pos = tuple(map(sum, zip(loc, di)))
            while self.valid_place(loc, pos):
                locs.append(pos) 
                if(self.board[pos[0]][pos[1]] != None):
                    break
                pos = tuple(map(sum, zip(pos, di)))
        return locs 


    def silver_rule(self, loc, side):
        locs = []
        locs.append((loc[0]+side , loc[1]))
        locs.append((loc[0]+side , loc[1]+1))
        locs.append((loc[0]+side , loc[1]-1))
        locs.append((loc[0]-side , loc[1]+1))
        locs.append((loc[0]-side , loc[1]-1))
        locs = self.valid_places(loc, locs)
        return locs 

    def gold_rule(self, loc, side):
        locs = []
        locs.append((loc[0]+side , loc[1]))
        locs.append((loc[0]+side , loc[1]+1))
        locs.append((loc[0]+side , loc[1]-1))
        locs.append((loc[0], loc[1]+1))
        locs.append((loc[0], loc[1]-1))
        locs.append((loc[0]-side, loc[1]))
        locs = self.valid_places(loc, locs)
        return locs

    def rook_rule(self, loc, side):
        locs = []
        dirs = [(0,1), (0, -1), (1, 0), (-1,0)]
        for di in dirs:
            pos = tuple(map(sum, zip(loc, di)))
            while self.valid_place(loc, pos):
                locs.append(pos) 
                if(self.board[pos[0]][pos[1]] != None):
                    break
                pos = tuple(map(sum, zip(pos, di)))
               

        return locs

    def king_rule(self, loc, side):
        locs = []
        locs.append((loc[0]+side , loc[1]))
        locs.append((loc[0]+side , loc[1]+1))
        locs.append((loc[0]+side , loc[1]-1))
        locs.append((loc[0]-side , loc[1]+1))
        locs.append((loc[0]-side , loc[1]-1))
        locs.append((loc[0]-side, loc[1]))
        locs.append((loc[0], loc[1]+1))
        locs.append((loc[0], loc[1]-1))
        locs = self.valid_places(loc, locs)
        return locs

    def prom_rook_rule(self, loc, side):
        lc1 = self.rook_rule(loc, side)
        lc2 = self.king_rule(loc, side)
        return list(set(lc1).union(lc2))

    def prom_bishop_rule(self, loc, side):
        lc1 = self.bishop_rule(loc, side)
        lc2 = self.king_rule(loc, side)
        return list(set(lc1).union(lc2))

    
def test_init():
    init = "lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL b - 1"
    init = "8l/1l+R2P3/p2pBG1pp/kps1p4/Nn1P2G2/P1P1P2PP/1PS6/1KSG3+r1/LN2+p3L w Sbgn3p 124"
    board = Board(init)
    board.valid_move('7d')
    board.valid_move('p*')
    print(board.is_checkmate)
    # do eat piece 
    board.do_move('9d9e')
    print(board.output_usi())
    # do promote move
    board.do_move('4b4a+')
    # do put piece 
    print(board.output_usi())
    board.do_move('B*9a')
    print(board.output_usi())
    # do simple move
    print(board)
    board.do_move('1f1g')
    
    print(board.output_usi())
    print(board)
    board.init_board('1k7/1G7/pG1pBG1pp/1p2p4/NnsP2G2/P1P1P2PP/1PS6/1KSG3+r1/LN2+p3L w Sbgn3p 125')
    board.is_win()

