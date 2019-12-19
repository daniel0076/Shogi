'''
    the output form would be three colors white, black, and gray 
    the white means the territory belongs to the white front, the black 
    the gray means it is the neatral area
    the output form would be same as the usi replace by w, b, g
'''


class Territory():
    def __init__(self, valid_moves):
        #self.board = self.parse_board(board)
        self.valid_moves = valid_moves
        self.territory = [[0 for i in range(9)] for j in range(9)]
        self.cal_overlap()

    def usi2loc(self, lc):
        return (ord(lc[1])- ord('a'), 9-int(lc[0]))

    def cal_overlap(self):
        valid_move = self.valid_moves
        sides = [-1, 1]
        for i in range(2):
            side = sides[i]
            for lc in valid_move[i]:
                #print(lc)
                if lc[1] != '*':
                    for move in valid_move[i][lc]:
                        self.territory[move[0]][move[1]] += side
        return

    def output_terr(self):
        board = [''] * 9
        for i in range(9):
            for j in range(9):
                if(self.territory[i][j] > 0):
                   board[i] += 'W'
                elif(self.territory[i][j] < 0):
                   board[i] += 'B'
                else:
                   board[i] += 'G'
        board = '/'.join(board)
        return  board


