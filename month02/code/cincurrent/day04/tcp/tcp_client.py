import socket
import time
import os
class TCPClient:
    def __init__(self):
        self.client = socket.socket()
        self.HOST = "127.0.0.1"
        self.PORT = 18629
        self.ADDR = (self.HOST, self.PORT)

    def __select(self):
        # os.system("clear")
        while True:
            print("========================")
            print("S 查看文件夹")
            print("D 下载文件")
            print("U 上传文件")
            print("Q 退出")
            print("========================")
            result = input("请选择你的操作:")
            if result not in ("S","D","U","Q"):
                print("操作错误...")
                time.sleep(2)
            else:
                return result

    def __look(self,str):
        self.client.send(str.encode())
        data = self.client.recv(4096)
        for item in data.decode().split(" "):
            print(item)
        time.sleep(2)

    def __upload(self,str):
        file = input("需要上传的文件名:")
        msg = str+" "+file
        self.client.send(msg.encode())
        data = self.client.recv()
        if data.decode() == "OK":
            with open(file,"rb") as f:
                while True:
                    msg = f.read(1024)
                    if not msg:
                        time.sleep(0.1)
                        self.client.send(b"##")
                        break
                    self.client.send(msg)


    def start(self):
        try:
            self.client.connect(self.ADDR)
        except Exception as e:
            print(e)
            return

        self.client.send("0".encode())
        data = self.client.recv(4096)
        if data:
            print(data.decode())
            while True:
                result = self.__select()
                if result == "S":
                    self.__look(result)
                elif result == "D":
                    pass
                elif result == "U":
                    self.__upload(result)
                elif result == "Q":
                    pass
