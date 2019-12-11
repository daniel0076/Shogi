from websocket import create_connection
import time

ws = create_connection("ws://127.0.0.1:8000/ws/")
print("Websocket connect...")

def send(text):
    ws.send(text)
    result =  ws.recv()
    print("=> '%s'" % result)

send('{"type": "login"}')

ws.send('{"type": "game"}')

send('{ "type": "move", "content":{"type":"move", "content":"9c9d"}}')
send('{ "type": "move", "content":{"type":"move", "content":"9g9f"}}')
send('{ "type": "move", "content":{"type":"move", "content":"8c8d"}}')
send('{ "type": "move", "content":{"type":"move", "content":"8g8f"}}')
send('{ "type": "move", "content":{"type":"move", "content":"7c7d"}}')
send('{ "type": "move", "content":{"type":"move", "content":"7g7f"}}')
send('{ "type": "move", "content":{"type":"move", "content":"6c6d"}}')
send('{ "type": "move", "content":{"type":"move", "content":"6g6f"}}')
send('{ "type": "move", "content":{"type":"move", "content":"5c5d"}}')
send('{ "type": "move", "content":{"type":"move", "content":"5g5f"}}')
time.sleep(20)
send('{ "type": "move", "content":{"type":"back"}}')
send('{ "type": "move", "content":{"type":"surrender", "content": 1}}')

ws.close()

