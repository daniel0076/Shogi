from websocket import create_connection
import time

ws = create_connection("ws://127.0.0.1:8000/ws/")
print("Websocket connect...")

def send(text):
    ws.send(text)
    result =  ws.recv()
    print("=> '%s'" % result)

send('{"type": "login", "content":{"username":"test", "password":"password"}}')

send('{"type": "game", "content":{"type": "record"}}')

send('{ "type": "move", "content":{"type":"setRecord", "content":21}}')
send('{ "type": "move", "content":{"type":"exit"}}')

send('{"type": "game", "content":{"type": "record"}}')

send('{ "type": "move", "content":{"type":"setRecord", "content":21}}')
send('{ "type": "move", "content":{"type":"exit"}}')
