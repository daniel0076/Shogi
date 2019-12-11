import json

import Shogi.ShogiBoard as ShogiBoard

class Game:
    def __init__(self, game_id, user1_id, user2_id, user1_ws, user2_ws):
        self.game_id = game_id
        self.user1_id = user1_id
        self.user2_id = user2_id
        self.user1_ws = user1_ws
        self.user2_ws = user2_ws

        self.board = ShogiBoard.Board()
        self.round = 1
        self.is_finish = False
        self.winner    = 0
        self.history_board = [self.board.output_usi()]
        self.history_move  = []

    def __str__(self):
        return 'user_id({0}, {1})'.format(self.user1_id, self.user2_id)

    def move(self, data):
        self.board.do_move(data)
        self.round = self.round + 1
        self.history_board.append(self.board.output_usi())
        self.history_move.append(data)
        self.check_finish()

    def back(self):
        if (len(self.history_board) < 2):
            # No previous board
            return False
        self.board.init_board(self.history_board[-2])
        self.round = self.round - 1
        self.history_board.pop()
        self.history_move.pop()
        return True

    def surrender(self, data):
        self.is_finish = True
        self.winner = 3 - data
        self.send_game_status()
        self.exit()

    def exit(self):
        # Store game in DB
        # and tell the user info manager to update
        print({"id": self.game_id, "user1": self.user1_id, "user2": self.user2_id, "usi": self.history_move})
        # del self
        # set user info manager user not in game

    def update(self, data):
        if data['type'] == 'move':
            self.move(data['content'])
            self.send_game_status()

        if data['type'] == 'back':
            self.back()
            self.send_game_status()

        if data['type'] == 'surrender':
            self.surrender(data['content'])

        # only in single game
        if data['type'] == 'exit':
            self.exit()
        
    def send_game_status(self):
        data = {}
        data['content'] = {}
        data['type'] = "gameStatus"
        data['content']['round']       = self.round
        data['content']['isFinish']    = self.is_finish
        data['content']['winner']      = self.winner
        data['content']['usi']         = self.board.output_usi()
        data['content']['validMove']   = ''
        # All valid move?
        data['content']['isCheckmate'] = self.board.is_checkmate
        data['content']['checkmate']   = self.board.checkmater
        data['content']['territory']   = ''
        # Wait territory API
        self.user1_ws.send(json.dumps(data))
        if (self.user2_id != -1):
            self.user2_ws.send(json.dumps(data))
        print(self.board)

    def check_finish(self):
        # Check game finish and winner
        # Wait ShogiBoard
        pass

class Single(Game):
    def __init__(self, game_id, user_id, user_ws):
        super().__init__(game_id, user_id, -1, user_ws, -1)

    
class Online(Game):
    def __init__(self, game_id, user1_id, user2_id, user1_ws, user2_ws):
        super().__init__(game_id, user1_id, user2_id, user1_ws, user2_ws)

    def exit(self):
        # online gmae can't surrender
        pass
