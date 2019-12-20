from websocket import create_connection
import time

ws = create_connection("ws://127.0.0.1:8000/ws/")
print("Websocket connect...")

def send(text):
    ws.send(text)
    result =  ws.recv()
    print("=> '%s'" % result)

send('{"type": "login", "content":{"username":"test", "password":"password"}}')
result =  ws.recv()
print("=> '%s'" % result)

send('{"type": "game", "content":{"type": "puzzle"}}')
send('{ "type": "move", "content":{"type":"setPuzzle", "content":1}}')

'''
send('{ "type": "move", "content":{"type":"next"}}')
send('{ "type": "move", "content":{"type":"next"}}')
send('{ "type": "move", "content":{"type":"prev"}}')
send('{ "type": "move", "content":{"type":"next"}}')
send('{ "type": "move", "content":{"type":"prev"}}')
'''
