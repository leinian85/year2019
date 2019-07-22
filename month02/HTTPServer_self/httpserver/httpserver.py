import socket
from config import *
from threading import *
import re
import sys
import json

# 服务器地址
ADDR = (HOST, PORT)


# 将http的基本功能封装为类
class HTTPServer:
    def __init__(self):
        self.address = ADDR
        self.create_socket() #和浏览器交互
        self.connect_socket() #和webframe交互
        self.bind()

    def create_socket(self):
        self.sockfd = socket.socket()
        self.sockfd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, DEBUG)

    # 创建webframe交互的套接字
    def connect_socket(self):
        self.connect_sockfd = socket.socket()
        frame_addr = (frame_id,frame_port)
        try:
            self.connect_sockfd.connect(frame_addr)
        except Exception as e:
            print(e)
            sys.exit()

    def bind(self):
        self.sockfd.bind(self.address)
        self.ip = self.address[0]
        self.port = self.address[1]

    # 具体处理客户端请求任务
    def handle(self, client):
        # 获取http请求
        request = client.recv(4096).decode()
        pattern = r"(?p<method>[A-Z]+)\s+(?p<info>/\S*)"
        try:
            env = re.match(pattern,request).groupdict()
            print(env)
        except:
            client.close()
            return
        else:
            data = json.dumps(env)
            # 将解析后的请求发送给webfrmae
            self.sockfd.send(data.encode())
            data = self.connect_sockfd.recv(4096*100).decode()
            print(json.loads(data))
            self.respense(client,json.loads(data))

    # 给浏览器发送数据
    def response(self,client,data):
        if data["status"] == "200":
            pass
        elif data["status"] == "404":
            pass


    def serve_forever(self):
        self.sockfd.listen(5)
        print("Listen the port %d" % self.port)
        while True:
            connfd, addr = self.sockfd.accept()
            client = Thread(target=self.handle, args=(connfd,))
            client.setDaemon(True)
            client.start()


httpd = HTTPServer()
httpd.serve_forever()
