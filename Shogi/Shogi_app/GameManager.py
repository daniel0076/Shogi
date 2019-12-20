import json
import threading
import time

import Shogi_app.Game as Game
from Shogi_app.UserInfoManager import UserInfoManagerSingleton

class GameManager:
    def __init__(self):
        self.online_lock     = threading.Lock()
        self.online_status   = 0
        self.online_user1_id = -1
        self.online_user1_ws = -1
        self.online_game     = -1

    def new_game(self, data, user_id, ws):
        if UserInfoManagerSingleton.is_ingame(user_id):
            return

        if data['type'] == 'single':
            UserInfoManagerSingleton.update_ingame(user_id, True)
            game_obj = Game.Single(user_id, ws)
            return game_obj

        if data['type'] == 'record':
            UserInfoManagerSingleton.update_ingame(user_id, True)
            game_obj = Game.Record(user_id, ws)
            return game_obj

        if data['type'] == 'puzzle':
            UserInfoManagerSingleton.update_ingame(user_id, True)
            game_obj = Game.Puzzle(user_id, ws)
            return game_obj

        if data['type'] == 'online':
            self.online_lock.acquire()
            UserInfoManagerSingleton.update_ingame(user_id, True)
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
                game_obj = Game.Online(self.online_user1_id, user_id, self.online_user1_ws, ws)

                self.online_game = game_obj
                self.online_status = 2
                while 1:
                    if self.online_status == 3:
                        break
                    time.sleep(1)
                self.online_status = 0
                self.online_lock.release()
                return game_obj

GameManagerSingleton = GameManager()
