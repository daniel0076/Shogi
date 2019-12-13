from channels.generic.websocket import WebsocketConsumer

import json
import logging

from Shogi_app.GameManager import GameManagerSingleton
from Shogi_app.UserInfoManager import UserInfoManagerSingleton

class Gateway(WebsocketConsumer):

    def connect(self):
        # as a constructor
        self.user_id   = -1
        self.is_login = False
        self.in_game  = 0
        self.accept()
        #self.send(text_data="[Welcome %s!]" % self.username)

    def receive(self, *, text_data):
        # Resolve the type of message and send to different servise
        msg = json.loads(text_data)
        
        if not self.is_login:
            if msg['type'] == "login":
                ret_msg = UserInfoManagerSingleton.login(msg['content'])
                self.send(json.dumps(ret_msg))
                self.is_login = ret_msg['status']
                self.user_id  = ret_msg['userId']
            
            elif msg['type'] == "register":
                ret_msg = UserInfoManagerSingleton.register(msg['content'])
                self.send(json.dumps(ret_msg))

            else:
                print("invalid request type %s" % msg['type'])

        else:
            if msg['type'] == "game":
                # register a new game
                self.game = GameManagerSingleton.new_game(msg['content'], self.user_id, self)
                
                # for dev
                #self.game = Shogi.Game.Game(87, 1, -1, self, self)
                #self.in_game = 1
                
            elif msg['type'] == "move":
                # pass data to the game
                self.game.update(msg['content'])
    
            elif msg['type'] == "set":
                # do setting
                pass

            else:
                print("invalid request type %s" % msg['type'])
    
       
    def disconnect(self, message):
        # Need to tell the user info module that user deconnect
        pass
