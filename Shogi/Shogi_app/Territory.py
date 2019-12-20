'''
    the output form would be three colors white, black, and gray 
    the white means the territory belongs to the white front, the black 
    the gray means it is the neatral area
    the output form would be same as the usi replace by w, b, g
'''


class Territory():
    def __init__(self, valid_moves, board):
        self.board = self.parse_board(board)
        self.valid_moves = valid_moves
        self.territory = [[0 for i in range(9)] for j in range(9)]
        self.cal_overlap()

    def usi2loc(self, lc):
        return (ord(lc[1])- ord('a'), 9-int(lc[0]))

    def parse_board(self, board_s):
        board = []
        for i in range(9):
            j , row = 0, []
            for token in board_s[i]:
                if(type(token) == int):
                    row.extend([0] * token)
                    j += token
                else:
                    if(token.islower()):
                        row.append(1)
                    else:
                        row.append(-1)
                    j += 1
            board.append(row)

        return board


    def cal_overlap(self):
        valid_move = self.valid_moves
        sides = [-1, 1]
        for i in range(2):
            side = sides[i]
            for lc in valid_move[i]:
                if lc[1] != '*':
                    self.territory[lc[0]][lc[1]] += side
                    for move in valid_move[i][lc]:
                        self.territory[move[0]][move[1]] += side
        return

    def output_terr(self):
        board = [''] * 9
        for i in range(9):
            for j in range(9):
                if(self.territory[i][j] > 0 or self.board[i][j] == 1):
                    board[i] += 'W'
                elif(self.territory[i][j] < 0 or self.board[i][j] == -1):
                    board[i] += 'B'
                else:
                    board[i] += 'G'


        board = '/'.join(board)
        return  board

    def __str__(self):
        output = ''
        for i in range(9):
            for j in range(9):
                if(self.territory[i][j] > 0):
                   output += ' W'
                elif(self.territory[i][j] < 0):
                   output += ' B'
                else:
                   output += ' G'
            output += '\n'
        return output

