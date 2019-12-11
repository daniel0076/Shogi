from websocket import create_connection
import time

ws1 = create_connection("ws://127.0.0.1:8000/ws/")
print("Websocket1 connect...")

ws2 = create_connection("ws://127.0.0.1:8000/ws/")
print("Websocket2 connect...")

def send1(text):
    ws1.send(text)
    result =  ws1.recv()
    print("1=> '%s'" % result)

def send2(text):
    ws2.send(text)
    result =  ws2.recv()
    print("2=> '%s'" % result)

send1('{"type": "login"}')
send2('{"type": "login"}')

ws1.send('{"type": "game", "content":{"type": "online"}}')

ws2.send('{"type": "game", "content":{"type": "online"}}')

result =  ws1.recv()
print("1=> '%s'" % result)
result =  ws2.recv()
print("2=> '%s'" % result)

time.sleep(5)
