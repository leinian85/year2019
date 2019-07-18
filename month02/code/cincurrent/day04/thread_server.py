import socket
import os
import threading

def handle(client):
    while True:
        data = client.recv(4096)
        if not data:
            break
        print(data.encode())
        client.send(" asd ".encode())

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
HOST = "127.0.0.1"
PORT = 18629
ADDR = (HOST,PORT)
s.bind(ADDR)
s.listen(100)

while True:
    try:
        c,addr = s.accept()
        print("connect from ",addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    t = threading.Thread(target=handle,args=(c,))
    t.setDaemon(True)
    t.start()