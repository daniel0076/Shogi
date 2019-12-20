import json
import time

import Shogi_app.ShogiBoard as ShogiBoard
from Shogi_app.UserInfoManager import UserInfoManagerSingleton

from Shogi_app.models import GameHistory
from Shogi_app.models import GamePuzzle
from django.db.models import Q
from django.core import serializers

class Game:
    def __init__(self, user1_id, user2_id, user1_ws, user2_ws):
        self.user1_id = user1_id
        self.user2_id = user2_id
        self.user1_ws = user1_ws
        self.user2_ws = user2_ws
        self.type     = 'proto'

        self.board = ShogiBoard.Board()
        self.round = 0
        self.is_finish = False
        self.winner    = -1
        self.history_board = [self.board.output_usi()]
        self.history_move  = []
        self.record_move   = []
        self.start_time_str= time.strftime("%Y-%m-%d %H:%M", time.localtime()), 
        self.start_time_str= self.start_time_str[0]
        self.start_time    = time.time()
        self.need_save     = True

    def __str__(self):
        return 'user_id({0}, {1})'.format(self.user1_id, self.user2_id)

    def move(self, data):
        self.board.do_move(data)
        self.round = self.round + 1
        self.history_board.append(self.board.output_usi())
        self.history_move.append(data)
        self.check_finish()

    def check_finish(self):
        # Check game finish and winner
        self.is_finish = self.board.is_win
        self.winner = self.board.winner

    def prev(self):
        if (len(self.history_board) < 2):
            # No previous board
            return False
        self.board.init_board(self.history_board[-2])
        self.round = self.round - 1
        self.history_board.pop()
        self.history_move.pop()
        return True

    def next(self):
        if (len(self.record_move) < self.round):
            # No next move
            return False
        self.move(self.record_move[self.round])
        return True

    def surrender(self, data):
        self.is_finish = True
        if (data == self.user1_id):
            self.winner = 1
        else:
            self.winner = 0
        #self.winner = 2 - data

    def exit(self):
        if not self.is_finish:
            return
        if self.need_save:
            time_diff = time.time() - self.start_time
            record = GameHistory(date     = self.start_time_str, 
                                 duration = ('%d:%d' % (time_diff / 3600, (time_diff % 3600) / 60)), 
                                 user1_id = self.user1_id, 
                                 user2_id = self.user2_id, 
                                 init_usi = self.history_board[0], 
                                 moves = json.dumps(self.history_move))
            record.save()
        UserInfoManagerSingleton.update_ingame(self.user1_id, False)
        UserInfoManagerSingleton.update_ingame(self.user2_id, False)

    def setRecord(self, data):
        r = GameHistory.objects.filter(id = data).values()[0]
        self.board = ShogiBoard.Board(r['init_usi'])
        self.round = 0
        self.is_finish = False
        self.winner    = -1
        self.history_board = [self.board.output_usi()]
        self.history_move  = []
        self.record_move   = json.loads(r['moves'])

    def setPuzzle(self, data):
        #r = GamePuzzle.objects.filter(id = data).values()[0]
        #self.board = ShogiBoard.Board(r['init_usi'])
        self.board = ShogiBoard.Board('k4S2l/4+R4/G1NNp2pp/3s2p2/5s3/1PP3P2/P1KS3pp/4R1g2/LN5Nl b 8PGBbgl 0')
        self.round = 0
        self.is_finish = False
        self.winner    = -1

    def update(self, data):
        if data['type'] == 'move':
            self.move(data['content'])

        if data['type'] == 'prev':
            self.prev()

        if data['type'] == 'next':
            self.next()

        if data['type'] == 'surrender':
            self.surrender(data['content'])

        if data['type'] == 'exit':
            self.exit()
        
        if data['type'] == 'setRecord':
            self.setRecord(data['content'])

        if data['type'] == 'setPuzzle':
            self.setPuzzle(data['content'])

        if data['type'] == 'exit':
            self.is_finish = True
            self.exit()
        else:
            self.send_game_status()

    def send_game_status(self):
        data = {}
        data['content'] = {}
        data['type'] = "[Game] Update Game State" 
        data['content']['turn']        = 0
        data['content']['round']       = self.round
        data['content']['isFinish']    = self.is_finish
        data['content']['winner']      = self.winner
        data['content']['usi']         = self.board.output_usi()
        data['content']['validMove']   = self.board.legal_moves()
        data['content']['isCheckmate'] = self.board.is_checkmate
        data['content']['checkmater']  = self.board.checkmater
        data['content']['territory']   = self.board.output_territory()
        data['content']['gameType']    = self.type

        if (self.user1_id == self.user2_id):
            data['content']['turn']        = self.round % 2
            self.user1_ws.send(json.dumps(data))
            return data
        else:
            self.user1_ws.send(json.dumps(data))
            data['content']['turn']   = 1
            self.user2_ws.send(json.dumps(data))
            return data
        #print(self.board)

    def send_records(self):
        data = {}
        data['type'] = "[Game] Select Record"
        r = GameHistory.objects.filter(Q(user1_id = self.user1_id) | Q(user2_id = self.user1_id))
        data['content'] = [{"game_id": x['pk'], "date": x['fields']['date'], "duration": x['fields']['duration']} for x in json.loads(serializers.serialize('json', r))]
        self.user1_ws.send(json.dumps(data))

    def send_puzzle(self):
        data = {}
        data['type'] = "[Game] Select Puzzle"
        r = GamePuzzle.objects.all()
        data['content'] = [{"game_id": x['pk'], "puzzleName": x['fields']['puzzle_name']} for x in json.loads(serializers.serialize('json', r))]
        data['content'] = [{"game_id": 1, "puzzleName": "puzzle1"}]
        self.user1_ws.send(json.dumps(data))

class Single(Game):
    def __init__(self, user_id, user_ws):
        super().__init__(user_id, user_id, user_ws, -1)
        self.need_save = True
        self.type      = 'single'
        self.send_game_status()
    
    def update(self, data):
        if data['type'] == 'move' or data['type'] == 'prev' or data['type'] == 'exit': 
            super().update(data)
    
class Online(Game):
    def __init__(self, user1_id, user2_id, user1_ws, user2_ws):
        super().__init__(user1_id, user2_id, user1_ws, user2_ws)
        self.need_save = True
        self.type      = 'online'
        self.send_game_status()

    def update(self, data):
        if data['type'] == 'move' or data['type'] == 'surrender': 
            super().update(data)

class Record(Game):
    def __init__(self, user_id, user_ws):
        super().__init__(user_id, user_id, user_ws, -1)
        self.need_save = False
        self.type      = 'record'
        self.send_records()

    def update(self, data):
        if data['type'] == 'prev' or data['type'] == 'next' or data['type'] == 'exit' or data['type'] == 'setRecord': 
            super().update(data)

class Puzzle(Game):
    def __init__(self, user_id, user_ws):
        super().__init__(user_id, user_id, user_ws, -1)
        self.need_save = False
        self.type      = 'puzzle'
        self.send_puzzle()

    def update(self, data):
        if data['type'] == 'prev' or data['type'] == 'move' or data['type'] == 'exit' or data['type'] == 'setPuzzle': 
            super().update(data)
