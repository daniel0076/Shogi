import json
import threading
import time

import Shogi.Game as Game

class GameManager:
    def __init__(self, start_game_id):
        self.game_id         = start_game_id
        self.game_id_lock    = threading.Lock()

        self.online_lock     = threading.Lock()
        self.online_status   = 0
        self.online_user1_id = -1
        self.online_user1_ws = -1
        self.online_game     = -1

    def new_game(self, data, user_id, ws):
        if data['type'] == 'single':
            # Critial section protect game_id to be unique
            self.game_id_lock.acquire()
            game_obj = Game.Single(self.game_id, user_id, ws)
            self.game_id = self.game_id + 1
            self.game_id_lock.release()
            # End of critical section
            return game_obj

        if data['type'] == 'online':
            self.online_lock.acquire()
            if (self.online_status == 0):
                self.online_user1_id = user_id
                self.online_user1_ws = ws
                self.online_status = 1
                self.online_lock.release()
                while 1:
                    if self.online_status == 2:
                        break
                    time.sleep(1)
                game_obj = self.online_game
                self.online_status = 3
                return game_obj
            elif (self.online_status == 1):
                self.game_id_lock.acquire()
                game_obj = Game.Online(self.game_id, self.online_user1_id, user_id, self.online_user1_ws, ws)
                self.game_id = self.game_id + 1
                self.game_id_lock.release()

                self.online_game = game_obj
                self.online_status = 2
                while 1:
                    if self.online_status == 3:
                        break
                    time.sleep(1)
                self.online_status = 0
                self.online_lock.release()
                return game_obj



