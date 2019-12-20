from channels.generic.websocket import WebsocketConsumer

import json
import logging

from Shogi_app.GameManager import GameManagerSingleton
from Shogi_app.UserInfoManager import UserInfoManagerSingleton

class Gateway(WebsocketConsumer):

    def connect(self):
        # as a constructor
        self.user_id  = -1
        self.is_login = False
        self.accept()

    def receive(self, *, text_data):
        # Resolve the type of message and send to different servise
        msg = json.loads(text_data)
        
        if not self.is_login:
            if msg['type'] == "login":
                ret_msg = UserInfoManagerSingleton.login(msg['content'])
                self.send(json.dumps(ret_msg))
                self.is_login = ret_msg['content']['status']
                self.user_id  = ret_msg['content']['userId']
                self.send(json.dumps(UserInfoManagerSingleton.get_settings(self.user_id)))
            
            elif msg['type'] == "register":
                ret_msg = UserInfoManagerSingleton.register(msg['content'])
                self.send(json.dumps(ret_msg))

            else:
                print("invalid request type %s" % msg['type'])

        else:
            if msg['type'] == "game":
                # register a new game
                self.game = GameManagerSingleton.new_game(msg['content'], self.user_id, self)
                
            elif msg['type'] == "move":
                # pass data to the game
                msg['content']['userId'] = self.user_id
                self.game.update(msg['content'])
    
            elif msg['type'] == "get_settings":
                self.send(json.dumps(UserInfoManagerSingleton.get_settings(self.user_id)))

            elif msg['type'] == "update_settings":
                UserInfoManagerSingleton.update_settings(self.user_id, msg['content'])
                self.send(json.dumps(UserInfoManagerSingleton.get_settings(self.user_id)))

            else:
                print("invalid request type %s" % msg['type'])
    
       
    def disconnect(self, message):
        UserInfoManagerSingleton.update_online(self.user_id, False)
        try:
            self.game.exit()
        except:
            pass
        UserInfoManagerSingleton.update_ingame(self.user_id, False)

