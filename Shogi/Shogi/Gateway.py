from channels.generic.websocket import WebsocketConsumer

import json
import logging

import Shogi.Game

class Gateway(WebsocketConsumer):

    def connect(self):
        # as a constructor
        self.userid   = -1
        self.is_login = 0
        self.in_game  = 0
        self.accept()
        #self.send(text_data="[Welcome %s!]" % self.username)

    def receive(self, *, text_data):
        # Resolve the type of message and send to different servise
        msg = json.loads(text_data)
        
        if msg['type'] == "login":
            # do login
            #self.userid = 
            self.is_login = 1
            self.send(text_data = "suc")
        
        elif msg['type'] == "register":
            # do register
            pass

        elif msg['type'] == "game":
            # register a new game
            #self.gmae = Game_manager.new_game(msg.content)
            
            # for dev
            self.game = Shogi.Game.Game(87, 1, -1, self, self)
            self.in_game = 1
            
        elif msg['type'] == "move":
            # pass data to the game
            self.game.update(msg['content'])

        elif msg['type'] == "set":
            # do setting
            pass

       
    def disconnect(self, message):
        # Need to tell the user info module that user deconnect
        pass
