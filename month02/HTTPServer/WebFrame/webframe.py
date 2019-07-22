"""
webframe.py  模拟后端应用工作流程

从httpserver接收具体请求
根据请求进行逻辑处理和数据处理
将需要的数据反馈给httpserver
"""

from socket import *
import json
from settings import *
from select import select


# 应用类，处理某一方面的请求
class Application:
    def __init__(self):
        self.rlist = []
        self.wlist = []
        self.xlist = []
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,
                               SO_REUSEADDR,
                               DEBUG)
        self.sockfd.bind((frame_ip,frame_port))

    # 启动服务
    def start(self):
        self.sockfd.listen(5)
        print("Start app listen %s"%frame_port)
        self.rlist.append(self.sockfd)
        # select 监控请求
        while True:
            rs,ws,xs = select(self.rlist,
                              self.wlist,
                              self.xlist)
            for r in rs:
                if r is self.sockfd:
                    connfd,addr = r.accept()
                    self.rlist.append(connfd)
                else:
                    self.handle(r)
                    self.rlist.remove(r)

    # 处理具体的httpserver 请求
    def handle(self,connfd):
        request = connfd.recv(1024).decode()
        request = json.loads(request)
        print(request)
        d = {'status':'200','data':'xxxxxx'}
        connfd.send(json.dumps(d).encode())




app = Application()
app.start() # 启动应用服务




