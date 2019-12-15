from websocket import create_connection
import time

ws = create_connection("ws://127.0.0.1:8000/ws/")
print("Websocket connect...")

def send(text):
    ws.send(text)
    result =  ws.recv()
    print("=> '%s'" % result)

send('{"type": "register", "content":{"username":"test", "password":"password"}}')
send('{"type": "register", "content":{"username":"test4", "password":"password"}}')
