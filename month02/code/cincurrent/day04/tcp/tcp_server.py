import socket
import os
from multiprocessing import Process
import signal

class FTPServer:
    def __init__(self):
        self.socket = socket.socket()
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.HOST = "127.0.0.1"
        self.PORT = 18629
        self.ADDR = (self.HOST, self.PORT)
        self.socket.bind(self.ADDR)
        self.socket.listen(100)
        signal.signal(signal.SIGCHLD, signal.SIG_IGN)  # 将僵尸进程交给四通处理

    def start(self):
        while True:
            try:
                client, addr = self.socket.accept()
                print("connect from ", addr)
            except KeyboardInterrupt:
                os._exit(0)
            except Exception as e:
                print(e)
                continue

            p = Process(target=self.__handle, args=(client,))
            p.start()

    def __find(self):
        dirlist = []
        for file in os.listdir("./dir"):
            dirlist.append(file)
        return dirlist


    def __handle(self,client):
        while True:
            data = client.recv(4096)
            if not data:
                break
            data = data.decode()
            if data == "0":
                client.send("connect succeed".encode())
            elif data == "S":
                send_data = " ".join(self.__find())
                client.send(send_data.encode())
            elif data == "U":
                # upload()
                pass
            elif data == "3":
                # download()
                pass
            else:
                break

