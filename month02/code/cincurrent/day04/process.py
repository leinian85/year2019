from multiprocessing import Process
import socket
import os
import signal
HOST = "127.0.0.1"
PORT = 18629
ADDR = (HOST,PORT)

def handle(client):
    while True:
        data = client.recv(1024)
        if not data:
            break
        print(data.decode())
        client.send("asd".encode())

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(1000)
signal.signal(signal.SIGCHLD,signal.SIG_IGN) #将僵尸进程交给四通处理
while True:
    try:
        c,addr = s.accept()
        print("connect from ",addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    p = Process(target=handle,args=(c,))
    p.daemon = True
    p.start()

